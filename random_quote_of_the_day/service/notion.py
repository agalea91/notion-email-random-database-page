import requests
import os

HEADERS = {
    "Authorization": f"Bearer {os.getenv('NOTION_SECRET_TOKEN')}",
    "Notion-version": "2021-05-13",
}


def retrieve_database(database_id, query=None) -> dict:
    url = f"https://api.notion.com/v1/databases/{database_id}/query"
    print(f"POST {url}")
    response = requests.post(url=url, headers=HEADERS, json=query or {})
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
