#电信231-徐梓轩-231404160124-x13339156780
def solution(lst1,lst2):
    length1=len(lst1)
    length2=len(lst2)
    if(length1!=length2):
        return 'false'
    else:
        for i in range(length1):
            if(lst1[i]!=lst2[i]):
                return 'false'
            else:
                a=1
                continue
        if(a==1):
            return 'true'
str1=input('请输入第一个根节点：')
str2=input('请输入第二个根节点：')
str1= str1.replace('[', '').replace(']', '')
str1 =str1[2:]
lst1=str1.split(',')
str2= str2.replace('[', '').replace(']', '')
str2 =str2[2:]
lst2=str2.split(',')
print(solution(lst1,lst2))