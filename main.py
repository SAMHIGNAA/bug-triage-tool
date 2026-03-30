import logging
from src.reader import read_bugs
from src.analyzer import analyze_bugs, filter_by_priority, get_critical_bugs
from src.reporter import print_summary, print_critical, save_report

def main():
    # 🔹 Logging setup
    logging.basicConfig(
        filename="app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    print("=== Bug Triage Tool ===")
    logging.info("Application started")

    file_path = input("Enter file path (default: data/bugs.csv): ") or "data/bugs.csv"

    bugs = read_bugs(file_path)

    if not bugs:
        logging.error("No bugs loaded. Exiting.")
        return

    logging.info(f"Loaded {len(bugs)} bugs")

    priority_count, severity_count = analyze_bugs(bugs)

    print_summary(priority_count, severity_count)

    choice = input("\nFilter High priority bugs? (y/n): ")
    if choice.lower() == 'y':
        high_bugs = filter_by_priority(bugs, "High")
        print("\nHigh Priority Bugs:")
        for b in high_bugs:
            print(f"{b['id']} - {b['title']}")
        logging.info("Displayed high priority bugs")

    critical = get_critical_bugs(bugs)
    print_critical(critical)

    save_report(priority_count, severity_count)
    logging.info("Report generated successfully")

    print("\nReport saved!")

if __name__ == "__main__":
    main()
