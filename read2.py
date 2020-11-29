data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f: #line為一筆留言
		data.append(line)
		count += 1
		if count % 1000 == 0: # %是和後面數字求餘數的意思
			print(len(data))

print('The file has all been read. There are', len(data), 'datas in total.')

sum_len = 0
for d in data: #d為一個字母 #意思是每一筆留言的字數
	sum_len = sum_len + len(d)
print('The average of the comments are', sum_len / len(data), 'words.')

new = []
for d in data: #data清單裡面有很多筆留言
	if len(d) < 100: #每一筆留言的字數小於100
		new.append(d)
print('There are', len(new), 'comments that are shorter than 100 words in total.')

good = []
for d in data: #每一筆留言的內容字母中
	if 'good' in d: #有包含good 因連在一起所以可以當作搜尋一個單字
		good.append(d)
print('There are', len(good), 'comments that include the word "good".')

#words counting

wc = {} # word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增新的key進wc字典

for word in wc:
	if wc[word] > 50000 :
		print(word, wc[word])

print(len(wc))

while True:
	word = input('Which word do you want to look for:')
	if word == 'q':
		break
	if word in wc:
		print(word, 'appears', wc[word], 'times')
	else:
		print('The word has not appeared before.')

print('Thanks for using our searching engine.')










