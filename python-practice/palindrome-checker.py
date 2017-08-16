import sys

text = sys.argv[1]

stack = list(text)

stack.reverse()

# print(stackR)
stackR = "".join(stack)
print(stackR)

print(text == stackR)