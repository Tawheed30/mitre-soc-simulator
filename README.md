# MITRE ATT&CK SOC Incident Response Simulator

## Overview
This project simulates a real-world Security Operations Center (SOC) workflow.
It analyzes Linux authentication logs to detect SSH brute-force attacks, maps
them to MITRE ATT&CK techniques, and triggers automated incident response actions.

## Key Features
- SSH brute-force attack detection from authentication logs
- MITRE ATT&CK technique mapping (T1110 – Brute Force)
- Severity-based automated incident response
- Alert logging for SOC visibility
- SOC-style incident report generation

## Project Architecture
Logs → Detection Engine → MITRE Mapping → Incident Response → SOC Report

## Technologies Used
- Python
- Linux Authentication Logs
- MITRE ATT&CK Framework
- SOC & Incident Response Concepts

## How to Run
```bash
python3 detector.py
python3 report_generator.py

