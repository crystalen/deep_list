from PIL import Image, ImageEnhance
from docopt import docopt

def rgb(red,green,blue):
    return 16+(red*36)+(green*6)+blue

ASCII= "Q0RMNWBDHK@$U8&AOkYbZGPXgE4dVhgSqm6pF523yfwCJ#TnuLjz7oeat1[]!?I}*{srlcxvi)><\\)|\"/+=^;,:'_-`. "

im=Image.open('/Users/luyujin/文档/python/爬虫＋基础/map.jpg')
im=im.convert('RGBA')
width=int(im.width/6)
height=int(im.height/15)
im=im.resize((width,height),Image.NEAREST)
enhancer=ImageEnhance.Contrast(im)
im=enhancer.enhance(1.5)
img=im.getdata()
im=im.convert('L')
bg=rgb(0,0,0)
fg=rgb(5,5,5,)
bold=False  #True加粗


def set_style(fg=None,bg=None):
    end=''
    print(_set_style(fg,bg),end='')

def _set_style(fg=None,bg=None):
    result=''
    if fg:
        result += '\x1b[38;5;%dm' % fg
    if bg:
        result += '\x1b[48;5;%dm' % bg    
    return result


def print_color(*args,**kwargs):
    fg=kwargs.pop('fg',None)
    bg=kwargs.pop('bg',None)
    set_style(fg,bg)
    print(*args,end='')
    
row_len=0
for (count,i) in enumerate(im.getdata()):
    ascii_char=ASCII[int((i/255.0)*(len(ASCII)-1))]
    color=rgb(int((img[count][0]/255.0)*5),int((img[count][1]/255.0)*5),int((img[count][2]/255.0)*5))
    fg=color
    bg=rgb(0,0,0)
    print_color(ascii_char,fg=fg,bg=bg,end='')
    row_len += 1
    if row_len==width:
        row_len=0
        print('')