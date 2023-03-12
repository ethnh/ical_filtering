#!/usr/bin/python3

from filter import apply_filters
import requests
import os
from icalendar import Calendar
from config import urls, filter_options, to_save_as

def main():
    print("Coded by Ehtan Hindmarsh. Hi mom!")
    print("Fun fact: did you know running is faster than walking?")

    calendars = []

    if not urls:
        print("No URLs supplied, quitting")
        exit(1)

    # Download all calendars
    for url in urls:
        if not url.startswith(("http", "webcal")):
            print(f"Warning: Url {url} is not recognized as a valid calendar URL.")
            continue
        url = url.replace("webcal://", "https://")
        response = requests.get(url)
        calendars.append(Calendar.from_ical(response.content))


    # Concat calendars
    concatenated_calendar = Calendar()
    for calendar in calendars:
        concatenated_calendar.subcomponents.extend(calendar.subcomponents)


    # Filter calendars
    new_calendar = apply_filters(concatenated_calendar, filter_options)

    # Save and quit
    if not os.path.exists(os.path.dirname(to_save_as)):
        os.makedirs(os.path.dirname(to_save_as))

    with open(to_save_as, 'wb') as f:
        f.write(new_calendar.to_ical())

if __name__ == "__main__":
    main()
