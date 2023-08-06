import logging
import platform
import subprocess
from pathlib import Path

logging.basicConfig(level=logging.INFO)

jar_file = Path(__file__).parent.parent / "lib/openxes-cli.jar"


def xes_to_csv(xes_path: Path, csv_path: Path, jar_file: Path = jar_file):
    """
    Converts XES to CSV using openxes-cli.jar. Java 8 is required.

    :param xes_path: Event log in XES format either with the .xes or .xes.gz extension.
    :param csv_path: Output path for the CSV file.
    :param jar_file: Path to the openxes-cli.jar file. Default: lib/openxes-cli.jar.
    :return: Exit code of the Java process.
    """
    if platform.system().lower() == "windows":
        xes_path = '"' + str(xes_path) + '"'
        csv_path = '"' + str(csv_path) + '"'
    return run_jar(jar_file, "-f", str(xes_path), "-t", "csv", "-o", str(csv_path))


def csv_to_xes(csv_path: Path, xes_path: Path, jar_file: Path = jar_file):
    """
    Converts CSV to XES using openxes-cli.jar. Java 8 is required.

    :param csv_path: Event log in CSV format.
    :param xes_path: Output path for the XES file.
    :return: Exit code of the Java process.
    """
    if not is_csv_valid(csv_path):
        raise ValueError(
            "Event log is not valid. It must contain the following columns: "
            "case:concept:name, concept:name, org:timestamp, start_timestamp, time:timestamp"
        )

    if platform.system().lower() == "windows":
        xes_path = '"' + str(xes_path) + '"'
        csv_path = '"' + str(csv_path) + '"'

    return run_jar(jar_file, "-f", str(csv_path), "-t", "xes", "-o", str(xes_path))


def is_csv_valid(csv_path: Path) -> bool:
    with open(csv_path, "r") as f:
        first_line = f.readline()

    return all(
        col in first_line
        for col in [
            "case:concept:name",
            "concept:name",
            "org:resource",
            "start_timestamp",
            "time:timestamp",
        ]
    )


def run_jar(jar_file: Path, *args) -> int:
    # Prepare system dependent command
    if platform.system().lower() == "windows":
        jar_file_path = '"' + str(jar_file) + '"'
        cmd = f"java -jar {jar_file_path} {' '.join(args)}"
    else:
        jar_file_path = str(jar_file)
        cmd = ["java", "-jar", jar_file_path] + list(args)

    # Convert to string for logging
    cmd_str = " ".join(cmd) if isinstance(cmd, list) else cmd
    logging.info(f"Running {cmd_str}")

    # Run the command
    return subprocess.call(cmd)
