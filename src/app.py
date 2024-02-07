import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the Jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# 1) Get all family members
@app.route('/members', methods=['GET'])
def get_all_members():
    try:
        members = jackson_family.get_all_members()
        return jsonify(members), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 2) Retrieve one member by id
@app.route('/member/<int:id>', methods=['GET'])
def get_member(id):
    try:
        member = jackson_family.get_member(id)
        if member:
            return jsonify(member), 200
        else:
            return jsonify({"error": "Member not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 3) Add new member
@app.route('/member', methods=['POST'])
def add_member():
    try:
        new_member = request.json
        jackson_family.add_member(new_member)
        return jsonify({"message": "Member added successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# 4) Delete one member by id
@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    try:
        success = jackson_family.delete_member(id)
        if success:
            return jsonify({"done": True}), 200
        else:
            return jsonify({"error": "Member not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
