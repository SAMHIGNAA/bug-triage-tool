import csv
from collections import Counter

def analyze_bugs(file_path):
    priorities = []
    severities = []

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            priorities.append(row['priority'])
            severities.append(row['severity'])

    print("Bug Triage Report")
    print("------------------")

    print("\nPriority Count:")
    for k, v in Counter(priorities).items():
        print(f"{k}: {v}")

    print("\nSeverity Count:")
    for k, v in Counter(severities).items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    analyze_bugs("bugs.csv")