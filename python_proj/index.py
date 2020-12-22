from tkinter import *
from PIL import Image,ImageTk
from PIL import ImageFilter
from PIL import ImageEnhance
import cv2 
from skimage.color import rgb2gray
from skimage.io import imread, imsave
import matplotlib.pyplot as plt
import numpy as np

def beginWindow():
    window1 = Toplevel(window)
    window1.geometry("600x400")
    window1.config(background='#41B77F')
    window1.resizable(FALSE, FALSE)
    lbl = Label(window1, text="Let's apply some filters", font=("Courrier",32), bg='#41B77F', fg='white')
    lbl.pack()
    
    #button filters
    btn2 = Button(window1, text="Filters", command=filterWindow)
    btn2.pack()
    
    #button contrast
    btn3 = Button(window1, text=" Contrast", command=contrastWindow)
    btn3.pack()
    
    #button resize image
    btn6 = Button(window1, text="Resize an Image", command=resWindow)
    btn6.pack()
    
    #button blur 
    btn7 = Button(window1, text="Gaussian Blur", command=gWindow)
    btn7.pack()

    #button median blur 
    btn8 = Button(window1, text="Median Blur", command=mWindow)
    btn8.pack()
    
    #button median blur 
    btn9 = Button(window1, text="Detect Edges", command=eWindow)
    btn9.pack()
    
    #button median blur 
    btn10 = Button(window1, text="Convert image to grayscale (Black & White)", command=bWindow)
    btn10.pack()
    
    #button median blur 
    btn11 = Button(window1, text="Reduce Noise", command=rnWindow)
    btn11.pack()
    
    #button median blur 
    btn12 = Button(window1, text="Get image contour", command=gcWindow)
    btn12.pack()
    ###########
    btnf = Button(window1, text="Close Me", command=lambda: window1.destroy())
    btnf.pack()

#filtres function
def filterWindow():
    
    new_window = Toplevel(window)
    new_window.resizable(FALSE, FALSE)
    image = Image.open(r"G:\projets\python_proj\loup-entretien-marianne.jpg")
    new_window.geometry("800x700")
    photo = ImageTk.PhotoImage(image)
    label = Label(new_window,image=photo)
    label.image =photo  
    label.pack()

  
    btn22 = Button(new_window, text="Change filtre", command=filtre1 )
    btn22.pack()
    btn22 = Button(new_window, text="Close Me", command=lambda: new_window.destroy())
    btn22.pack()

#filtres button function
def filtre1():
    filename = r"G:\projets\python_proj\loup-entretien-marianne.jpg"
    img_read_as_grayscale = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    plt.imshow(img_read_as_grayscale)
    plt.title('img_read_as_grayscale')
    plt.show()    


#contrast function   
def contrastWindow():
    windoww = Toplevel(window)
    windoww.resizable(FALSE, FALSE)
    image = Image.open(r"G:\projets\python_proj\loup-entretien-marianne.jpg")
    windoww.geometry("800x700")
    photo = ImageTk.PhotoImage(image)

    label = Label(windoww,image=photo)
    label.image = photo  
    label.pack()

    btn22 = Button(windoww, text="change contrast", command=contrast )
    btn22.pack()
    btn22 = Button(windoww, text="Close Me", command=lambda: windoww.destroy())
    btn22.pack()

#contrast button function
def contrast():
    filename = r"G:\projets\python_proj\loup-entretien-marianne.jpg"
    img = cv2.imread(filename)
    contrast_img = cv2.addWeighted(img, 2.5, np.zeros(img.shape, img.dtype), 0, 0)
    cv2.imshow('Contrast Image', contrast_img)
    cv2.waitKey(0)


#resize function
def resWindow():
    new_window = Toplevel(window)
    new_window.resizable(FALSE, FALSE)
    image = Image.open(r"G:\projets\python_proj\loup-entretien-marianne.jpg")
    new_window.geometry("800x700")
    photo = ImageTk.PhotoImage(image)
    label = Label(new_window,image=photo)
    label.image =photo  
    label.pack()

  
    btn22 = Button(new_window, text="Resize ", command=resize )
    btn22.pack()
    btn22 = Button(new_window, text="Close Me", command=lambda: new_window.destroy())
    btn22.pack()
#resize button function
def resize():
    filename = r"G:\projets\python_proj\loup-entretien-marianne.jpg"
    img = cv2.imread(filename)
    newImg = cv2.resize(img, (0,0), fx=0.75, fy=0.75)
    cv2.imshow('Resized Image', newImg)
    cv2.waitKey(0)    

#gaussian blur function
def gWindow():
    new_window = Toplevel(window)
    new_window.resizable(FALSE, FALSE)
    image = Image.open(r"G:\projets\python_proj\loup-entretien-marianne.jpg")
    new_window.geometry("800x700")
    photo = ImageTk.PhotoImage(image)
    label = Label(new_window,image=photo)
    label.image =photo  
    label.pack()

  
    btn22 = Button(new_window, text="Gaussian ", command=gaussian )
    btn22.pack()
    btn22 = Button(new_window, text="Close Me", command=lambda: new_window.destroy())
    btn22.pack()
#gaussian button function
def gaussian():
    filename = r"G:\projets\python_proj\loup-entretien-marianne.jpg"
    img = cv2.imread(filename)
    blur_image = cv2.GaussianBlur(img, (7,7), 0)
    cv2.imshow('Blur Image', blur_image)
    cv2.waitKey(0)   


