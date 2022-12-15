#KingOfMongeese
#12/14/2022
#Install minecraft mods to mods folder

import os
import tkinter.messagebox
from tkinter import *
import tkinter
import time
from zipfile import ZipFile
import sys

#get target dir
userprof = os.environ['USERPROFILE']
targetdir = userprof + "\\AppData\Roaming\\.minecraft\\mods"


def get_all_file_paths(directory):
    # initializing empty file paths list
    file_paths = []

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    # returning all file paths
    return file_paths

def makeDir(targetdir):
    #make dir if not there
    proceed = tkinter.messagebox.askyesno(title="Make Target Dir", message="Target Directory: %s not found.\nMake now?" % (targetdir))
    if proceed:
        cmd = "mkdir %s" % (targetdir)
        os.system(cmd)
    else:
        tkinter.messagebox.showwarning(message="No target dir open. Shutting Down")
        exit(1)

def changeDirLaunch():
    #ui for change dir function


    changeDirWindow = tkinter.Toplevel(window)
    changeDirWindow.title("Change target directory")
    tkinter.Label(changeDirWindow, text = "Enter new target full path: ").grid(row = 0, column= 0)
    tkinter.Entry(changeDirWindow, textvariable= newTargetdir).grid(row= 0, column=1)

    def changeDir():
        global targetdir
        newTargetdir2 = newTargetdir.get()
        targetdir = newTargetdir2
        global targetLabel
        targetLabel.config(text="Target Directory: %s" % (targetdir))
        changeDirWindow.destroy()
        changeDirWindow.update()

    tkinter.Button(changeDirWindow, text = "done", command=changeDir).grid(row = 0, column = 2)

def install():
    installWindow = tkinter.Toplevel(window)
    installWindow.title("Installing Mods . . .")

    #items contained within a listview
    scrollbar = Scrollbar(installWindow)
    scrollbar.pack(side= RIGHT, fill=Y)

    mylist = Listbox(installWindow, yscrollcommand = scrollbar.set, width = 150, height= 45 )
    mylist.pack(side = LEFT, fill = BOTH, padx= 30, pady = 30,)

    scrollbar.config(command = mylist.yview)

    global targetdir

    #make sure targer dir exists
    if os.path.exists(targetdir):
        mylist.insert(END, "Target Directory: %s" % (targetdir))
        mylist.update()
    else:
        makeDir(targetdir)
        mylist.insert(END, "Target Directory: %s" % (targetdir))

    #check if dir is empty, then back up dir in a zip if it is not
    targetdirNums = os.listdir(targetdir)
    if len(targetdirNums) != 0:
        tkinter.messagebox.showinfo(title = "Target Directory Info", message="Target directory is not empty.\nCurrent contents will be backed up to zip file placed on the Desktop.")

        targetdirContents = get_all_file_paths(targetdir)
        time_var = time.process_time_ns()

        ziptarget = os.environ['USERPROFILE']
        ziptarget += "\\Desktop\\R_mc_mod_install_%s.zip" % (time_var)


        with ZipFile(ziptarget, 'w') as zip:
            for file in targetdirContents:
                zip.write(file)

        for file in targetdirNums:
            target = targetdir + "\\" + file
            if os.path.isdir(target):
                cmd = "rmdir /s /q %s" % target
                os.system(cmd)
            else:
                os.remove(target)

    #get mod list
    modlist = os.listdir(os.getcwd())

    count = 1
    fails = 0
    failed =[]
    failedcmds = []

    #copy files
    for mod in modlist:
        if mod.__contains__(".jar"):
            mylist.insert(END, "%d. Mod:  %s" % (count, mod))
            mylist.insert(END, "Copying %s to %s" % (mod, targetdir))
            mylist.update()
            newModLocation = targetdir + "\\" + mod
            mod = os.getcwd() + "\\" + mod

            #must use xcopy for special chars
            cmd = '"xcopy %s %s"' % (mod, targetdir)
            os.system(cmd)
            if os.path.exists(newModLocation):
                mylist.insert(END, "Success")
                mylist.update()
                installWindow.update()
            else:
                mylist.insert(END, "Fail")
                mylist.update()
                installWindow.update()
                failed.append(mod)
                fails += 1
                failedcmds.append(cmd)
            count += 1
            time.sleep(.3)

    #error handleing
    if fails > 0:
        tkinter.messagebox.showerror(title = "Status", message= "Failed to copy %d files.\n\nFiles: %s\n\nCmds: %s\nView Error Log file." % (fails, str(failed),str(failedcmds)))
        date = time.ctime()
        date = date.replace(" ", "-")
        date = date.replace(":", ".")
        fname = "log\\Error-Log-" + date + ".txt"
        os.system("mkdir log")


        with open(fname, 'w') as file:
            for fail in failed:
                out = str(fail) + "\n"
                file.write(out)
            for cmd in failedcmds:
                out = str(cmd) + "\n"
                file.write(out)
        installWindow.destroy()
        installWindow.update()
        exit(2)

    #normal exit
    else:
        tkinter.messagebox.showinfo(title = "Status", message = "All mods copied")
        installWindow.destroy()
        installWindow.update()
        sys.exit(0)





window=tkinter.Tk()
window.geometry("750x90")
window.title("Mods Install")
window.resizable(False, False)

newTargetdir = tkinter.StringVar()

targetLabel = tkinter.Label(window, text="Target Directory: %s" % (targetdir), font=("calibre", 12))
targetLabel.grid(row = 0, columnspan = 1)

installButton = tkinter.Button(text="Install", command = install, height = 2, width = 30)
installButton.grid(row = 1, column= 0)


changedirButton = tkinter.Button(text="Change Target Directory", command = changeDirLaunch, height = 2, width = 30)
changedirButton.grid(row = 1, column= 1)


window.mainloop()
