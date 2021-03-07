# input: two strings str1 and str2
# returns: minimum number of edits (add/del/edit) required to convert str1 to str2

def levenshteinDistance(str1, str2):
	dist = [[j for j in range(len(str2)+1)] for i in range(len(str1)+1)]

	for i in range(1, len(str1)+1):
		dist[i][0] = dist[i-1][0]+1

	for r in range(1, len(str1)+1):
		for c in range(1, len(str2)+1):
			if(str1[r-1]==str2[c-1]):
				dist[r][c] = dist[r-1][c-1]
			else:
				dist[r][c] = 1+min(dist[r-1][c-1], 
									dist[r][c-1], 
									dist[r-1][c])
	return dist[-1][-1]


def main():
    solution = levenshteinDistance("abc", "yabd")
    print(solution)


if __name__=='__main__':
    main()
	
