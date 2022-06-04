def pss(input,output):
    if len(input)==0:
        print(output,end=" ")
        return

    pss(input[1:],output+input[0])
    pss(input[1:],output)

output=""
input="abcd"
print(pss(input,output))