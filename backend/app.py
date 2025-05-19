from flask import Flask, jsonify, render_template
from parser import parse_logs
from classifier import classify_events

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Render the dashboard template
    return render_template('dashboard.html')

@app.route('/api/logs', methods=['GET'])
def get_logs():
    # Parse the logs and classify each event
    raw_logs = parse_logs()
    classified_logs = classify_events(raw_logs)
    return jsonify(classified_logs)

if __name__ == '__main__':
    app.run(debug=True)
