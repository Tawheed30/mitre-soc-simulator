from datetime import datetime

def respond(incident):
    action = "BLOCK IP & RESET CREDENTIALS"

    log = (
        f"{datetime.now()} | "
        f"{incident['attack']} | "
        f"{incident['technique_id']} | "
        f"{incident['severity']} | "
        f"IP: {incident['ip']} | "
        f"Action: {action}\n"
    )

    print(log)

    with open("response/incident_actions.log", "a") as f:
        f.write(log)
