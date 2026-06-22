class User:
    def __init__(self, user_email, user_password, name, current_job_title):
        # sets initial values for class obj attributes
        self.email = user_email
        self.password = user_password
        self.name = name
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        # method to update a user's password
        self.password = new_password

    def change_job_title(self, new_job_title):
        # method to update a user's job title
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently works as a {self.current_job_title}. You can contact them at {self.email}.")
        