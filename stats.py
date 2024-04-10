user_points = []
computer_points = []

for item in range(0, 6):
    user_point = int(input("Please enter user score: "))
    computer_point = int(input("Please enter computer score: "))

    user_points.append(user_point)
    computer_points.append(computer_point)

user_points.sort()
computer_points.sort()

user_low = user_points[0]
user_high = user_points[-1]
user_average = sum(user_points) / len(user_points)

print("low ", user_low)
print("high ", user_high)
print("average ", user_average)
