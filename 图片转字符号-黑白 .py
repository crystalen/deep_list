from PIL import Image
from PIL import ImageFont,ImageDraw

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r,g,b,alpha=256):
    if alpha==0:
        return ''
    length=len(ascii_char)
    gray=int(0.2126*r+0.7152*g+0.0722*b)
    unit=(256.0+1)/length
    return ascii_char[int(gray/unit)]

if __name__ == "__main__":
    img='/Users/luyujin/文档/python/爬虫＋基础/wechat.jpg'
    im=Image.open(img)
    width=int(im.width/6)
    height=int(im.height/15)
    im=im.resize((width,height),Image.NEAREST)
    txt=''
    for i in range(height):
        for j in range(width):
            txt +=get_char(*im.getpixel((j,i)))
        txt =txt+'\n'
    print(txt)
    