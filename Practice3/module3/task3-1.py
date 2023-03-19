import csv
import datetime
import matplotlib.pyplot as plt
import ast


def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))


# Load the data
messages = load_csv('messages.csv')
checks = load_csv('checks.csv')
statuses = load_csv('statuses.csv')
"""

# Extract the timestamps of messages and checks
message_times = [parse_time(row[4]) for row in messages]
check_times = [parse_time(row[2]) for row in checks]
"""
"""
# Задача 1
# Count the number of messages and checks for each day of the week
message_counts = [0] * 7
check_counts = [0] * 7
for time in message_times:
    message_counts[time.weekday()] += 1
for time in check_times:
    check_counts[time.weekday()] += 1

# Plot the histogram
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
plt.bar(days_of_week, message_counts, label='Messages')
plt.bar(days_of_week, check_counts, label='Checks', alpha=0.5)
plt.legend()
plt.title('Student Activity by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Actions')
plt.show()


"""
"""
# Задача 2
# Extract the hours of the day for messages and checks
message_hours = [time.hour for time in message_times]
check_hours = [time.hour for time in check_times]

# Count the number of messages and checks for each hour of the day
message_counts = [0] * 24
check_counts = [0] * 24
for hour in message_hours:
    message_counts[hour] += 1
for hour in check_hours:
    check_counts[hour] += 1

# Plot the histogram
hours_of_day = [str(hour) for hour in range(24)]
plt.bar(hours_of_day, message_counts, label='Messages')
plt.bar(hours_of_day, check_counts, label='Checks', alpha=0.5)
plt.legend()
plt.title('Student Activity by Time of Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Actions')
plt.show()
"""

"""
# Задача 3
# Extract the task and group columns
tasks = [row[1] for row in messages]
groups = [row[3] for row in messages]

# Calculate the number of unique problems
unique_tasks = set(tasks)
num_tasks = len(unique_tasks)

# Calculate the total number of messages
num_messages = len(tasks)

# Calculate the average number of messages per problem
avg_messages_per_task = num_messages / num_tasks

print(f'Average messages per task: {avg_messages_per_task}')
"""

"""
# Задача 4
tasks = [row[1] for row in messages]
# Extract the timestamps of messages
message_times = [parse_time(row[4]) for row in messages]

# Calculate the earliest timestamp
earliest_time = min(message_times)
unique_tasks = set(tasks)
num_tasks = len(unique_tasks)
# Calculate the number of days since the earliest timestamp
days_since_start = [(time - earliest_time).days for time in message_times]

# Create a dictionary to store the number of messages for each task
task_counts = {}
for i, task in enumerate(tasks):
    if task not in task_counts:
        task_counts[task] = [0] * len(message_times)
    task_counts[task][i] += 1

# Plot the line chart
for task in unique_tasks:
    plt.plot(days_since_start, task_counts[task], label=task)
plt.legend()
plt.title('Student Activity by Task')
plt.xlabel('Days Since Beginning of Semester')
plt.ylabel('Number of Messages')
plt.show()
"""

"""
# Задача 5
# Create a dictionary to store the number of messages for each group
groups = [row[3] for row in messages]

group_counts = {}
for i, group in enumerate(groups):
    if group not in group_counts:
        group_counts[group] = 0
    group_counts[group] += 1

# Plot the histogram
plt.bar(group_counts.keys(), group_counts.values())
plt.title('Messages by Group')
plt.xlabel('Group')
plt.ylabel('Number of Messages')
plt.show()
"""

"""
#Задача 6
# Create a dictionary to store the number of correct solutions for each group
statuses = load_csv('statuses.csv')
groups = [row[2] for row in statuses]
tasks = [row[0] for row in statuses]
achievements = [row[5] for row in statuses]

# Create a dictionary to store the number of correct solutions for each group
correct_counts = {}
for i, group in enumerate(groups):
    if group not in correct_counts:
        correct_counts[group] = 0
    if achievements[i] == 'correct':
        correct_counts[group] += 1

# Plot the bar chart
plt.bar(correct_counts.keys(), correct_counts.values())
plt.title('Correct Solutions by Group')
plt.xlabel('Group')
plt.ylabel('Number of Correct Solutions')
plt.show()
"""

