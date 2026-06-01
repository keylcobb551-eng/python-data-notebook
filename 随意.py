import random
from datetime import datetime
a = random.choice(['正','反'])
#print(a)
b = random.randint(0,1)
#if b == 0:
#    print('正')
#else:
#    print('反')


list = ['大安','留连','速喜','赤口','小吉','空亡']
time_dict = {'子':1,'丑':2,'寅':3,'卯':4,'辰':5,'巳':6,'午':7,'未':8,'申':9,'酉':10,'戌':11,'亥':12}
hour1 = datetime.now().hour
def time_transfer(hour):
    if hour >=1 and hour <3:
        return '丑'#这可以简略 
    elif hour >=3 and hour < 5:
        return '寅'
    elif hour >=5 and hour < 7:
        return '卯'
    elif hour >=7 and hour < 9:
        return '辰'
    elif hour >=9 and hour < 11:
        return '巳'
    elif hour >=11 and hour < 13:
        return '午'
    elif hour >=13 and hour < 15:
        return '未'
    elif hour >=15 and hour < 17:
        return '申'
    elif hour >=17 and hour < 19:
        return '酉'
    elif hour >=19 and hour < 21:
        return '戌'
    elif hour >=21 and hour < 23:
        return '亥'
    else:
        return '子'
three = time_dict[time_transfer(hour1)]#hour1输入的是当前时间点   
def xiaoliuren(month,day,shichen=three):
    A = (month - 1)%6
    B = (month + day -1 -1 )%6#因为第一轮后，开始要以第一轮的点为起点所以多减1
    C = (month + day + shichen -1-1-1)%6
    return list[A],list[B],list[C]
    #print(list[A])
    #print(list[B])
    #print(list[C])
#分别代表前中后三个阶段
#xiaoliuren(11,11,11)
list_2 = ['大安','留连','速喜','赤口','小吉','空亡','病符','桃花','天德']
def xiaojiuren(month,day,shichen=three):
    A = (month - 1)%9
    B = (month + day -1-1)%9
    C = (month + day + shichen -1-1-1)%9
    return list_2[A],list_2[B],list_2[C]
    #print(list_2[A])
    #print(list_2[B])
    #print(list_2[C])
#xiaojiuren(11,11,11)

print("====切勿当真====")
yue = int(input("输入农历月份(1-12):"))
ri = int(input("输入农历日子(1-30):"))
shi = int(input("输入时间的几时(0-24)最好不要挑整点来:"))
shichen = time_dict[time_transfer(shi)]
kai = xiaojiuren(yue,ri,shichen)
zhi = xiaoliuren(yue,ri,shichen)
print(f"小六壬的结果是{kai},阉割版为{zhi}")
print("===闹着玩,一切灵感内容均来自网络===")
 

