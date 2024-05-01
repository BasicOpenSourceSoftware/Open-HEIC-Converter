import PIL
from pillow_heif import register_heif_opener
from tkinter import filedialog
from tkinter import messagebox
import os

filepathtotake=""
filepathtosave=""
done="Done!"
fileswitherrors=[]
#Give instructions
messagebox.showinfo("Open HEIC Converter","Please select what folder contains the files you want to convert then select where you want to save to")

#Ask for file paths
filepathtotake=filedialog.askdirectory()
filepathtosave=filedialog.askdirectory()

#for each item in folder open then convert the file using the file name
for file in os.listdir(filepathtotake):
    if file.endswith(".HEIC"):
        register_heif_opener()
        image = PIL.Image.open(filepathtotake+"\\"+file)
        print("Converting!",file)
        file=file.replace(".HEIC",".jpg")
        print(file)
        try:
            image.save(filepathtosave+"\\"+file)
        except:
            done="Done with errors one or more files could not be saved"
            fileswitherrors.append(file)
fileswitherrorsstr=''.join(str("\n"+x)for x in fileswitherrors)
messagebox.showinfo("Open HEIC Converter",done+fileswitherrorsstr)
