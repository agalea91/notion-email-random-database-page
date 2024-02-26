import os


DB_TYPE = os.getenv("NOTION_DATABASE_TYPE")


def quote_html(quote, author):
    return f"""
<div>
    <blockquote>
        <p>{quote}</p>
        <cite>{author}</cite>
    </blockquote>
</div>
"""


def pretty_quote_html(quote, author, **kwargs):
    return f"""
    <figure style='margin: 0; background: #eee; padding: 1em; border-radius: 1em;'>
        <blockquote style='margin: 1em;'>
            {quote}
        </blockquote>
        <figcaption style='margin: 1em;'>
            <cite>{author}</cite>
        </figcaption>
    </figure>
    """


def recipe_html(recipe, page_url, page_name, **kwargs):
    return f"""
    <h2>{page_name}</h2>
    <p>{recipe}</p>
    <p><a href={page_url}>Link to recipe in Notion</p>
    """

def note_html(note, page_url, page_name, **kwargs):
    return f"""
    <h2>{page_name}</h2>
    <p>{note}</p>
    <p><a href={page_url}>Link to note in Notion</p>
    """


inner_html = {
    "quote": pretty_quote_html,
    "recipe": recipe_html,
    "note": note_html,
}


def construct_html_msg(**kwargs):
    html_template = f"""\
<html>
    <body style='margin: 1em; font: 1.2rem/1.4 Georgia, serif;'>
        {inner_html[DB_TYPE](**kwargs)}
    </body>
</html>
"""
    return html_template


def get_email_subject(topic):
    return f"Your daily {topic} {DB_TYPE}"
