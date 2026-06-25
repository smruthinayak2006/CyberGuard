import subprocess
import json


def run_powershell(command):

    try:

        result = subprocess.run(
            [
                "powershell",
                "-Command",
                command
            ],
            capture_output=True,
            text=True
        )


        if result.stdout:

            return json.loads(result.stdout)


        return None


    except Exception as error:

        return {
            "error": str(error)
        }



def collect_windows_security():

    security_data = {


        "firewall_status":

            run_powershell(
                "Get-NetFirewallProfile | Select Name,Enabled | ConvertTo-Json"
            ),


        "local_users":

            run_powershell(
                "Get-LocalUser | Select Name,Enabled | ConvertTo-Json"
            ),


        "installed_updates":

            run_powershell(
                "Get-HotFix | Select HotFixID,Description | ConvertTo-Json"
            )

    }


    return security_data