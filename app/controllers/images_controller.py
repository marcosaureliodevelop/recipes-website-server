from flask import request, jsonify
from ..models.images import Images

def create_image():
    data = request.get_json()
    
    if not data:
        return jsonify({
            "status": False,
            "message": "Erro: Nenhum dado encontrado na requisição."
        }), 400
    
    required_fields = ['path', 'alt']
    missing_fields = [field for field in required_fields if field not in data]
    
    if missing_fields:
        return jsonify({
            "status": False,
            "message": f"Faltando os campos: {', '.join(missing_fields)}"
        }), 400
    
    path = data.get('path')
    alt = data.get('alt')
    
    new_image = Images.insert(path, alt)
    
    if new_image:
        return jsonify({
            "status": True,
            "message": "Imagem cadastrada com sucesso!",
            "id_image": new_image.id_image
        }), 201
    
    return jsonify({
        "status": False,
        "message": "Erro ao tentar cadastrar método de preparo."
    }), 500
    
def get_image(id_image):
    image = Images.get(id_image)
    return jsonify({
        "status" : False, 
        "image" : image
    })