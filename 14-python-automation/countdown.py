# an app to count down to the time til deadline
import datetime

user_input = input("Enter your goal with a deadline. Separate it with a colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
time_till = deadline_date - today_date


print(f"Dear user, hello! The time remaining until your goal: {goal} is {int(time_till.total_seconds() / 60 / 60)} hours")
