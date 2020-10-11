import os
files = os.listdir()
files.remove("008.OrganisingFoldersAndFilesUsingProgram.py")
# print(files)  # To make a list of the present directory 

def FolderExitsOrNot(NameOfTheFolder):
    if not os.path.exists(NameOfTheFolder):
        os.mkdir(NameOfTheFolder)


# Making the directories 
FolderExitsOrNot("Images")
FolderExitsOrNot("Docs")
FolderExitsOrNot("Videos")
FolderExitsOrNot("Compressed")

# IDVC = image documents video compressed 
def sortingOutAll(li):
    IDVC = [file for file in files if os.path.splitext(file)[1].lower in li]
    return IDVC
    

# Adding the images extension to it 
imageExt = [".jpg", ".png",".jpeg"]
image = sortingOutAll(imageExt)

# Adding the Docs Files now 
docExt = [".docx",".doc",".txt",".pdf"]
document = sortingOutAll(docExt)

# Adding media extensions 
mediaExt = [".mp4",".mp3",".mkv",".flv"]
media = sortingOutAll(mediaExt)

# Adding the compressed files now 
compressedExt = [".rar",".zip"]
compressed = sortingOutAll(compressedExt)

# adding all others to the separate folder 
other = [] 
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in imageExt) and (ext not in mediaExt) and (ext not in compressedExt) and (ext not in docExt) and os.path.isfile(file):
        other.append(file)

FolderExitsOrNot("Other Folder")


def movingToTheRespectiveLocation(folderName , files):
    for file in files:
        os.replace(file , f"{folderName} / {file}")

movingToTheRespectiveLocation("Images" , image)
movingToTheRespectiveLocation("Documents" , document)
movingToTheRespectiveLocation("Videos" , media)
movingToTheRespectiveLocation("Compressed" , compressed)
movingToTheRespectiveLocation("Other Folder " , other)

