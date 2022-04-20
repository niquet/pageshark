import abc

class IQueryString(metaclass=abc.ABCMeta):
    pass

class QueryString(IQueryString):
    pass

class MonsterQueryString(IQueryString):
    pass
