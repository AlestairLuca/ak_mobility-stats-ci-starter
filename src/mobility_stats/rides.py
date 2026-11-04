import csv
import os
from collections import defaultdict


def load_rides(path: str) -> list[dict[str, object]]:
    """Load ride data from a CSV file."""
    rides = []
    if not os.path.exists(path):
        raise FileNotFoundError(f"Could not find file: {path}")
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for a in r:
            rides.append(
                {
                    "ride_id": a["ride_id"],
                    "start_station": a["start_station"],
                    "end_station": a["end_station"],
                    "duration_min": float(a["duration_min"]),
                    "rider_type": a["rider_type"],
                }
            )
    return rides


def average_duration(rides):
    """Return the average ride duration in minutes."""
    if len(rides) == 0:
        return 0.0
    total = 0.0
    for ride in rides:
        total += ride["duration_min"]
    return total / len(rides)


def count_by_rider_type(rides):
    """Count rides for each rider type."""
    riders = defaultdict(int)
    for ride in rides:
        riders[ride["rider_type"]] += 1
    return dict(riders)


def busiest_start_station(rides):
    """Return the start station with the most rides."""
    if rides is None:
        raise ValueError("rides must not be None")
    if len(rides) == 0:
        raise ValueError("rides must not be empty")
    stations = {}
    for ride in rides:
        station = ride["start_station"]
        stations[station] = stations.get(station, 0) + 1
    return max(stations, key=stations.get)


def filter_long_rides(rides, max_duration=30):
    """Return all rides with duration greater than or equal to b minutes."""
    long_rides = []
    for ride in rides:
        if ride["duration_min"] >= max_duration:
            long_rides.append(ride)
    return long_rides
