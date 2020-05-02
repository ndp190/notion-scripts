# notion-export
Export notion utilities 

## Installation
### Setup .env

- copy `.env.sample` to `.env`

- replace `.env` content to your desired value

- setup google API https://gspread.readthedocs.io/en/latest/oauth2.html

- run

```
pip install -r requirements.txt
python -m notion_export --notion-url <notion-url> --gg-key <google-sheet-key> --gg-index <google-sheet-index>
```
