import os
import shutil
fromdir = "C:\\Users\Shradha\\Downloads"
todir = "C:\\Users\\Shradha\\Desktop\\Documents"
listoffile = os.listdir(fromdir)

for filename in listoffile:
    name,extension = os.path.splitext(filename)
    if extension == "":
        continue
    if extension in [ ".txt", ".doc", ".docx", ".pdf"]:
        path1 = fromdir + "/" + filename
        path2 = todir + "/" + "Document_File"
        path3 = todir + "/" + "Document_File" + "/" + filename

        if os.path.exists(path2):
            print("moving " + filename)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving " + filename)
            shutil.move(path1,path3)
