from sumo.sumo_control import run_sumo
from flask import Flask, jsonify
from flask_cors import CORS

from signal_control import get_signal_plan
# from yolo_detector import get_lane_counts  (use later)

app = Flask(__name__)
CORS(app)

# Dummy data for now
lane_counts = [12, 25]


# HOME ROUTE
@app.route("/data")
def get_data():

    lane_counts = [12, 25]

    # TEMP manual values (NO ERROR)
    green_lane = 2
    green_time = 40

    # Launch SUMO
    run_sumo(lane_counts)

    return jsonify({
        "lane_counts": lane_counts,
        "green_lane": green_lane,
        "green_time": green_time
    })


if __name__ == "__main__":
    app.run(debug=True)