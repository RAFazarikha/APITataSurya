from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Data awal planet-planet dalam tata surya
planets = {
    "1": {
        "name": "Mercury",
        "description": "Planet terdekat dari matahari dan terkecil di tata surya.",
        "diameter_km": 4879,
        "moons": 0,
        "orbit_period_days": 88
    },
    "2": {
        "name": "Venus",
        "description": "Planet kedua dari matahari dengan suhu permukaan tertinggi.",
        "diameter_km": 12104,
        "moons": 0,
        "orbit_period_days": 225
    },
    "3": {
        "name": "Earth",
        "description": "Planet ketiga dari matahari dan satu-satunya yang diketahui memiliki kehidupan.",
        "diameter_km": 12742,
        "moons": 1,
        "orbit_period_days": 365
    },
    "4": {
        "name": "Mars",
        "description": "Planet keempat yang dikenal sebagai 'Planet Merah'.",
        "diameter_km": 6779,
        "moons": 2,
        "orbit_period_days": 687
    }
    # Tambahkan data planet lainnya jika diperlukan
}

# Endpoint untuk mendapatkan semua planet
class PlanetList(Resource):
    def get(self):
        return {
            "error": False,
            "message": "Success",
            "count": len(planets),
            "planets": planets
        }

# Endpoint untuk mendapatkan detail planet berdasarkan ID
class PlanetDetail(Resource):
    def get(self, planet_id):
        if planet_id in planets:
            return {
                "error": False,
                "message": "Success",
                "planet": planets[planet_id]
            }
        return {"error": True, "message": "Planet not found"}, 404

# Endpoint untuk menambahkan planet baru
class AddPlanet(Resource):
    def post(self):
        data = request.get_json()
        planet_id = str(len(planets) + 1)
        new_planet = {
            "name": data.get("name"),
            "description": data.get("description"),
            "diameter_km": data.get("diameter_km"),
            "moons": data.get("moons"),
            "orbit_period_days": data.get("orbit_period_days")
        }
        planets[planet_id] = new_planet
        return {
            "error": False,
            "message": "Planet added successfully",
            "planet": new_planet
        }, 201

# Endpoint untuk mengupdate data planet berdasarkan ID
class UpdatePlanet(Resource):
    def put(self, planet_id):
        if planet_id in planets:
            data = request.get_json()
            planet = planets[planet_id]
            planet["name"] = data.get("name", planet["name"])
            planet["description"] = data.get("description", planet["description"])
            planet["diameter_km"] = data.get("diameter_km", planet["diameter_km"])
            planet["moons"] = data.get("moons", planet["moons"])
            planet["orbit_period_days"] = data.get("orbit_period_days", planet["orbit_period_days"])
            return {
                "error": False,
                "message": "Planet updated successfully",
                "planet": planet
            }
        return {"error": True, "message": "Planet not found"}, 404

# Endpoint untuk menghapus data planet berdasarkan ID
class DeletePlanet(Resource):
    def delete(self, planet_id):
        if planet_id in planets:
            deleted_planet = planets.pop(planet_id)
            return {
                "error": False,
                "message": "Planet deleted successfully",
                "planet": deleted_planet
            }
        return {"error": True, "message": "Planet not found"}, 404

# Menambahkan endpoint ke API
api.add_resource(PlanetList, '/planets')
api.add_resource(PlanetDetail, '/planets/<string:planet_id>')
api.add_resource(AddPlanet, '/planets/add')
api.add_resource(UpdatePlanet, '/planets/update/<string:planet_id>')
api.add_resource(DeletePlanet, '/planets/delete/<string:planet_id>')

if __name__ == '__main__':
    app.run(debug=True)
