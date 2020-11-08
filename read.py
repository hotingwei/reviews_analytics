data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # %是和後面數字求餘數的意思
			print(len(data))

print('The file has all been read. There are', len(data), 'datas in total.')

sum_len = 0
for d in data: #d 為字串
	sum_len = sum_len + len(d)
print('The average of the comments is', sum_len / len(data))