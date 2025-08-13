from flask import request, abort
import time

rate_limit = {}
MAX_REQUESTS = 100
WINDOW = 10  # secondes

def anti_ddos_middleware():
    ip = request.remote_addr
    now = time.time()

    # Initialiser la liste des timestamps
    timestamps = rate_limit.get(ip, [])
    # Garder uniquement les requêtes dans la fenêtre
    timestamps = [t for t in timestamps if now - t < WINDOW]
    timestamps.append(now)
    rate_limit[ip] = timestamps

    if len(timestamps) > MAX_REQUESTS:
        print(f"IP bloquée : {ip} ({len(timestamps)} requêtes)")
        abort(429, description="Trop de requêtes")