#Median Blur function
def mWindow():
    new_window = Toplevel(window)
    new_window.resizable(FALSE, FALSE)
    image = Image.open(r"G:\projets\python_proj\loup-entretien-marianne.jpg")
    new_window.geometry("800x700")
    photo = ImageTk.PhotoImage(image)
    label = Label(new_window,image=photo)
    label.image =photo  
    label.pack()

  
    btn22 = Button(new_window, text="Median  ", command=median )
    btn22.pack()
    btn22 = Button(new_window, text="Close Me", command=lambda: new_window.destroy())
    btn22.pack()
#Median Blur button function
def median():
    filename = r"G:\projets\python_proj\loup-entretien-marianne.jpg"
    img = cv2.imread(filename)
    blur_image = cv2.medianBlur(img,5)
    cv2.imshow('Blur Image', blur_image)
    cv2.waitKey(0) 




#Detect Edges function
def eWindow():
    new_window = Toplevel(window)
    new_window.resizable(FALSE, FALSE)
    image = Image.open(r"G:\projets\python_proj\loup-entretien-marianne.jpg")
    new_window.geometry("800x700")
    photo = ImageTk.PhotoImage(image)
    label = Label(new_window,image=photo)
    label.image =photo  
    label.pack()

  
    btn22 = Button(new_window, text="Detect Edges  ", command=edge )
    btn22.pack()
    btn22 = Button(new_window, text="Close Me", command=lambda: new_window.destroy())
    btn22.pack()
#edge button function
def edge():
    filename = r"G:\projets\python_proj\loup-entretien-marianne.jpg"
    img = cv2.imread(filename)
    edge_img = cv2.Canny(img,100,200)
    cv2.imshow("Detected Edges", edge_img)
    cv2.waitKey(0) 



#Detect Edges function
def bWindow():
    new_window = Toplevel(window)
    new_window.resizable(FALSE, FALSE)
    image = Image.open(r"G:\projets\python_proj\loup-entretien-marianne.jpg")
    new_window.geometry("800x700")
    photo = ImageTk.PhotoImage(image)
    label = Label(new_window,image=photo)
    label.image =photo  
    label.pack()

  
    btn22 = Button(new_window, text="Black & White", command=black )
    btn22.pack()
    btn22 = Button(new_window, text="Close Me", command=lambda: new_window.destroy())
    btn22.pack()
#edge button function
def black():
    filename = r"G:\projets\python_proj\loup-entretien-marianne.jpg"
    img = cv2.imread(filename)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Scale Image", gray_img)
    cv2.waitKey(0) 


#Reduce Noise function
def rnWindow():
    new_window = Toplevel(window)
    new_window.resizable(FALSE, FALSE)
    image = Image.open(r"G:\projets\python_proj\loup-entretien-marianne.jpg")
    new_window.geometry("800x700")
    photo = ImageTk.PhotoImage(image)
    label = Label(new_window,image=photo)
    label.image =photo  
    label.pack()

  
    btn22 = Button(new_window, text="Reduce Noise", command=noise )
    btn22.pack()
    btn22 = Button(new_window, text="Close Me", command=lambda: new_window.destroy())
    btn22.pack()
#Reduce Noise button function
def noise():
    filename = r"G:\projets\python_proj\loup-entretien-marianne.jpg"
    img = cv2.imread(filename)
    result = cv2.fastNlMeansDenoisingColored(img,None,20,10,7,21)
    cv2.imshow("Denoised Image", result)
    cv2.waitKey(0) 

#Get image contour function
def gcWindow():
    new_window = Toplevel(window)
    new_window.resizable(FALSE, FALSE)
    image = Image.open(r"G:\projets\python_proj\loup-entretien-marianne.jpg")
    new_window.geometry("800x700")
    photo = ImageTk.PhotoImage(image)
    label = Label(new_window,image=photo)
    label.image =photo  
    label.pack()

  
    btn22 = Button(new_window, text="Get image contour", command=contour )
    btn22.pack()
    btn22 = Button(new_window, text="Close Me", command=lambda: new_window.destroy())
    btn22.pack()
#Get image contour button function
def contour():
    filename = r"G:\projets\python_proj\loup-entretien-marianne.jpg"
    img = cv2.imread(filename)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    retval, thresh = cv2.threshold(gray_img, 127, 255, 0)
    img_contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, img_contours, -1, (0, 255, 0))
    cv2.imshow('Image Contours', img)
    cv2.waitKey(0) 




window = Tk()
window.title("My Application")
window.geometry("600x400")
window.iconbitmap(r"G:\projets\python_proj\log.ico")
window.config(background='#41B77F')
label_title = Label(window, text="Welcome", font=("Courrier",40), bg='#41B77F', fg='white')
label_title.pack()
#task1#
b1=Button(window, text="Let's Begin", command=beginWindow)
b1.pack()

#boutonquitter
bQuitter = Button(window, text ='Close', command = window.destroy)
bQuitter.pack(padx = 20, pady = 20)

#############
label_footer = Label(window, text="CREATED BY HLAOUI GHASSEN", font=("Courrier",13), bg='#41B77F', fg='white')
label_footer.pack(padx = 20, pady = 110)
window.mainloop()