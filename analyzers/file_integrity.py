import hashlib
import json
from pathlib import Path

BASELINE_FILE = "database/hash_baseline.json"


def calculate_sha256(file_path):

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:

        while chunk := file.read(4096):

            sha256.update(chunk)

    return sha256.hexdigest()


def load_baseline():

    path = Path(BASELINE_FILE)

    if not path.exists():

        return {}

    with open(path, "r") as file:

        return json.load(file)


def save_baseline(data):

    with open(BASELINE_FILE, "w") as file:

        json.dump(data, file, indent=4)


def scan_directory(directory):

    baseline = load_baseline()

    current = {}

    results = []

    path = Path(directory)

    for file in path.rglob("*"):

        if file.is_file():

            file_path = str(file)

            current_hash = calculate_sha256(file)

            current[file_path] = current_hash

            if file_path not in baseline:

                status = "NEW"

            elif baseline[file_path] == current_hash:

                status = "UNCHANGED"

            else:

                status = "MODIFIED"

            results.append({

                "file": file_path,

                "sha256": current_hash,

                "status": status

            })

    save_baseline(current)

    return results