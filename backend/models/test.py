from backend import db,ma

class Test(db.Model):
    name = db.Column(db.String(128), primary_key=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Test %r>' % self.name

class TestSchema(ma.ModelSchema):
	class Meta:
		model = Test