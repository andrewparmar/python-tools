import math

def palindormic_partitions(text):

    text_tokenize = list(text)

    l = 0
    r = len(text_tokenize) - 1

    partition_list = []

    for i in range(0, r):
        flag = True
        j = i - 1
        k = i + 1
        while flag:
            print(j, i, k)
            while text_tokenize[j] == text_tokenize[k]:
                flag = True
                if j == 0 or k == r+1:
                    flag=False
                    partition_list.append(''.join(text_tokenize[j+1: k]))
                else:
                    j -= 1
                    k += 1
            else:
                flag = False
                partition_list.append(''.join(text_tokenize[j+1: k]))
        # i += 1

    return partition_list

def is_palindrome(subtext):
    return subtext == subtext[::-1]

print(palindormic_partitions('ksjkjsnitinkjsdhf'))
