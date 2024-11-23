from ..extensions import db

class Recipes(db.Model):
    id_recipe = db.Column(db.Integer, primary_key=True)
    id_image = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    time = db.Column(db.Integer, nullable=False)
    portions = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    registration_date = db.Column(db.Integer, nullable=False)
    
    @classmethod
    def insert(cls, id_image, name, description, time, portions, status, registration_date):
        new_recipe = cls(
            id_image=id_image,
            name=name,
            description=description,
            time=time,
            portions=portions,
            status=status,
            registration_date=registration_date
        )
        
        db.session.add(new_recipe)
        db.session.commit()
        
        return new_recipe

    @classmethod
    def update(cls, id_recipe, id_image, name, description, time, portions, status):
        recipe = cls.query.get(id_recipe)
        if recipe:
            recipe.id_image = id_image
            recipe.name = name
            recipe.description = description
            recipe.time = time
            recipe.portions = portions
            recipe.status = status

            db.session.commit()
            return recipe
        else:
            return None

    @classmethod
    def get(cls, id_recipe):
        recipe = cls.query.get(id_recipe)
        return recipe.to_dict()

    @classmethod
    def get_all(cls):
        recipes = cls.query.all()
        recipes_dict = [recipe.to_dict() for recipe in recipes]
        return recipes_dict

    @classmethod
    def delete(cls, id_recipe):
        item = cls.query.get(id_recipe)
        if item:
            db.session.delete(item)
            db.session.commit()
            
            return True
        else:
            return False
        
    # Método to_dict que converte a instância de Recipe para um dicionário
    def to_dict(self):
        return {
            "id_recipe": self.id_recipe,
            "id_image": self.id_image,
            "name": self.name,
            "description": self.description,
            "time": self.time,
            "portions": self.portions,
            "status": self.status,
            "registration_date": self.registration_date
        }