from icalendar import Calendar, Event
from datetime import timedelta, datetime, date


# A function that takes a Calendar and returns a new calendar with no events
# which last > 1 day
def filter_long_events(cal):
    events = filter(lambda x: type(x) == Event and x.decoded('dtend') - x.decoded('dtstart') <= timedelta(days=1),cal.subcomponents)
    new_cal = Calendar()
    for event in events:
        new_cal.add_component(event)
    return new_cal


# A function that takes a calendar and returns a new calendar with all events,
# except those that include a certain sting in the summary
def filter_by_words(cal, words):
    new_cal = Calendar()
    for component in cal.subcomponents:
        if type(component) == Event:
            if not any(word in component.get('summary') for word in words):
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
    for component in cal.subcomponents:
        if isinstance(component, Event):
            event_start = component.decoded('dtstart')
            event_end = component.decoded('dtend')
            if type(event_start) == date:
                event_start = datetime.combine(event_start, datetime.min.time())
            if type(event_end) == date:
                event_end = datetime.combine(event_end, datetime.min.time())

            should_append = True
            for start, end in times:
                if start <= event_start <= end or start <= event_end <= end:
                    should_append = False
                    break

            if should_append:
                new_cal.add_component(component)

    return new_cal

def apply_filters(calendar, filter_options):
    filters = [
        filter_long_events,
        lambda c: filter_by_words(c, filter_options.get("filter_words", [])),
        lambda c: filter_by_times(c, filter_options.get("filter_within", [])),
    ]

    for f in filters:
        calendar = f(calendar)

    return calendar


