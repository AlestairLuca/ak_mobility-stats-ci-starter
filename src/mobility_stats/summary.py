from mobility_stats.rides import average_duration, busiest_start_station, count_by_rider_type


def build_summary(input):
    """Build a compact dictionary with headline statistics."""
    headline_statistics = {
        "ride_count": len(input),
        "average_duration": average_duration(input),
        "rider_types": count_by_rider_type(input),
    }
    if input:
        headline_statistics["busiest_start_station"] = busiest_start_station(input)
    else:
        headline_statistics["busiest_start_station"] = None
    return headline_statistics


def format_summary(statistics):
    """Create a human-readable text summary."""
    title = "Mobility summary"
    line1 = f"Rides: {statistics['ride_count']}"
    line2 = f"Average duration: {statistics['average_duration']:.1f} min"
    line3 = f"Busiest start: {statistics['busiest_start_station']}"
    return title + "\n" + line1 + "\n" + line2 + "\n" + line3
