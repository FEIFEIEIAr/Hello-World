# HYJ
# TIME: 2021-5-30 13:10

from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import re
from PIL import Image
import numpy as np
text = open("./关键词1.txt",encoding='utf-8').read()
text = text.replace('\n',"").replace("\u3000",'').replace('"','')
text=re.split(r'\s*[;,]\s*', text)
text_cut = ';'.join(text)


background = Image.open("扇子.jpeg")
graph = np.array(background)

image_colors = ImageColorGenerator(graph)
word_cloud = WordCloud(font_path="simsun.ttc",  # 字体
                       background_color="white",
                       mask=graph, max_words=800)  # 背景颜色
word_cloud.generate(text_cut)
plt.subplots(figsize=(12, 8), dpi = 1000)
plt.imshow(word_cloud.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.savefig('关键词.png')
