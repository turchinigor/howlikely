"""Command-line entry point for the ETL stages: extract -> transform -> load."""

import argparse
from pathlib import Path

from howlikely_etl.gbd import combine_exports

STAGES = ("extract", "transform", "load")


def extract(raw_dir: Path, out: Path) -> None:
    df = combine_exports(raw_dir)
    out.parent.mkdir(parents=True, exist_ok=True)
    df.write_csv(out)
    print(f"[howlikely-etl] extract: {df.height} rows -> {out}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="howlikely-etl", description=__doc__)
    parser.add_argument("stage", choices=(*STAGES, "all"))
    parser.add_argument("--raw-dir", type=Path, default=Path("data/raw"))
    parser.add_argument("--out", type=Path, default=Path("data/interim/gbd_2023_death_rates.csv"))
    args = parser.parse_args(argv)

    stages = STAGES if args.stage == "all" else (args.stage,)
    for stage in stages:
        if stage == "extract":
            extract(args.raw_dir, args.out)
        else:
            print(f"[howlikely-etl] {stage}: not implemented yet")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
