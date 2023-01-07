from model import Calendar

if __name__ == "__main__":

    calendar = Calendar.from_today()
    print(calendar, end="\n\n")
    
    for date, holiday in calendar.public_holidays().items():
        print(f"{date}: {holiday}")

    print(
        "\nThe number of public holidays " +
        "that are not the same as a normal weekend: " +
        f"{calendar.real_holidays()}"
    )
