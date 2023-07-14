# Notion Email Random Database Page

## CLI GCP Cloud Function Deploy

```
gcloud functions deploy notion-email-random-recipe --source=./ --trigger-http --memory=256MB --timeout=60 --env-vars-file=.env.recipe.yaml --max-instances=1 --runtime=python37 --no-allow-unauthenticated --entry-point run
```

## Zip GCP Cloud Function Deploy

Upload zip to gs and deploy using console

```
zip -r notion-email-random-database-page.zip * -x ".git/*" "venv/*" "*/__pycache__/*" .env
```

## Running locally

Uncomment first two lines of main.py

```
python main.py
```

## Environment vars

Set NOTION_DATABASE_TYPE to "quote" or "recipe"

```
EMAIL_TO
EMAIL_FROM
NOTION_DATABASE_TYPE
NOTION_DATABASE_ID
NOTION_SECRET_TOKEN
SENDGRID_SECRET_TOKEN
```

## New database connection

Requires an integration https://www.notion.so/my-integrations

Go to database and add the integration as a connection

Get database ID from URL

e.g.

```
https://www.notion.so/6a58d3231dd24124b44ca8b42529795c?v=9db65cfe1cb74b398dad38f2b2207e5e
                      <------------------------------>
```


