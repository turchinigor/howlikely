from howlikely_etl.cli import main


def test_cli_runs_all_stages() -> None:
    assert main(["all"]) == 0
