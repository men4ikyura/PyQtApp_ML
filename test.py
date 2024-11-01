
from PIL import Image, ImageDraw #Подключим необходимые библиотеки. 

def modificated_image(file_path):
	mode = 2
	image = Image.open(file_path) #Открываем изображение. 
	draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 
	width = image.size[0] #Определяем ширину. 
	height = image.size[1] #Определяем высоту. 	
	pix = image.load() 

	if (mode == 2):
		for i in range(width):
			for j in range(height):
				a = pix[i, j][0]
				b = pix[i, j][1]
				c = pix[i, j][2]
				draw.point((i, j), (255 - a, 255 - b, 255 - c))
				
	image.save("drop1_1.jpg", "JPEG")
	del draw