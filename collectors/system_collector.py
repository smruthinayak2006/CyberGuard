import platform
import socket
import getpass
import psutil
from datetime import datetime



def collect_system_info():


    boot_time = datetime.fromtimestamp(
        psutil.boot_time()
    )


    system_data = {

        "hostname": socket.gethostname(),

        "ip_address": socket.gethostbyname(
            socket.gethostname()
        ),

        "username": getpass.getuser(),

        "operating_system": platform.system(),

        "os_version": platform.version(),

        "architecture": platform.machine(),

        "processor": platform.processor(),

        "boot_time": str(boot_time),

        "cpu_usage": round(psutil.cpu_percent(interval=1), 1),
        "ram_usage": round(psutil.virtual_memory().percent, 1),
        "disk_usage": round(psutil.disk_usage('/').percent, 1)

    }


    return system_data