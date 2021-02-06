import cv2 as cv

img = cv.imread("assets/images/education-page/deep_learning_ai.jpg")

img2=cv.imread("assets/images/education-page/coursera1.png")

dimensions = ( img2.shape[1],img2.shape[0] )

img_rescale = cv.resize(img,dimensions,interpolation=cv.INTER_AREA)

cv.imwrite("assets/images/education-page/GreyLogoName360x3602.png",img_rescale)