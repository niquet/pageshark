import abc

class IPagination(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and 
                callable(subclass.load_data_source) and 
                hasattr(subclass, 'extract_text') and 
                callable(subclass.extract_text))

class Pagination(IPagination):
    pass

class DicePagination(IPagination):
    pass

class IndeedPagination(IPagination):
    pass

class LinkedInPagination(IPagination):
    pass

class MonsterPagination(IPagination):
    pass
