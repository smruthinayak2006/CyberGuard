from models.finding import Finding


class FindingFactory:

    _counter = 1

    @classmethod
    def create(
        cls,
        title,
        category,
        severity,
        raw_score,
        description,
        recommendation,
        module
    ):

        finding = Finding(

            finding_id=f"CG-{cls._counter:04}",

            title=title,

            category=category,

            severity=severity.upper(),

            raw_score=raw_score,

            description=description,

            recommendation=recommendation,

            module=module

        )

        cls._counter += 1

        return finding