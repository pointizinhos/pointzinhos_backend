from backend import db, ma

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(50))
    name = db.Column(db.String(100))
    assigned_gender = db.Column(db.String(50))
    assigned_age = db.Column(db.String(50))
    email = db.Column(db.String(50))
    is_deleted = db.Column(db.Boolean)
    establishment_id = db.Column(db.Integer)

    def __init__(self, id=None,phone_number,name,assigned_gender,assigned_age,email,is_deleted=None,establishment_id):
        self.id = id
        self.phone_number = phone_number
        self.name = name
        self.assigned_gender = assigned_gender
        self.assigned_age = assigned_age
        self.email = email
        self.is_deleted = is_deleted
        self.establishment_id = establishment_id

    def __repr__(self):
        return "<Client %r>" % self.id % self.phone_number % self.name % self.assigned_gender % self.assigned_age % self.email % self.is_deleted % self.establishment_id

class ClientSchema(ma.ModelSchema):
    class Meta:
        model = Client
