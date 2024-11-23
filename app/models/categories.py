from ..extensions import db

class Categories(db.Model):
    id_category = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(80), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    registration_date = db.Column(db.Integer, nullable=False)
    
    @classmethod
    def insert(cls, category_name, status, registration_date):
        new_category = cls(
            category_name=category_name,
            status=status,
            registration_date=registration_date
        )
        
        db.session.add(new_category)
        db.session.commit()
        
        return new_category

    @classmethod
    def update(cls, id_category, category_name, status):
        category = cls.query.get(id_category)
        if category:
            category.category_name = category_name
            category.status = status

            db.session.commit()
            return category
        else:
            return None

    @classmethod
    def get(cls, id_category):
        category = cls.query.get(id_category)
        return category.to_dict()

    @classmethod
    def get_all(cls):
        categories = cls.query.all()
        categories_dict = [category.to_dict() for category in categories]
        return categories_dict

    @classmethod
    def delete(cls, id_category):
        item = cls.query.get(id_category)
        if item:
            db.session.delete(item)
            db.session.commit()
            
            return True
        else:
            return False
        
    # Método to_dict que converte a instância de Recipe para um dicionário
    def to_dict(self):
        return {
            "id_category": self.id_category,
            "category_name": self.category_name,
            "status": self.status,
            "registration_date": self.registration_date,
        }