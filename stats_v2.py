def get_stats(stats_list):
    stats_list.sort()

    lowest_point = stats_list[0]
    highest_point = stats_list[-1]
    point_average = sum(stats_list) / len(stats_list)
    return [lowest_point, highest_point, point_average]


user_points = [10, 0, 13, 7, 10, 11]
computer_points = [10, 11, 0, 0, 10, 11]

# for item in range(0, 6):
#     user_point = int(input("Please enter user score: "))
#     computer_point = int(input("Please enter computer score: "))
#
#     user_points.append(user_point)
#     computer_points.append(computer_point)

user_stats = get_stats(user_points)
comp_stats = get_stats(computer_points)

print("Game Stats")
print(f"User     - low {user_stats[0]}\t "
      f"high {user_stats[1]}\t "
      f"average {user_stats[2]}")

print(f"Computer - low {comp_stats[0]}\t "
      f"high {comp_stats[1]}\t "
      f"average {comp_stats[2]}")
