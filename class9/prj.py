def say_hello():
    print("Hello!")
#定義一個簡單的函式
#定義一個可以接收參數的函式
def run_with_announce(func):
    print("😊😊準備執行...")
    func()
    print("😊😊執行完成！")

print("直接呼叫:")
say_hello()

print()
print("透過 run_with_announce 呼叫:")
run_with_announce(say_hello)

print("-------------------------")


#==================================
#第2段:包裝函式(裝飾詞原理)
#==================================
#核心概念:用一個函式包裝另一個函式，包起來
#就像在禮物外面包裝紙一樣，包裝紙裡面是禮物


def gift_wrap(func):#接收要包裝的函式
    def wrapper():#定義一個新的函式，這個函式會取代原本的函式
        print("__前置動作__")
        func()#執行原本的函式
        print("__後置動作__")
    return wrapper#回傳包裝好的函式

def say_hi():
    print("Hi!")





say_hello = gift_wrap(say_hello)#將 say_hello 包裝起來，得到一個新的函式

say_hello