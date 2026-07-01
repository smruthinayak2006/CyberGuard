from models.finding import Finding


class FindingFactory:

    counter = 1

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

            id=f"CG-{cls.counter:04}",

            title=title,

            category=category,

            severity=severity,

            raw_score=raw_score,

            description=description,

            recommendation=recommendation,

            module=module

        )

        cls.counter += 1

        return finding