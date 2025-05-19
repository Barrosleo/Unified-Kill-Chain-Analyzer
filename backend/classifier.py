def classify_event(event):
    """
    Classify a security event into a Unified Kill Chain phase.
    Example classification rules:
      - If the event action contains "login" or "access", classify as "In"
      - If the event action contains "lateral" or "propagation", classify as "Through"
      - If the event action contains "exfiltration" or "data", classify as "Out"
      - Otherwise, classify as "Unknown"
    """
    action = event.get("action", "").lower()
    if "login" in action or "access" in action:
        return "In"
    elif "lateral" in action or "propagation" in action:
        return "Through"
    elif "exfiltration" in action or "data" in action:
        return "Out"
    else:
        return "Unknown"

def classify_events(events):
    """
    Process a list of events and add a 'phase' key based on their classification.
    """
    for event in events:
        event['phase'] = classify_event(event)
    return events

if __name__ == '__main__':
    # For testing purposes, call parse_logs from the parser module
    sample_events = [
        {"timestamp": "2025-05-15T10:00:00Z", "action": "User login from suspicious location", "artifact": "192.168.1.50"},
        {"timestamp": "2025-05-15T10:05:00Z", "action": "Lateral movement detected between hosts", "artifact": "Host123"},
        {"timestamp": "2025-05-15T10:10:00Z", "action": "Data exfiltration using encrypted channel", "artifact": "EncryptedPayload"}
    ]
    classified = classify_events(sample_events)
    import json
    print(json.dumps(classified, indent=2))
