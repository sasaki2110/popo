# popo
    Plane Old Python Object 。。。。って、単なる pojo のパクり。
    要は、フレームワークや機械学習を無視して、素の python の習得ように作った。

    あ、参考サイトはってなかった
    https://atmarkit.itmedia.co.jp/ait/subtop/features/di/pybasic_index.html

### Pythonってどんな言語なの？
    01_whatsPython.py
    まあ、ざくっとした概説 

### Hello Python：一番簡単なプログラムを作ってみよう
    さすがにここで学ぶ事はないな・・・・

### 数値と算術演算
    うん、特記事項はないな・・・

### 変数とは
    まあ、ないわな・・・・
    あ、でも命名規約は独特なのね。

    変数名には大文字を使わない事が推奨。
    キャメルとかパスカルとか使わずに小文字でと。
    で、長いときは_で区切れと。（スネーク）

    基本はすべてスネーク
    例外は
    　定数：大文字のスネーク（コンストって言語使用が無いから、大文字で定数を判断するらしい。）
    　クラス名：パスカル

### 文字列の基本
    python3 では基本の文字コードはUnicodeだと。
    （この環境は？ja_JP.UTF-8になってた。）
    
	raw 文字列。これは大切（というか俺に馴染みがないから覚えておかないと）
        文字列の前に「r」をつけると raw と扱われ、エスケープが不要と。
        raw_str = r"C:\Users\deepinsider\Documents\work\data.txt"
        print(raw_str)

	フォーマット済み文字列 これもなかなか
	JSXに似た表記やね。
        x = 1
        y = 100
        result = f'{x} + {y} = {x + y}'
        print(result)

### 文字列の操作
    明日はここからやね。