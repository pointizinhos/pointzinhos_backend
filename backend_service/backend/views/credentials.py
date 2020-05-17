from backend import Blueprint, request, db
from backend.models.credential import Credential, CredentialSchema

credentials = Blueprint("credentials", __name__)

@credentials.route("/create", methods=["POST"])
def create():
    username = request.args.get("username")
    password = request.args.get("password")

	try:
        credential = Credential(username=username,password=password)
        db.session.add(credential)
        db.session.commit()

        return True
    except Exception as e:
        print e.message, e.args
    
    return False

@credentials.route("/update", methods=["POST"])
def update():
    username = request.args.get("username")
    password = request.args.get("password")
    new_password = request.args.get("new_password")
    delete = request.args.get("delete")

    try:
        credential = Credential.query.filter_by(username=username,password=password).first()

        if(credential is not null):
            if(delete):
                credential.is_deleted = True
            else:
                credential.password = new_password
            db.session.commit()

            return True
    except Exception as e:
        print e.message, e.args
            
    return False