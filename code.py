from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube#pip install pytube

Folder_Name = ''
fileSizeInBytes = 0
MazFileSize = 0

#open the location where to save the file
def openDirectory():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if (len(Folder_Name)> 1):
        locError.config(text=Folder_Name,fg="green")
    else:
        locError.config(text='enter the correct location!',fg='red')

#download file
def download():
    global MazFileSize,fileSizeInBytes
    choice = ytChoices.get()
    video = ytEntry.get()

    if (len(video)>1):
        ytEntryError.config(text='')
        print(video,'at',Folder_Name)
        yt = YouTube(video,on_progress_callback=progress)
        print('video name is:\n\n',yt.title)

        if (choice == choices[0]):
            loadingLabel.config(text='1080p video file downloading..')
            selectVideo = yt.streams.filter(progressive=True).first()

        elif (choice == choices[1]):
            loadingLabel.config(text='720p video file downloading..')
            selectVideo = yt.streams.filter(progressive=True).first()

        elif (choice == choices[2]):
            loadingLabel.config(text='480p video file downloading..')
            selectVideo = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif (choice == choices[3]):
            loadingLabel.config(text='3gp video file downloading..')
            selectVideo = yt.streams.filter(progressive=True,file_extension='3gp').first()

        elif (choice == choices[4]):
            loadingLabel.config(text='Audio file is downloading...')
            selectVideo = yt.streams.filter(only_audio=True).first()
        
        fileSizeInBytes = selectVideo.filesize
        MazFileSize = fileSizeInBytes / 1024000
        MB = str(MazFileSize) + 'MB'
        print('DOWNLOAD ON: {}'.format(Folder_Name))
        complete()
    else:
        ytEntryError.config(text="please enter the youtube link....",fg="red")

def progress(stream=None, chunk=None, file_handle=None, remaning=None):
    percent = (100 * (fileSizeInBytes - remaning)) / fileSizeInBytes
    print('{00.0f} downloaded'.format(percent))

def complete():
    loadingLabel.config(text='Download completed')

root = Tk()
root.title("youtube downloader")
root.columnconfigure(0, weight=1)#making all content center

#"enter the link here" label
ytlabel = Label(root, text="Enter the URL of the video", font=("anton", 30, "bold"))
ytlabel.grid()

#enter the url here
ytEnterUrl = StringVar()
ytEntry = Entry(root,width=50,textvariable=ytEnterUrl)
ytEntry.grid(pady=(0,20))

#error msg
ytEntryError = Label(root,fg='red',text='',font=('anton',20))
ytEntryError.grid()

#SaveLabel
SaveLabel = Label(root,text="Save the video",font=("anton", 20, "bold"))
SaveLabel.grid()

#btn for save location
entryBtn = Button(root,width=20,bg="blue",fg="white",text="select location", command=openDirectory)
entryBtn.grid()

#loction Error
locError = Label(root,text="",font=("anton", 10),fg="red")
locError.grid(pady=(0,0))

#select Quality label
selectQuality = Label(root,text="choose the Quality", font=("anton", 20, "bold"))
selectQuality.grid()

#combo box
choices = ["1080p","720p","480","360p","mp3"]
ytChoices = ttk.Combobox(root,values=choices)
ytChoices.grid()

#Download Btn
downloadBtn = Button(root, width=10,bg="black",fg="white",text="Download", command=download)
downloadBtn.grid()

loadingLabel = ttk.Label(root,text='coding-Bot',font=('anton',20,UNDERLINE))
loadingLabel.grid()
root.mainloop()
