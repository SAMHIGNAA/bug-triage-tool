from collections import Counter

def analyze_bugs(bugs):
    priorities = [b['priority'] for b in bugs]
    severities = [b['severity'] for b in bugs]

    return Counter(priorities), Counter(severities)

def filter_by_priority(bugs, level):
    return [b for b in bugs if b['priority'].lower() == level.lower()]

def get_critical_bugs(bugs):
    return [b for b in bugs if b['severity'].lower() == 'critical']