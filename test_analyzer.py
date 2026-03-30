from src.analyzer import analyze_bugs, filter_by_priority, get_critical_bugs

def test_analyze_bugs():
    sample = [
        {"priority": "High", "severity": "Critical"},
        {"priority": "Low", "severity": "Minor"},
        {"priority": "High", "severity": "Major"}
    ]

    priority_count, severity_count = analyze_bugs(sample)

    assert priority_count["High"] == 2
    assert severity_count["Critical"] == 1


def test_filter_by_priority():
    sample = [
        {"id": 1, "priority": "High"},
        {"id": 2, "priority": "Low"}
    ]

    result = filter_by_priority(sample, "High")

    assert len(result) == 1
    assert result[0]["id"] == 1


def test_get_critical_bugs():
    sample = [
        {"id": 1, "severity": "Critical"},
        {"id": 2, "severity": "Minor"}
    ]

    result = get_critical_bugs(sample)

    assert len(result) == 1
    assert result[0]["id"] == 1