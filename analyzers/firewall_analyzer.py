from core.finding_factory import FindingFactory


def analyze_firewall(security_info):

    findings = []

    firewall_profiles = security_info.get(
        "Firewall Status",
        []
    )

    for profile in firewall_profiles:

        if not profile["Enabled"]:

            findings.append(

                FindingFactory.create(

                    title="Firewall Disabled",

                    category="Windows Security",

                    severity="CRITICAL",

                    raw_score=40,

                    description=(
                        f"{profile['Name']} firewall profile is disabled."
                    ),

                    recommendation=(
                        "Enable Windows Firewall immediately."
                    ),

                    module="Windows Audit"

                )

            )

    return findings