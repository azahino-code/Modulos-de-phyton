import sys
import os
import site

if __name__ == "__main__":
    if sys.prefix == sys.base_prefix:
        print("LABORATORY STATUS: You are working in the open\n")
        print(f"Current Pyhton: {sys.executable}")
        print("Virtual Enviroment: None detected\n")
        print(
            "WARNING: You are in the global enviroment"
            "\nEvery reagent you install here leaks into the whole system.\n\n"
            "To seal the laboratory, run:\n"
            "python3 -m venv lab_env\n"
            "source lab_env/bin/activate # On Unix\n"
            "lab_env\\Scripts\\activate # On Windows\n\n"
            "Then run this program again."
        )
    else:
        print(
            "LABORATORY STATUS: The laboratory is sealed\n\n"
            f"Current Pyhton: {sys.executable}\n"
            f"Virtual Environment: {os.path.basename(sys.prefix)}"
            f"Environment Path: {sys.prefix}\n"
            "\nSUCCES: You are working in an isolated enviroment!\n"
            "Safe to install reagents without affecting"
            "\nthe global system.\n\n"
            "Reagent installation path:\n"
            f"{site.getsitepackages()}"
        )
        print("Virtual Enviroment: Detected\n")
