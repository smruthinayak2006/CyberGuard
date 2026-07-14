from core.finding_factory import FindingFactory


SUSPICIOUS_LOCATIONS = [

    "appdata",
    "temp",
    "downloads",
    "public"

]


def analyze_startup_programs(startup_programs):

    findings = []

    for program in startup_programs:

        command = program["command"].lower()

        if any(

            location in command

            for location in SUSPICIOUS_LOCATIONS

        ):

            findings.append(

                FindingFactory.create(

                    title="Suspicious Startup Program",

                    category="Startup Programs",

                    severity="HIGH",

                    raw_score=25,

                    description=(

                        f"{program['name']} starts automatically "

                        "from a user-writable location."

                    ),

                    recommendation=(

                        "Verify whether this startup entry "

                        "is legitimate."

                    ),

                    module="Startup Analyzer"

                )

            )

    return findings