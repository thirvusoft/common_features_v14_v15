import os
import shutil

from frappe.utils import update_progress_bar
def file_override():
    list = [
        {
            'source':'/common_features_v14/common_features_v14/core_backup/list_view.js',
            'destination':'/frappe/frappe/public/js/frappe/list/list_view.js'
        },
        {
            'source':'/common_features_v14/common_features_v14/core_backup/page.js',
            'destination':'/frappe/frappe/public/js/frappe/ui/page.js'
        },
    ]
    l=len(list)
    n=0
    for i in list:
        source_to_destination(i['source'],i['destination'])
        update_progress_bar(f"File Overriding in Common Features V14", n, l)
        n =n+1
    print()

def source_to_destination(s,d):
    directory = os.getcwd()
    path = directory.replace('sites','apps')
    source = path+s
    destination = path+d
    shutil.copy(source, destination)

