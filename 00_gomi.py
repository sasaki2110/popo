# さすがに保存するほどの内容もないから、しばらくはゴミでいいか。

# unicord のエンドポイントを求めるには ord()を使う。

as_code_point = ord("a")
print("hex end point = ", hex(as_code_point))

as_code_point = ord("漢")
print("漢字だと hex end point = ", hex(as_code_point))
print(chr(0x6f22)) # まあ使う事は無いけど、エスケープシーケンスで頑張るよりchrの方が速い

# raw 文字列。これは大切
# 文字列の前に「r」をつけると raw と扱われ、エスケープが不要と。
raw_str = r"C:\Users\deepinsider\Documents\work\data.txt"
print(raw_str)

# フォーマット済み文字列 これもなかなか
# JSXに似た表記やね。
x = 1
y = 100
result = f'{x} + {y} = {x + y}'
print(result)