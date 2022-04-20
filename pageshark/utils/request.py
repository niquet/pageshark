import abc

class IRequest(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and 
                callable(subclass.load_data_source) and 
                hasattr(subclass, 'extract_text') and 
                callable(subclass.extract_text))

class Request(IRequest):
    pass

class BingRequest(IRequest):
    pass

class DuckDuckGoRequest(IRequest):
    pass

class GoogleRequest(IRequest):
    pass

class StartPageRequest(IRequest):
    pass

class YahooRequest(IRequest):
    pass
