from backend import db, ma

class Credential(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    is_deleted = db.Column(db.Boolean)

    def __init__(self, username, password, id=None, is_deleted=None):
        self.id = id
        self.username = username
        self.password = password
        self.is_deleted = is_deleted

    def __repr__(self):
        return "<Credential %r>" % self.id % self.username % self.password % self.is_deleted

class CredentialSchema(ma.ModelSchema):
    class Meta:
        model = Credential
