from google.oauth2.service_account import Credentials
from notion.client import NotionClient
from notion_export import settings
import time

def export_epics(notion_url):
    client = NotionClient(token_v2=settings.NOTION_TOKEN)
    cv = client.get_collection_view(notion_url)
    # Filter not working here, check for this later
    # table = cv.build_query(filter=filter_params).execute()
    table = cv.build_query().execute()
    sprint_tasks = []
    cur_timestamp = int(time.time())
    for i, row in enumerate(table):
        try:
            # filter out not InTheFlow mission item
            if len(row.get_property('areas')) == 0 or row.get_property('areas')[0].title != 'InTheFlow':
                continue

            # id | title | app | epic | status | point | import_time
            id = 'https://www.notion.so/' + row.id.replace('-','')
            title = row.get_property('name')
            app = "\n".join(row.get_property('app'))
            epics = []
            for e in row.get_property('epic'):
                epics.append('https://www.notion.so/' + e.id.replace('-',''))
            epic = "\n".join(epics)
            status = row.get_property('status')
            points = row.get_property('points')
            
            should_skip = False
            sprints = row.get_property('sprint')
            if len(sprints) == 0:
                should_skip = True

            sprint = []
            for s in sprints:
                if (s is None):
                    continue
                elif (s.title in ['Backlog', '', None]):
                    should_skip = True
                else:
                    sprint.append(s.title)

            if should_skip:
                continue

            sprint = "\n".join(sprint)

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
