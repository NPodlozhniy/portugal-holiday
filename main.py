import argparse

from model import Calendar

parser = argparse.ArgumentParser(
    description="Calculate holiday calendar", epilog="Have a nice holiday!"
)
parser.add_argument(
    "--year",
    action="store",
    help="specify the year (current year by default)",
    metavar="<YOUR YEAR>",
    nargs="?",
    type=int,
)
args = parser.parse_args()

if __name__ == "__main__":

    if args.year:
        calendar = Calendar(args.year)
    else:
        calendar = Calendar.from_today()

    print(f"\n{calendar}\n")

    for date, holiday in calendar.public_holidays().items():
        print(f"{date}: {holiday}")

    print(
        "\nThe number of public holidays "
        + "that are not the same as a normal weekend: "
        + f"{calendar.real_holidays()}"
    )
