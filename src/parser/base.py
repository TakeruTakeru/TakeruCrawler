from abc import abstractmethod

class ParserBase:
    '''Parser Interface'''
    @abstractmethod
    def find_all_tag(self, tag: str, **kwargs):
        pass

    @abstractmethod
    def find_tag(self, tag: str, **kwargs):
        pass

class Converter:
    '''HTML Objects to Built-in Objects'''

    def serialize(self):
        pass

    def deserialize(self):
        pass