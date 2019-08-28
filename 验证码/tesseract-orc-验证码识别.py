

import  pytesseract
from PIL import  Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
#=====================
#打开图片
img=Image.open(r'C:\pythonWorkspace\test_python\验证码\3cmd.png')
#-------灰色处理-----------------
img=img.convert('L')
#处理前弹出画板查看图片
# img.show()

#灰色处理（二值化处理）
threshold=140
table=[]
for i in range(256):
    if i<threshold:
        table.append(0)
    else:
        table.append(1)
out=img.point(table,'1')
#处理后弹出画板查看图片
# out.show()

# img=img.convert('RGB')
#-----输出---------------------
#这一步识别就要安装pytesseract-orc.exe
code=pytesseract.image_to_string(img)
print('code=',code)
#=====================




