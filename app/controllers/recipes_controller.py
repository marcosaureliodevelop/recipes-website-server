from flask import request, jsonify
from ..models.recipes import Recipes
from datetime import datetime

def create_recipe():
    data = request.get_json()
    
    if not data:
        return jsonify({
            "status": False,
            "message": "Erro: Nenhum dado encontrado na requisição."
        }), 400
    
    required_fields = ['id_image', 'name', 'description', 'time', 'portions']
    missing_fields = [field for field in required_fields if field not in data]
    
    if missing_fields:
        return jsonify({
            "status": False,
            "message": f"Faltando os campos: {', '.join(missing_fields)}"
        }), 400
    
    id_image = data.get('id_image')
    name = data.get('name')
    description = data.get('description')
    time = data.get('time')
    portions = data.get('portions')
    status = 1
    registration_date = int(datetime.now().timestamp())
    
    new_recipe = Recipes.insert(
        id_image,
        name,
        description,
        time,
        portions,
        status,
        registration_date
    )
    
    if new_recipe:
        return jsonify({
            "status": True,
            "message": "Receita cadastrada com sucesso!",
            "id_recipe": new_recipe.id_recipe
        }), 201
    
    return jsonify({
        "status": False,
        "message": "Erro ao cadastrar a receita"
    }), 500
    
def update_recipe(id_recipe):
    data = request.get_json()
    
    if not data:
        return jsonify({
            "status": False,
            "message": "Erro: Nenhum dado encontrado na requisição."
        }), 400
        
    required_fields = ['id_image', 'name', 'description', 'time', 'portions', 'status']
    missing_fields = [field for field in required_fields if field not in data]
    
    if missing_fields:
        return jsonify({
            "status": False,
            "message": f"Faltando os campos: {', '.join(missing_fields)}"
        }), 400
    
    id_image = data.get('id_image')
    name = data.get('name')
    description = data.get('description')
    time = data.get('time')
    portions = data.get('portions')
    status = data.get('status')
    
    update_recipe = Recipes.update(
        id_recipe,
        id_image,
        name,
        description,
        time,
        portions,
        status
    )
    
    if update_recipe:
        return jsonify({
            "status": True,
            "message": "Receita atualizada com sucesso!"
        }), 200 
    else: jsonify({
        "status": False,
        "message": "Erro ao tentar atualizar esta receita."
    }), 400
    
def get_all_recipes():
    recipes = Recipes.get_all()
    return jsonify({
        "status" : True,
        "recipes" : recipes
    })
    
def get_recipe(id_recipe):
    recipe = Recipes.get(id_recipe)
    return jsonify({
        "status" : False, 
        "recipe" : recipe
    })
    
def delete_recipe(id_recipe):
    delete_recipe = Recipes.delete(id_recipe)
    
    if delete_recipe:
        return jsonify({
            "status" : True,
            "message" : "Receita excluída com sucesso"
        })
    else:
        return jsonify({
            "status" : False,
            "message" : "Falha ao tentar excluir esta receita"
        })