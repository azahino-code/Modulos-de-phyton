#!/usr/bin/env python3

import sys
import os
import site

if __name__ == "__main__":
    if sys.prefix == sys.base_prefix:
        print("LABORATORY STATUS: You are working in the open\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print(
            "WARNING: You are in the global environment"
            "\nEvery reagent you install here leaks into the whole system.\n"
            "\nTo seal the laboratory, run:\n"
            "python3 -m venv lab_env\n"
            "source lab_env/bin/activate # On Unix\n"
            "lab_env\\Scripts\\activate # On Windows\n\n"
            "Then run this program again."
        )
    else:
        print(
            "LABORATORY STATUS: The laboratory is sealed\n\n"
            f"Current Python: {sys.executable}\n"
            f"Virtual Environment: {os.path.basename(sys.prefix)}\n"
            f"Environment Path: {sys.prefix}\n"
            "\nSUCCESS: You are working in an isolated environment!\n"
            "Safe to install reagents without affecting"
            "\nthe global system.\n\n"
            "Reagent installation path:"
        )
        for path in site.getsitepackages():
            print(path)
        print("Virtual Environment: Detected\n")
