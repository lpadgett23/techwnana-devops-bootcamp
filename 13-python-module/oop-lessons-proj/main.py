from user import User
from post import Post


def main():
    app_user_one = User("ll@ll.com", "pwd", "Laura Padgett", "Data Engineer")
    app_user_one.get_user_info()

    app_user_one.change_job_title("Sr Data Engineer")
    app_user_one.get_user_info()

    app_user_two = User("ts@ll.com", "pwd2", "Timothy Second", "DevOps Engineer")
    app_user_two.get_user_info()

    new_post_1 = Post("On a secret project today.", app_user_one.name)
    new_post_1.get_post_info()

if __name__ == "__main__":
    main()