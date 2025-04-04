from flask import Blueprint, jsonify
from app.services.vote_result_service import VoteResultService

vote_results_bp = Blueprint('vote_results', __name__, url_prefix='/vote_results')

@vote_results_bp.route('/')
def get_all_vote_results(service: VoteResultService):
    vote_results = service.get_vote_results()
    return jsonify(vote_results)

@vote_results_bp.route('/bill/<int:bill_id>')
def get_vote_results_by_bill_id(bill_id: int, service: VoteResultService):
    vote_results_by_bill_id = service.get_vote_result_by_bill_id(bill_id)
    return jsonify(vote_results_by_bill_id)





