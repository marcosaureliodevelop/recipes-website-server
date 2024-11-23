from ..extensions import db

class Ingredients(db.Model):
    id_ingredient = db.Column(db.Integer, primary_key=True)
    id_recipe = db.Column(db.Integer, nullable=False)
    ingredient_description = db.Column(db.String(150), nullable=False)
    
    @classmethod
    def insert(cls, id_recipe, ingredient_description):
        new_ingredient = cls(
            id_recipe=id_recipe,
            ingredient_description=ingredient_description
        )
        
        db.session.add(new_ingredient)
        db.session.commit()
        
        return new_ingredient

    @classmethod
    def update(cls, id_ingredient, ingredient_description):
        # atualiza somente a descrição do ingrediente
        ingredient = cls.query.get(id_ingredient)
        if ingredient:
            ingredient.ingredient_description = ingredient_description

            db.session.commit()
            return ingredient
        else:
            return None

    @classmethod
    def get(cls, id_ingredient):
        ingredient = cls.query.get(id_ingredient)
        return ingredient.to_dict()

    @classmethod
    def get_all(cls):
        ingredients = cls.query.all()
        ingredient_dict = [ingredient.to_dict() for ingredient in ingredients]
        return ingredient_dict
    
    @classmethod
    def get_for_recipe(cls, id_recipe):
        ingredients = cls.query.filter_by(id_recipe=id_recipe).all()
        ingredient_dict = [ingredient.to_dict() for ingredient in ingredients]
        return ingredient_dict

    @classmethod
    def delete(cls, id_ingredient):
        ingredient = cls.query.get(id_ingredient)
        if ingredient:
            db.session.delete(ingredient)
            db.session.commit()
            
            return True
        else:
            return False
        
    # Método to_dict que converte a instância de Recipe para um dicionário
    def to_dict(self):
        return {
            "id_ingredient": self.id_ingredient,
            "id_recipe": self.id_recipe,
            "ingredient_description": self.ingredient_description
        }