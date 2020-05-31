class User:
    # create the class here
    n_active = 0
    users = []

    def __init__(self, active, user_name):
        self.active = True
        self.user_name = user_name
