# import dotenv

# dotenv.load_dotenv()


def run(_):
    from random_quote_of_the_day import send_random_quote

    send_random_quote()


if __name__ == "__main__":
    run(None)
