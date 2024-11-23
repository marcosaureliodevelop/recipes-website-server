from .controllers.recipes_controller import create_recipe, update_recipe, get_all_recipes, get_recipe, delete_recipe
from .controllers.ingredients_controller import create_ingredient, update_ingredient, get_all_ingredients, get_ingredient, delete_ingredient
from .controllers.preparation_methods_controller import create_method, update_method, get_all_methods, get_method, delete_method
from .controllers.images_controller import create_image, get_image

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
    
    
    # methods routes
    @app.route('/methods/create', methods=['POST'])
    def create_method_route():
        return create_method()

    @app.route('/methods/update/<int:id_method>', methods=['PATCH'])
    def update_method_route(id_method):
        return update_method(id_method)

    @app.route('/methods/get_all', methods=['GET'])
    def get_all_methods_route():
        return get_all_methods()

    @app.route('/methods/get/<int:id_method>', methods=['GET'])
    def get_method_route(id_method):
        return get_method(id_method)

    @app.route('/methods/delete/<int:id_method>', methods=['DELETE'])
    def delete_method_route(id_method):
        return delete_method(id_method)
    
    
    # image routes
    @app.route('/images/create', methods=['POST'])
    def create_image_route():
        return create_image()

    @app.route('/images/get/<int:id_image>', methods=['GET'])
    def get_image_route(id_image):
        return get_image(id_image)