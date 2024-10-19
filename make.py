from wordcloud import WordCloud,ImageColorGenerator
from PIL import Image
import numpy as np
f=open('result.txt',encoding='utf-8')
texts=f.read()
f.close()
icon=Image.open('maxresdefault.png')
icon=icon.resize((1280,720))#TODO: 이거 크기 적정량 찾아야함 
mask = Image.new("RGB", icon.size, (255,255,255))
mask.paste(icon,icon)
mask = np.array(mask)
image_colors = ImageColorGenerator(mask)
wordcloud = WordCloud(
        font_path='C:/USERS/MOON/APPDATA/LOCAL/MICROSOFT/WINDOWS/FONTS/ONE MOBILE POP.TTF',
        width=10000, height=10000,
        mask=mask,
        max_words=texts.count(' ')+1
        ).generate(texts[:-1])
wordcloud.recolor(color_func=image_colors).to_file('word.png')
