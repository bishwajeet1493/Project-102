import os 
import shutil
from_directory= "C:/Users/Lenovo/Downloads/Project 102"
to_directory= "C:/Users/Lenovo/OneDrive/Documents/Document_Files"
listOfFiles= os.listdir(from_directory)
print(listOfFiles)
for file_name in listOfFiles:
    name,extension= os.path.splitext(file_name)
    if extension== '':
        continue
    if extension in [ '.txt', '.doc', '.docx', '.pdf','.xlsx','.xls']:
        path1= from_directory +'/'+ file_name
        path2= to_directory +'/'+ "Document_Files"
        path3= to_directory + '/' + "Document_Files" + '/' + file_name
        if os.path.exists(path2):
            print('Moving'+file_name)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving"+file_name)    
            shutil.move(path1,path3)