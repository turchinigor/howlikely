from pathlib import Path

from howlikely_etl.cli import main


def test_cli_extract_writes_combined_csv(raw_dir: Path) -> None:
    out = raw_dir / "out" / "combined.csv"
    assert main(["extract", "--raw-dir", str(raw_dir), "--out", str(out)]) == 0
    assert out.read_text().count("\n") == 4  # header + 3 rows


def test_cli_stub_stages_run() -> None:
    assert main(["transform"]) == 0
    assert main(["load"]) == 0
