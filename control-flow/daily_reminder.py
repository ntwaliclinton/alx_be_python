# daily_reminder.py

def daily_reminder():
    # Prompt the user for a task description
    task = input("Enter your task: ").strip()
    
    # Prompt the user for the task's priority
    priority = input("Priority (high/medium/low): ").strip().lower()
    
    # Prompt the user to check if the task is time-bound
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    
    # Process the task based on priority and time sensitivity using match case
    match priority:
        case 'high':
            reminder = f"Reminder: '{task}' is a high priority task."
        case 'medium':
            reminder = f"Note: '{task}' is a medium priority task."
        case 'low':
            reminder = f"Note: '{task}' is a low priority task."
        case _:
            reminder = f"Note: '{task}' has an unknown priority level."
    
    # Modify the reminder if the task is time-bound
    if time_bound == 'yes':
        reminder += " It requires immediate attention today!"
    elif time_bound == 'no':
        reminder += " Consider completing it when you have free time."
    else:
        reminder += " The time sensitivity of this task is unclear."
    
    # Print the customized reminder
    print("Reminder:", reminder)

if __name__ == "__main__":
    daily_reminder()

