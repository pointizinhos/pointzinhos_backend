from backend import Blueprint, request

basic = Blueprint("basic", __name__)


@basic.route("/schi")
def index():
    return "This is the pointzinhos backend API"
