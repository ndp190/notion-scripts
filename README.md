# notion-scripts

Some scripts for Notion

## Installation

### Setup .env

- copy `.env.sample` to `.env`

- replace `.env` content to your desired value

## Scripts

### Notion export

```
# setup google API https://gspread.readthedocs.io/en/latest/oauth2.html
pip install -r requirements.txt
python -m notion_export --notion-url <notion-url> --gg-key <google-sheet-key> --gg-index <google-sheet-index>
```
