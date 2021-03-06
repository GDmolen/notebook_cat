import json
import sys

# handle argument exceptions
if len(sys.argv) < 3:
    raise Exception('参数数量必须大于 2！')


# accept argument list
notebook_path_lst = sys.argv[1:]

target_notebook = {}
cells_lst = []

# read notebook path list
for path in notebook_path_lst:
    with open(path) as notebook:
        notebook_str = notebook.read()
        notebook_json = json.loads(notebook_str)
        cells = notebook_json['cells']
        cells_lst += cells

target_notebook['cells'] = cells_lst





del notebook1_json['cells']

# cat two notebooks
target_cells = cells1 + cells2



# target_notebook['cells'] = target_cell
target_notebook.update(notebook1_json)

target_str = json.dumps(target_notebook)



target = open('target_notebook.ipynb', 'w')
target.write(target_str)