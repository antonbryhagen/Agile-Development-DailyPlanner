"""Handle activities."""

class Activities:
    """Create object of Activities"""

    def __init__(self, activity, prio, time, username):
        """Create activity object."""
        self.activity = activity
        self.time = time
        self.username = username
        self.prio = prio
