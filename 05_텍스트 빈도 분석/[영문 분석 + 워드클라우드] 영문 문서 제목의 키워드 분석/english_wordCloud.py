# -*-coding: euc-kr -*-
import pandas as pd
import matplotlib.pyplot as plt
import glob
import re
import nltk

from functools import reduce
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
from wordcloud import STOPWORDS, WordCloud

# 데이터 조합 - 파일 병합하기
all_files = glob.glob('excel_data/myCabinetExcelData*.xls')

all_files_data = []
for file in all_files:
	data_frame = pd.read_excel(file)
	all_files_data.append(data_frame)

# print(all_files_data[0])

all_files_data_concat = pd.concat(all_files_data, axis = 0, ignore_index = True)
# print(all_files_data_concat)

# all_files_data_concat.to_csv("./riss_bigdata.csv", encoding = "utf-8", index = False)

all_title = all_files_data_concat['제목']
# print(all_title)

stopWords = set(stopwords.words("english"))
lemma = WordNetLemmatizer()

words = []

for title in all_title:
	EnWords = re.sub("r[^a-zA-z]+", " ", str(title))
	EnWordsToken = word_tokenize(EnWords.lower())
	EnWordsTokenStop = [w for w in EnWordsToken if w not in stopWords]
	EnWordsTokenStopLemma = [lemma.lemmatize(w) for w in EnWordsTokenStop]
	words.append(EnWordsTokenStopLemma)

# print(words)

words2 = list(reduce(lambda x, y: x+y, words))
#print(words2)

Count = Counter(words2)
# print(Count)

word_count = dict()

for tag, counts in Count.most_common(50):
	if (len(str(tag)) > 1):
		word_count[tag] = counts
		# print("%s : %d" %(tag, counts))

# del word_count['big']
# del word_count['data'] 

sorted_Keys = sorted(word_count, key= word_count.get, reverse = True)
sorted_Values = sorted(word_count.values(), reverse = True)
plt.bar(range(len(word_count)), sorted_Values, align = 'center')
plt.xticks(range(len(word_count)), list(sorted_Keys), rotation = '85')
# plt.show()

all_files_data_concat['doc_count'] = 0
summary_year = all_files_data_concat.groupby('출판일', as_index = False)['doc_count'].count()
# print(summary_year)

plt.figure(figsize = (12,5))
plt.xlabel("year")
plt.ylabel("doc-count")
plt.grid(True)
plt.plot(range(len(summary_year)), summary_year['doc_count'])
plt.xticks(range(len(summary_year)), [text for text in summary_year['출판일']])

stopwords = set(STOPWORDS)
wc = WordCloud(background_color = 'ivory', stopwords = stopwords, width = 800, height = 600)
cloud = wc.generate_from_frequencies(word_count)
plt.figure(figsize = (8,8))
plt.imshow(cloud)
plt.axis('off')
plt.show()