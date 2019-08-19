from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from store import extract_telemetry_data, store_name

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# allows to easily add resources
api = Api(app)


class TelemetryData(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        # retrieving "start" and "end" arguments from the query string
        parser.add_argument("end", type=int)
        parser.add_argument("start", type=int)
        args = parser.parse_args()
        # extract data as json array of records
        data = extract_telemetry_data("timestamp", args.start, args.end)
        # returns a json for any client to process
        return jsonify({
            "data": data,
            "log": store_name,
            "end": args.end,
            "start": args.start
        })


# define the endpoint
api.add_resource(TelemetryData, "/telemetry-data")

app.run(port=5000)
