from backend import db, ma

class Establishment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    credentials_id = db.Column(db.Integer)
    name = db.Column(db.String(50))
    address = db.Column(db.String(100))
    operator = db.Column(db.String(50))
    description = db.Column(db.String(100))
    whatsapp = db.Column(db.String(50))
    email = db.Column(db.String(50))
    points_money_ratio = db.Column(db.Integer)
    photos = db.Column(db.Array(String(100)))
    is_deleted = db.Column(db.Boolean)

    def __init__(self, id=None,credentials_id,name,address,operator,description,whatsapp,email,points_money_ratio,photos,is_deleted=None):
        id = db.Column(db.Integer, primary_key=True)
        credentials_id = db.Column(db.Integer)
        name = db.Column(db.String(50))
        address = db.Column(db.String(100))
        operator = db.Column(db.String(50))
        description = db.Column(db.String(100))
        whatsapp = db.Column(db.String(50))
        email = db.Column(db.String(50))
        points_money_ratio = db.Column(db.Integer)
        photos = db.Column(db.Array(String(100)))
        is_deleted = db.Column(db.Boolean)

    def __repr__(self):
        return "<Establishment %r>" % self.id % self.credentials_id % self.name % self.address % self.operator % self.description % self.whatsapp % self.email % self.points_money_ratio % self.photos % self.is_deleted

class EstablishmentSchema(ma.ModelSchema):
    class Meta:
        model = Establishment
