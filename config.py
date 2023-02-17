from pytz import utc
from datetime import datetime as dt

# File path & name 
to_save_as = "/tmp/new_webcal.ical"

# Webcal links
urls = [
        "http://www.webcal.guru/en-US/download_calendar?calendar_instance_id=169",
        "webcal://www.webcal.guru/en-US/download_calendar?calendar_instance_id=142",
        ]

# Filter options
filter_options = {
    "filter_long_events": True, # Remove events that last longer than 1 day
    "filter_words": ["Test"], # Remove events with "Test" in the summary
    "filter_within": [ # Remove events from Jan 1, 2022 -> Jan 2, 2022
        [
            # YYYY, MM, DD, HH, MM, SS, MS
            dt(2022, 1, 1, 0, 0, 0, 0),
            dt(2022, 1, 2)
        ]
    ]
}
