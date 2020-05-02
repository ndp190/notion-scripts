from google.oauth2.service_account import Credentials
from notion.client import NotionClient
from notion_export import settings
import time

def export_sprint_tasks(notion_url):
    client = NotionClient(token_v2=settings.NOTION_TOKEN)
    cv = client.get_collection_view(notion_url)
    # Filter not working here, check for this later
    # table = cv.build_query(filter=filter_params).execute()
    table = cv.build_query().execute()
    sprint_tasks = []
    cur_timestamp = int(time.time())
    for i, row in enumerate(table):
        try:
            # id | title | app | epic | status | point | import_time
            id = 'https://www.notion.so/' + row.id.replace('-','')
            title = row.get_property('name')
            app = "\n".join(row.get_property('app'))
            epics = []
            for e in row.get_property('epic'):
                epics.append('https://www.notion.so/' + e.id.replace('-',''))
            epic = "\n".join(epics)
            sprint = row.get_property('sprint')
            status = row.get_property('status')
            points = row.get_property('points')

            # filter out not-in-sprint item
            if sprint in ['Backlog', '', None]:
                continue

            sprint_tasks.append([
                id,
                title,
                app,
                epic,
                sprint,
                status,
                points,
                cur_timestamp
            ])
        except AttributeError as err:
            print("[Error] {0} (row {1})".format(err, i))

    return sprint_tasks


def get_row_data(table_row):
    # get title
    # get status
    try:
        table_row.get_property('not exists')
    except AttributeError as err:
        print("[Error] {0}".format(err))
        pass
    pass


