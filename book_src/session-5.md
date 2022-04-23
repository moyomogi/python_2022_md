# 第 5 回 Python 勉強会 2022 | 有名データ構造、クラス、計算オーダー

# 1. 有名データ構造 set, deque, heapq をさらっと紹介

1. set 集合型

- (7) set [ABC085B - Kagami Mochi](https://atcoder.jp/contests/abs/tasks/abc085_b)

```py
n = int(input())
st = set()
for _ in range(n):
    x = int(input())
    st.add(x)
print(len(st))
```

2. deque 両端キュー
   機能としては list とほぼ同じ。内部実装の違いから、諸操作の計算量が異なります。

| メソッド名 | collections.deque  |
| ---------- | ------------------ |
| append(x)  | 末尾に x を追加    |
| pop(i=-1)  | i 番目の要素を削除 |
| count(x)   | 出現数を数える     |
| sort()     | ソートする         |
| reverse()  | 逆順にする         |

- 参考資料 [Python の deque でキュー、スタック、デック（両端キュー）を扱う](https://note.nkmk.me/python-collections-deque/)

3. heapq 優先度キュー

- 参考資料 [【Python】優先度付きキューの使い方【heapq】【ABC141 D】](https://qiita.com/ell/items/fe52a9eb9499b7060ed6)

(heapq に関する説明をここに)

# 2. クラス (Class)

クラスを自分で書く必要に迫られることはほとんどないと思います。
しかし、他人の描いたクラスがどのように動作しているのかは理解できると嬉しいので、クラスも紹介しておきます。
理解できなくても全く問題ないのでお気軽に～。

## 2-1. クラスを作ってみよう
```py
TODO: クラスに慣れるため、calc_rect_area の Class ver. を書く予定。
```

## 2-2. (発展) Complex クラスを作ってみよう

```py
class Complex:
    # class の中の関数をメソッドと呼びます。
    # メソッド名が __xxx__ の形のメソッドは、特別な働きをします。
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __add__(self, c):
        return Complex(self.re + c.re, self.im + c.im)

    def __mul__(self, c):
        return Complex(self.re * c.re - self.im * c.im, self.re * c.im + self.im * c.re)

    def __iadd__(self, c):
        self.re += c.re
        self.im += c.im
        return self

    def __imul__(self, c):
        re2 = self.re * c.re - self.im * c.im
        im2 = self.re * c.im + self.im * c.re
        self.re, self.im = re2, im2
        # 上 3 行と等価
        # self.re, self.im = self.re * c.re - self.im * c.im, self.re * c.im + self.im * c.re
        return self

    def __repr__(self):
        return f"{self.re} + {self.im}i"

    # 自由に命名できます
    def debug_print(self):
        print(f"self.re: {self.re}, self.im: {self.im}")

a = Complex(0, 1)
b = Complex(1, 0)
a.debug_print()  # self.re: 0, self.im: 1
b.debug_print()  # self.re: 1, self.im: 0
print(a)  # 0 + 1i
print(b)  # 1 + 0i
print(a + b)  # 1 + 1i
print(a * a)  # -1 + 0i
print(a * b)  # 0 + 1i

b += a
print(b)  # 1 + 1i
b *= a
print(b)  # -1 + 1i
```

# 3. 計算オーダーを考えよう

- (8) 計算オーダーを考える [C085C - Otoshidama](https://atcoder.jp/contests/abs/tasks/abc085_c)
  3 重 for 文は不要で、2 重 for 文を回すと k が一意に定まる。

```py
n, y = map(int, input().split())
for i in range(n + 1):
    for j in range(n + 1):
        k = n - i - j
        if k < 0:
            continue
        if i * 10000 + j * 5000 + k * 1000 == y:
            print(i, j, k)
            exit()
print("-1 -1 -1")
```

# 4. 競プロ er 必携の `online-judge-tools` を使ってみよう

## 4-1. `online-judge-tools` をインストール

(工事中)

## 4-2. `oj t` を使ってみよう

(工事中)

## 4-3. `oj s` を使ってみよう

(工事中)

# 5. `online-judge-verify-helper` を用いて GitHub 上にライブラリを公開してみよう

## 5-1. 準備
### 5-1-1. GitHub のアカウントを作る。  

### 5-1-2. GitHub Desktop をインストール。  

### 5-1-3. GitHub の各種設定

GitHub に SSH 接続するなど。ライブラリ整備 (GitHub Pages) をしましょう。(GitHub の練習として)  
(工事中)  


## 5-3. ライブラリを公開

[cheran-senthil/PyRival](https://github.com/cheran-senthil/PyRival) を参考に、ライブラリを公開してみましょう。  
(GitHub Desktop の使い方)  
(とりあえず Complex のみでよい)  

# 6. ？？？「Web 制作にご興味が？」

<img src="https://i.imgur.com/OCMiU8x.png" width="480">

今回、GitHub Pages でのウェブサイト公開がとても簡単に出来ることが分かりましたね。
ところで、友好祭に向けて Web サイト制作の会も行う予定ですので、是非お気軽にご参加ください。
[RVW 2022 Spring](https://rvw2022s.herokuapp.com) 程度のクオリティの Web サイトを自力で作れるようになることを目標にします。

# 7. 合作をしよう

公立大の部活 [App Navi](https://opuappnavi.com/#/) と不定期に hackathon を行っています。
合作に参加すると、他人のコードを読めて、知識が深まります。
プログラミング以外にも、「BGM・SE を探す」「タイトル画面のデザインをする」といった仕事があるので、合作に参加したことがない人も気負わず参加しましょう。

- 参考: Hackathon2022Spring
  テーマ「ジャンプ」(テーマは各 hackathon ごとに異なる) に沿ったゲームを作り合う対抗戦。
  - Computer House Random の作ったゲーム [Nisk36/Hackathon](https://github.com/Nisk36/Hackathon)
  - App Navi の作ったゲーム [JumPin](https://blog.opuappnavi.com/post/games-in-2021/#jumpin)

# 8. 競プロをしよう

## 8-1. バチャに参加しよう
毎週月・木の 21:00-22:00 にバチャをしています。  
この勉強会を通じて、競プロに興味を持った方はぜひ参加して、アルゴリズム力を高めましょう。  

## 8-2. 競プロの大会に出場しよう

Computer House Random では [ICPC](https://icpc.iisf.or.jp/blog/2022/03/29/icpc-regional-2022/) と [PG BATTLE](https://products.sint.co.jp/pg_battle) に出場しています (任意参加)。  
バチャに定期的に参加している人に声をかけるので、よろしくお願いします。  

# 9. 競プロだけに傾倒しないように

競プロ**だけ**に現を抜かし、Web 制作やゲーム制作を通じて実際にコードを書くことを疎かにしてはなりません (大会に出場しようと言っておいてあれですが)。  
競プロ (AtCoder など) は飽くまでも、実際に (つまり競プロ以外で) コードを書く際に、自分の中での固まった命名規則で変数を命名したり (「camelCase, PascalCase, snake_case が混ざったコードを書かない」など)、用いるべきデータ構造を見極めたり、構築すべき構造を大局的に捉えて完成形から逆算してコードを書いたりするための基礎練習に過ぎません。何かしらのプロダクトを作ることに時間を割くべきと、よもぎは思います。  

> 我々の目的の一つは、我々が始めてしまった競技プログラミングを我々が終わらせることです。  
>  \- [Twitter で医師を拾ってきて Google のソフトウェアエンジニアにするだけの簡単なお仕事](https://nuc.hatenadiary.org/entry/2021/03/31)

# 任意課題

難しいので (9), (10) は任意課題としたいと思います。  
なお、質問は受け付けておりますので、お気軽に。

- (7) set [ABC085B - Kagami Mochi](https://atcoder.jp/contests/abs/tasks/abc085_b)
- (8) 計算オーダーを考える [C085C - Otoshidama](https://atcoder.jp/contests/abs/tasks/abc085_c)
- (9) 後ろから見るテク [ABC049C - 白昼夢](https://atcoder.jp/contests/abs/tasks/arc065_a)
- (10) マンハッタン距離, パリティ [ABC086C - Traveling](https://atcoder.jp/contests/abs/tasks/arc089_a)
  意欲的な方は [Boot camp for Beginners](https://kenkoooo.com/atcoder/#/training/Boot%20camp%20for%20Beginners) も埋めておきましょう。

# 任意課題の解答

- (7) 掲載済みのため略。

- (8) 掲載済みのため略。

- (9) 後ろから見るテク [ABC049C - 白昼夢](https://atcoder.jp/contests/abs/tasks/arc065_a)

```py
s = input()
ts = ["dream", "dreamer", "erase", "eraser"]
while s != "":
    for t in ts:
        if s.endswith(t):
            s = s[:-len(t)]
            break
    else:
        print("NO")
        exit()
print("YES")
```

- (10) マンハッタン距離, パリティ [ABC086C - Traveling](https://atcoder.jp/contests/abs/tasks/arc089_a)

```py
n = int(input())
t0 = 0
x0 = 0
y0 = 0
for i in range(n):
    t, x, y = map(int, input().split())
    # 座標 (x0, y0) と 座標 (x, y) のマンハッタン距離
    manhattan = abs(x - x0) + abs(y - y0)
    # 余った時間
    rest_time = t - t0 - manhattan
    # 余った時間が負 or 奇数なら No
    if rest_time < 0 or rest_time % 2 == 1:
        print("No")
        exit()
    t0 = t
    x0 = x
    y0 = y
print("Yes")
```

# おわり

お疲れ様でした。強くなれましたか？
