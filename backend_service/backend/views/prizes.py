from backend import Blueprint, request, db
from backend.models.prize import Prize, PrizeSchema

prizes = Blueprint("prizes", __name__)

@prizes.route("/create", methods=["POST"])
def create():
    name = request.args.get("name")
    photo = request.args.get("photo")
    amount_to_redeem = request.args.get("amount_to_redeem")
    description = request.args.get("description")
    establishment_id = request.args.get("establishment_id")

	try:
        prize = Prize(name=name,photo=photo,amount_to_redeem=amount_to_redeem,description=description,establishment_id=establishment_id)
        db.session.add(prize)
        db.session.commit()
        
        return True
    except Exception as e:
        print e.message, e.args

    return False

@prizes.route("/update", methods=["POST"])
def update():
    name = request.args.get("name")
    photo = request.args.get("photo")
    amount_to_redeem = request.args.get("amount_to_redeem")
    description = request.args.get("description")
    delete = request.args.get("delete")
    establishment_id = request.args.get("establishment_id")

    prize = Prize.query.filter_by(name=name,establishment_id=establishment_id).first()

    if(prize is not null):
        try:
            if(delete):
                prize.is_deleted = True
            else:
                prize.name = name
                prize.photo = photo
                prize.amount_to_redeem = amount_to_redeem
                prize.description = description
            db.session.commit()

            return True
        except Exception as e:
            print e.message, e.args

    return False
