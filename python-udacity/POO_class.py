class Person:
    def __init__(self, person_id, person_name, person_age):
        self._id = person_id
        self.name = person_name
    
    def get_id(self):
        return self._id
    
    def set_id(self, new_id):
        self._id = new_id
        

