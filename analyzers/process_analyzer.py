import psutil


def collect_processes():

    processes = []

    for process in psutil.process_iter(

        ["pid",
         "name",
         "username",
         "cpu_percent",
         "memory_percent"]

    ):

        try:

            info = process.info

            processes.append({
                "pid": info["pid"],
                "name": info["name"] or "Unknown",
                "user": info["username"],
                "cpu": round(info["cpu_percent"], 2),
                "memory": round(info["memory_percent"], 2),
                "path": process.exe() if process.is_running() else "Unavailable"
            })

        except (

            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess

        ):

            continue

    return processes