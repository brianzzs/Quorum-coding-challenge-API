from flask import Blueprint, jsonify
from app.services.bill_service import BillService
bill_bp = Blueprint('bill', __name__, url_prefix='/bill')

@bill_bp.route('/')
def get_bills(service: BillService):
    bills = service.get_bills()
    return jsonify(bills)

@bill_bp.route('/id/<int:bill_id>')
def get_bill_by_id(bill_id: int, service: BillService):
    bill = service.get_bill_by_id(bill_id)
    return jsonify(bill)

@bill_bp.route('/vote-summary')
def get_every_bill_vote_summary(service: BillService):
    return jsonify(service.get_every_bill_vote_summary())






