def list_creator(s_list):
	a = ""

	for s in s_list:
		b = "<li> {} </li>\n".format(s)
		a = a + b

	c = "<ul>{}</ul>".format(a)

	print(c)

my_list = ['ant','bat','cat']

list_creator(my_list)