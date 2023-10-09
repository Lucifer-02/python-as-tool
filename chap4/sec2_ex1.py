def log(x, base, epsilon):
    """Assumes x and epsilon int or float, base an int,
        x > 1, epsilon > 0 & power >= 1
    Returns float y such that base**y is within epsilon of x."""

    lower_bound = 0
    while base**lower_bound < x:
        lower_bound += 1

    high = lower_bound + 1
    low = lower_bound - 1

    power = (high + low) / 2

    while abs(base**power - x) > epsilon:
        if base**power > x:
            high = power
        else:
            low = power

        power = (high + low) / 2

    return power


def test_log(x_vals, bases, epsilons):
    for x in x_vals:
        for base in bases:
            for epsilon in epsilons:
                power = log(x, base, epsilon)
                result = "Not Pass"
                if base**power > epsilon:
                    result = "Pass"

                print(f"x={x}, base={base}, epsilon={epsilon}, {result}")


x_vals = (1, 52.6, 48, 2)
bases = (2, 8, 10, 6)
epsilons = (0.001, 0.01, 0.005)

test_log(x_vals, bases, epsilons)
