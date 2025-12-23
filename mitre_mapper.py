import json

def map_to_mitre(attack_type, ip):
    with open("mitre/mitre_mapping.json", "r", encoding="utf-8") as f:
        raw = f.read().strip()

    if not raw:
        raise ValueError("MITRE mapping file is empty at runtime")

    data = json.loads(raw)

    return {
        "attack": attack_type,
        "ip": ip,
        "technique_id": data[attack_type]["technique_id"],
        "technique_name": data[attack_type]["technique_name"],
        "tactic": data[attack_type]["tactic"],
        "severity": data[attack_type]["severity"]
    }
