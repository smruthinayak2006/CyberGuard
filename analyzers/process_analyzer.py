import psutil
from pathlib import Path


def collect_processes():

    processes = []

    for process in psutil.process_iter(
        [
            "pid",
            "name",
            "username",
            "cpu_percent",
            "memory_percent"
        ]
    ):

        try:

            info = process.info

            try:
                executable = process.exe()
            except Exception:
                executable = ""

            processes.append({

                "pid": info["pid"],

                "name": info["name"] or "Unknown",

                "user": info["username"],

                "cpu": round(info["cpu_percent"], 2),

                "memory": round(info["memory_percent"], 2),

                "path": executable,

                "is_temp": (
                    "temp" in executable.lower()
                    if executable else False
                ),

                "is_appdata": (
                    "appdata" in executable.lower()
                    if executable else False
                ),

                "missing_path": executable == ""

            })

        except (

            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess

        ):

            continue

    return processes