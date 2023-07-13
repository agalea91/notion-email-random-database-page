import re
import random
import json
import os

DB_TYPE = os.getenv("DB_TYPE")


def get_random_page(database):
    if database["has_more"]:
        raise NotImplementedError("Database has more pages. Must implement pagination.")

    idx = random.choice(list(range(len(database["results"]))))
    page = database["results"][idx]
    return page


def get_page_id(database_page):
    return re.findall(r"/([^/]+)$", database_page["url"])[0]


def get_page_topic(database_page):
    return database_page["properties"]["Tags"]["multi_select"][0]["name"]


def parse_page_quote_content(block_page):
    try:
        quote = block_page["results"][0]["paragraph"]["text"][0]["text"]["content"]
        attrib = block_page["results"][1]["paragraph"]["text"][0]["text"]["content"]
    except Exception as e:
        print(f"Error parsing quote from page {json.dumps(block_page, indent=2)}")
        raise
    return quote, attrib


def parse_page_recipe_content(block_page):
    try:
        recipe = ""
        for r in block_page["results"]:
            for t in r["paragraph"]["text"]:
                recipe += f"{t['text']['content']}\n"
    except Exception as e:
        print(f"Error parsing recipe from page {json.dumps(block_page, indent=2)}")
        raise
    return recipe


content_parser = {
    "quote": parse_page_quote_content,
    "recipe": parse_page_recipe_content,
}


def parse_page_content(block_page):
    return content_parser[DB_TYPE](block_page)
