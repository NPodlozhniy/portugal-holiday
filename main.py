import argparse

from model import Calendar

parser = argparse.ArgumentParser(
    description="Calculate holiday calendar", epilog="Have a nice holiday!"
)
parser.add_argument(
    "--year",
    action="store",
    help="specify the year between 1900 and 2099 (current year by default)",
    metavar="<YEAR>",
    nargs="?",
    type=int,
)
parser.add_argument(
    "--region",
    action="store",
    help=f"include a regional holiday for the given municipality "
         f"(optional). Available: {', '.join(Calendar.REGIONAL_HOLIDAYS)}",
    metavar="<REGION>",
    nargs="?",
    type=str,
)
args = parser.parse_args()

if __name__ == "__main__":

    if args.year:
        calendar = Calendar(args.year, region=args.region)
    else:
        calendar = Calendar.from_today(region=args.region)

    print(f"\n{calendar}\n")

    for date, holiday in calendar.public_holidays().items():
        print(f"{date}: {holiday}")

    print(
        "\nThe number of public holidays "
        + "that are not the same as a normal weekend: "
        + f"{calendar.real_holidays()}"
    )
