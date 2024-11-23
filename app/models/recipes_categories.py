from ..extensions import db

class RecipesCategories(db.Model):
    id_recipe_category = db.Column(db.Integer, primary_key=True)
    id_recipe = db.Column(db.Integer, nullable=False)
    id_category = db.Column(db.Integer, nullable=False)
    
    @classmethod
    def insert(cls, id_recipe, id_category):
        new_recipe_category = cls(
            id_recipe=id_recipe,
            id_category=id_category
        )
        
        db.session.add(new_recipe_category)
        db.session.commit()
        
        return new_recipe_category

    @classmethod
    def update(cls, id_recipe_category, id_recipe, id_category):
        recipe_category = cls.query.get(id_recipe_category)
        if recipe_category:
            recipe_category.id_recipe = id_recipe
            recipe_category.id_category = id_category

            db.session.commit()
            return recipe_category
        else:
            return None

    @classmethod
    def get(cls, id_recipe_category):
        recipe_category = cls.query.get(id_recipe_category)
        return recipe_category.to_dict()

    @classmethod
    def get_all(cls):
        recipes_categories = cls.query.all()
        recipes_categories_dict = [recipe_category.to_dict() for recipe_category in recipes_categories]
        return recipes_categories_dict

    @classmethod
    def delete(cls, id_recipe_category):
        item = cls.query.get(id_recipe_category)
        if item:
            db.session.delete(item)
            db.session.commit()
            
            return True
        else:
            return False
        
    # Método to_dict que converte a instância de Recipe para um dicionário
    def to_dict(self):
        return {
            "id_recipe_category": self.id_recipe_category,
            "id_recipe": self.id_recipe,
            "id_category": self.id_category
        }