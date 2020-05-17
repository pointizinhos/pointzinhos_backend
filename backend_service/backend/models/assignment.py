from backend import db, ma

class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer)
    establishment_id = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    is_purchase = db.Column(db.Boolean)

    def __init__(self,id=None,client_id,establishment_id,amount,is_purchase):
        self.id = id
        self.client_id = client_id
        self.establishment_id = establishment_id
        self.amount = amount
        self.is_purchase = is_purchase

    def __repr__(self):
        return "<Assignment %r>" % self.id % self.client_id % self.establishment_id % self.amount % self.is_purchase

class AssignmentSchema(ma.ModelSchema):
    class Meta:
        model = Assignment
