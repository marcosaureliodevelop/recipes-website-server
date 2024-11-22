from .controllers.recipes_controller import create_recipe, update_recipe, get_all_recipes, get_recipe, delete_recipe

def register_routes(app):
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