from icalendar import Calendar, Event
from datetime import timedelta, datetime, date


# A function that takes a Calendar and returns a new calendar with no events
# which last >1 day
def filter_long_events(cal):
    new_cal = Calendar()
    for component in cal.subcomponents:
        if type(component) == Event:
            if component.decoded('dtend') - component.decoded('dtstart') \
                    <= timedelta(days=1):
                new_cal.add_component(component)
    return new_cal


# A function that takes a calendar and returns a new calendar with all events,
# except those that include a certain sting in the summary
def filter_by_words(cal, words):
    new_cal = Calendar()
    for component in cal.subcomponents:
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
    for component in cal.subcomponents:
        if type(component) == Event:
            append = True
            for start, end in times:
                
                startdate = component.decoded('dtstart')
                enddate = component.decoded('dtend')
                if type(startdate) == date:
                    startdate = datetime.combine(
                                                startdate,
                                                datetime.min.time()
                                                )
                
                if type(enddate) == date:
                    enddate = datetime.combine(
                                                enddate,
                                                datetime.min.time()
                                                )
                # if the event is within the given start->end time range
                if (start < startdate < end) or (start < enddate < end):
                    append = False
            if append:
                new_cal.add_component(component)
    return new_cal
