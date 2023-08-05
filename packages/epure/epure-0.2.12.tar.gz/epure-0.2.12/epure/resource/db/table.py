from __future__ import annotations
from types import LambdaType, NoneType
from typing import TYPE_CHECKING, Dict, Union, List, ItemsView, Any, Type, Callable, cast
from ..savable import Savable
from .constraint import Constraint
from ..resource import Resource
from ..node.node import Node
from ...parser.term import Term
from ...parser.leaf import TableProxy, QueryingProxy, DbProxy, ColumnProxy
from ..db.table_column import TableColumn
from collections import OrderedDict
from ..node.proto import Proto

from ...errors import DeserializeError

if TYPE_CHECKING:
    from .table_storage import TableStorage
    from ...parser.term_parser import TermParser
from .db_entity import DbEntity
from ...helpers.type_helper import check_type
from ...errors import EpureError, DbError
from .table_header import TableHeader
from ..node_promise import FieldPromise, NodePromise
from ...epure import Epure


class Table(DbEntity):
    header:TableHeader
    if TYPE_CHECKING:
        parser: TermParser
    querying_proxy: QueryingProxy
    resource_proxy: DbProxy

    if TYPE_CHECKING:
        resource:TableStorage

    @property
    def db(self):
        return self.resource

    def __init__(self, name: str,
            header:Union[TableHeader, Dict[str, Any]]=None, resource:Resource=None, namespace:str = '') -> None:        
        check_type('header', header, [TableHeader, dict, NoneType])
        from ...parser.term_parser import TermParser

        self._set_header(header)
        super().__init__(name, namespace, resource)

        self.parser = TermParser(self)
        self.querying_proxy = TableProxy(self.db, self)
        self.resource_proxy = DbProxy(self.db)
        


    def _serialize(self, node: Savable) -> Dict[str, str]:
        res = {}
        for field_name, field_type in node.annotations.items():
            if isinstance(field_type, Constraint):
                field_type = field_type.py_type
                
            if node.is_excluded(field_name, field_type):
                continue
            if field_name not in self.header:
                continue
            if not hasattr(node, field_name):
                continue

            field_val = getattr(node, field_name, None)
            #working for db:
            if isinstance(field_val, Savable):
                field_type = field_val.annotations['node_id']
                field_val = field_val.save(True).node_id
            
            if (isinstance(field_type, type) and issubclass(field_type, Savable)\
                and not isinstance(field_val, Savable)):
                field_type = type(field_val)
                
            field_val = self.db.cast_py_db_val(field_val, field_type)

            res[field_name] = field_val
        
        return res



    def create(self, node: Node, asynch:bool=False) -> object:
        node.node_id = self.generate_id()
        script = self.serialize_for_create(node)
        if asynch:
            self.cache(script)
        else:
            self.execute(script)
        return node

    
    def read(self, *args, **kwargs) -> Any:        
        # if not (args or kwargs):
        #     return self.read_by_fields(**kwargs)
        
        if kwargs:
            return self.read_by_kwargs(*args, **kwargs)

        if args:
            selector = args[0]
        else:
            # args.__add__(self.querying_proxy)
            selector = self.querying_proxy@True
            args = args + (selector,)

        if isinstance(selector, str):
            return self.read_by_sql(selector)

        if callable(selector):
            return self.read_by_function(selector)

        if isinstance(args[-1], Term):
            selector = args[-1]
            return self.read_by_term(args[0:-1], selector)

        raise NotImplementedError(f'couldn read by object of type {type(selector)}')


    # def read_by_fields(self):
    #     raise NotImplementedError

    def read_by_kwargs(self, header:List[str]=[], operator:str="", **kwargs):
        term_header = []
        tp = self.querying_proxy
        for col_name in header:
            column = getattr(tp, col_name)
            term_header.append(column)
        
        if not term_header:
            term_header.append(tp)
        # from ...parser.leaf import Primitive 
        # term = term_header @ Primitive(True)
        kwargs_items = list(kwargs.items())
        first_item = kwargs_items[0]
        term = term_header @ getattr(tp, first_item[0]) == first_item[1]
        for (key, val) in kwargs_items[1:]:
            if operator == 'or':
                term = term | getattr(tp, key) == val
            else:
                term = term & getattr(tp, key) == val
        return self.read(term)

    def read_by_sql(self, selector):
        res = self.execute(selector)
        res = self.deserialize(res)
        return res

    def read_by_function(self, func):
        selector = func(self.querying_proxy, self.resource_proxy)
        if isinstance(selector, list) or isinstance(selector, tuple):
            return self.read(*selector)
        return self.read(selector)

    def read_by_term(self, header, selector:Term):
        sql = self.parser.parse(header, selector)
        res = self.read(sql)
        return res

        

    def deserialize(self, rows: dict, lazy_read:bool=True):
        res = []
        if not rows:
            return res
        full_name_epure_dict = self._column_full_name_epure_dict(rows[0])        
        for node_dict in rows:
            res_row = self._init_epures_row(node_dict, full_name_epure_dict, lazy_read)
            res.append(res_row)
        return res


    def _init_epures_row(self, node_dict, full_name_epure_dict, lazy_read) -> Dict[type, dict]:
        epure_attrs_dict = OrderedDict()
        for full_name, db_val in node_dict.items():
            column_tuple = full_name_epure_dict[full_name]
            epure_cls = column_tuple[0]
            column = column_tuple[1]
            if epure_cls not in epure_attrs_dict:
                epure_attrs_dict[epure_cls] = {}

            attrs = epure_attrs_dict[epure_cls]            
            # db_val = node_dict[full_name]
            if isinstance(column, TableColumn):
                field_type = column.py_type
                if isinstance(field_type, Constraint):
                    field_type = field_type.py_type
                val = self.db.cast_db_py_val(db_val, field_type)
                attrs[column.name] = val
            else:
                val = self.db.cast_db_py_val(db_val)
                attrs[column] = val

        res = []
        for epure_cls, attrs in epure_attrs_dict.items():
            epure_obj = self._init_epure(epure_cls, attrs, lazy_read)
            res.append(epure_obj)
        return res


    def _init_epure(self, epure_cls:Epure, attrs:dict, lazy_read):

        res = None
        if True in epure_cls.init_params:
            res = epure_cls(**attrs)
        else:
            arguments = {}
            for name in epure_cls.init_params:
                if isinstance(name, str) and name in attrs:
                    arguments[name] = attrs[name]
            try:
                res = epure_cls(**arguments)
            except Exception as ex:
                raise ex
        if res is None:
            raise DeserializeError
        
        for field_name, field_val in attrs.items():
            setattr(res, field_name, field_val)

        if not (hasattr(res, 'annotations') and 'node_id' in attrs):
            return res

        for field_name, field_type in res.annotations.items():

            if epure_cls.is_excluded(field_name):
                continue

            if field_name not in attrs:
                node_id = attrs['node_id']
                promise = FieldPromise(epure_cls.resource, node_id, field_name)
                setattr(res, field_name, promise)

            elif isinstance(field_type, Epure):
                node_id = attrs[field_name]
                if issubclass(field_type, Proto) and field_name == '__proto__':
                    proto = field_type.resource.read(node_id=node_id)
                    res.set_proto_fields(proto)
                elif lazy_read:
                    promise = NodePromise(field_type.resource, node_id)
                    setattr(res, field_name, promise)
                elif not lazy_read:
                    node = field_type.resource.read(node_id=node_id)
                    setattr(res, field_name, node)
        return res



    def _column_full_name_epure_dict(self, node_dict) -> Dict[str, tuple]:
        res = OrderedDict()
        for full_name, val in node_dict.items():
            dot_name = full_name.replace('___', '.')
            split = dot_name.rsplit('.', 1)
            table_name = split[0]
            field_name = split[1]            
            epure_cls = self.db.get_epure_by_table_name(table_name)
            if not epure_cls:
                res[full_name] = (object, field_name)
                continue

            epure_table = getattr(epure_cls, 'resource', None)
            if epure_table == None or not isinstance(epure_table, Table):
                raise DbError(f'epure {epure_cls} must have table as resourse')
            column = epure_table.header[field_name]
            res[full_name] = [epure_cls, column]
        return res


    def update(self, node: Savable, asynch:bool=False) -> object:
        script = self.serialize_for_update(node)
        if asynch:
            self.cache(script)
        else:
            self.execute(script)
        return node


    def cache(self, script: str):        
        self.db.cache_queue.append(script)


    def _set_header(self, header):
        if header == None:
            header = TableHeader(table=self)
        
        if isinstance(header, Dict):
            header = TableHeader(columns=header, table=self)
        
        self.header = header
        self.header.resource = self
       
    def serialize_for_create(self, node: Savable, **kwargs) -> object:
        raise NotImplementedError

    def serialize_for_read(self, node: Savable, **kwargs) -> object:
        raise NotImplementedError

    def serialize_for_update(self, node: Savable, **kwargs) -> object:
        raise NotImplementedError

    def serialize_for_delete(self, node: Savable, **kwargs) -> object:
        raise NotImplementedError

    
    def serialize_header(self, db: TableStorage=None, **kwargs) -> List[Dict[str, str]]:
        res: List[Dict[str, str]] = list()

        if db == None:
            db = self.db

        if db == None:
            raise EpureError('undefined db for header serialization')
        
        header = self.header
        for column_name in header:
            column = header[column_name]
           
            serialized = {
                "column_name": column.name,
                "column_type": column.serialize_type(db) #db.get_db_type(column.column_type)
            }
            res.append(serialized)
        return res

    def _add_node_id_fields(self, header:List[QueryingProxy]):
        res = []
        for item in header:
            if isinstance(item, ColumnProxy):
                tp = item.__table_proxy__
                node_id = getattr(tp, 'node_id', None)
                if node_id is not None and not node_id.in_header(header + res):
                    res.append(node_id)
        
        # res = tuple(res)
        header = tuple(header)
        
        if isinstance(header[0],str):
            res = set()
            for item in header:
                sp = item.split('.')

                if len(sp) == 3:
                    node_id_column = f'{sp[0]}.{sp[1]}.node_id'
                    if node_id_column not in header:
                        res.add(node_id_column)
                    
        res = tuple(res)



        return header + res


    # def get_column_header_name(self, column_name:str):
    #     raise NotImplementedError

        # tables = []
        # columns = []
        # for item in header:
        #     if isinstance(item, TableProxy):
        #         table_name = item.str(False, True)
        #         tables.append(table_name)
        #     if isinstance(item, ColumnProxy):
        #         column_name = item.str(False, True)
        #         columns.append(column_name)

        # res = []
        # for item in header:
        #     if isinstance(item, ColumnProxy):
        #         tp = item.__table_proxy__
        #         table_name = tp.str(False, True)
        #         if (not table_name in tables) and\
        #                 hasattr(tp, 'node_id') and\
        #                 tp.node_id.str(False, True) not in columns:
        #             res.append(tp.node_id)
        #             columns.append(tp.node_id.str(False, True))
        # return res