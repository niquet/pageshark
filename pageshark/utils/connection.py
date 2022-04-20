import abc

class IConnection(metaclass=abc.ABCMeta):
    pass

class Connection(IConnection):
    pass

class MongoDBConnection(IConnection):
    pass

class SQLiteConnection(IConnection):
    pass
