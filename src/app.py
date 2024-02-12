"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints


@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
    }

    return jsonify(response_body), 200


#Para hacer un get de un miembro concreto, sería la misma ruta que uso para añadir, ya que especifico
#al final de la ruta el id del miembro con la información que quiero ver
@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    #Si el miembro existe, devuelvo su información, sino un error
    if member:
        return jsonify(member), 200
    else:
        raise APIException("El miembro no existe", status_code=400)

@app.route('/member', methods=['POST'])
def add_member():
    #Recojo la request (en este caso la petición que envio desde postman) y la guardo en data
    data = request.json
    #Paso data a la función add_member
    jackson_family.add_member(data)
    #Devuelvo el contenido de data dentro de jsonify para poder visualizarlo al hacer la petición
    return jsonify(data), 200

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    #Como el metodo DELETE no genera un payload, no tiene sentido guardar su respuesta ya que no la voy a usar
    #asi que directamene paso el id a la función para que se elimine el usuario
    jackson_family.delete_member(member_id)
    #Devuelvo el contenido de data dentro de jsonify para poder visualizarlo al hacer la petición
    return jsonify("Eliminación correcta"), 200

@app.route('/member/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    #Recojo la request (en este caso la petición que envio desde postman) y la guardo en data
    data = request.json
    #Paso el id recibido y los datos del miembro
    jackson_family.update_member(member_id, data)
    #Devuelvo el contenido de data dentro de jsonify para poder visualizarlo al hacer la petición
    return jsonify("Actualización correcta"), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)