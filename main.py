import os
from time import sleep

import jieba
import collections
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from you_get_script import get_video_danmaku
from matchXML import _getfiles
import argparse

parser = argparse.ArgumentParser(description="analysing what is discussed when watching this video")
group = parser.add_mutually_exclusive_group()
group.add_argument("-bgc",help="background color of the word cloud",default="white",type=str)
group.add_argument("-weight",help="width of word cloud",default=900,type=int)
group.add_argument("-height",help="height of the word cloud",default=600,type=int)
group.add_argument('-max_font',help="max font size",default=99,type=int)
group.add_argument('-max_word',help="max word in word cloud",default=200,type=int)
group.add_argument('-min_font',help="min font size",default=16,type=int)
group.add_argument('-color_state',help="random color state",default=50,type=int)
group.add_argument("-save_path",help="save generated image to path",default="./word_cloud.png")
parser.add_argument("url", help="url of the bilibili video")
args = parser.parse_args()

#get danmuku file
get_video_danmaku(args.url)
while(1):
    filename = _getfiles(".")
    if(filename):
        break
    sleep(0.5)
data = ""
with open(filename,encoding="UTF-8") as f:
    data += f.readline()


result = re.findall("\">.*?</d>",data)
new_data = ""
for i in result:
    #print(i)
    i = i[2:-4]
    #print(i)
    new_data += i
#print(new_data)
# 文本分词
seg_list_exact = jieba.cut(new_data, cut_all=True)

result_list = []
with open('stop_words.txt', encoding='utf-8') as f:
    con = f.readlines()
    stop_words = set()
    for i in con:
        i = i.replace("\n", "")   # 去掉读取每一行数据的\n
        stop_words.add(i)

for word in seg_list_exact:
    # 设置停用词并去除单个词
    if word not in stop_words and len(word) > 1:
        result_list.append(word)
#print(result_list)

# 筛选后统计
word_counts = collections.Counter(result_list)
# 获取词频靠前的词
word_counts_top = word_counts.most_common(200)
#print(word_counts_top)

# 绘制词云
my_cloud = WordCloud(
    background_color=args.bgc,  # 设置背景颜色  默认是black
    width=args.weight, height=args.height,
    max_words=args.max_word,            # 词云显示的最大词语数量
    font_path='simhei.ttf',   # 设置字体  显示中文
    max_font_size=args.max_font,         # 设置字体最大值
    min_font_size=args.min_font,         # 设置子图最小值
    random_state=args.color_state           # 设置随机生成状态，即多少种配色方案
).generate_from_frequencies(word_counts)

# 显示生成的词云图片
plt.imshow(my_cloud, interpolation='bilinear')
# 显示设置词云图中无坐标轴
plt.axis('off')
plt.savefig(args.save_path)
os.remove(filename)