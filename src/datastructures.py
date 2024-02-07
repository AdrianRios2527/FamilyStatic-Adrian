from random import randint
class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [

        ]
    def _generateId(self):
        return randint(0, 99999999)
    
    def add_member(self, member):
        self._members.append(member)
        return None
    def _initialize_members(self):
        # Agregar miembros iniciales de la familia
        self.add_member({"name": "John Jackson", "age": 33, "lucky_numbers": [7, 13, 22]})
        self.add_member({"name": "Jane Jackson", "age": 35, "lucky_numbers": [10, 14, 3]})
        self.add_member({"name": "Jimmy Jackson", "age": 5, "lucky_numbers": [1]})
    
    def delete_member(self, id):
        for position, member in enumerate(self._members):
            if member["id"] == id:
                self._members.pop(position)
                return None


    def get_member(self, id):
        for member in self._members:
            if member["id"] == int(id):
                return member
        return None
    def get_all_members(self):
        return self._members