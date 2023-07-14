import os

import app.service.notion as notion_client
import app.service.sg as sendgrid_client
import app.utils.notion as notion_utils
import app.utils.email as email_utils

# import datetime
# from datetime import timezone


def _check_databse_type():
    db_type = os.getenv("NOTION_DATABASE_TYPE")
    if not db_type:
        raise ValueError("Must set NOTION_DATABASE_TYPE env variable")
    if db_type not in ("quote", "recipe"):
        raise NotImplementedError


def email_random_database_page():
    _check_databse_type()

    database = notion_client.retrieve_database(
        database_id=os.getenv("NOTION_DATABASE_ID"),
    )

    database_page = notion_utils.get_random_page(database)
    page_id = notion_utils.get_page_id(database_page)
    page_url = notion_utils.get_page_url(database_page)
    page_topic = notion_utils.get_page_topic(database_page)
    page_name = notion_utils.get_page_name(database_page)
    block_page = notion_client.retrieve_page_content(page_id)

    parsed_page_content = notion_utils.parse_page_content(block_page)
    html_msg = email_utils.construct_html_msg(
        page_url=page_url, page_name=page_name, **parsed_page_content
    )
    email_subject = email_utils.get_email_subject(page_topic)

    print(html_msg)
    print(email_subject)

    sendgrid_client.send_email(
        os.getenv("EMAIL_FROM"),
        os.getenv("EMAIL_TO"),
        email_subject,
        html_msg,
    )
