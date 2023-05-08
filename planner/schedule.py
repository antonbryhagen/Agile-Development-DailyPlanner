class Schedule:
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

    def generate_schedule(self):
        pass

    