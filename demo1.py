import cv2

# 使用函数 cv2.imread() 读入图像。这幅图像应该在此程序的工作路径，
# 或者给函数提供完整路径，
# 第二个参数是要告诉函数应该如何读取这幅图片。
# • cv2.IMREAD_COLOR：读入一副彩色图像。图像的透明度会被忽略，这是默认参数。
# • cv2.IMREAD_GRAYSCALE：以灰度模式读入图像
# • cv2.IMREAD_UNCHANGED：读入一幅图像，并且包括图像的 alpha 通道


img = cv2.imread('20200214174846.jpg', 1)

#设置可以调整窗口的大小
#若参数是cv2.WINDOW_AUTOSIZE，则窗口大小是不可以调整的
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# 注意此处的图片名称不支持中文的
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 保存图像
cv2.imwrite('20200214174846.png', img)

