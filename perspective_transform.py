import cv2
import numpy as np
import os
img = cv2.imread(r"E:\dataset\carla\Town05_Opt\Default\clips\normal\9\0001.jpg")
Y, X = img.shape[:2]
print(X, Y)
list_pst = []


def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    list_xy = []
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        list_xy.append(x)
        list_xy.append(y)
        print(list_xy)
        cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=-1)
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (255, 255, 0), thickness=1)
        cv2.imshow("original_img", img)
        list_pst.append(list_xy)
        if (len(list_pst) == 4):
            # 原图中书本的四个角点(左上、右上、左下、右下),与变换后矩阵位置
            pts1 = np.float32(list_pst)
            pts2 = np.float32([[X / 2 - 100, 0], [X / 2 + 100, 0], [X / 2 - 100, Y], [X / 2 + 100, Y]])

            # 生成透视变换矩阵；进行透视变换
            M = cv2.getPerspectiveTransform(pts1, pts2)
            print(M)
            dst = cv2.warpPerspective(img, M, (X, Y))

            cv2.imshow("result", dst)


# cv2.namedWindow("original_img")
# cv2.setMouseCallback("original_img", on_EVENT_LBUTTONDOWN)
# cv2.imshow("original_img", img)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# a = [[-2.46892079e-01, -3.02070942e+00, 1.04091514e+03],
#      [1.20729385e-15, -2.32992914e+00, 7.19948105e+02],
#      [-4.18708285e-07, -3.57428853e-03, 1.00000000e+00]]
img_paths=r'E:\dataset\carla\Town05_Opt\Default\clips\keep_left\0'
M = np.array([[-7.66999702e-01, -3.41318360e+00, 1.13166696e+03],
     [5.84161617e-15, -4.04335921e+00, 8.65278870e+02],
     [-3.80473646e-07, -5.33460665e-03, 1.00000000e+00]])
for i in os.listdir(img_paths):
    img_path=os.path.join(img_paths,i)
    img=cv2.imread(img_path)
    dst = cv2.warpPerspective(img, M, (X, Y))
    cv2.imshow("result"+i, dst)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
