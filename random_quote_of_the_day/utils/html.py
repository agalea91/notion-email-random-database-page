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


def construct_html_msg(quote, attrib):
    html_template = f"""\
<html>
    <body style='margin: 1em; font: 1.2rem/1.4 Georgia, serif;'>
        {pretty_quote_html(quote, attrib)}
    </body>
</html>
"""
    return html_template
