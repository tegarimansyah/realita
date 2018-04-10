from flask import Flask, jsonify, abort, make_response
from flask_restful import Api, Resource, reqparse, fields, marshal

app = Flask(__name__)
api = Api(app)

# Mekanisme Routing
# Memanggil fungsi dan API


# Mekanisme Database


if __name__ == '__main__':
    app.run()