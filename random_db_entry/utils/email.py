import os


DB_TYPE = os.getenv("DB_TYPE")


def quote_html(quote, author):
    return f"""
<div>
    <blockquote>
        <p>{quote}</p>
        <cite>{author}</cite>
    </blockquote>
</div>
"""


def pretty_quote_html(quote, author):
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


def recipe_html(text):
    return f"""
    <p>{text}</p>
    """


inner_html = {
    "quote": pretty_quote_html,
    "recipe": recipe_html,
}


def construct_html_msg(**parsed_page_content):
    html_template = f"""\
<html>
    <body style='margin: 1em; font: 1.2rem/1.4 Georgia, serif;'>
        {inner_html[DB_TYPE](**parsed_page_content)}
    </body>
</html>
"""
    return html_template


def get_email_subject(topic):
    return f"Your Daily {topic.capitalize()} {DB_TYPE.capitalize()}"
