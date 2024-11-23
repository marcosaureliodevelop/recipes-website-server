from ..extensions import db

class PreparationMethods(db.Model):
    id_method = db.Column(db.Integer, primary_key=True)
    id_recipe = db.Column(db.Integer, nullable=False)
    method_description = db.Column(db.String(500), nullable=False)
    
    @classmethod
    def insert(cls, id_recipe, method_description):
        new_method = cls(
            id_recipe=id_recipe,
            method_description=method_description
        )
        
        db.session.add(new_method)
        db.session.commit()
        
        return new_method

    @classmethod
    def update(cls, id_method, method_description):
        # atualiza somente a descrição do ingrediente
        method = cls.query.get(id_method)
        if method:
            method.method_description = method_description

            db.session.commit()
            return method
        else:
            return None

    @classmethod
    def get(cls, id_method):
        method = cls.query.get(id_method)
        return method.to_dict()

    @classmethod
    def get_all(cls):
        methods = cls.query.all()
        methods_dict = [method.to_dict() for method in methods]
        return methods_dict
    
    @classmethod
    def get_for_recipe(cls, id_recipe):
        methods = cls.query.filter_by(id_recipe=id_recipe).all()
        methods_dict = [method.to_dict() for method in methods]
        return methods_dict

    @classmethod
    def delete(cls, id_method):
        method = cls.query.get(id_method)
        if method:
            db.session.delete(method)
            db.session.commit()
            
            return True
        else:
            return False
        
    # Método to_dict que converte a instância de Recipe para um dicionário
    def to_dict(self):
        return {
            "id_method": self.id_method,
            "id_recipe": self.id_recipe,
            "method_description": self.method_description
        }