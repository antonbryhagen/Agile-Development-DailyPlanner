"""Handle schedules."""

import random

class Schedule:
    """Schedule class to sort activities."""
    def __init__(self, activities, wake_hours):
        """Create instance attributes for schedule."""
        self.activities = activities
        self.wake_hours = wake_hours
        self.days = {
            "Monday" : [],
            "Tuesday" : [],
            "Wednesday" : [],
            "Thursday" : [],
            "Friday" : [],
            "Saturday" : [],
            "Sunday" : []
        }

        self.time_per_day = {
            "Monday" : self.wake_hours,
            "Tuesday" : self.wake_hours,
            "Wednesday" : self.wake_hours,
            "Thursday" : self.wake_hours,
            "Friday" : self.wake_hours,
            "Saturday" : self.wake_hours,
            "Sunday" : self.wake_hours
        }

    def sort_activities(self):
        """Sort the activties depending on priority and shuffle the order within each priority."""
        sorted_activities = []

        importance_levels = {
            "Very important": [],
            "Important": [],
            "Not so important": []
        }
        for activity in self.activities:
            importance_levels[activity[1]].append(activity)

        random.shuffle(importance_levels["Very important"])
        random.shuffle(importance_levels["Important"])
        random.shuffle(importance_levels["Not so important"])

        sorted_activities = (importance_levels["Very important"] +
                             importance_levels["Important"] +
                             importance_levels["Not so important"])
        self.activities = sorted_activities


    def generate_schedule(self, start_time, lunchtime):
        """Generate the schedule from sorted activties."""
        self.all_planned = True
        self.planned_days = {
            "Monday" : False,
            "Tuesday" : False,
            "Wednesday" : False,
            "Thursday" : False,
            "Friday" : False,
            "Saturday" : False,
            "Sunday" : False}
        for activity in self.activities:
            planned = False
            for day in self.days:
                if not planned:
                    if activity[2] <= self.time_per_day[day]:
                        self.days[day].append(activity)
                        self.time_per_day[day] -= activity[2]
                        planned = True
                        if (self.planned_days[day] is False and
                            start_time + self.wake_hours - self.time_per_day[day] > 12):
                            self.time_per_day[day] -= lunchtime
                            self.days[day].append(('Lunch','Very important',lunchtime,'',))
                            self.planned_days[day] = True
        planned_activites = 0
        activites = len(self.activities)
        for day in self.days:
            planned_activites += len(self.days[day])
        print(planned_activites)
        print(activites)
        if planned_activites-1 < activites:
            self.all_planned = False
