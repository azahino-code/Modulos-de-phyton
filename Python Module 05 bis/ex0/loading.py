import pandas
import numpy

print(pandas.__version__)
print(pandas.__version__)

if __name__ == "__main__":
    print(
        "REAGENT STATUS: Loading reagents...\n\n"
        "Cheacking dependencies:\n"
    )
    try:
        print(
            f"[OK] {pandas.__name__} ({pandas.__version__})"
            " - Data manipulation ready"
        )
    except ImportError, ModuleNotFoundError:
        print(
            "Error: pandas is not installed.\n"
            "Install pip: python -m pip install pandas\n"
            "Install Poetry: poetry add pandas"
        )
    try:
        print(
            f"[OK] {numpy.__name__} ({numpy.__version__})"
            " - Numerical computation ready"
        )
    except ImportError, ModuleNotFoundError:
        print(
            "Error: numpy is not installed.\n"
            "Install pip: python -m pip install numpy\n"
            "Install Poetry: poetry add numpy"
        )
    finally:
        print(
            "pip vs Poetry\n"
            "   requirements.txt declares what to install;"
            " pip resolves it at install time.\n"
            "   pyproject.toml declares the same constraints,"
            " and Poetry pins the resolved\n"
            "   versions in poetry.lock so every install is identical"
            "\n\n"
            "All reagents present and accounted for."
        )
