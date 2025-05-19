import json
import os

def parse_logs():
    """
    Reads and parses the sample log file.
    """
    log_file = os.path.join('..', 'data', 'sample_logs.json')
    try:
        with open(log_file, 'r') as f:
            logs = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []
    return logs

if __name__ == '__main__':
    logs = parse_logs()
    print(json.dumps(logs, indent=2))
