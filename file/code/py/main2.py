"""
(大创项目自动命名脚本 .py)
使用说明:
脚本所在文件夹需要有以下的文件夹及文件:

某个文件夹
├─ final         # 存放处理后的文件
├─ ori           # 存放原本的文件
├─ info.xls      # 一览表
└─ main.py       # 脚本

运行脚本即可在 final 文件夹看到处理结果
有些无法转化, 记得去final文件夹中检查
"""

import pandas as pd
import os
import shutil

class XlsItem:
    def __init__( self, id, keyId, type, projectName,
                 headAuthor, **kwargs ):
        self.id = id
        self.keyId = str(keyId).replace('\n', '').rstrip()
        self.type = str(type).replace('\n', '').rstrip()
        self.projectName = str(projectName).replace('\n', '').rstrip()
        self.headAuthor = str(headAuthor).replace('\n', '').rstrip()
        self.__dict__.update(kwargs)
    
    def __str__( self ):
        ss = "id=" + str(self.id) + ", keyId=" + self.keyId + ", type=" + self.type
        ss += ", projectName=" + self.projectName + ", headAuthor=" + self.headAuthor
        return "{" + ss + "}"
    


excelRoad = "./info.xls"
oriFileDirRoad = './ori'
finalFileDirRoad = './final'
xlsInfos = []
xlsInfosMapByKeyId = {}
xlsInfosMapByProjectName_5 = {}
xlsInfosMapByProjectAuthor = {}
xlsColumnsMapper = {"id" : 0, "keyId" : 0, "type" : 2, "projectName": 4, "headAuthor" : 5}

def processXls( fileRoad ):
    data = pd.read_excel( fileRoad )
    for i in range( 1, data.shape[0] ):
        item = XlsItem( data.iloc[:, xlsColumnsMapper["id"]][i],
                        data.iloc[:, xlsColumnsMapper["keyId"]][i],
                        data.iloc[:, xlsColumnsMapper["type"]][i],
                        data.iloc[:, xlsColumnsMapper["projectName"]][i],
                        data.iloc[:, xlsColumnsMapper["headAuthor"]][i])
        # print( item )
        xlsInfosMapByKeyId[ item.keyId ] = item
        xlsInfosMapByProjectName_5[ item.projectName[ : 5] ] = item
        xlsInfosMapByProjectAuthor[ item.headAuthor ] = item

def formName( type, name, headAuthor ):
    return type + "+" + name[ : 7] + "+" + headAuthor

def tryFigureDivide( ch, ori_name ):
    pos = ori_name.find( ch )
    fileType = ori_name[ ori_name.rfind(".") :]
    if pos != -1:
        projectName = ori_name.split( ch )[1].rstrip().strip()
        if len(projectName) > 5 :
            tem = projectName[:5]
            if tem in xlsInfosMapByProjectName_5:
                return formName( xlsInfosMapByProjectName_5[tem].type , 
                                    projectName, xlsInfosMapByProjectName_5[tem].headAuthor ) + fileType
        headAuthor = ori_name.split( ch )[2].rstrip().strip()
        headAuthor = headAuthor[: headAuthor.find('.')].rstrip().strip()
        if headAuthor in xlsInfosMapByProjectAuthor:
            return formName( xlsInfosMapByProjectAuthor[headAuthor].type, 
                                xlsInfosMapByProjectAuthor[headAuthor].projectName, headAuthor) +  fileType
    return "NULL"

def getStanderdName( ori_name ):
    fileType = ori_name[ ori_name.rfind(".") :]
    # if devide by '+', order : keyId+progectName+headAuthor
    ss = tryFigureDivide( "+", ori_name )
    if ss != "NULL":
        return ss
    ss = tryFigureDivide( " ", ori_name )
    if ss != "NULL":
        return ss
    projectName = ori_name[:5]
    if projectName in xlsInfosMapByProjectName_5:
            return formName( xlsInfosMapByProjectName_5[projectName].type , 
                             projectName, xlsInfosMapByProjectName_5[projectName].headAuthor ) + fileType
    
    raise Exception("Cannot get Standerd Name")

def process( ori_dir, final_dir ):
    files = os.listdir( ori_dir )
    for pr in files :
        # print(pr)
        ori_road = ori_dir + "/" + pr
        final_road = ""
        try :
            final_road = final_dir + "/" + getStanderdName( pr )
        except :
            print( pr + " cannot be transform")
            final_road = final_dir + "/" + pr      
        # print(final_road)
        shutil.copy( ori_road, final_road )

if __name__ == "__main__":
    processXls( excelRoad )
    process( oriFileDirRoad , finalFileDirRoad )