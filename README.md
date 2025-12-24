k## Project Structure

```text
soar-incident-response/
├── alerts/
│   └── alerts.json          # Sample security alerts (input)
├── config/
│   └── response_rules.json  # Response playbooks and actions
├── reports/
│   └── incident_report.txt  # Generated incident reports
├── src/
│   ├── alert_ingestor.py    # Loads and parses alerts
│   ├── decision_engine.py  # Determines response actions
│   ├── response_engine.py  # Executes response playbooks
│   ├── mitre_mapper.py     # Maps alerts to MITRE ATT&CK
│   ├── reporter.py         # Generates incident reports
│   └── main.py             # Application entry point
├── README.md
├── requirements.txt
└── .gitignore

