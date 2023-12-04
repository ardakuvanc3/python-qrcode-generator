import qrcode as qr
import tkinter as tk

isGenerate = False
def createWindow():
    global rootWindow
    rootWindow = tk.Tk()
    rootWindow.configure(width=400, height=400)
    rootWindow.title("QRCode Generator")
    rootWindow.configure(background='azure2')
    rootWindow.resizable(False, False)

    generateButton()
    generateInput()
    generateName()
    labels()


    rootWindow.mainloop()

def createQRCode():
    qrGenerate = qr.make(generateInputVar.get())
    qrGenerate.save(generateNameVar.get() + ".png")
    isGenerate = True


def generateButton():
    generateBTN = tk.Button(rootWindow, text="Generate", command=createQRCode, background='azure2', height=2, width=10, fg="black",font="sans 10 bold", border=3)
    generateBTN.place(x="140", y="250")

def generateInput():
    global generateInputVar
    generateInputVar = tk.Entry(rootWindow)
    generateInputVar.place(x="90", y="50")

def generateName():
    global generateNameVar
    generateNameVar = tk.Entry(rootWindow)
    generateNameVar.place(x="90", y="100")

def labels():
    global urlLabel, nameLabel, product
    urlLabel = tk.Label(rootWindow, text="URL: ", background='azure2',font="sans 13 bold")
    urlLabel.place(x="20", y="50")

    nameLabel = tk.Label(rootWindow, text="File Name: ", background='azure2',font="sans 13 bold")
    nameLabel.place(x="20", y="100")

    product = tk.Label(rootWindow, text="Development by Arda Kuvanç", background='azure2', font="sans 9 italic")
    product.place(x="210", y="380")

createWindow()

#Arda Kuvanç