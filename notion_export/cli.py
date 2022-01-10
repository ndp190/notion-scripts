from notion_export.utils.notion_export import export_sprint_tasks
from notion_export.utils.export_epics import export_epics
from notion_export.utils.gsheet_import import import_sprint_tasks
import sys
import getopt

def main(argv):
    notion_url = gg_sheet_key = gg_sheet_index = None
    help_text = 'notion_export --notion-url <notion-url> --gg-key <google-sheet-key> --gg-index <google-sheet-index> [--action <export_sprint_tasks|export_epic>]'

    try:
        opts, args = getopt.getopt(
            argv, "hi:o:", ["notion-url=", "gg-key=", "gg-index="])
    except getopt.GetoptError as e:
        print(help_text)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(help_text)
            sys.exit()
        elif opt in ("--notion-url"):
            notion_url = arg
        elif opt in ("--gg-key"):
            gg_sheet_key = arg
        elif opt in ("--gg-index"):
            gg_sheet_index = arg
        elif opt in ("--action"):
            action = arg
    if None in (notion_url, gg_sheet_key, gg_sheet_index):
        print(help_text)
        sys.exit()
    
    if action == 'export_sprint_task':
        sprint_tasks = export_sprint_tasks(notion_url)
        import_sprint_tasks(sprint_tasks, gg_sheet_key, gg_sheet_index)
    elif action == 'export_epic':
        epics = export_epics(notion_url)
        println(epics)
        # import_sprint_tasks(sprint_tasks, gg_sheet_key, gg_sheet_index)

if __name__ == "__main__":
    main()
