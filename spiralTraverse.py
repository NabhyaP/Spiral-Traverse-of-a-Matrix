matrix = [[1, 2, 3, 4],
		   [5, 6, 7, 8],
		   [9, 10, 11, 12],
		   [13, 14, 15,16]]
c=4
r=4

ans = []
x=c
y=r
while len(ans)<(r*c):
	#top
	for j in matrix[r-y][c-x:x-1]:
		if len(ans)==(r*c):
			break
		ans.append(j)
			
	#right
	for j in matrix[r-y:y]:
		if len(ans)==(r*c):
			break
		ans.append(j[x-1])
			
	#bottom
	for j in matrix[y-1][::-1][1+c-x:x]:
		if len(ans)==(r*c):
			break
		ans.append(j)
			
	#left
	for j in matrix[::-1][1+r-y:y-1]:
		if len(ans)==(r*c):
			break
		ans.append(j[c-x])
			
	x-=1
	y-=1
