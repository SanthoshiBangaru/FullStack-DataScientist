# 3. Classroom Performance Tracker
def calculate_average(students):
    averages = {name: round(sum(marks)/len(marks), 2) for name, marks in students.items()}
    return averages

def top_performer(averages):
    return max(averages, key=averages.get)

if __name__ == "__main__":
    students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
    avg = calculate_average(students)
    print("Average Marks:", avg)
    print("Top Performer:", top_performer(avg))