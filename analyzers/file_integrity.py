import hashlib
from pathlib import Path


def calculate_sha256(file_path):

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:

        while chunk := file.read(4096):

            sha256.update(chunk)

    return sha256.hexdigest()


def scan_directory(directory):

    results = []

    path = Path(directory)

    for file in path.rglob("*"):

        if file.is_file():

            try:

                results.append({

                    "file": str(file),

                    "sha256": calculate_sha256(file)

                })

            except Exception:

                continue

    return results