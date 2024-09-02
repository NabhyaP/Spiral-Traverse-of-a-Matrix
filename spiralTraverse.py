matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]]
c=10
r=10

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
