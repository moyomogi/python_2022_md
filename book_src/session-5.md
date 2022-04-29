# 第 5 回 Python 勉強会 2022 | 有名データ構造、クラス、計算オーダー、GitHub、Netlify

# 1. 有名データ構造 set, deque, heapq をさらっと紹介

1. 集合型 `set`

- (7) set [ABC085B - Kagami Mochi](https://atcoder.jp/contests/abs/tasks/abc085_b)

```py
n = int(input())
st = set()
for _ in range(n):
    x = int(input())
    st.add(x)
print(len(st))
```

2. 両端キュー `deque`  
   機能としては list に似ていますが、先頭に要素を追加する `appendleft` や先頭の要素を削除する `popleft` があります。

- list の主要なメソッド

  | メソッド名   | 機能             | 計算量 |
  | ------------ | ---------------- | ------ |
  | append(x)    | 末尾に要素を追加 | $O(1)$ |
  | insert(i, x) | 途中に要素を追加 | $O(n)$ |
  | pop()        | 末尾の要素を削除 | $O(1)$ |

- deque の主要なメソッド

  | メソッド名    | 機能             | 計算量 |
  | ------------- | ---------------- | ------ |
  | append(x)     | 末尾に要素を追加 | $O(1)$ |
  | appendleft(x) | 先頭に要素を追加 | $O(1)$ |
  | pop()         | 末尾の要素を削除 | $O(1)$ |
  | popleft()     | 先頭の要素を削除 | $O(1)$ |

```py
TODO: deque の説明コード
```

- さらに詳しくは [Python の deque でキュー、スタック、デック（両端キュー）を扱う](https://note.nkmk.me/python-collections-deque/) を参照。

3. 優先度キュー `heapq`  
   ほとんど使わないので説明略。

- 参考資料 [【Python】優先度付きキューの使い方【heapq】【ABC141 D】](https://qiita.com/ell/items/fe52a9eb9499b7060ed6)

# 2. クラス (Class)

クラスを自分で書く必要に迫られることはほとんどないと思います。  
しかし、他人の描いたクラスがどのように動作しているのかは理解できると嬉しいので、クラスも紹介しておきます。  
理解できなくても全く問題ないので気軽に聞いてください。

## 2-1. クラスを作ってみよう

```py
class Calculator:
    # class の中の関数をメソッドと呼びます。
    def __init__(self, w=50, h=70):
        self.w = w
        self.h = h

    # 面積は w * h です。
    def calc_rect_area(self):
        return self.w * self.h

    # 周の長さは 2 * w + 2 * h です。
    def calc_perimeter_len(self):
        return 2 * self.w + 2 * self.h


c1 = Calculator(20, 30)
print(c1.calc_rect_area())  # 600

# c2 = Calculator(20, 70) として解釈される
c2 = Calculator(20)
print(c2.calc_rect_area())  # 1400

# c3 = Calculator(50, 70) として解釈される
c3 = Calculator()
print(c3.calc_rect_area())  # 3500
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

# 3. (発展) 計算オーダーを考えよう

- (8) 計算オーダーを考える [C085C - Otoshidama](https://atcoder.jp/contests/abs/tasks/abc085_c)

  3 重 for 文は不要で、2 重 for 文を回すと k が一意に定まる。  
  $10^8$ 回の演算で大体 1000ms (= 1s) かかります。  
  AtCoder の問題の 9 割は制限が 2000ms なので、O$(2 \prod 10^9)$。
  - 3 重 for 文による実装の計算量: $O(n^3) = O(2000^3)$  
  - 2 重 for 文による実装の計算量: $O(n^2) = O(2000^2)$  

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

# 4. (発展) GitHub 上にライブラリを公開してみよう

GitHub の練習として、ライブラリを GitHub Pages に公開してみましょう。

## 4-1. 準備

### 4-1-1. GitHub のアカウントを作る

[Hoin GitHub - GitHub](https://github.com/join) から登録してください。

### 4-1-2. GitHub Desktop をインストール

(GitHub Desktop に関する説明、誰か書いてほしい。  
僕はコマンドでやってるので、何も分かりません。)

- (参考) なお、GitHub Desktop を使わずとも、コマンドで GitHub にファイルをアップロードすることができます。
  1. github に ssh 接続する。
  - 参考資料 [GitHub に ssh 接続するまでの手順](https://zenn.dev/schnell/articles/0e1c2e9db5c08d)
  2. 以下のコマンドを実行。

```sh
# ★以下のコマンドは、かなり高度です。
#   GitHub Desktop があれば、以下のコマンドを使う必要は
#   全くないので、このコマンドはスルーしてもいいです。
# 下 4 行は初回のみ実行
$ git init
# moyomogi, python_2022_lib は自分のものに読み替えてください
git remote add origin git@github.com:moyomogi/python_2022_lib.git
# moyomogi は自分のものに読み替えてください
$ git config --local user.name "moyomogi"
# mozuyomogi@gmail.com は自分のものに読み替えてください
$ git config --local user.email "mozuyomogi@gmail.com"

# ファイルをアップロード
$ git add .
$ git commit -m "First commit"
$ git push origin master
```

### 4-1-3. GitHub の各種設定

## 4-2. ライブラリを公開

1. 勉強会用のフォルダと同じ階層に、別のフォルダ (フォルダ名は例えば `python_2022_lib` として、`YOUR_NAME/python_2022_lib` のように) を作ってください。
2. [moyomogi/python_2022_lib](https://github.com/moyomogi/python_2022_lib) の Download Zip からコードをダウンロードして、中身を 1. で作ったフォルダ内に貼り付け。
3. ライブラリ用のレポジトリを新規作成。
4. GitHub Desktop を用いてファイルをアップロード。
5. GitHub のアカウントで [Netlify](https://app.netlify.com) にログインし、ライブラリのレポジトリを選択して、デプロイ。詳しい操作は [Setting up your own digital garden with Jekyll](https://maximevaillancourt.com/blog/setting-up-your-own-digital-garden-with-jekyll) を参照。

# 5. (余談) ？？？「Web 制作にご興味が？」

<img src="https://i.imgur.com/OCMiU8x.png" width="480">

今回、Netlify でのウェブサイト公開がとても簡単に出来ることが分かりましたね。
ところで、友好祭に向けて Web サイト制作の会も行う予定ですので、是非お気軽にご参加ください。
[RVW 2022 Spring](https://rvw2022s.herokuapp.com) 程度のクオリティの Web サイトを自力で作れるようになることを目標にします。

# 6. (余談) 合作をしよう

OMU の部活 [App Navi](https://opuappnavi.com/#/) と不定期にハッカソンを行っています。  
合作に参加すると、他人のコードを読めて、知識が深まります。  
プログラミング以外にも、「BGM・SE を探す」「タイトル画面のデザインをする」といった仕事があるので、合作に参加したことがない人も気負わず参加しましょう。

- 参考: 2022 年の春に行ったハッカソン「Hackathon2022Spring」の内容は以下の通り。
  テーマ「ジャンプ」(テーマは各ハッカソンごとに異なる) に沿ったゲームを作り合う対抗戦。
  - Computer House Random の作ったゲーム [Nisk36/Hackathon](https://github.com/Nisk36/Hackathon)
  - App Navi の作ったゲーム [JumPin](https://blog.opuappnavi.com/post/games-in-2021/#jumpin)

# 7. (余談) 競プロをしよう

## 7-1. バチャに参加しよう

毎週月・木の 21:00-22:00 にバチャをしています。  
この勉強会を通じて、競プロに興味を持った方はぜひ参加して、アルゴリズム力を高めましょう。

## 7-2. 競プロの大会に出場しよう

Computer House Random では [ICPC](https://icpc.iisf.or.jp/blog/2022/03/29/icpc-regional-2022/) と [PG BATTLE](https://products.sint.co.jp/pg_battle) に出場しています (任意参加)。  
バチャに定期的に参加している人に声をかけるので、よろしくお願いします。

## 7-3. 競プロだけに傾倒しないように

競プロ**だけ**に現を抜かし、Web 制作やゲーム制作を通じて実際にコードを書くことを疎かにしてはなりません (大会に出場しようと言っておいてあれですが)。  
競プロ (AtCoder など) は飽くまでも、実際に (つまり競プロ以外で) コードを書く際に、自分の中での固まった命名規則で変数を命名したり (「camelCase, PascalCase, snake_case が混ざったコードを書かない」など)、用いるべきデータ構造を見極めたり、構築すべき構造を大局的に捉えて完成形から逆算してコードを書いたりするための基礎練習に過ぎません。何かしらのプロダクトを作ることに時間を割くべきと、よもぎは思います。

> 我々の目的の一つは、我々が始めてしまった競技プログラミングを我々が終わらせることです。  
>  \- [Twitter で医師を拾ってきて Google のソフトウェアエンジニアにするだけの簡単なお仕事](https://nuc.hatenadiary.org/entry/2021/03/31)

# 補遺

- GitHub の基本操作の学習には [Introduction to GitHub](https://lab.github.com/githubtraining/introduction-to-github) がお薦めです。

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
