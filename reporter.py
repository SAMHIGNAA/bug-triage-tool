def print_summary(priority_count, severity_count):
    print("\nPriority Count:")
    for k, v in priority_count.items():
        print(f"{k}: {v}")

    print("\nSeverity Count:")
    for k, v in severity_count.items():
        print(f"{k}: {v}")

def print_critical(bugs):
    print("\nCritical Bugs:")
    print("------------------")
    for b in bugs:
        print(f"{b['id']} - {b['title']}")

def save_report(priority_count, severity_count):
    with open("report.txt", "w") as f:
        f.write("Bug Report\n\n")

        f.write("Priority Count:\n")
        for k, v in priority_count.items():
            f.write(f"{k}: {v}\n")

        f.write("\nSeverity Count:\n")
        for k, v in severity_count.items():
            f.write(f"{k}: {v}\n")