"""
# Задача 7
# Create a dictionary to store the number of correct and incorrect solutions for each task
statuses = load_csv('statuses.csv')
groups = [row[2] for row in statuses]
tasks = [row[0] for row in statuses]
achievements = [row[5] for row in statuses]

task_counts = {}
for i, task in enumerate(tasks):
    if task not in task_counts:
        task_counts[task] = {'correct': 0, 'incorrect': 0}
    if achievements[i] == 'correct':
        task_counts[task]['correct'] += 1
    else:
        task_counts[task]['incorrect'] += 1

# Plot the bar chart
tasks = sorted(task_counts.keys())
correct_counts = [task_counts[task]['correct'] for task in tasks]
incorrect_counts = [task_counts[task]['incorrect'] for task in tasks]
plt.bar(tasks, correct_counts, label='Correct')
plt.bar(tasks, incorrect_counts, bottom=correct_counts, label='Incorrect')
plt.legend()
plt.title('Solutions by Task')
plt.xlabel('Task')
plt.ylabel('Number of Solutions')
plt.show()
"""

"""
# Задача 8
achievements_by_group = {}
for row in statuses:
    group = row[2]
    achievements = row[5]
    if achievements.startswith('[') and achievements.endswith(']'):
        # If the achievements field is a list, extract the integer value from it
        achievements_list = ast.literal_eval(achievements)
        if len(achievements_list) > 0:
            achievements = achievements_list[0]
        else:
            achievements = 0
    else:
        achievements = int(achievements)
    if group not in achievements_by_group:
        achievements_by_group[group] = 0
    achievements_by_group[group] += achievements

# Plot a bar graph of achievements by group
plt.bar(achievements_by_group.keys(), achievements_by_group.values())
plt.xlabel('Group')
plt.ylabel('Total Achievements Earned')
plt.title('Achievements Earned by Group')
plt.show()
"""

"""
#Задача 9
# Extract the achievements data and group by student ID
achievements_by_student = {}
for row in statuses:
    student_id = row[0]
    achievements = row[5]
    if achievements.startswith('[') and achievements.endswith(']'):
        # If the achievements field is a list, extract the integer value from it
        achievements_list = ast.literal_eval(achievements)
        if len(achievements_list) > 0:
            achievements = achievements_list[0]
        else:
            achievements = 0
    else:
        achievements = int(achievements)
    if student_id not in achievements_by_student:
        achievements_by_student[student_id] = 0
    achievements_by_student[student_id] += achievements

# Sort the students by their total achievements in descending order
sorted_students = sorted(achievements_by_student.items(), key=lambda x: x[1], reverse=True)

# Print the top 10 students
num_students = min(len(sorted_students), 10)
for i in range(num_students):
    print(f"{i+1}. Student {sorted_students[i][0]} earned {sorted_students[i][1]} achievements.")
"""

"""
#Задача 9
# Create a dictionary to hold the number of unique solutions for each group and task
unique_solutions = {}

# Iterate over the checks list to count the number of unique solutions for each group and task
for row in checks:
    task = row[1]
    group = row[3]
    if task not in unique_solutions:
        unique_solutions[task] = {}
    if group not in unique_solutions[task]:
        unique_solutions[task][group] = set()
    unique_solutions[task][group].add(row[2])

# Iterate over the statuses list to compute the number of unique solutions for each group and task
for row in statuses:
    task = row[0]
    group = row[2]
    if task not in unique_solutions:
        unique_solutions[task] = {}
    if group not in unique_solutions[task]:
        unique_solutions[task][group] = set()
    if isinstance(row[5], str) and row[5].startswith('[') and row[5].endswith(']'):
        # If the achievements field is a list, extract the integer value from it
        achievements_list = ast.literal_eval(row[5])
        if len(achievements_list) > 0:
            unique_solutions[task][group].add(str(achievements_list[0]))
    elif isinstance(row[5], int):
        unique_solutions[task][group].add(str(row[5]))

# Compute the average number of unique solutions per group for each task
avg_unique_solutions = {}
for task, groups in unique_solutions.items():
    total_unique_solutions = sum(len(solutions) for solutions in groups.values())
    num_groups = len(groups)
    avg_unique_solutions[task] = total_unique_solutions / num_groups

# Sort the tasks by the average number of unique solutions per group
sorted_tasks = sorted(avg_unique_solutions.items(), key=lambda x: x[1], reverse=True)

# Print the tasks with the highest average number of unique solutions per group
for task, avg_solutions in sorted_tasks[:5]:
    print(f"{task}: {avg_solutions:.2f} unique solutions per group on average.")
"""

# Задача 10
