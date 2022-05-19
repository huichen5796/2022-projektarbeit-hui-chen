'''
- markieren linien durch HoughLinesP
- get location of table --- not done
# https://wenku.baidu.com/view/8bdffcf175a20029bd64783e0912a21614797fd3.html

'''
import cv2
import numpy as np
from get_linien import GetTable


def LineMark(bina_image):
    ### Line makieren durch HoughLines()
    edges = cv2.Canny(bina_image, 50, 250, apertureSize= 7) ## apertureSize is the size of kernel, also soble

    lines = cv2.HoughLinesP(edges, 1.0, np.pi/180, 50, minLineLength=20, maxLineGap=10) 

    ### show the line
    color_img = cv2.merge((bina_image, bina_image, bina_image))

    for line in lines:
        x1, y1, x2, y2 = line[0]

        img_line = cv2.line(color_img, (x1,y1), (x2, y2), (0, 0, 255), 2)
    

    cv2.imshow("output", img_line)
    cv2.waitKey()

    return lines



def Main():
    bina_image = GetTable(r'Development\imageTest\einfach_table.jpg')  # einfache Tabelle
    # bina_image = GetTable(r'Development\imageTest\rotate_table.png')  # komplexe Tabelle
    LineMark(bina_image)
    
if __name__ == '__main__':
    Main()