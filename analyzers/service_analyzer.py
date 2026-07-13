from core.finding_factory import FindingFactory


def analyze_services(services):

    findings = []

    for service in services:

        path = service["binpath"].lower()

        # --------------------------------------------------
        # Suspicious executable location
        # --------------------------------------------------

        if (
            path
            and "windows" not in path
            and "program files" not in path
        ):

            findings.append(

                FindingFactory.create(

                    title="Suspicious Windows Service",

                    category="Windows Services",

                    severity="MEDIUM",

                    raw_score=10,

                    description=(
                        f"{service['display_name']} "
                        "is running from an unusual location."
                    ),

                    recommendation=(
                        "Verify the executable path and "
                        "ensure the service is legitimate."
                    ),

                    module="Service Analyzer"

                )

            )

        # --------------------------------------------------
        # Disabled Service
        # --------------------------------------------------

        if service["status"] == "stopped":

            findings.append(

                FindingFactory.create(

                    title="Stopped Windows Service",

                    category="Windows Services",

                    severity="LOW",

                    raw_score=5,

                    description=(
                        f"{service['display_name']} "
                        "is currently stopped."
                    ),

                    recommendation=(
                        "Verify whether the service "
                        "should be running."
                    ),

                    module="Service Analyzer"

                )

            )

    return findings