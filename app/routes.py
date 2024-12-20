from .controllers.recipes_controller import create_recipe, update_recipe, get_all_recipes, get_recipe, delete_recipe
from .controllers.ingredients_controller import create_ingredient, update_ingredient, get_all_ingredients, get_ingredient, delete_ingredient
from .controllers.preparation_methods_controller import create_method, update_method, get_all_methods, get_method, delete_method
from .controllers.images_controller import create_image, get_image
from .controllers.categories_controller import create_category, update_category, get_all_categories, get_category, delete_category
from .controllers.recipes_categories_controllers import create_recipe_category, update_recipe_category, get_all_recipes_categories, get_recipe_category, delete_recipe_category

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
    
    
    # categories routes
    @app.route('/categories/create', methods=['POST'])
    def create_category_route():
        return create_category()

    @app.route('/categories/update/<int:id_category>', methods=['PATCH'])
    def update_category_route(id_category):
        return update_category(id_category)

    @app.route('/categories/get_all', methods=['GET'])
    def get_all_categories_route():
        return get_all_categories()

    @app.route('/categories/get/<int:id_category>', methods=['GET'])
    def get_category_route(id_category):
        return get_category(id_category)

    @app.route('/categories/delete/<int:id_category>', methods=['DELETE'])
    def delete_category_route(id_category):
        return delete_category(id_category)
    
    
    # recipes categories routes
    @app.route('/recipes_categories/create', methods=['POST'])
    def create_recipes_categories_route():
        return create_recipe_category()

    @app.route('/recipes_categories/update/<int:id_recipe_category>', methods=['PATCH'])
    def update_recipe_category_route(id_recipe_category):
        return update_recipe_category(id_recipe_category)

    @app.route('/recipes_categories/get_all', methods=['GET'])
    def get_all_recipes_categories_route():
        return get_all_recipes_categories()

    @app.route('/recipes_categories/get/<int:id_recipe_category>', methods=['GET'])
    def get_recipe_category_route(id_recipe_category):
        return get_recipe_category(id_recipe_category)

    @app.route('/recipes_categories/delete/<int:id_recipe_category>', methods=['DELETE'])
    def delete_recipe_category_route(id_recipe_category):
        return delete_recipe_category(id_recipe_category)