import http.client

from flask import Flask

from app import util
from app.calc import Calculator

CALCULATOR = Calculator()
api_application = Flask(__name__)
HEADERS = {"Content-Type": "text/plain", "Access-Control-Allow-Origin": "*"}


@api_application.route("/")
def hello():
    return "Hello from The Calculator!\n"


@api_application.route("/calc/add/<op_1>/<op_2>", methods=["GET"])
def add(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.add(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/calc/substract/<op_1>/<op_2>", methods=["GET"])
def substract(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.substract(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)



# nuevo codigo 


@api_application.route("/calc/multiply/<op_1>/<op_2>", methods=["GET"])
def multiply(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.multiply(num_1, num_2)), http.client.OK, HEADERS)
    except (TypeError, InvalidPermissions) as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route("/calc/divide/<op_1>/<op_2>", methods=["GET"])
def divide(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.divide(num_1, num_2)), http.client.OK, HEADERS)
    except (TypeError, ValueError) as e:  # Captura errores de tipo y división por cero
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route("/calc/power/<op_1>/<op_2>", methods=["GET"])
def power(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.power(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)



@api_application.route("/calc/raiz_cuadrada/<op>", methods=["GET"])
def raiz_cuadrada(op):
    try:
        num = util.convert_to_number(op)
        return ("{}".format(CALCULATOR.raiz_cuadrada(num)), http.client.OK, HEADERS)
    except Exception as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route("/calc/logaritmo_base_diez/<op>", methods=["GET"])
def logaritmo_base_diez(op):
    try:
        num = util.convert_to_number(op)
        return ("{}".format(CALCULATOR.logaritmo_base_diez(num)), http.client.OK, HEADERS)
    except Exception as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)