from backend import Blueprint, request, db
from backend.models.test import Test,TestSchema

testing = Blueprint('testing', __name__)

@testing.route("/get_test", methods=['GET'])
def get_test():
	test = Test.query.first()
	testSchema = TestSchema()
	outputTest = testSchema.dump(test).data
	return outputTest

@testing.route("/post_test", methods=['POST'])
def post_test():
	name=request.args.get('name')

	try:
		test=Test(name=name)
		db.session.add(test)
		db.session.commit()
		return "Test succeeded!"
	except Exception as e:
		return(str(e))