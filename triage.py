import csv
from collections import Counter

def read_bugs(file_path):
    bugs = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            bugs.append(row)
    return bugs

def analyze_bugs(bugs):
    priorities = [bug['priority'] for bug in bugs]
    severities = [bug['severity'] for bug in bugs]

    priority_count = Counter(priorities)
    severity_count = Counter(severities)

    return priority_count, severity_count

def show_critical_bugs(bugs):
    print("\nCritical Bugs:")
    print("------------------")
    for bug in bugs:
        if bug['severity'].lower() == 'critical':
            print(f"ID: {bug['id']} | Title: {bug['title']}")

def save_report(priority_count, severity_count):
    with open("report.txt", "w") as file:
        file.write("Bug Triage Report\n")
        file.write("------------------\n")

        file.write("\nPriority Count:\n")
        for k, v in priority_count.items():
            file.write(f"{k}: {v}\n")

        file.write("\nSeverity Count:\n")
        for k, v in severity_count.items():
            file.write(f"{k}: {v}\n")

def main():
    file_path = input("Enter bug file name (default: bugs.csv): ") or "bugs.csv"

    bugs = read_bugs(file_path)
    priority_count, severity_count = analyze_bugs(bugs)

    print("\nBug Triage Report")
    print("------------------")

    print("\nPriority Count:")
    for k, v in priority_count.items():
        print(f"{k}: {v}")

    print("\nSeverity Count:")
    for k, v in severity_count.items():
        print(f"{k}: {v}")

    show_critical_bugs(bugs)
    save_report(priority_count, severity_count)

    print("\nReport saved as report.txt")

if __name__ == "__main__":
    main()