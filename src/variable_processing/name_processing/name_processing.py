import json

def remove_null_var_name(raw_path_data):
    for i in data['edges']:
        count = 0
        if (i['attribute'][1] != "NaN"):
            att = json.loads(i['attribute'][1])
            for key in att.keys():
                if (att[key]['name'] == 'null'):
                    att[key]['name'] = f'var{count}'
                    count += 1
            i['attribute'][1] = str(att)

json_object = json.dumps(data, indent=4)
with open(file_out, "w") as outfile:
    outfile.write(json_object)
f.close()