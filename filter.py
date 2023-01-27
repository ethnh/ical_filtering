from icalendar import Calendar, Event
from datetime import timedelta


# A function that takes a Calendar and returns a new calendar with no events
# which last >1 day
def filter_long_events(cal):
    new_cal = Calendar()
    for component in cal.subcomponents():
        if type(component) == Event:
            if component.get('dtend').dt - component.get('dtstart').dt \
                    < timedelta(days=1):
                new_cal.add_component(component)
    return new_cal


# A function that takes a calendar and returns a new calendar with all events,
# except those that include a certain sting in the summary
def filter_by_words(cal, words):
    new_cal = Calendar()
    for component in cal.subcomponents():
        if type(component) == Event:
            for word in words:
                append = True
                if word in component.get('summary'):
                    append = False
                if append:
                    new_cal.add_component(component)
    return new_cal


# A function that takes a calendar and returns a new calendar without events
# that occur within a certain time range
def filter_by_times(cal, times):
    # Times should be a list of datetime.datetime objs such that
    # Times = [
    #           [ Start_Time: datetime.datetime,
    #             End_Time: datetime.datetime,
    #           ],
    #           ...
    #         ]

    new_cal = Calendar()
    for component in cal.subcomponents():
        if type(component) == Event:
            append = True
            for start, end in times:
                if start < component.get('dtstart').dt < end:
                    append = False
            if append:
                new_cal.add_component(component)
    return new_cal