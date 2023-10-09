high_floor = 102
low_floor = 1

ans_floor = 101  # assume

count_step = 1

guess_floor = (high_floor + low_floor) // 2

while guess_floor != ans_floor:
    if guess_floor > ans_floor:  # mean the egg break
        high_floor = guess_floor - 1
    else:  # mean the egg not break
        low_floor = guess_floor + 1

    guess_floor = (high_floor + low_floor) // 2

    count_step += 1

print(f"Take {count_step} eggs")
