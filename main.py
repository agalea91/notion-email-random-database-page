# import dotenv
# 
# dotenv.load_dotenv()


def run(_):
    from app import email_random_database_page

    email_random_database_page()


if __name__ == "__main__":
    run(None)
