import json

def Doc_handler_mieten(dict_item):
    f = open("HausMieten_results.txt", "a")
    json_objct=json.dumps(dict_item)
    f.write(json_objct)
    f.write("\n")
    f.close()

def Doc_handler_kaufen(dict_item):
    f = open("HauseKaufen_results.txt", "a")
    json_objct=json.dumps(dict_item)
    f.write(json_objct)
    f.write("\n")
    f.close()