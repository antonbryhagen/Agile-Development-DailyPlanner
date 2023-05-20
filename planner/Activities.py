"""Handle activities."""

class Activities:
    """Create object of Activities"""

    def __init__(self, Activity, PRIO, Time, username):
        """Create activity object."""
        self.Activity = Activity
        self.Time = Time
        self.username = username
        self.PRIO = PRIO
