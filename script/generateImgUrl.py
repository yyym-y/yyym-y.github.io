import os
import json

unuse_path = "../assets/util"
use_path = "../assets/cover"
ori_path = "../assets/util/ori"
js_path = "../js/data/imgData.js"
abs_path = "/assets/"

infos = { "img" : [], "ori" : [] }
ori_info = []

def _check( ori_, url ):
    # print(ori_.split(".")[0])
    # print(url.split(".")[0])
    for i in range( min( len(ori_.split(".")[0]), len(url.split(".")[0]) ) ):
        if (ori_[i] != url[i]):
            return False
    return True

def find_ori( url, path ):
    for pr in ori_info:
        if _check( pr, url ):
            # print("/assets/util/ori/" + pr)
            return "/assets/util/ori/" + pr
    return path[2:] + "/" + url


for pr in os.listdir( ori_path ):
    ori_info.append( pr )

for pr in os.listdir( unuse_path ):
    if os.path.isdir( unuse_path + "/" + pr ):
        continue
    infos["img"].append( abs_path + "util/" + pr )
    infos["ori"].append( find_ori( pr, unuse_path ) )

def find_use( path ):
    for pr in os.listdir( path ):
        new_path = fi_d = os.path.join( path, pr )
        if  os.path.isdir( new_path ):
            find_use( new_path )
        else:
            infos["img"].append( new_path[2:] )
            infos["ori"].append( find_ori( pr, new_path ) )

find_use( use_path )

strr = "export default"
strr += json.dumps(infos)

with open( js_path, 'w' ) as file:
    file.write( strr )