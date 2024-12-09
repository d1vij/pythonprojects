import os
import shutil

#get extension
def extension(file):
    return file.split(".")[1]

#initiate folders

def mkfolders():
    try :
        for folder in ["text","images",'audio','video','program files','archive formats']:
            os.mkdir(folder)
    except FileExistsError:pass #:)

#mapping filetypes to their corresponding folders
def mapp():
    #to add new file extensions to group , add down here in variables
    #to make a custom folder for your desiered file types ,
    #add a new variable and corresponding codeblock down
    #egfolder = [ent.strip for ext in "<enter all filetypes here>"]
    #for ext in egfolder : map[ext] = "<foldername>"

    text = [ext.strip() for ext in "txt , rtf , docx , csv , doc , wps , wpd , msg".split(",")]
    images = [ext.strip() for ext in "jpg , png , webp , gif , tif , bmp , eps ".split(",")]
    audio = [ext.strip() for ext in "mp3 , wma , snd , wav , ra , au , aac".split(",") ]
    video = [ext.strip() for ext in "mp4 , 3pg , avi , mpg , mov , wmv".split(",")]
    programfiles = [ext.strip() for ext in "c ,py, cpp , java , py , js , ts , cs , swift , sh , bat , com , exe , html , htm , xhtml , css".split(",")]
    archivedformats = [ext.strip() for ext in "rar , zip , tar , gz , z".split(",")]

    map = {}

    for ext in text:map[ext] = "text"
    for ext in images:map[ext] = "images"
    for ext in audio:map[ext] = "audio"
    for ext in archivedformats:map[ext] = "archive formats"
    for ext in programfiles:map[ext] = "program files"

    return map

#copying part
def move():
    #list of all the files in the cwd
    cwd_files = [file for file in os.listdir() if os.path.isfile(file)]

    #current working directory
    curwd = os.path.abspath(os.path.realpath(os.getcwd()))
    mapping = mapp()
    mf=[]
    for file in cwd_files:
        try:
            dst_folder = mapping[extension(file)]
            shutil.copy2(file, dst_folder)
            mf.append(file)
        except KeyError:
            print(f"Cannot group file {file} no folder for {extension(file)} is defined !")
    for file in mf:os.remove(file) #removes all the files from current directory which haved been moved / grouped

if __name__=="__main__":
    mkfolders()
    move()
