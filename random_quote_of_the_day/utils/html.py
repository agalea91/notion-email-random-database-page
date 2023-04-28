STYLE = """\
        .styled-table {
            border-collapse: collapse;
            margin: 25px 0;
            font-size: 0.9em;
            font-family: sans-serif;
            min-width: 400px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
        }

        .styled-table thead tr {
            background-color: #009879;
            color: #ffffff;
            text-align: left;
        }

        .styled-table th,
        .styled-table td {
            padding: 12px 15px;
        }

        .styled-table tbody tr {
            border-bottom: 1px solid #dddddd;
        }

        .styled-table tbody tr:nth-of-type(even) {
            background-color: #f3f3f3;
        }

        .styled-table tbody tr:last-of-type {
            border-bottom: 2px solid #009879;
        }

        .styled-table tbody tr.active-row {
            font-weight: bold;
            color: #009879;
        }

        h1 {
            color: #009879;
            font-family: arial, sans-serif;
            font-size: 16px;
            font-weight: bold;
            margin-top: 0px;
            margin-bottom: 1px;
        }
"""


def quote_html(quote, author):
    quote_html = f"""\
<div>
    <blockquote>
        <p>{quote}</p>
        <cite>{author}</cite>
    </blockquote>
</div>
"""
    return quote_html


def construct_html_msg(quote, attrib):
    html_template = f"""\
<html>
    <head>
    <style>
        {STYLE}
    </style>
    </head>
    <body>
        {quote_html(quote, attrib)}
    </body>
</html>
"""
    return html_template
