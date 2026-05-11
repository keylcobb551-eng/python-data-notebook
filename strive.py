class A():
    reply = "one by one,persevering"
    def day(self):
        print(f"今天天气很好,please {self.reply}")#T会传入self
T = A() #实例化
T.day()
print(T.reply)
Q = []
Q.append(T.reply)        
print(Q)
print(len(Q))