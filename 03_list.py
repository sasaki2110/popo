# listはさすがにソースを残しておくか。

# 後でclassも欲しいから、ここで適当に宣言
class Nn():
    def __init__(self):
        super().__init__()
nn = Nn()

# リストにはなんでも入ると。
items = ["aaa", 1, 2.543e2, lambda x:x+1, nn, [1, 2], (lambda y:y+1, 4), {5, nn}]
for item in items:
    print(type(item))
    print(item)

# 直接宣言だけじゃなく、list()関数でも生成できる
clists = list("Python")
print(clists)

ilist = list(range(10))
print(ilist)

# スライスでリストを更新すると、要素数が一致してなくても、いい感じでやってくれる。
ii = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(ii)

ii[1:4] = [10, 11, 12, 13, 14]
print(ii)

ii[1:3] = []
print(ii)

# まあ、append やら remove もある。

# リスト内包表記 酔いがさめてから見るか。
inlist = [] # 普通バージョン
for x in range(10):
    inlist.append(x)

inlist = [x for x in range(10)]   # 内包表記バージョン　
#最初のｘは、上のappendに該当する。だからもう決まり事。
#いや、 x * 2 をリストに入れたりもできるのか。
print(inlist)