from src.brain.sensors import get_sensor_values


def test_detects_food_ahead():
    sensors = get_sensor_values(
        head=(5, 5),
        direction=(0, -1),
        food=(5, 2),
        occupied_positions={(5, 4)},
        board_width=10,
        board_height=10,
    )

    assert sensors["food_ahead"] == 1.0
    assert sensors["danger_ahead"] == 1.0
    assert sensors["path_clear"] == 0.0


def test_detects_food_to_the_left():
    sensors = get_sensor_values(
        head=(5, 5),
        direction=(1, 0),
        food=(5, 2),
        occupied_positions=set(),
        board_width=10,
        board_height=10,
    )

    assert sensors["food_left"] == 1.0
    assert sensors["danger_ahead"] == 0.0
    assert sensors["path_clear"] == 1.0


def test_detects_wall_ahead():
    sensors = get_sensor_values(
        head=(5, 0),
        direction=(0, -1),
        food=(8, 8),
        occupied_positions=set(),
        board_width=10,
        board_height=10,
    )

    assert sensors["danger_ahead"] == 1.0
    assert sensors["path_clear"] == 0.0