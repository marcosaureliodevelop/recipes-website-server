from flask import request, jsonify
from ..models.recipes_categories import RecipesCategories

def create_recipe_category():
    data = request.get_json()
    
    if not data:
        return jsonify({
            "status": False,
            "message": "Erro: Nenhum dado encontrado na requisição."
        }), 400
    
    required_fields = ['id_recipe', 'id_category']
    missing_fields = [field for field in required_fields if field not in data]
    
    if missing_fields:
        return jsonify({
            "status": False,
            "message": f"Faltando os campos: {', '.join(missing_fields)}"
        }), 400
    
    id_recipe = data.get('id_recipe')
    id_category = data.get('id_category')
    
    new_recipe_category = RecipesCategories.insert(id_recipe, id_category)
    
    if new_recipe_category:
        return jsonify({
            "status": True,
            "message": "Categoria de receita cadastrada com sucesso!",
            "id_recipe_category": new_recipe_category.id_recipe_category
        }), 201
    
    return jsonify({
        "status": False,
        "message": "Falha ao tentar cadastrar categoria de receita."
    }), 500
    
def update_recipe_category(id_recipe_category):
    data = request.get_json()
    
    if not data:
        return jsonify({
            "status": False,
            "message": "Erro: Nenhum dado encontrado na requisição."
        }), 400
        
    required_fields = ['id_recipe', 'id_category']
    missing_fields = [field for field in required_fields if field not in data]
    
    if missing_fields:
        return jsonify({
            "status": False,
            "message": f"Faltando os campos: {', '.join(missing_fields)}"
        }), 400
    
    id_recipe = data.get('id_recipe')
    id_category = data.get('id_category')
    
    update = RecipesCategories.update(id_recipe_category, id_recipe, id_category)
    
    if update:
        return jsonify({
            "status": True,
            "message": "Categoria de receita atualizada com sucesso!"
        }), 200 
    else: jsonify({
        "status": False,
        "message": "Falha ao tentar atualizar essa categoria de receita."
    }), 400
    
def get_all_recipes_categories():
    categories = RecipesCategories.get_all()
    return jsonify({
        "status" : True,
        "categories" : categories
    })
    
def get_recipe_category(id_recipe_category):
    recipe_category = RecipesCategories.get(id_recipe_category)
    return jsonify({
        "status" : False, 
        "category" : recipe_category
    })
    
def delete_recipe_category(id_recipe_category):
    delete_category = RecipesCategories.delete(id_recipe_category)
    
    if delete_category:
        return jsonify({
            "status" : True,
            "message" : "Categoria de receita removida com sucesso!"
        })
    else:
        return jsonify({
            "status" : False,
            "message" : "Falha ao tentar remover categoria de receita."
        })