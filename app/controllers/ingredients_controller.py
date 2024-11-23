from flask import request, jsonify
from ..models.ingredients import Ingredients

def create_ingredient():
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
    
    new_ingredient = Ingredients.insert(id_recipe, description)
    
    if new_ingredient:
        return jsonify({
            "status": True,
            "message": "Ingrediente cadastrado com sucesso!",
            "id_ingredient": new_ingredient.id_ingredient
        }), 201
    
    return jsonify({
        "status": False,
        "message": "Erro ao tentar cadastrar ingrediente."
    }), 500
    
def update_ingredient(id_ingredient):
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
    
    update = Ingredients.update(id_ingredient, description)
    
    if update:
        return jsonify({
            "status": True,
            "message": "Ingrediente atualizado com sucesso!"
        }), 200 
    else: jsonify({
        "status": False,
        "message": "Erro ao tentar atualizar este ingrediente."
    }), 400
    
def get_all_ingredients():
    ingredients = Ingredients.get_all()
    return jsonify({
        "status" : True,
        "ingredients" : ingredients
    })
    
def get_ingredient(id_ingredient):
    ingredient = Ingredients.get(id_ingredient)
    return jsonify({
        "status" : False, 
        "ingredient" : ingredient
    })
    
def delete_ingredient(id_ingredient):
    delete_ingredient = Ingredients.delete(id_ingredient)
    
    if delete_ingredient:
        return jsonify({
            "status" : True,
            "message" : "Ingrediente excluído com sucesso"
        })
    else:
        return jsonify({
            "status" : False,
            "message" : "Falha ao tentar excluir este ingrediente"
        })