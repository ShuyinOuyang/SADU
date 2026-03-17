import json
import shutil
import os
from generate_QA_fill_in_the_blank import *


def complete_json_object():
    base_path = '../../dataset/'
    dirs = ['long_arrow', 'multiple_arrow', 'not_right_arrow', 'not_straight_arrow', 'overlap_arrow']
    for dir in dirs:
        path = base_path + 'SAD_hard/' + dir + '/'
        for i in range(5):
            folder = path + str(i) + '/Diagram/'
            target_folder = path + str(i) + '/json_object/'
            names = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
            file = names[0].replace('.png', '.json')
            copy_source = base_path + 'SAD/structural/json_object/' + file
            copy_target = target_folder + file
            print(copy_source, copy_target)
            shutil.copy2(copy_source, target_folder + file)

def write_json_in_file(x, file):
    with open(file, 'w') as f:
        f.write(json.dumps([x], indent=4))

# SAD_hard/long_arrow
base_path = '../../dataset/'
dirs = ['long_arrow', 'multiple_arrow', 'not_right_arrow', 'not_straight_arrow', 'overlap_arrow']
dir = dirs[4]
i = 4
# for dir in dirs:
# for i in range(5):
path = base_path + 'SAD_hard/' + dir + '/'

folder = path + str(i) + '/json_object/'

names = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
file = names[0]
print(dir, i, file)
with open(folder + file, 'r') as f:
    json_object = json.load(f)

# QA_list_ = generate_relation_source(json_object)
QA_list_ = generate_relation_target(json_object)
for x in QA_list_:
    # print(x['question'])
    if 'Team' in x['question']:
        print(x, flush=True)
        a = x
        break
        # QA_list_2 = generate_relation_target(json_object)

# write_json_in_file(a, folder.replace('json_object', 'QA') + file.replace('.json', '_QA.json'))
