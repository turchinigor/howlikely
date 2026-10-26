import pytest

from howlikely.core.risk import AnnualRisk, absolute_difference_per_100k, rate_ratio


def test_rates() -> None:
    risk = AnnualRisk(deaths=50, population=1_000_000)
    assert risk.per_100k == pytest.approx(5.0)
    assert risk.percent == pytest.approx(0.005)
    assert risk.one_in_n == 20_000


def test_zero_deaths_has_no_one_in_n() -> None:
    assert AnnualRisk(deaths=0, population=1000).one_in_n is None


@pytest.mark.parametrize(("deaths", "population"), [(-1, 100), (1, 0)])
def test_invalid_inputs(deaths: float, population: float) -> None:
    with pytest.raises(ValueError):
        AnnualRisk(deaths=deaths, population=population)


def test_comparison() -> None:
    a = AnnualRisk(deaths=20, population=100_000)
    b = AnnualRisk(deaths=10, population=100_000)
    assert rate_ratio(a, b) == pytest.approx(2.0)
    assert absolute_difference_per_100k(a, b) == pytest.approx(10.0)


def test_ratio_suppressed_for_zero_denominator() -> None:
    a = AnnualRisk(deaths=5, population=100_000)
    b = AnnualRisk(deaths=0, population=100_000)
    assert rate_ratio(a, b) is None
