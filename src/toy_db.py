import json
from pathlib import Path

class ToyDB:
    def __init__(self, path) -> None:
        self.path = Path(path)
        self.load(self.path.absolute())
    
    def load(self, path) -> bool:
        if path.exists():
            self._load()
        else:
            self.db = {}
        
        return True
    

    def _load(self):
        self.db = json.load(open(self.path.absolute(), "r"))
    

    def dumpdb(self):
        try:
            json.dump(self.db, open(self.path.absolute(), "w+"))
            return True

        except:
            return False
        


    def set(self, key, value) -> bool:
        try:
            self.db[str(key)] = value
            self.dumpdb()
            return True

        except Exception as e:
            print("Error Saving to the Database\n", e)
            return False
    

    def get(self, key):
        try:
            return self.db[key]
        
        except KeyError:
            print("No Value found with the Key given")
            return False
    
    
    def delete(self, key):
        if not key in self.db.keys():
            return False
        
        del self.db[key]
        self.dumpdb()
        return True
