import json

def Doc_handler(dict_item):
    f = open("scrap_results.txt", "a")
    json_objct=json.dumps(dict_item)
    f.write(json_objct)
    f.write("\n")
    f.close()