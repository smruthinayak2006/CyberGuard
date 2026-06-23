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

        "cpu_usage": str(psutil.cpu_percent(interval=1)) + "%",

        "ram_usage": str(psutil.virtual_memory().percent) + "%",

        "disk_usage": str(psutil.disk_usage('/').percent) + "%"

    }


    return system_data