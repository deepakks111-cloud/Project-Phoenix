from pathlib import Path

# ==========================================================
# PROJECT PHOENIX
# Build Script
#
# Release : PHX-R001
# Version : 0.1.0
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

SRC = PROJECT_ROOT / "src"
BUILD = PROJECT_ROOT / "build"

OUTPUT_FILE = BUILD / "Phoenix_v0.1.0.pine"

MODULE_ORDER = [
    "PHX_Header.pine",
    "PHX_Config.pine",
    "PHX_Types.pine",
    "PHX_Core.pine",
    "PHX_State.pine",
    "PHX_EMA.pine",
    "PHX_Trend.pine",
    "PHX_Visualization.pine",
    "PHX_Dashboard.pine",
    "PHX_Alerts.pine",
    "PHX_Main.pine",
]


def validate_modules():

    missing = []

    for module in MODULE_ORDER:

        if not (SRC / module).exists():
            missing.append(module)

    return missing


def build():

    BUILD.mkdir(exist_ok=True)

    with OUTPUT_FILE.open("w", encoding="utf-8") as outfile:

        outfile.write(
            "//======================================================\n"
        )

        outfile.write(
            "// PROJECT PHOENIX\n"
        )

        outfile.write(
            "// Release : PHX-R001\n"
        )

        outfile.write(
            "// Version : 0.1.0\n"
        )

        outfile.write(
            "//======================================================\n\n"
        )

        for module in MODULE_ORDER:

            print(f"Adding {module}")

            outfile.write(
                f"\n\n//======================================================\n"
            )

            outfile.write(
                f"// MODULE : {module}\n"
            )

            outfile.write(
                "//======================================================\n\n"
            )

            outfile.write(
                (SRC / module).read_text(encoding="utf-8")
            )

    print()
    print("====================================")
    print("Phoenix build completed successfully")
    print(OUTPUT_FILE)
    print("====================================")


if __name__ == "__main__":

    missing = validate_modules()

    if missing:

        print()

        print("Missing modules:")

        for item in missing:
            print(f" - {item}")

    else:

        build()
