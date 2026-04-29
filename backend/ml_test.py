# ===== ML TRAFFIC ANALYSIS MODULE =====

import numpy as np

# -------- FEATURE EXTRACTION --------
def extract_features(lane_counts):
    """
    Convert raw lane counts into ML features
    """
    total = sum(lane_counts)
    avg = np.mean(lane_counts)
    max_lane = max(lane_counts)
    min_lane = min(lane_counts)

    return {
        "total": total,
        "avg": avg,
        "max": max_lane,
        "min": min_lane
    }


# -------- TRAFFIC CLASSIFICATION --------
def classify_traffic(features):
    """
    Classify traffic level using ML-like logic
    """
    total = features["total"]

    if total > 50:
        return "HIGH"
    elif total > 25:
        return "MEDIUM"
    else:
        return "LOW"


# -------- GREEN TIME PREDICTION --------
def predict_green_time(features):
    """
    Predict green signal time dynamically
    """
    total = features["total"]

    # Base timing logic (acts like regression)
    if total > 50:
        return 60   # seconds
    elif total > 25:
        return 40
    else:
        return 20


# -------- FINAL ML PIPELINE --------
def ml_pipeline(lane_counts):
    """
    Complete ML pipeline
    """
    features = extract_features(lane_counts)
    traffic_level = classify_traffic(features)
    green_time = predict_green_time(features)

    return {
        "traffic_level": traffic_level,
        "predicted_green_time": green_time,
        "features": features
    }