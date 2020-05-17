from backend import Blueprint, request, db
from backend.models.client import Client, ClientSchema
from backend.models.establishment import Establishment, EstablishmentSchema

clients = Blueprint("clients", __name__)

@clients.route("/create", methods=["POST"])
def create():
    phone_number = request.args.get("phone_number")
    name = request.args.get("name")
    assigned_gender = request.args.get("assigned_gender")
    assigned_age = request.args.get("assigned_age")
    email = request.args.get("email")    
    establishment_name = request.args.get("establishment_name")

	try:
        establishment = Establishment.query.filter_by(establishment_name=establishment_name).first()
        establishment_id = establishment.id

        client = Client(phone_number=phone_number,name=name,assigned_gender=assigned_gender,assigned_age=assigned_age,email=email,establishment_id=establishment_id)
        db.session.add(client)
        db.session.commit()

        return True
    except Exception as e:
        print e.message, e.args
    
    return False

@clients.route("/update", methods=["POST"])
def update():
    phone_number = request.args.get("phone_number")
    name = request.args.get("name")
    assigned_gender = request.args.get("assigned_gender")
    assigned_age = request.args.get("assigned_age")
    email = request.args.get("email")
    delete = request.args.get("delete")
    establishment_name = request.args.get("establishment_name")

    try:
        establishment = Establishment.query.filter_by(establishment_name=establishment_name).first()
        establishment_id = establishment.id

        client = Client.query.filter_by(phone_number=phone_number,establishment_id=establishment_id).first()

        if(client is not null):
            if(delete):
                client.is_deleted = True
            else:
                client.phone_number = phone_number
                client.name = name
                client.assigned_gender = assigned_gender
                client.assigned_age = assigned_age
                client.email = email
                client.establishment_id = establishment_id
            db.session.commit()

            return True
    except Exception as e:
        print e.message, e.args
            
    return False

@clients.route("/read", methods=["GET"])
def read():
    establishment_name = request.args.get("establishment_name")

    try:
        establishment = Establishment.query.filter_by(establishment_name=establishment_name).first()
        establishment_id = establishment.id

        if(establishment_id is not null):
            clients = Client.query.filter_by(establishment_id=establishment_id)
            clientSchema = ClientSchema()
            return clientSchema.dump(clients).data # check this, given multiple

    except Exception as e:
        print e.message, e.args
    
    return False