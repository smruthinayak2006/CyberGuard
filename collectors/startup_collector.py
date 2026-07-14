import winreg


RUN_KEYS = [

    (
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Run"
    ),

    (
        winreg.HKEY_LOCAL_MACHINE,
        r"Software\Microsoft\Windows\CurrentVersion\Run"
    )

]


def collect_startup_programs():

    startup_programs = []

    for hive, key_path in RUN_KEYS:

        try:

            key = winreg.OpenKey(hive, key_path)

            index = 0

            while True:

                try:

                    name, value, _ = winreg.EnumValue(key, index)

                    startup_programs.append({

                        "name": name,

                        "command": value,

                        "registry": key_path

                    })

                    index += 1

                except OSError:

                    break

        except FileNotFoundError:

            continue

    return startup_programs