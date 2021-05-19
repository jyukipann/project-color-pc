import cv2
#コールバック関数
#マウスイベントが起こるとここへ来る
def printCoor(event,x,y,flags,param):
	if event == cv2.EVENT_LBUTTONDOWN:
		print(x, y)
img = cv2.imread('gazou.bmp')
#画像のウインドウに名前をつけ、コールバック関数をセット
cv2.namedWindow('image')
cv2.setMouseCallback('image',printCoor)
cv2.moveWindow('image', 100, 200)
while(1):
	cv2.imshow('image',img)
	#ESCキーでブレーク
	if cv2.waitKey(20) & 0xFF == 27:
		break
cv2.destroyAllWindows()