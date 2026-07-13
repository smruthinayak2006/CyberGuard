import psutil


def collect_windows_services():

    services = []

    for service in psutil.win_service_iter():

        try:

            info = service.as_dict()

            services.append({

                "name": info.get("name", ""),

                "display_name": info.get("display_name", ""),

                "status": info.get("status", ""),

                "start_type": info.get("start_type", ""),

                "username": info.get("username", ""),

                "binpath": info.get("binpath", "")

            })

        except Exception:

            continue

    return services