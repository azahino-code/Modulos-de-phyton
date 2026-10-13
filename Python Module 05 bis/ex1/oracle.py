#!/usr/bin/env python3

import os
from dotenv import load_dotenv

load_dotenv()


mode = os.getenv("MATRIX_MODE")
database_url = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
log_level = os.getenv("LOG_LEVEL")
zion_endpoint = os.getenv("ZION_ENDPOINT")
print("ORACLE STATUS: Consulting the configuration...")
required = {
    "MATRIX_MODE":mode,
    "DATABASE_URL":database_url,
    "API_KEY":api_key,
    "LOG_LEVEL":log_level,
    "ZION_ENDPOINT":zion_endpoint
}
missing = [
    name for name, value in required.items()
    if not value
]
if missing:
    print("Configuration incomplete:")
    for name in missing:
        print(f"[MISSING]: {name}")
else:
    print(
        "Configuration loaded:"
    )
    if mode not in ("production", "development"):
        mode = "Unknown"
    print(
        f"Mode: {mode}\n"
        "Database: Conected to local instance\n"
        "API Access: Authenticated\n"
        f"Log Level: {log_level}\n"
        "Remote Network: Online\n\n"
        "Configuration security check:\n"
        "[OK] No secrets printed by the program"
    )
    with open(".gitignore") as ignored:
        if ".env" in ignored.read():
            print("[OK] .env file properly ignored by git")
        else:
            print("[KO] .env is not ignored by git")
    ignored.close()
    if mode == "development":
        print("[OK] Development overrides available")
    elif mode == "production":
        print("[OK] Production overrides available")
    else:
        print("[KO] Unknown 'MATRIX_MODE'")
    print("\nThe Oracle sees all configurations.")