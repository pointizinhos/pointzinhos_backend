from backend import db, ma

class Prize(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    photo = db.Column(db.String(100))
    amount_to_redeem = db.Column(db.Integer)
    description = db.Column(db.String(100))
    is_deleted = db.Column(db.Boolean)
    establishment_id = db.Column(db.Integer)

    def __init__(self,id=None,name,photo,amount_to_redeem,description,is_deleted=None,establishment_id):
        self.id = id
        self.name = name
        self.photo = photo
        self.amount_to_redeem = amount_to_redeem
        self.description = description
        self.is_deleted = is_deleted
        self.establishment_id = establishment_id

    def __repr__(self):
        return "<Prize %r>" % self.id % self.name % self.photo % self.amount_to_redeem % self.description % self.is_deleted % self.establishment_id

class PrizeSchema(ma.ModelSchema):
    class Meta:
        model = Prize
