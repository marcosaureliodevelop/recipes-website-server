from ..extensions import db

class Images(db.Model):
    id_image = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(250), nullable=False)
    alt = db.Column(db.String(250), nullable=False)
    
    @classmethod
    def insert(cls, path, alt):
        new_image = cls(
            path=path,
            alt=alt
        )
        
        db.session.add(new_image)
        db.session.commit()
        
        return new_image

    @classmethod
    def get(cls, id_image):
        image = cls.query.get(id_image)
        return image.to_dict()
        
    # Método to_dict que converte a instância de Recipe para um dicionário
    def to_dict(self):
        return {
            "id_image": self.id_image,
            "path": self.path,
            "alt": self.alt
        }