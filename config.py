from pytz import utc
from datetime import datetime as dt

# file path & name 
to_save_as = "/tmp/new_webcal.ical"

urls = [
        # webcal links:
        "http://www.webcal.guru/en-US/download_calendar?calendar_instance_id=169",
        "webcal://www.webcal.guru/en-US/download_calendar?calendar_instance_id=142",
        ]

# Remove events that last longer than a day
filter_long_events = True

filter_words = [
        # Remove events with the word "Test"
        "Test",
        ]

filter_within = [
            # Remove events from Jan 1, 2022 -> Jan 2, 2022
            [
                #  YYYY,MM,DD,HH,MM,SS,MS, Timezone
                dt(2022, 1, 1, 0, 0, 0, 0, tzinfo=utc),
                dt(2022, 1, 2)
            ],
        ]
