
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    # Como parámetros recibo self (para que detecte que pertenece la clase de la familia Jackson)
    # Y data, se podría poner cualquier nombre pero con data es más especifico ya que es lo que
    # paso como parámetro desde la ruta.
    def add_member(self, data):
        # Si el id del miembro a añadir no se encuentra en data (lo que recibo), entonces
        # se crea un id para ese miembro llamando a generateId y con append meto el miembro a la lista
        if "id" not in data:
            data["id"] = self._generateId()
        self._members.append(data)

    # En el caso de eliminar, recibo la clase y el parámetro que envío desde postman
    def delete_member(self, member_id):
        #Creo una lista vacía, la cual contendrá los miembros que no quiero eliminar
        final_members = []
        # Recorro la lista
        for member in self._members:
        # Si el ID de alguno de los miembros coincide con el que recibo, no hago nada, ya que el append
        #se hará cuando los ids existentes no coincidan con el que quiero borrar, para asegurarme de que la 
        #lista actualizada tendrá todos los ids excepto el que paso en postman.
            if member["id"] == member_id:
                continue
            # Entonces en el else, la condición sería que si el id no coincide, se añada a la lista de miembros finales
            else:
                final_members.append(member)
            # Actualizo la lista original con la actualizada
            self._members = final_members

    #Recibo la clase, el id que paso desde postman y data que contiene los datos correspondiente a ese id
    def update_member(self, member_id, data):
        #Recorro la lista
        for member in self._members:
            #Si el id coincide con el que paso, se lleva a cabo la actualización
            if member["id"] == member_id:
            # Uso update(), una función de python que actualiza el contenido de un diccionario (objeto) con el que 
            #yo le pase, de forma que member que contiene el mismo id que quiero actualizar, obtiene el contenido de data
                member.update(data)
                #Con break me aseguro que después de hacer la actualización, no continue el for
                break

    #Recibo la clase y el id
    def get_member(self, member_id):
        # fill this method and update the return
        #Recorro la lista
        for member in self._members:
            #Si el id coincide con alguno existente, devuelvo la información del miembro que 
            #tenga ese id
            if member["id"] == member_id:
                return member
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members