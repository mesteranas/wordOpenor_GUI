import os,json,settings
bookMarksPath=os.path.join(os.getenv('appdata'),settings.app.appName,"bookmarks.json")
if not os.path.exists(bookMarksPath):
    with open(bookMarksPath,"w",encoding="utf-8") as file:
        json.dump({},file,ensure_ascii=False,indent=4)
def editPage(path:str,pageNumber:int):
    with open(bookMarksPath,"r",encoding="utf-8") as file:
        data=json.load(file)
    data[path]=pageNumber
    with open(bookMarksPath,"w",encoding="utf-8") as file:
        json.dump(data,file,ensure_ascii=False,indent=4)
def getPageNumber(path:str):
    with open(bookMarksPath,"r",encoding="utf-8") as file:
        data=json.load(file)
    try:
        return data[path]
    except:
        return 0