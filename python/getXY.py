import cv2
#コールバック関数
#マウスイベントが起こるとここへ来る
def printCoor(event,x,y,flags,param):
	if event == cv2.EVENT_LBUTTONDOWN:
		print(x, y)
img = cv2.imread('1597739520_490239122.jpg')
#画像のウインドウに名前をつけ、コールバック関数をセット
cv2.imshow('image',img)
cv2.setMouseCallback('image',printCoor)
cv2.waitKey(0)
cv2.destroyAllWindows()