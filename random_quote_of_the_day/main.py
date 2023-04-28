import os
import random_quote_of_the_day.service.notion as notion_client
import random_quote_of_the_day.service.sg as sendgrid_client
import random_quote_of_the_day.utils.notion as notion_utils
import random_quote_of_the_day.utils.html as html_utils

# import datetime
# from datetime import timezone


def send_random_quote():
    database = notion_client.retrieve_database(
        database_id=os.getenv("NOTION_DATABASE_ID"),
    )

    database_page = notion_utils.get_random_page(database)
    page_id = notion_utils.get_page_id(database_page)
    topic = notion_utils.get_page_topic(database_page)
    block_page = notion_client.retrieve_page_content(page_id)
    quote, attrib = notion_utils.parse_page_quote_content(block_page)

    html_msg = html_utils.construct_html_msg(quote, attrib)

    sendgrid_client.send_email(
        os.getenv("EMAIL_FROM"),
        os.getenv("EMAIL_TO"),
        f"Your daily {topic} quote",
        html_msg,
    )
