def get_sensor_values(
    head,
    direction,
    food,
    occupied_positions,
    board_width,
    board_height
):
    x, y = head
    dx, dy = direction

    if abs(dx) + abs(dy) != 1:
        raise ValueError(
            "Direction must be a cardinal unit vector"
        )

    # Position directly in front of the snake
    ahead = (x + dx, y + dy)
    ax, ay = ahead

    # Check walls and occupied cells
    danger = (
        ax < 0
        or ax >= board_width
        or ay < 0
        or ay >= board_height
        or ahead in occupied_positions
    )

    # Food position relative to the snake's heading
    fx = food[0] - x
    fy = food[1] - y

    forward_projection = fx * dx + fy * dy
    side_projection = fx * dy - fy * dx

    food_ahead = (
        forward_projection > 0
        and forward_projection >= abs(side_projection)
    )

    food_behind = (
        forward_projection < 0
        and -forward_projection >= abs(side_projection)
    )

    food_left = (
    side_projection > 0
    and abs(side_projection) > abs(forward_projection)
)
    
    food_right = (
    side_projection < 0
    and abs(side_projection) > abs(forward_projection)
)

    return {
        "danger_ahead": float(danger),
        "path_clear": float(not danger),
        "food_left": float(food_left),
        "food_right": float(food_right),
        "food_ahead": float(food_ahead),
        "food_behind": float(food_behind),
    }