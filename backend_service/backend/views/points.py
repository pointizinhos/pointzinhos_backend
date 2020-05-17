from backend import Blueprint, request, db
from backend.models.assignment import Assignment, AssignmentSchema
from backend.models.redemption import Redemption, RedemptionSchema
from backend.models.client import Client, ClientSchema

points = Blueprint("points", __name__)

@points.route("/assign", methods=["POST"])
def assign():
    phone_number = request.args.get("phone_number")
    establishment_name = request.args.get("establishment_name")
    amount = request.args.get("amount")
    is_purchase = request.args.get("is_purchase")

	try:
        establishment = Establishment.query.filter_by(establishment_name=establishment_name).first()
        establishment_id = establishment.id

        client = Client.query.filter_by(phone_number=phone_number,establishment_id=establishment_id)
        client_id = client.id

        assignment = Assignment(client_id=client_id,establishment_id=establishment_id,amount=amount,is_purchase=is_purchase)
        db.session.add(assignment)
        db.session.commit()

        return True
    except Exception as e:
        print e.message, e.args
    
    return False

@points.route("/redeem", methods=["POST"])
def redeem():
    phone_number = request.args.get("phone_number")
    establishment_name = request.args.get("establishment_name")
    prize_id = request.args.get("prize_id")

    try:
        establishment = Establishment.query.filter_by(establishment_name=establishment_name).first()
        establishment_id = establishment.id

        client = Client.query.filter_by(phone_number=phone_number,establishment_id=establishment_id)
        client_id = client.id

        redemption = Redemption.query.filter_by(client_id=client_id,establishment_id=establishment_id,prize_id=prize_id).first()
        db.session.add(redemption)
        db.session.commit()

        return True
    except Exception as e:
        print e.message, e.args

    return False