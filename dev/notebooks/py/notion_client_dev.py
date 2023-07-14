#!/usr/bin/env python
# coding: utf-8

import os
for k, v in dict(
    EMAIL_TO='agalea91@gmail.com',
    EMAIL_FROM='Toc <toc.adi.now@gmail.com>',
    NOTION_DATABASE_ID='',
    NOTION_SECRET_TOKEN='',
    SENDGRID_SECRET_TOKEN=''
).items():
    os.environ[k] = v


# ## 2023-04
# 
# Grok the API

import requests
import os

HEADERS = {
    "Authorization": f"Bearer {os.getenv('NOTION_SECRET_TOKEN')}",
    "Notion-version": "2021-05-13",
}


def retrieve_database(database_id, query=None, start_cursor=None) -> dict:
    url = f"https://api.notion.com/v1/databases/{database_id}/query"
    data = query or {}
    if start_cursor:
        data["start_cursor"] = start_cursor
    print(f"POST {url}")
    response = requests.post(url=url, headers=HEADERS, json=data)
    response.raise_for_status()
    database = response.json()
    return database


def retrieve_page_content(page_id) -> dict:
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    print(f"GET {url}")
    response = requests.get(url=url, headers=HEADERS)
    response.raise_for_status()
    page = response.json()
    return page


import re
import random
import json


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



database1 = retrieve_database(
    database_id=os.getenv("NOTION_DATABASE_ID"),
    start_cursor=None
)


database1["has_more"]


database1["next_cursor"]


database2 = retrieve_database(
    database_id=os.getenv("NOTION_DATABASE_ID"),
    start_cursor=database1["next_cursor"]
)


database2["has_more"]


len(database1["results"])



len(database2["results"])


database1["results"][0]["url"]



database2["results"][0]["url"]


type(database1)


# ## 2023-07
# 
# Get full text of database page

import requests
import os
import time

MAX_PAGINATION = 100

HEADERS = {
    "Authorization": f"Bearer {os.getenv('NOTION_SECRET_TOKEN')}",
    "Notion-version": "2021-05-13",
}

def retrieve_database(database_id, query=None) -> dict:
    database = {"has_more": True, "next_cursor": None, "results": []}

    i = 0
    while database["has_more"]:
        i += 1
        if i > MAX_PAGINATION:
            raise NotImplementedError(f"Max pagination reached ({MAX_PAGINATION})")

        next_cursor = database.get("next_cursor")
        if not next_cursor and i > 1:
            break

        next_database = _retrieve_paginated_database(database_id, query, next_cursor)
        for k, v in next_database.items():
            if k == "results":
                database["results"].extend(v)
            else:
                database[k] = v

        time.sleep(1)
    return database


def _retrieve_paginated_database(database_id, query=None, start_cursor=None) -> dict:
    url = f"https://api.notion.com/v1/databases/{database_id}/query"
    data = query or {}
    if start_cursor:
        data["start_cursor"] = start_cursor
    print(f"POST {url} with data: {data}")
    response = requests.post(url=url, headers=HEADERS, json=data)
    response.raise_for_status()
    database = response.json()
    return database


def retrieve_page_content(page_id) -> dict:
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    print(f"GET {url}")
    response = requests.get(url=url, headers=HEADERS)
    response.raise_for_status()
    page = response.json()
    return page



def retrieve_page_content(page_id) -> dict:
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    print(f"GET {url}")
    response = requests.get(url=url, headers=HEADERS)
    if not response.ok:
        print(response.text)
        response.raise_for_status()
    page = response.json()
    return page

import re
import random
import json


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




database1 = retrieve_database(
    database_id=os.getenv("NOTION_DATABASE_ID"),
)


database_page = get_random_page(database1)


print(json.dumps(database_page, indent=4))


database_page["properties"].get("Name", {})["title"][0]["text"]["content"]


database_page["id"]


topic = get_page_topic(database_page)
topic


block_page = retrieve_page_content(database_page["id"])


print(json.dumps(block_page, indent=4))


def parse_page_recipe_content(block_page):
    try:
        recipe = ""
        for r in block_page["results"]:
            result_type = r["type"]
            result_text_blocks = r[result_type]["text"]
            if not result_text_blocks:
                recipe += "\n"
            else:
                for t in result_text_blocks:
                    content = t['text']['content']
                    content_is_bold = t.get('annotations', {}).get("bold")
                    if result_type.startswith("heading"):
                        styled_content = f"<h2>{content}</h2>\n"
                    elif content_is_bold:
                        styled_content = f"<b>{content}</b>\n"
                    else:
                        styled_content = f"{content}\n"
                    recipe += styled_content
                        
                        
    except Exception as e:
#         print(f"Error parsing recipe from page {json.dumps(block_page, indent=2)}")
        raise
    return recipe




text = parse_page_recipe_content(block_page)
print(text)




