from flask import request, jsonify
from ..models.categories import Categories
from datetime import datetime

def create_category():
    data = request.get_json()
    
    if not data:
        return jsonify({
            "status": False,
            "message": "Erro: Nenhum dado encontrado na requisição."
        }), 400
    
    required_fields = ['name']
    missing_fields = [field for field in required_fields if field not in data]
    
    if missing_fields:
        return jsonify({
            "status": False,
            "message": f"Faltando os campos: {', '.join(missing_fields)}"
        }), 400
    
    name = data.get('name')
    status = 1
    registration_date = int(datetime.now().timestamp())
    
    new_category = Categories.insert(name, status, registration_date)
    
    if new_category:
        return jsonify({
            "status": True,
            "message": "Categoria cadastrada com sucesso!",
            "id_category": new_category.id_category
        }), 201
    
    return jsonify({
        "status": False,
        "message": "Falha ao tentar cadastrar categoria."
    }), 500
    
def update_category(id_category):
    data = request.get_json()
    
    if not data:
        return jsonify({
            "status": False,
            "message": "Erro: Nenhum dado encontrado na requisição."
        }), 400
        
    required_fields = ['name', 'status']
    missing_fields = [field for field in required_fields if field not in data]
    
    if missing_fields:
        return jsonify({
            "status": False,
            "message": f"Faltando os campos: {', '.join(missing_fields)}"
        }), 400
    
    name = data.get('name')
    status = data.get('status')
    
    update = Categories.update(id_category, name, status)
    
    if update:
        return jsonify({
            "status": True,
            "message": "Categoria atualizada com sucesso!"
        }), 200 
    else: jsonify({
        "status": False,
        "message": "Falha ao tentar atualizar essa categoria."
    }), 400
    
def get_all_categories():
    categories = Categories.get_all()
    return jsonify({
        "status" : True,
        "categories" : categories
    })
    
def get_category(id_category):
    category = Categories.get(id_category)
    return jsonify({
        "status" : False, 
        "category" : category
    })
    
def delete_category(id_category):
    delete_category = Categories.delete(id_category)
    
    if delete_category:
        return jsonify({
            "status" : True,
            "message" : "Categoria removida com sucesso!"
        })
    else:
        return jsonify({
            "status" : False,
            "message" : "Falha ao tentar remover categoria."
        })