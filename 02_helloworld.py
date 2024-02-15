# hello world で 言語の特徴が見えてくると。。。。

# python だとあまりに簡単・・・まあ、環境が整ってるからだけどな。
# print("hello world")

# もうちょっと難しいの。名前を入力して、その名前にhello する。
#name = input("what is your name?")
#print("hello " + name)

# 最後に関数化
def helloWorld(name):
    print("hello " + name)

name = input("what is your name?")
helloWorld(name)