import cv2
import numpy as np

img =  cv2.imread('assets/ball.jpg', 0) 
template = cv2.imread('assets/ball_crop.jpg', 0)

h,w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]


for method in methods : 
    img2 = img.copy()
    result = cv2.matchTemplate(img2,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0] + w , top_left[1]+h )

    cv2.rectangle(img2 , top_left , bottom_right , 255 , 2)

    cv2.imshow('match' ,img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()