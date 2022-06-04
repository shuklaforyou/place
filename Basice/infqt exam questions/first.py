

test_str = str(input()).upper()



# print("The original string is : " + str(test_str))

res = ''.join(format(ord(i), '08b') for i in test_str)
tep=res
# printing result
# print("The string after binary conversion : " + str(res))

# split_strings = []
# n  = 4
# for index in range(0, len(a_string), n):
#     split_strings.append(a_string[index : index + n])

# print(split_strings)
inverse_s=''
for i in tep:
    
    if i == '0':
        inverse_s += '1'
          
    else:
        inverse_s += '0'

# print(inverse_s)

test_string = inverse_s

split_strings = []
n  = 4
for index in range(0, len(test_string), n):
    split_strings.append(test_string[index : index + n])

# print(split_strings)
# final=''
# for i in range(0,len(split_strings)):
#     final +=split_strings[i]

# print(final)
# Python3 code to demonstrate working of
# Converting binary to string
# Using BinarytoDecimal(binary)+chr()


# Defining BinarytoDecimal() function
def binToHexa(n):
    
    # convert binary to int
    num = int(n, 2)
      
    # convert int to hexadecimal
    hex_num = format(num, 'x')
    return(hex_num)
  
# Driver code
strop=''
for i in range(0,len(split_strings)):
    wel=split_strings[i]
    strop +=binToHexa(wel)
    

print(strop.upper())   

