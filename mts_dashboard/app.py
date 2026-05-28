import pandas as pd
import os
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Load & prepare data once at startup
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

routes_df     = pd.read_csv(os.path.join(DATA_DIR, "routes.txt"))
trips_df      = pd.read_csv(os.path.join(DATA_DIR, "trips.txt"))
stops_df      = pd.read_csv(os.path.join(DATA_DIR, "stops.txt"))
stop_times_df = pd.read_csv(os.path.join(DATA_DIR, "stop_times.txt"), low_memory=False)

# Build the route dropdown options sorted by route_id (numeric where possible)
routes_sorted = routes_df.copy()
routes_sorted["_sort_key"] = pd.to_numeric(routes_sorted["route_id"], errors="coerce")
routes_sorted = routes_sorted.sort_values(
    ["_sort_key", "route_id"], na_position="last"
).drop(columns="_sort_key")

route_options = [
    {
        "route_id": str(row["route_id"]),
        "label": f"{row['route_short_name']} - {row['route_long_name']}",
    }
    for _, row in routes_sorted.iterrows()
]

# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html", route_options=route_options)


@app.route("/api/directions")
def directions():
    """Return sorted direction_name values for a given route_id."""
    route_id = request.args.get("route_id", "")
    dirs = (
        trips_df.loc[trips_df["route_id"].astype(str) == str(route_id), "direction_name"]
        .dropna()
        .unique()
        .tolist()
    )
    dirs_sorted = sorted(dirs)
    return jsonify(dirs_sorted)


@app.route("/api/timetable")
def timetable():
    """Return stop-time rows for a route + direction, sorted by stop_sequence."""
    route_id  = request.args.get("route_id", "")
    direction = request.args.get("direction", "")

    # Filter trips to this route + direction (all IDs stored as strings)
    trip_mask = (
        (trips_df["route_id"].astype(str) == str(route_id)) &
        (trips_df["direction_name"] == direction)
    )

    trip_ids = trips_df.loc[trip_mask, "trip_id"].unique()

    if len(trip_ids) == 0:
        return jsonify([])

    # Use the first trip_id as the representative schedule for this route/direction
    representative_trip = trip_ids[0]

    # Get stop times for that trip
    st = stop_times_df[stop_times_df["trip_id"] == representative_trip].copy()
    st["stop_id"] = st["stop_id"].astype(str)

    # Join to stops to get stop_name
    stops_lookup = stops_df[["stop_id", "stop_name"]].copy()
    stops_lookup["stop_id"] = stops_lookup["stop_id"].astype(str)
    st = st.merge(stops_lookup, on="stop_id", how="left")

    # Sort by stop_sequence and select display columns
    st = st.sort_values("stop_sequence")[
        ["stop_sequence", "arrival_time", "departure_time", "stop_name"]
    ]

    return jsonify(st.to_dict(orient="records"))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
