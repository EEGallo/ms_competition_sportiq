from flask import jsonify, Blueprint, request
from app.services.competition_services import CompetitionService
from app.models.response_message import ResponseBuilder
from app.mapping import ResponseSchema, CompetitionSchema
from app.services.atomic_process import AtomicProcess
import random

competition = Blueprint('competition', __name__)
competition_schema = CompetitionSchema()
response_schema = ResponseSchema()

"""
id: int ingresado por el usuario
return: json con los datos del usuario
"""

@competition.route('/', methods=['GET'])
def index():
    resp = jsonify({"microservicio": "4", "status": "ok"})
    resp.status_code = random.choice([200, 404])
    return resp

@competition.route('/add/', methods=['POST'])
def post_competition():
    try:
        service = CompetitionService()
        competition = competition_schema.load(request.json)
        created_competition = service.create(competition)
        response = {"competition": competition_schema.dump(created_competition)}
        return jsonify(response), 201
    except Exception as e:
        error_message = f"Error al agregar competición: {str(e)}"
        return jsonify({"error": error_message}), 400


@competition.route('/<int:id>', methods=['GET'])
def find(id):
    service = CompetitionService()
    raffle = service.find_by_id(id)

    if raffle:
        response_builder = ResponseBuilder()
        response_builder.add_message("Competición encontrada").add_status_code(100).add_data(competition_schema.dump(raffle))
        return jsonify(response_schema.dump(response_builder.build()))
    else:
        return jsonify({"error": "Competición no encontrado"}), 404


@competition.route('/all', methods=['GET'])
def find_all():
    service = CompetitionService()
    response_builder = ResponseBuilder()
    competitions = service.find_all()
    competitions_json = [competition_schema.dump(competition) for competition in competitions]
    response_builder.add_message("Competiciones encontradas").add_status_code(100).add_data({'competitions': competitions_json})
    return response_schema.dump(response_builder.build())
  

@competition.route('/update/<int:competition_id>', methods=['PUT'])
def update_competition(competition_id):
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Datos de competición no proporcionados"}), 400

        service = CompetitionService()
        updated_competition = service.update(competition_id, data)

        if updated_competition:
            response_builder = ResponseBuilder()
            response_builder.add_message("Competición actualizado con éxito").add_status_code(200).add_data(competition_schema.dump(updated_competition))
            return response_schema.dump(response_builder.build())

        return jsonify({"error": "La competición no se pudo actualizar"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@competition.route('/delete/<int:competition_id>', methods=['DELETE'])
def delete_competition(competition_id):
    try:
        service = CompetitionService()
        deleted = service.delete(competition_id)

        if deleted:
            return jsonify({"message": "Competición eliminada con éxito", "status_code": 200}), 200

        return jsonify({"error": "Competición no encontrado", "status_code": 404}), 404
    except Exception as e:
        return jsonify({"error": str(e), "status_code": 500}), 500