N,M = map(int, input().split())
lines_len = list(map(int, input().split()))

for _ in range(M):
	i_min = 0
	for i in range(N):
		if lines_len[i]<lines_len[i_min]:
			i_min = i
	print(lines_len[i_min])
	lines_len[i_min] +=1


""" 
input:
5 3
2 2 3 3 3
output:
2
2
3
3
3
"""