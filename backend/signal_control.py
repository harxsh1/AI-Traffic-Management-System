def get_signal_plan(lane_counts):
    max_count = max(lane_counts)
    green_lane = lane_counts.index(max_count)

    # Decide traffic level
    if max_count > 30:
        traffic_level = "HIGH"
        green_time = 60
    elif max_count > 15:
        traffic_level = "MEDIUM"
        green_time = 40
    else:
        traffic_level = "LOW"
        green_time = 20

    return {
        "lane": green_lane + 1,
        "green_time": green_time,
        "traffic_level": traffic_level   
    }