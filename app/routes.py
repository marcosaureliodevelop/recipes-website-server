from .controllers.recipes_controller import create_recipe, update_recipe, get_all_recipes, get_recipe, delete_recipe
from .controllers.ingredients_controller import create_ingredient, update_ingredient, get_all_ingredients, get_ingredient, delete_ingredient

def register_routes(app):
    
    # recipes routes
    @app.route('/recipes/create', methods=['POST'])
    def create_recipe_route():
        return create_recipe()

    @app.route('/recipes/update/<int:id_recipe>', methods=['PATCH'])
    def update_recipe_route(id_recipe):
        return update_recipe(id_recipe)

    @app.route('/recipes/get_all', methods=['GET'])
    def get_all_recipe_route():
        return get_all_recipes()

    @app.route('/recipes/get/<int:id_recipe>', methods=['GET'])
    def get_recipe_route(id_recipe):
        return get_recipe(id_recipe)

    @app.route('/recipes/delete/<int:id_recipe>', methods=['DELETE'])
    def delete_recipe_route(id_recipe):
        return delete_recipe(id_recipe)
    
    
    # ingredients routes
    @app.route('/ingredients/create', methods=['POST'])
    def create_ingredient_route():
        return create_ingredient()

    @app.route('/ingredients/update/<int:id_ingredient>', methods=['PATCH'])
    def update_ingredient_route(id_ingredient):
        return update_ingredient(id_ingredient)

    @app.route('/ingredients/get_all', methods=['GET'])
    def get_all_ingredients_route():
        return get_all_ingredients()

    @app.route('/ingredients/get/<int:id_ingredient>', methods=['GET'])
    def get_ingredient_route(id_ingredient):
        return get_ingredient(id_ingredient)

    @app.route('/ingredients/delete/<int:id_ingredient>', methods=['DELETE'])
    def delete_ingredient_route(id_ingredient):
        return delete_ingredient(id_ingredient)