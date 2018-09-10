def format_name(s):
    s1=s[0:1].upper()+s[1:].lower()
    return s1
print(list(map(format_name, ['adam', 'LISA', 'barT'])))



"""
或者使用自带的方法
"""

str = "one,two,three,four,file"

print("方法1:",str.title())

list_str = str.split(",")

list_st = []
for i in list_str:
    list_st.append(i.capitalize())

a = ",".join(list_st)
print("方法2:",a)