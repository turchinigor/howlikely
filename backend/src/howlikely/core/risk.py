"""Annual mortality risk calculations (see docs/methodology.md).

All functions describe population-level annual rates for one
country x year x age group x sex x cause cell. They are not individual predictions.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AnnualRisk:
    deaths: float
    population: float

    def __post_init__(self) -> None:
        if self.deaths < 0:
            raise ValueError("deaths must be non-negative")
        if self.population <= 0:
            raise ValueError("population must be positive")

    @property
    def rate(self) -> float:
        return self.deaths / self.population

    @property
    def percent(self) -> float:
        return self.rate * 100

    @property
    def per_100k(self) -> float:
        return self.rate * 100_000

    @property
    def one_in_n(self) -> int | None:
        """Approximate '1 in N'; None when there are no deaths."""
        if self.deaths == 0:
            return None
        return round(self.population / self.deaths)


def rate_ratio(primary: AnnualRisk, comparison: AnnualRisk) -> float | None:
    """Relative risk of primary vs comparison; None when the denominator is zero."""
    if comparison.deaths == 0:
        return None
    return primary.rate / comparison.rate


def absolute_difference_per_100k(primary: AnnualRisk, comparison: AnnualRisk) -> float:
    return primary.per_100k - comparison.per_100k
