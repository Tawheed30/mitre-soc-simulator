import re
from collections import defaultdict
from mitre_mapper import map_to_mitre
from responder import respond

failed_attempts = defaultdict(int)

with open("logs/auth.log") as log:
    for line in log:
        if "Failed password" in line:
            match = re.search(r'from ([\d.]+)', line)
            if not match:
                continue

            ip = match.group(1)
            failed_attempts[ip] += 1

            if failed_attempts[ip] == 3:
                incident = map_to_mitre("SSH_BRUTE_FORCE", ip)
                respond(incident)
