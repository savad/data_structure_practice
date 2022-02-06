import json


class SearchByTag:

    def __init__(self, data_file, query_tag):
        self._data = data1["items"]
        self.query = query_tag

    def search(self):
        return (item for item in self._data if item.get('tags') and self.query in item.get('tags'))

    def first(self):
        try:
            return next(self.search())
        except:
            raise StopIteration
        
        
data1 = {'items': [
{'name': 'M1', 'tags': ['france', '80s', 'drama']},
{'name': 'M2', 'tags': ['usa', 'thriller']},
{'name': 'M3', 'tags': ['poland', '80s']}, 
{'name': 'M4', }
]}    
        
        

obj = SearchByTag(data1, "80s")
print(obj.first())
print(list(obj.search()))

