import json

UNKNOWN_ENTRY = {
    "technique_id": "UNKNOWN",
    "technique_name": "Unknown Technique",
    "tactic": "Unknown",
    "severity": "UNKNOWN",
}

def map_to_mitre(attack_type, ip):
    with open("mitre/mitre_mapping.json", "r", encoding="utf-8") as f:
        raw = f.read().strip()

    if not raw:
        raise ValueError("MITRE mapping file is empty at runtime")

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        raise ValueError(f"MITRE mapping file is not valid JSON: {e}") from e

    entry = data.get(attack_type, UNKNOWN_ENTRY)

    return {
        "attack": attack_type,
        "ip": ip,
        "technique_id": entry.get("technique_id", "UNKNOWN"),
        "technique_name": entry.get("technique_name", "Unknown Technique"),
        "tactic": entry.get("tactic", "Unknown"),
        "severity": entry.get("severity", "UNKNOWN"),
    }
