from PIL import Image,ImageFont,ImageDraw
I = Image.open(r"E:\abc(图片)\未标题-1.png")
#i.show()
font = ImageFont.truetype(r"C:\WINDOWS\Fonts\SIMSUN.TTC",size=100)
draw = ImageDraw.Draw(I)
draw.text(xy = (900,900),text = "@Kazhi",fill="aqua",font=font)
I.show()