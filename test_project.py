import pytest
from project import calculate_bmr, estimate_calories_burned, recommend_workout_plan

def test_calculate_bmr():
    assert round(calculate_bmr(70, 175, 25, "male"), 2) == 1723.86
    assert round(calculate_bmr(60, 160, 30, "female"), 2) == 1366.60
    assert calculate_bmr(80, 180, 40, "other") is None

def test_estimate_calories_burned():
    assert estimate_calories_burned("running", 30, 70) == pytest.approx(360.15, rel=1e-2)
    assert estimate_calories_burned("cycling", 45, 80) == pytest.approx(472.50, rel=1e-2)
    assert estimate_calories_burned("unknown_activity", 30, 70) is None

def test_recommend_workout_plan():
    assert recommend_workout_plan("beginner", "weight loss") == "30 min cardio, 3x per week + light strength training"
    assert recommend_workout_plan("advanced", "muscle gain") == "Body part split strength training, 5-6x per week"
    assert recommend_workout_plan("intermediate", "general fitness") == "Balanced cardio and weights, 5x per week"
    assert recommend_workout_plan("invalid_level", "weight loss") == "No plan available"