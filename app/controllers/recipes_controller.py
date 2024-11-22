from flask import jsonify

def create_recipe():
    return jsonify({
        "status": True,
        "message": "Recipe created with success!"
    })