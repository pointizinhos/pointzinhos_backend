from backend import Blueprint, request, db
from backend.models.establishment import Establishment, EstablishmentSchema, 
from backend.models.credential import Credential, CredentialSchema

establishments = Blueprint("establishments", __name__)

@establishments.route("/create", methods=["POST"])
def create():
    username = request.args.get("username")
    password = request.args.get("password")
    name = request.args.get("name")
    address = request.args.get("address")
    operator = request.args.get("operator")
    description = request.args.get("description")
    whatsapp = request.args.get("whatsapp")
    email = request.args.get("email")
    points_money_ratio = request.args.get("points_money_ratio")
    photos = request.args.get("photos")

	try:
        credential = Credential.query.filter_by(username=username,password=password)
        credentials_id = credential.id

        establishment = Establishment(credentials_id=credentials_id,name=name,address=address,operator=operator,description=description,whatsapp=whatsapp,email=email,points_money_ratio=points_money_ratio,photos=photos)
        db.session.add(establishment)
        db.session.commit()

        return True
    except Exception as e:
        print e.message, e.args
    
    return False

@establishments.route("/update", methods=["POST"])
def update():
    username = request.args.get("username")
    password = request.args.get("password")
    name = request.args.get("name")
    address = request.args.get("address")
    operator = request.args.get("operator")
    description = request.args.get("description")
    whatsapp = request.args.get("whatsapp")
    email = request.args.get("email")
    points_money_ratio = request.args.get("points_money_ratio")
    photos = request.args.get("photos")
    delete = request.args.get("delete")
    
    try:
        credential = Credential.query.filter_by(username=username,password=password)
        credentials_id = credential.id

        establishment = Establishment.query.filter_by(credentials_id=credentials_id).first()

        if(establishment is not null):
            if(delete):
                establishment.is_deleted = True
            else:
                establishment.name = name
                establishment.address = address
                establishment.operator = operator
                establishment.description = description
                establishment.whatsapp = whatsapp
                establishment.email = email
                establishment.points_money_ratio = points_money_ratio
                establishment.photos = photos    
            db.session.commit()
            
            return True
    except Exception as e:
        print e.message, e.args
            
    return False

@establishments.route("/read", methods=["GET"])
def read():
    username = request.args.get("username")
    password = request.args.get("password")

    try:
        credential = Credential.query.filter_by(username=username,password=password)
        credentials_id = credential.id

        establishment = Establishment.query.filter_by(credential_id=credentials_id).first()

        if(establishment is not null):
            establishmentSchema = EstablishmentSchema()
            return establishmentSchema.dump(establishment).data
    except Exception as e:
        print e.message, e.args
    
    return False