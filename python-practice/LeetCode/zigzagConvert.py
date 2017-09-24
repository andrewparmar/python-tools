# def convert(s, numRows):
#         """
#         :type s: str
#         :type numRows: int
#         :rtype: str
#         """
        
#         target = numRows
#         going_up = True
#         going_down = False
#         direction = going_up
        
#         dic = {}
        
#         row = 0
#         index = 0
        
#         if numRows == 1 or numRows > len(s)
#             return s

#         while index < len(s):
            
#             if row < target and direction == going_up:
#                 dic.setdefault(row, []).append(s[index])
#                 # print(s[index], row, direction)
#                 row += 1
#                 index += 1
                
#             elif row == target and direction == going_up:
#                 target = -1
#                 direction = going_down
#                 row -= 2

#             elif row > target and direction == going_down:
#                 dic.setdefault(row, []).append(s[index])
#                 # print(s[index], row, direction)
#                 row -= 1
#                 index += 1
                
#             elif row == target and direction == going_down:
#                 target = numRows
#                 direction = going_up
#                 row += 2
            
#         converted_string = ""
#         for key in dic:
#             converted_string += "".join(dic[key])
                
#         # print dic
        
#         return converted_string

# print(convert("AB", 1))

def convert(s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        dic = {}
        
        row, step = 0, 1
        
        if numRows == 1 or numRows > len(s):
            return s

        for x in s:
    
            dic.setdefault(row,[]).append(x)
            if row == numRows - 1:
                step = -1
            if row == 0:
                step = 1
            row += step
            
        converted_string = ""
        for key in dic:
            converted_string += "".join(dic[key])
                
        return converted_string

print(convert("PAYPALISHIRING", 3))
