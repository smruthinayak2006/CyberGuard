from core.finding_factory import FindingFactory


def analyze_file_integrity(file_results):

    findings = []

    for file in file_results:

        if file["status"] == "MODIFIED":

            findings.append(

                FindingFactory.create(

                    title="Modified File",

                    category="File Integrity",

                    severity="MEDIUM",

                    raw_score=15,

                    description=(
                        f"{file['file']} has changed since the previous scan."
                    ),

                    recommendation=(
                        "Verify the file modification."
                    ),

                    module="File Integrity"

                )

            )

    return findings