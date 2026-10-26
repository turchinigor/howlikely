"""Command-line entry point for the ETL stages: extract -> transform -> load."""

import argparse

STAGES = ("extract", "transform", "load")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="howlikely-etl", description=__doc__)
    parser.add_argument("stage", choices=(*STAGES, "all"))
    args = parser.parse_args(argv)

    stages = STAGES if args.stage == "all" else (args.stage,)
    for stage in stages:
        print(f"[howlikely-etl] {stage}: not implemented yet")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
