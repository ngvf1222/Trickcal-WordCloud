import requests
import pickle
from bs4 import BeautifulSoup
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
p='/b/trickcal?p=1'
texts=''
icon=Image.open('maxresdefault.png')
mask = Image.new("RGB", icon.size, (255,255,255))
mask.paste(icon,icon)
mask = np.array(mask)
image_colors = ImageColorGenerator(mask)
try:
    while True:
        print(p)
        url=f"https://arca.live{p}"
        html=requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        texts+=' '.join(map(lambda x: x.get_text().strip(),soup.select('span.title')))+' '
        p=list(soup.select('li.active')[0].next_siblings)[1].a['href']
except (Exception,KeyboardInterrupt) as e:
    print(e)
    f=open('result.txt','w',encoding='utf-8')
    f.write(texts)
    f.close()
