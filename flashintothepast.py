from zipfile import ZipFile
import os
import subprocess
import wget
execlocation = os.getcwd()

print("Downloading ZIP with Macromedia Flash executables...")
wget.download("https://download1581.mediafire.com/mt492gsjajtg/r9sop6ssvqyu4k3/flashyfiles.zip", out="flashyfiles.zip")
with ZipFile('flashyfiles.zip', 'r') as zipObj:
   print("Extracting ZIP with Macromedia Flash executables...")
   zipObj.extractall()

print("Entering Macromedia Flash directory...")
os.chdir("flashyfiles")
directory2go = "%s\\flashyfiles"%execlocation
def runflashfiles():
    print("Starting round!")
    os.chdir(directory2go)
    subprocess.Popen("flash1.exe")
    print("flash1.exe started.")
    subprocess.Popen("flash2.exe")
    print("flash2.exe started.")
    subprocess.Popen("flash3.exe")
    print("flash3.exe started.")
    subprocess.Popen("flash4.exe")
    print("flash4.exe started.")
    subprocess.Popen("flash5.exe")
    print("flash5.exe started.")
    subprocess.Popen("flash6.exe")
    print("flash6.exe started.")
    subprocess.Popen("flash7.exe")
    print("flash7.exe started.")
    subprocess.Popen("flash8.exe")
    print("flash8.exe started.")
    subprocess.Popen("flash9.exe")
    print("flash9.exe started.")
    subprocess.Popen("flash10.exe")
    print("flash10.exe started.")
    subprocess.Popen("flash11.exe")
    print("flash11.exe started.")
    subprocess.Popen("flash12.exe")
    print("flash12.exe started.")
    os.chdir("mmTour")
    subprocess.Popen("tour.exe")
    print("tour.exe started.")
    print("Starting next round...")
    runflashfiles()
    return

runflashfiles()
