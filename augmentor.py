import cv2
import numpy as np
from imutils import paths
np.random.seed()

class Augmenter:
	def __init__(self, channel, scale=0.5, shapes=["rectangle","circle"], rate=0.7, stepSize=10, limit=0.3) -> None: 
		self.channel = channel 
		self.scale = scale
		self.shapes = shapes
		self.rate = rate 
		self.stepSize = stepSize
		self.limit = limit

	def convert_space(self, image : np.ndarray, channel : int) -> list:
		res = []
		if channel == 3:
			res.append(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
			res.append(cv2.cvtColor(cv2.cvtColor(image,cv2.COLOR_BGR2GRAY),cv2.COLOR_GRAY2BGR))
		return res

	def zoom(self, image : np.ndarray, scale : float, stepSize : int) -> list:
		res = []
		H, W = image.shape[:2]
		winH, winW = int(H*scale), int(W*scale)
		for y in range(0,H,stepSize):
			for x in range(0,W,stepSize):
				if x + winW >= W or y + winH >= H:
					continue
				res.append(cv2.resize(image[y:y+winH,x:x+winW],(W,H)))
		return res

	def mirror(self, image : np.ndarray) -> list:
		return [cv2.flip(image,i) for i in [0,1]]

	def lighting(self, image : np.ndarray, rate : int) -> list:
		amount = np.ones(image.shape,np.uint8) * int((100*rate))
		bright = cv2.add(image,amount)
		dark = cv2.subtract(image,amount)
		return [bright,dark]

	def draw(self, image : np.ndarray, shapes : list, channel : int) -> list:  
		res = []
		H,W = image.shape[:2]
		for shape in shapes:
			Wrate, Hrate = int(W*0.9), int(H*0.9)
			for _ in range(np.random.randint(5,15)):
				clone = image.copy()
				for _ in range(np.random.randint(5,15)):
					x, y = np.random.randint(W-Wrate,Wrate), np.random.randint(H-Hrate,Hrate)
					thickness = np.random.choice([-1,2,3,4])
					color = (np.random.randint(1,256),
					 np.random.randint(1,256),
					 np.random.randint(1,256)) if channel == 3 else np.random.randint(1,256)
					if shape == "circle":
						cv2.circle(clone,(x,y),int(np.mean(np.array([W*0.05,H*0.05]))),color,thickness)
					if shape == "rectangle":
						cv2.rectangle(clone,(x,y),(x+int(W*0.1),y+int(H*0.1)),color,thickness)
				res.append(clone)
		return res
	
	def blur(self, image : np.ndarray) -> list:
		return [cv2.GaussianBlur(image,(k,k),0) for k in range(3,12,2)]

	def erode(self, image : np.ndarray) -> list:
		return [cv2.erode(image,np.ones((k,k),np.uint8)) for k in range(3,8,2)]

	def dilate(self, image : np.ndarray) -> list:
		return [cv2.dilate(image,np.ones((k,k),np.uint8)) for k in range(3,8,2)]

	def addNoise(self, image : np.ndarray, channel : int) -> list:
		return [np.uint8(np.clip(image + np.random.randn(*image.shape)*i,0,255)) for i in range(10,51,10)]

	def colorize(self, image : np.ndarray, channel : int) -> list:
		res = []
		if channel == 3:
			for colormap in [1,3,5,6,7,10,11,12,13,14,15,16,17,18,19,21]:
				res.append(cv2.applyColorMap(image,colormap))
		return res

	def rotate(self, image : np.ndarray) -> list:
		res = []
		image_center = tuple(np.array(image.shape[:2][::-1]) / 2)
		for angle in np.arange(10,351,10):
			rotated = cv2.getRotationMatrix2D(image_center,angle, 1.0)
			res.append(cv2.warpAffine(image, rotated, image.shape[:2][::-1], flags=cv2.INTER_LINEAR))
		return res

	def transfer(self, image : np.array, limit : int) -> list:
		vol = limit * 100
		H, W = image.shape[:2]
		res = []
		pts = [np.float32([[1,0,vol],[0,1,vol]]),
				np.float32([[1,0,-vol],[0,1,vol]]),
				np.float32([[1,0,-vol],[0,1,-vol]]),
				np.float32([[1,0,vol],[0,1,-vol]]),
				np.float32([[1,0,0],[0,1,vol]]),
				np.float32([[1,0,vol],[0,1,0]]),
				np.float32([[1,0,-vol],[0,1,0]]),
				np.float32([[1,0,0],[0,1,-vol]])]
		for pt in pts:
			res.append(cv2.warpAffine(image,pt,(W,H)))
		return res

	def addContour(self,image : np.ndarray, channel : int) -> list:
		res = []
		clone = image.copy()
		if channel == 3:
			clone = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
		edges = cv2.Canny(clone,100,150)
		cnts,_ = cv2.findContours(edges,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
		for _ in range(np.random.randint(5,15)):
			color = (np.random.randint(1,256),np.random.randint(1,256),np.random.randint(1,256)) if channel == 3 else np.random.randint(1,256)
			clone = image.copy()
			res.append(cv2.drawContours(clone,cnts,-1,color,1))
		return res

	def split(self, image : np.ndarray, channel : int) -> list:
		res = []
		uniques = []
		if channel == 3:
			b, g, r = cv2.split(image)
			channels = {0:b,1:g,2:r}
			for i in range(3):
				for j in range(3):
					for k in range(3):
						if (i == 0 and j == 1 and k == 2) or i==j==k:
							continue
						merged = cv2.merge([channels[i],channels[j],channels[k]])
						res.append(merged)
			return res
		return res 

	def validate(self, X : list, y : list) -> None:
		im_shape = np.array(X).shape
		assert self.channel in [3,1] and im_shape[-1] in [3,1], "Wrong channel number, Number of the channel of images or given channel must be wether 3 or 1"
		assert im_shape[-1] == self.channel, f"Channel number is not the same as image channel,\nGiven channel : {self.channel}\nExpected : {im_shape[-1]}"
		assert self.scale >= 0.1 and self.scale <= 0.9, "Scale argument must be between 0.1 <= X <= 0.9"
		assert len(self.shapes) in range(1,3) and supported_shapes(self.shapes), "Only two shapes are supported, rectangle and circle"
		assert self.rate >= 0.1 and self.rate <= 0.9, "Rate argument must be between 0.1 <= X <= 0.9"
		assert self.limit >= 0.1 and self.limit <= 0.9, "Limit argument must be between 0.1 <= X <= 0.9"

	def generate(self, X : list, y : list):
		self.validate(X, y)
		H,W,_ = np.array(X).shape[1:]
		new_x, new_y = [], []
		for x,Y in zip(X,y):
			yield x
			yield Y
			spaces = self.convert_space(x, self.channel)
			zoomed = self.zoom(x, self.scale, self.stepSize)
			mirrored = self.mirror(x)
			light = self.lighting(x, self.rate)
			blurred = self.blur(x)
			erode = self.erode(x)
			dilate = self.dilate(x)
			noisy = self.addNoise(x, self.channel)
			shaped = self.draw(x, self.shapes, self.channel)
			colorized = self.colorize(x, self.channel)
			rotated = self.rotate(x)
			shifted = self.transfer(x, self.limit)
			contour = self.addContour(x, self.channel)
			splited = self.split(x, self.channel)
			for change in [splited,contour,shifted,spaces,mirrored,rotated,colorized,shaped,noisy,erode,dilate,zoomed,light,blurred]:
				for c in change:
					if self.channel == 1:
						c = c.reshape(H,W,1) 
					yield c
					yield y 

	def decode(self, data) -> tuple:
		data = list(data)
		return data[0:len(data):2], data[1:len(data):2]

def supported_shapes(shapes) -> bool :
	for shape in shapes: 
		if shape not in ["rectangle","circle"]: return False
	return True

