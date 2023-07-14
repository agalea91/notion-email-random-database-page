import re
import random
import json
import os

DB_TYPE = os.getenv("NOTION_DATABASE_TYPE")


def get_random_page(database):
    if database["has_more"]:
        raise NotImplementedError("Database has more pages. Must implement pagination.")

    idx = random.choice(list(range(len(database["results"]))))
    page = database["results"][idx]
    return page


def get_page_id(database_page):
    return database_page["id"]


def get_page_url(database_page):
    return database_page["url"]


def get_page_topic(database_page):
    return database_page["properties"]["Tags"]["multi_select"][0]["name"]


def get_page_name(database_page):
    return database_page["properties"].get("Name", {})["title"][0]["text"]["content"]


def parse_page_quote_content(block_page):
    try:
        quote = block_page["results"][0]["paragraph"]["text"][0]["text"]["content"]
        attrib = block_page["results"][1]["paragraph"]["text"][0]["text"]["content"]
    except Exception as e:
        print(f"Error parsing quote from page {json.dumps(block_page, indent=2)}")
        raise
    return dict(
        quote=quote,
        attrib=attrib,
    )


def parse_page_text_content(block_page):
    try:
        text = ""
        for r in block_page["results"]:
            result_type = r["type"]
            result_text_blocks = r[result_type]["text"]
            if not result_text_blocks:
                text += "<br>"
            else:
                for t in result_text_blocks:
                    content = t["text"]["content"]
                    content_is_bold = t.get("annotations", {}).get("bold")
                    if result_type.startswith("heading"):
                        styled_content = f"<h3>{content}</h3><br>"
                    elif content_is_bold:
                        styled_content = f"<b>{content}</b><br>"
                    else:
                        styled_content = f"{content}<br>"
                    text += styled_content

    except Exception as e:
        print(f"Error parsing text from page {json.dumps(block_page, indent=2)}")
        raise
    return dict(text=text)


def parse_page_recipe_content(block_page):
    recipe = parse_page_text_content(block_page)["text"]
    return dict(recipe=recipe)


content_parser = {
    "quote": parse_page_quote_content,
    "recipe": parse_page_recipe_content,
}


def parse_page_content(block_page):
    return content_parser[DB_TYPE](block_page)
