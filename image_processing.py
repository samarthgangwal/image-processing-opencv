from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog

#selectfile
def select():
    root = Tk()
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*"), ("png files", "*.png")))
    print(root.filename)

    if selected.get() == 1:

        #Cartoonify
        import cv2
        import numpy as np

        img = cv2.imread(root.filename)

        # Edges of the picture
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

        # Change in colour
        color = cv2.bilateralFilter(img, 9, 300, 300)

        # Cartoon effect
        cartoon = cv2.bitwise_and(color, color, mask=edges)

        cv2.imshow("Cartoon", cartoon)
        cv2.imwrite("C://Users//samar//Desktop//Project Image//cartoon.jpeg", cartoon)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif selected.get() == 2:
        #Black&White
        import cv2

        image = cv2.imread(root.filename)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        cv2.imshow('Black & White', gray)
        cv2.imwrite("C://Users//samar//Desktop//Project Image//black&white.jpeg", gray)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif selected.get() == 4:
        # Pixelated

        from PIL import Image


        img = Image.open(root.filename)

        # Resize smoothly down to 256x256 pixels
        imgSmall = img.resize((256, 256), resample=Image.BILINEAR)

        # Scale back up using NEAREST to original size
        result = imgSmall.resize(img.size, Image.NEAREST)

        result.show('result.png')

        # Save
        result.save("C://Users//samar//Desktop//Project Image//pixelated.jpeg")

    elif selected.get() == 3:
        #Pencil Sketch
        import cv2
        import numpy as np

        img_rgb = cv2.imread(root.filename)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        img_gray_inv = 255 - img_gray
        img_blur = cv2.GaussianBlur(img_gray_inv, ksize=(21, 21), sigmaX=0, sigmaY=0)

        def dodgeNaive(image, mask):
            # determine the shape of the input image
            width, height = image.shape[:2]

            # prepare output argument with same size as image
            blend = np.zeros((width, height), np.uint8)

            for col in range(width):
                for row in range(height):
                    # do for every pixel
                    if mask[c, r] == 255:
                        # avoid division by zero
                        blend[c, r] = 255
                    else:
                        # shift image pixel value by 8 bits
                        # divide by the inverse of the mask
                        tmp = (image[c, r] << 8) / (255 - mask)

                        # make sure resulting value stays within bounds
                        if tmp > 255:
                            tmp = 255
                            blend[c, r] = tmp

            return blend

        def dodgeV2(image, mask):
            return cv2.divide(image, 255 - mask, scale=256)

        def burnV2(image, mask):
            return cv2.divide(255 - image, 255 - mask, scale=256)

        img_blend = dodgeV2(img_gray, img_blur)
        cv2.imshow("pencil sketch", img_blend)
        cv2.imwrite("C://Users//samar//Desktop//Project Image//pencil_sketch.jpeg", img_blend)

    elif selected.get() == 5:
        #Enhanced Detail

        # import image module

        from PIL import Image

        from PIL import ImageFilter

        # Open an already existing image

        imageObject = Image.open(root.filename)

        # Apply edge enhancement filter

        edgeEnahnced = imageObject.filter(ImageFilter.EDGE_ENHANCE)

        # Apply increased edge enhancement filter

        moreEdgeEnahnced = imageObject.filter(ImageFilter.EDGE_ENHANCE_MORE)

        # Show image - after applying edge enhancement filter

        edgeEnahnced.show()
        edgeEnahnced.save("C://Users//samar//Desktop//Project Image//enhanced_detail.jpeg")
    else:
        messagebox.showinfo('Notice', 'Please select an image')
#tkinter
window = Tk()

window.title("Welcome!")

lbl = Label(window, text="Welcome! Choose the options given below and change your image!", font=("Times New Roman", 12))

lbl.grid(column=0, row=0)

#Radiobuttons

selected = IntVar()

rad1 = Radiobutton(window, text='Cartoonify', value=1, variable=selected)

rad2 = Radiobutton(window, text='Black&White', value=2, variable=selected)

rad3 = Radiobutton(window, text='Pencil Sketch', value=3, variable=selected)

rad4 = Radiobutton(window, text='Pixelated', value=4, variable=selected)

rad5 = Radiobutton(window, text='Enhanced Sharpness', value=5, variable=selected)


def clicked():

    print(selected.get())
    if selected.get() == 1:
        return

rad1.grid(column=0, row=1, sticky=W)

rad2.grid(column=0, row=2, sticky=W)

rad3.grid(column=0, row=3, sticky=W)

rad4.grid(column=0, row=4, sticky=W)

rad5.grid(column=0, row=5, sticky=W)

#button2
btn2 = Button(window, text="Select File & Convert", command=select)

btn2.grid(column=0, row=6, sticky=W)


window.geometry("420x300")
window.mainloop()

