import os

import random_db_entry.service.notion as notion_client
import random_db_entry.service.sg as sendgrid_client
import random_db_entry.utils.notion as notion_utils
import random_db_entry.utils.email as email_utils

# import datetime
# from datetime import timezone


def _check_databse_type():
    db_type = os.getenv("DB_TYPE")
    if not db_type:
        raise ValueError("Must set DB_TYPE env variable")
    if db_type not in ("quote", "recipe"):
        raise NotImplementedError


def send_random_entry():
    _check_databse_type()

    database = notion_client.retrieve_database(
        database_id=os.getenv("NOTION_DATABASE_ID"),
    )

    database_page = notion_utils.get_random_page(database)
    page_id = notion_utils.get_page_id(database_page)
    topic = notion_utils.get_page_topic(database_page)
    block_page = notion_client.retrieve_page_content(page_id)

    parsed_page_content = notion_utils.parse_page_content(block_page)
    html_msg = email_utils.construct_html_msg(**parsed_page_content)
    email_subject = email_utils.get_email_subject(topic)

    sendgrid_client.send_email(
        os.getenv("EMAIL_FROM"),
        os.getenv("EMAIL_TO"),
        email_subject,
        html_msg,
    )
