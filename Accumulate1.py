def accumulate(n=100):
    one = 0 #局部变量
    for i in range(1,n+1):
        one = i + one
        
    print(f"由1到{n}的和为{one}")    
accumulate(10)

def accumulate1(n):
   two = 0
   if n > 10:
        for i in range(1,n+1):
            two = two+i
        return (f"由1到{n}的和为{two}")      
   else:
        return ('请输入大于10的数')
print(accumulate1(11)) #return 返回相当于变量，输出需要print

def encourage(name): #名字需要字符串类型
    word = name + "!" + " " + "Don't let laziness limit the person you're meant to be"
    return word
print(encourage("Mr.Ming"))