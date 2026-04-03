import os

class InteractionEnvironment:
    def exploring():
        # linux: Example output on Linux: '/home/username'
        # Example output on Windows: 'C:\\Users\\username'
        home_dir = os.path.expanduser('~')
        return home_dir