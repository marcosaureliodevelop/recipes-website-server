from flask import request, jsonify
from ..models.preparation_methods import PreparationMethods

def create_method():
    data = request.get_json()
    
    if not data:
        return jsonify({
            "status": False,
            "message": "Erro: Nenhum dado encontrado na requisição."
        }), 400
    
    required_fields = ['id_recipe', 'description']
    missing_fields = [field for field in required_fields if field not in data]
    
    if missing_fields:
        return jsonify({
            "status": False,
            "message": f"Faltando os campos: {', '.join(missing_fields)}"
        }), 400
    
    id_recipe = data.get('id_recipe')
    description = data.get('description')
    
    new_method = PreparationMethods.insert(id_recipe, description)
    
    if new_method:
        return jsonify({
            "status": True,
            "message": "Método de preparo cadastrado com sucesso!",
            "id_method": new_method.id_method
        }), 201
    
    return jsonify({
        "status": False,
        "message": "Erro ao tentar cadastrar método de preparo."
    }), 500
    
def update_method(id_method):
    data = request.get_json()
    
    if not data:
        return jsonify({
            "status": False,
            "message": "Erro: Nenhum dado encontrado na requisição."
        }), 400
        
    required_fields = ['description']
    missing_fields = [field for field in required_fields if field not in data]
    
    if missing_fields:
        return jsonify({
            "status": False,
            "message": f"Faltando os campos: {', '.join(missing_fields)}"
        }), 400
    
    description = data.get('description')
    
    update = PreparationMethods.update(id_method, description)
    
    if update:
        return jsonify({
            "status": True,
            "message": "Método de preparo atualizado com sucesso!"
        }), 200 
    else: jsonify({
        "status": False,
        "message": "Erro ao tentar atualizar este método de preparo."
    }), 400
    
def get_all_methods():
    methods = PreparationMethods.get_all()
    return jsonify({
        "status" : True,
        "methods" : methods
    })
    
def get_method(id_method):
    method = PreparationMethods.get(id_method)
    return jsonify({
        "status" : False, 
        "method" : method
    })
    
def delete_method(id_method):
    delete_method = PreparationMethods.delete(id_method)
    
    if delete_method:
        return jsonify({
            "status" : True,
            "message" : "Método de preparo removido com sucesso."
        })
    else:
        return jsonify({
            "status" : False,
            "message" : "Falha ao tentar remover este método de preparo"
        })