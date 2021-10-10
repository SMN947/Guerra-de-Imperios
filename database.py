from pymongo import MongoClient
import json

with open("config.json",'r') as f:
    CONFIG = json.load(f)

client = MongoClient(CONFIG["uri"])
db = client["Test"]
usuarios = db["usuarios"]

class DB():
    #def __init__(self):
        
    #collection.insert_one({"_id": "SMN947", "buildings": {}})
    def CrearBase(user):
        if usuarios.find({"_id": user.id}).count() == 0:
            usuarios.insert_one({
                "_id": user.id,
                "nombre": user.name,
                "recursos": {
                    "dinero": {"nombre": "💶Dinero", "valor": 1000},
                    "comida": {"nombre": "🍔Comida", "valor": 1000},
                    "hierro": {"nombre": "📎Hierro", "valor": 1000},
                    "madera": {"nombre": "🧱Madera", "valor": 1000},
                    "carbon": {"nombre": "⬛Carbon", "valor": 1000},
                    "petroleo": {"nombre": "💦Petroleo", "valor": 1000}
                },
                "edificios": {
                    "0": {
                        "nombre": "Centro de mando",
                        "nivel": "1",
                        "hp": 5000,
                    }
                },
                "unidades": {
                    "0": {
                        "nombre": "Espadachines",
                        "cantidad": 120,
                    }
                }

            })
            return True
        else:
            return False
    
    def recursos(user):
        if usuarios.find({"_id": user.id}).count() == 0:
            return False
        else:
            res = usuarios.find_one({"_id": user.id})
            res = res["recursos"]
            return res