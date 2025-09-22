# Enter your task: Finish project report
# Priority (high/medium/low): high
# Is it time-bound? (yes/no): yes

# Reminder: 'Finish project report' is a high priority task that requires immediate attention today!


task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ")
time_bounded = input("Is it time-bound? (yes/no): ")

match Priority:
    case "high":
        print(
            f"Reminder: 'Finish project {task}' is a {Priority} priority task that requires immediate attention today!")
    case "medium":
        print(
            f"Reminder: 'Finish project {task}' is a {Priority} priority task that requires attention this week!")
    case "low":
        print(
            f"Note: {task}is a {Priority} priority task. Consider completing it when you have free time.")
