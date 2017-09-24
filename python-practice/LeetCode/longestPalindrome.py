def longestPalindrome(string):
	start, end = 0, 0

	longest_subtring = ""
	for i,ch in enumerate(string):
		
		len1 = centerExpansion(string, i, i)
		len2 = centerExpansion(string, i, i+1)

		len_final = max(len1, len2)
		if len_final > end - start:
			start = i - (len_final)/2
			end = i + (len_final)/2

	return string[start:end+1]


def centerExpansion(s, left, right):

	while(left >= 0 and right < len(s) and s[left] == s[right]):
		left -= 1
		right += 1

	length = right - left - 1

	return length
	
test = "aksjkdfjkasjdkjjllkskdjowwd"

print(longestPalindrome(test))





