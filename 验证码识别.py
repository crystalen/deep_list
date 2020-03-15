from PIL import Image
import re,string,requests,base64
import pytesseract

def ocr_with_baidu(img):
    with open(img,'rb')as f_in:
        img_base64=base64.b64encode(f_in.read())
    url='https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=24.43292447aa78aad672c3e1a078f63506.2592000.1586779554.282335-18838855'
    headers={'Content-Type':'application/x-www-form-urlencoded'}
    data={'image':img_base64,
          'language_type':'CHN_ENG'}
    r=requests.post(url,headers=headers,data=data)
    print(r.text)


def check_valid(text):
    def extract_code(text):
        text=text.lower()
        valid=string.digits+string.ascii_lowercase
        for c in text:
            if not c in valid:
                text=text.replace(c,'')
        return text

    pattern='^[0-9a-z]{4}$'
    reg=re.compile(pattern)
    
    code=extract_code(text)
    is_valid=reg.match(code)

    if is_valid:
        return code
    else:
        return None

def ocr(img):
    im=Image.open(img)
    im=im.convert('L')
    text=pytesseract.image_to_string(im)
    return check_valid(text)

img='/Users/luyujin/Downloads/xian.jpg'
ocr_with_baidu(img)