# Unified Kill Chain Analyzer

## Purpose
Develop a tool that ingests security event data and maps individual events or alert artifacts to the phases of the Unified Kill Chain—from initial foothold ("In"), through network propagation ("Through"), to actions on objectives ("Out"). This tool helps SOC analysts visualize the progression of an attack, identify detection gaps, and refine mitigation strategies.

## Repository Structure
```
Unified-Kill-Chain-Analyzer/
├── backend/
│   ├── app.py                 # Main Flask app handling API endpoints and rendering the dashboard template
│   ├── parser.py              # Module for log ingestion and parsing
│   ├── classifier.py          # Module for mapping event artifacts to Unified Kill Chain phases
│   ├── requirements.txt       # Python dependencies
│   └── templates/
│       └── dashboard.html     # HTML template served by Flask for the dashboard
├── frontend/
│   ├── index.html             # Standalone dashboard page (if not using Flask’s built-in templates)
│   ├── css/
│   │   └── styles.css         # Styling for the dashboard
│   └── js/
│       └── dashboard.js       # JavaScript for fetching data and rendering visualizations via Chart.js
├── data/
│   └── sample_logs.json       # Example log file for testing and demonstration
└── README.md                  # Project overview, setup instructions, and usage guidelines
```

## Key Features
- **Log Ingestion & Parsing:**  
  Upload sample log files or connect to threat intelligence sources to ingest security event data. The tool parses logs and extracts key artifacts (e.g., IP addresses, suspicious commands).

- **Phase Classification:**  
  A rules-based engine assigns each event/artifact to a Unified Kill Chain phase:
  - **In:** Initial foothold
  - **Through:** Network propagation
  - **Out:** Actions on objectives

- **Threat Visualization Dashboard:**  
  A web interface displays a timeline/flowchart representing the progression of events through the kill chain phases using visual charts (bar charts, flow diagrams, etc.).

- **Reporting & Alerts:**  
  Generate detailed reports on which phases are most active; optionally trigger threshold alerts when a phase accumulates a high number of suspicious events.

- **Threat Intelligence (Optional):**  
  Enrich IoC data via public APIs (e.g., VirusTotal, MISP).

## Tech Stack
- **Backend:** Python with Flask for log ingestion, processing, and phase classification.
- **Frontend:** HTML/CSS/JavaScript with Chart.js for lightweight dashboard visualization.
- **Data Storage:** JSON files (or lightweight databases like SQLite).

## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/Unified-Kill-Chain-Analyzer.git
   cd Unified-Kill-Chain-Analyzer
   ```
   
2.  **Install Backend Dependencies:**
  ```
  cd backend
  pip install -r requirements.txt
  ```

3.  **Run the Flask App:**
  ```
  python app.py
  ```

4.  **View the Dashboard:**

- **Option 1:** Open http://localhost:5000 to see the Flask-served dashboard.

= **Option 2:** Alternatively, open the standalone frontend/index.html in your browser.

## Future Enhancements

- **SIEM Integration:** Pre-built detection rules for Splunk or ELK.

- **Automated Reporting:** Generate PDF reports for SOC teams.

- **Interactive Simulation Modes:** Red Team vs. Blue Team exercises.

## License

This project is licensed under the MIT License.
