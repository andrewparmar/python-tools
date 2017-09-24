import re

def myAtoi(str):
	
	raw_strig = str
	new_string = re.sub("^\s*", "", raw_strig)

	if not len(new_string):
		return 0
	elif new_string[0] == "-":
		if len(new_string) == 1:
			return 0
		multiplier = -1
		new_string = new_string[1:]
	elif new_string[0] == "+":
		if len(new_string) == 1:
			return 0
		multiplier = 1
		new_string = new_string[1:]
	else:
		multiplier = 1

	# print("New String: {}".format(new_string))
	
	integer_string = re.match(r"^[0-9]*", new_string)
	# print("Integer String: {}".format(integer_string))

	if integer_string.group() == "":
		return 0
	else:
		new_string = integer_string.group(0)
		# print new_string
		atoi = int(new_string) * multiplier

		if atoi >= 2147483648:
			atoi = 2147483647
		elif atoi < -2147483648:
			atoi = -2147483648

		return atoi


print(myAtoi("-2147483648"))
# print(myAtoi("     -23423423aljsd"))