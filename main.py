# main.py

# Function to get a task from the user
task = input("Enter your task: ")

# Ask the user if the task is complete
complete = input("Is the task complete? (yes/no): ")

# Check the user's response and print accordingly
if complete.lower() == 'yes':
    print(f'Task "{task}" is marked as complete.')
else:
    print(f'Task "{task}" is still pending.')
