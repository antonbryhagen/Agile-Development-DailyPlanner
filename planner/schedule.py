import random

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
    
    def sort_activities(self):
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
        
        sorted_activities = importance_levels["Very important"] + importance_levels["Important"] + importance_levels["Not so important"]
        return sorted_activities


    def generate_schedule(self): # Activity, PRIO, Time
        sorted_activities = self.sort_activities()
        for activity in sorted_activities:
            planned = False
            for day in self.days:
                if not planned:
                    if activity[2] <= self.time_per_day[day]:
                        self.days[day].append(activity)
                        self.time_per_day[day] -= activity[2]
                        planned = True
        planned_activites = 0
        activites = len(sorted_activities)
        for day in self.days:
            planned_activites += len(self.days[day])
        if planned_activites < activites:
            print("Some activities were not planned since there is not enough time for them.")
        for x in self.days:
            print(self.days[x])

    