# 第 2 回 Python 勉強会 2022 | Python 組み込み関数、条件分岐、print テク

# 0. 復習事項

整数・小数の四則計算 (+ - \* \*\* / // %) (再掲)

| 演算子 | 機能               | 実際の使い方     |
| ------ | ------------------ | ---------------- |
| +      | 加算               | print(1 + 2)     |
| -      | 減算               | print(2 - 1)     |
| \*     | 乗算               | print(2 \* 3)    |
| \*\*   | 累乗               | print(6 \*\* 10) |
| /      | 除算               | print(2 / 3)     |
| //     | 除算の商、切り捨て | print(31 // 7)   |
| %      | 除算の余り         | print(31 % 7)    |

# 1. Pylance (Linter), Formatter は入っていますか？

VSCode を入れてくれた人なら、拡張機能 `Python` の中に Pylance (Linter) が入っています。Formatter は black がおすすめです。  
(Linter が入っているかを確認しよう。)  
(Formatter が入っているかを確認しよう。)

# 2. (発展) 演算子の評価順序

ちなみに、Python では演算子の評価順序は以下の通りです。

| Tier | 演算子               |
| ---- | -------------------- |
| 1    | ()                   |
| 2    | \*\*                 |
| 3    | \*, /, //, %         |
| 4    | +, -                 |
| 5    | <, <=, >, >=, ==, != |
| 6    | not                  |
| 7    | and                  |
| 8    | or                   |

```py
# TODO: Tier に関するコードを書く
```

# 3. 文字列 (str)

"xxx" のように、" (ダブルクオーテーション) に囲まれた型を**文字列** (`str`) といいます。  
なお、ダブルクオーテーションで囲んでも、シングルクオーテーションで囲んでも構いません。  
シングルクオーテーションは両手で入力しなければならないのに対し、ダブルクオーテーションは片手で入力できるため、よもぎはダブルクオーテーションで文字列を書いています。

```py
print("羽衣ララ")  # 羽衣ララ

# 同じ結果となる
print('羽衣ララ')  # 羽衣ララ
```

# 4. 変数に数値を代入する

```py
x = 346
print(x)  # 346
x = 283
print(x)  # 283
```

```py
# 悲しいコード
print("1 year =", 365, "days")
print("1 year =", 365 * 24, "hours")
print("1 year =", 365 * 24 * 60, "minutes")
print("1 year =", 365 * 24 * 60 * 60, "seconds")

# 嬉しいコード
days = 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print("1 year =", days, "days")
print("1 year =", hours, "hours")
print("1 year =", minutes, "minutes")
print("1 year =", seconds, "seconds")
```

# 5. 組み込み関数 `max`, `min`, `abs`

Python では、これまで登場した `print` 以外にも、
`max`, `min`, `abs` という組み込み関数が存在します。
組み込み関数とは、関数を自分で定義 (関数は第 4 回で取り扱います。) せずとも、デフォルトで使える関数です。

| 組み込み関数の関数名 | 返り値                                   |
| -------------------- | ---------------------------------------- |
| max                  | 引数 (ひきすう) を複数取り、最大値を返す |
| min                  | 引数を複数取り、最小値を返す             |
| abs                  | 引数を 1 つ取り、絶対値を返す            |

```py
print(min(1, 2, 3))  # 1
print(max(1, 2, 3))  # 3
print(abs(32))  # 32
print(abs(-32))  # 32
print(float(10))  # 10.0
```

# 6. 文字列操作

デフォルトは `[0:n]`、つまり半開区間 $[0, n)$ です。(ただし $n := len(s)$ とした。)

```py
s = "DeepLearning"
print(len(s))  # 12 (文字数)
print(s[0])  # D (index は 0-indexed で指定します)
print(s[-1])  # g (負の数なら、末尾からの文字数と解釈される)
print(s[0:5])  # DeepL
print(s[:5])  # DeepL (上の行と等価)
print(s[-3:12])  # ing
print(s[-3:])  # ing (上の行と等価)

print(s[::5])  # Den (あまり使いませんが、3 番目の引数では step を指定できます。default は 1 です。)
print(s[::-1])  # gninraeLpeeD (負の数も指定可能)

print("Spam " * 4)  # Spam Spam Spam Spam

# 今回は 2 行しかないので \n で書いても良いが、文が長くなったときは """ で囲んで書くのが楽
print("hello\nworld")  # 下と等価
print("""hello
world""")  # """ で囲むと、literally に改行を書ける

# 文字列 (str) のメソッドに、count(s: str) があります
print("aaabbc".count("a"))  # 3
print("aaabbc".count("b"))  # 2
print("aaabbc".count("c"))  # 1
```

# 7. 条件分岐 (if, elif, else)

```py
x = 765
if x % 2 == 0:
    print(x, "は偶数")
else:
    print(x, "は奇数")  # 765 は奇数
```

```py
x = 346
if x > 500:
    print(x, "は 500 より大")
elif x == 500:
    print(x, "は 500 と等しい")
else:
    print(x, "は 500 より小")  # 346 は 500 より小
```

# 8. (発展) 三項演算子

三項演算子は `(True の時の値) if (条件) else (False の時の値)` と書きます。

```py
x = 765
print(x, "は偶数" if x % 2 == 0 else "は奇数")  # 765 は奇数
```

# 9. (発展) print テク

## 9-1. F 文字列 (F-Strings)

好みの問題ですが、コンマを使う代わりに F 文字列を用いて `print` することもできます。

```py
print("2 * 3:", 2 * 3)  # 2 * 3: 6
print(f"2 * 3: {2 * 3}")  # 2 * 3: 6

# Python 3.6 以前では、str.format メソッドしかありませんでした
print("2 * 3: {}".format(2 * 3))  # 2 * 3: 6
```

### 9-1-1. 書式指定
- 詳しくは、[Pythonの文字列フォーマット（formatメソッドの使い方）](https://gammasoft.jp/blog/python-string-format/) を参照。

```py
print("pi = {:.4}".format(3.141592653589793238462643383279))  # 3.142
```

## 9-2. エスケープ

シングルクオーテーションを出力する際は、ダブルクォーテーションで囲み、
ダブルクオーテーションを出力する際は、シングルクォーテーションで囲みます。

```py
print("シングルクオーテーションは ' です")  # シングルクオーテーションは ' です
print('ダブルクオーテーションは " です')  # ダブルクオーテーションは " です

# もちろん、以下のように出力することも可能ですが、ダサいです
print('シングルクオーテーションは \' です')  # シングルクオーテーションは ' です
print("ダブルクオーテーションは \" です")  # ダブルクオーテーションは " です
```

```py
print("バックスラッシュは \\ です")  # バックスラッシュは \ です
print("改行は\nです")
# 改行は
# です
```

## 9-3. Raw 文字列 (Raw Strings)

制御文字 (\\, \n) をそのまま出力。

```py
print("a\\b\nA\\B")
# a\b
# A\B
print(r"a\\b\nA\\B") # a\\b\nA\\B
```

## 9-4. sep, end に値を入れてみよう

```py
# default は sep=" "
print(1, 2, 3, sep=" < ")  # 1 < 2 < 3
# default は end="\n" (\n は改行を意味する制御文字)
print("No line break.", end="")  # No line break. (改行なし)
```

# 課題

本講座の課題を独力で解くのは難しいです。  
そのため、付属の解答を読んで、どのような仕組みで動いているか理解する (debug をして、変数がどのように変わるかを見るなど) だけで十分です。  
ただし、コピペ AC はしておいてください。

- (1) 条件分岐 (if, else) [ABC086A - Product](https://atcoder.jp/contests/abs/tasks/abc086_a)

# 課題の解答

- (1) 条件分岐 (if, else) [ABC086A - Product](https://atcoder.jp/contests/abs/tasks/abc086_a)

```py
a, b = map(int, input().split())
if a * b % 2 == 0:
    print("Even")
else:
    print("Odd")
```

# 次回 (第 3 回) へのリンク

{{< post 440 >}}
