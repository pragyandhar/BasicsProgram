# str1 = input("====>")
# ch = input("Enter a character = ")
# count = 0
# for i in str1:
#     if i == ch:
#         count += 1

# print(count)

#METHOD-1
str1 = input("==>>")
reg = ""
for x in str1:
    count = 0
    if x not in reg:
        for a in str1:
            if a == x:
                count += 1
        print(x,":",count)
        reg += x

# call = counting()
# print(call)

#METHOD-2
st = input("==>>")
ch = input("::")
register = ""
for i in st:
    if ch not in register:
        count = st.count(ch)
        print(f"{ch},{count}")
    register = register+1
