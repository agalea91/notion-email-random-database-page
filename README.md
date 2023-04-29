# Notion Random Quote of the Day

## Zip for GCP Cloud Function

```
zip -r notion-random-quote-of-the-day.zip * -x ".git/*" "venv/*" "*/__pycache__/*" .env

```

## Running locally

```
python main.py
```

## Environment vars

```
EMAIL_TO
EMAIL_FROM
NOTION_DATABASE_ID
NOTION_SECRET_TOKEN
SENDGRID_SECRET_TOKEN
```
