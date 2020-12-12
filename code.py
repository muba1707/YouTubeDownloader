from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube#pip install pytube

Folder_Name = ""

#file location
def openLocation():
  global Folder_Name
  Folder_Name = filedialog.askdirectory()
  if(len(Folder_Name) > 1):
    locationError.config(text=Folder_Name,fg="green")
  else:
    locationError.config(text="Please enter the correct location!!",fg="red")

#download the video
def downloadVideo():
  choice = ytChoices.get()
  url = ytEntry.get()

  if(len(url) > 1):
    ytError.config(text="")
    yt = YouTube(url)

    if(choice == choices[0]):
      select = yt.streams.filter(progressive=True).first()

    elif(choice == choices[1]):
      select = yt.streams.filter(progressive=True,file_extension='mp4').middle()
    
    elif(choice == choices[2]):
      select = yt.streams.filter(progressive=True,
      file_extension='mp4').last()

    elif(choice == choices[4]):
      select = yt.streams.filter(only_audio=True).first()

    else:
      ytError.config(text="Paste Link again!",fg="red")

  #download function
  select.download(Folder_Name)
  ytError.config(text="Download completed")

root = Tk()
root.title("youtube downloader")
root.geometry("350x400")
root.columnconfigure(0, weight=1)#making all content center

#"enter the link here" label
ytlabel = Label(root, text="Enter the URL of the video", font=("anton", 20, "bold"))
ytlabel.grid()

#enter the url here
ytEnterUrl = StringVar()
ytEntry = Entry(root,width=50,textvariable=ytEnterUrl)
ytEntry.grid()

#Error msg
ytError = Label(root,text="you enter the worng URL",font=("anton", 10),fg="red")
ytError.grid()

#SaveLabel
SaveLabel = Label(root,text="Save the video",font=("anton", 15, "bold"))
SaveLabel.grid()

#btn for save location
entryBtn = Button(root,width=10,bg="blue",fg="white",text="select location",command=openLocation)
entryBtn.grid()

#loction Error
locError = Label(root,text="you the coorect location",font=("anton", 10),fg="red")
locError.grid()

#select Quality label
selectQuality = Label(root,text="choose the Quality", font=("anton", 15, "bold"))
selectQuality.grid()

#combo box
choices = ["720p","360p","144p","Only Audio"]
ytChoices = ttk.Combobox(root,values=choices)
ytChoices.grid()

#Download Btn
downloadBtn = Button(root, width=10,bg="black",fg="white",text="Download",command=downloadVideo)
downloadBtn.grid()



root.mainloop()
