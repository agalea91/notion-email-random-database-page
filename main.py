# import dotenv

# dotenv.load_dotenv()


def run(_):
    from random_db_entry import send_random_entry

    send_random_entry()


if __name__ == "__main__":
    run(None)
