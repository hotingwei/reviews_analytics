data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f: #line為一串留言
		data.append(line)
		count += 1
		if count % 1000 == 0: # %是和後面數字求餘數的意思
			print(len(data))

print('The file has all been read. There are', len(data), 'datas in total.')

sum_len = 0
for d in data: #d為一個字母
	sum_len = sum_len + len(d)
print('The average of the comments are', sum_len / len(data), 'words.')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('There are', len(new), 'comments that are shorter than 100 words in total.')
