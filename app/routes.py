from app.controllers.recipes_controller import create_recipe

def register_routes(app):
    app.add_url_rule('/recipes/create', 'create_recipe', create_recipe, methods=['POST'])