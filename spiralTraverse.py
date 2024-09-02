c = int(input('Enter columns: '))
r = int(input('Enter rows: '))
matrix=[]
for i in range(r):
	a = []
	for j in range(1+(i*10),c+1+(i*10)):
		a.append(j)
	matrix.append(a)

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
print(ans)
