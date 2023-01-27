#!/usr/bin/python3

import filter
import requests
from icalendar import Calendar
from config import urls, filter_long_events, filter_words, filter_within, to_save_as

def main():

    calendars = []

    if urls == []:
        print("No URLs supplied, quitting")
        exit(1)

    
    # Download all calendars
    for url in urls:
        if "webcal://" in url:
            url = "https://" + url[9::]
        if "http" not in url:
            print(f"Warning: Url {url} is not recognized as a valid calendar URL.")

        with requests.get(url) as get:
            calendars.append(Calendar.from_ical(bytes(get.text, 'utf-8')))
    

    # Concat calendars
    concatenated_calendar = Calendar()
    for calendar in calendars:
        for component in calendar.subcomponents:
            concatenated_calendar.add_component(component)

    
    # Filter calendars
    new_calendar = concatenated_calendar
    if filter_long_events:
        new_calendar = filter.filter_long_events(new_calendar)

    if filter_words != []:
        new_calendar = filter.filter_by_words(new_calendar, filter_words)

    if filter_within != []:
        new_calendar = filter.filter_by_times(new_calendar, filter_within)

    # save and quit
    with open(to_save_as, 'wb') as f:
        f.write(new_calendar.to_ical())

if __name__ == "__main__":
    main()
