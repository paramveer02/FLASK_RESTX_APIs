from flask_restx import Namespace, Resource

orders_ns = Namespace("orders", description="Namespace for orders")


@orders_ns.route("/orders")
class OrderGetCreate(Resource):
    def get(self):
        """
        Get all orders
        """
        pass

    def post(self):
        """
        Create a new order
        """
        pass


@orders_ns.route("/order/<int:order_id>")
class GetUpdateDeleteOrder(Resource):
    def get(self, order_id):
        """
        Retrieve an order by id
        """
        pass

    def put(self, order_id):
        """
        Retrieve an order by id and update
        """
        pass

    def delete(self, order_id):
        """
        Retrieve and order by id and delete
        """
        pass


@orders_ns.route("/users/<int:user_id>/orders")
class UserSpecificOrders(Resource):
    def get(self, user_id):
        """
        Get all orders belonging to a specific user
        """
        pass
