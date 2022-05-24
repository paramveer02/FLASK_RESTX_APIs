from flask_restx import Namespace, Resource

auth_ns = Namespace("auth", description="Namespace for authentication")


@auth_ns.route("/signup")
class SignUp(Resource):
    def post(self):
        """
        Register a new user account
        """
        pass


@auth_ns.route("/login")
class Login(Resource):
    def post(self):
        """
        Generate a JWT token
        """
        pass
