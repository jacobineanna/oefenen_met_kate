from flask import Flask
from flask_cors import CORS
import hbo_max_jacobine
from flask import Flask, jsonify

app = Flask(__name__)
cors = CORS(app)

@app.route("/jacobine")
def jacobinestrial():
    parsed, json_res_num_votes, json_res_rating, json_res_correlatie = hbo_max_jacobine.start()
    return jsonify({"parsed": parsed, "num_votes": json_res_num_votes, "ratings": json_res_rating, "correlatie": json_res_correlatie})
