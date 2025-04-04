from flask import Blueprint, jsonify
from app.services.legislator_service import LegislatorService

legislator_bp = Blueprint('legislator', __name__, url_prefix='/legislator')


@legislator_bp.route('/')
def get_all_legislators(service: LegislatorService):
    legislators = service.get_legislators()
    return jsonify(legislators)

# just in case someone wants to test the api with a specific legislator id
@legislator_bp.route('/id/<int:legislator_id>')
def get_legislator_by_id(legislator_id: int, service: LegislatorService):
    legislator = service.get_legislator_by_id(legislator_id)
    return jsonify(legislator)

@legislator_bp.route('/id/<int:legislator_id>/bills-supported')
def get_count_bills_supported_by_legislator(legislator_id: int, service: LegislatorService):
    return jsonify(service.get_count_bills_supported_by_legislator(legislator_id))

@legislator_bp.route('/id/<int:legislator_id>/bills-opposed')
def get_count_bills_opposed_by_legislator(legislator_id: int, service: LegislatorService):
    return jsonify(service.get_count_bills_opposed_by_legislator(legislator_id))








