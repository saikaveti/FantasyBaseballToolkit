from datetime import date, timedelta
import datetime

import sys


class DateManipulation:

    def __init__(self):
        self.current_date = datetime.datetime.now()

    def get_previous_date(self):
        prev_date = self.current_date - timedelta(days = 1)

        prev_str = str(prev_date)
        args = prev_str.split()
        date_only = args[0]

        return date_only

    def get_date_for_num_days(self, num_day):
        prev_date = self.current_date - timedelta(days = num_day)

        prev_str = str(prev_date)
        args = prev_str.split()
        date_only = args[0]

        return date_only
