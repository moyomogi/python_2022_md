# 第 4 回 Python 勉強会 2022 | 関数、外部ライブラリ、Web Scraping

# 1. 自分で関数を作ってみよう (def)

下記は、長方形の面積を求めるプログラムです。

```py
def calc_rect_area(height, width):
    return height * width


print(calc_rect_area(20, 30))  # 600
```

## 1-1. デフォルト引数 (ひきすう) を付けてみよう

```py
def calc_rect_area2(height=50, width=70):
    return height * width


# print(calc_rect_area2(20, 70)) として解釈される
print(calc_rect_area2(20))  # 1400

# print(calc_rect_area2(50, 70)) として解釈される
print(calc_rect_area2())  # 3500
```

## 1-2. (参考) lambda (ラムダ) 関数

lambda 関数を使うと def を使って定義するよりも短く書けますが、
読みにくくなってしまうので、def を使うことをお薦めします。

```py
def calc_rect_area(height, width):
    return height * width

print(calc_rect_area(20, 30))  # 600

# calc_rect_area と等価な関数
calc_rect_area3 = lambda h, w: h * w
print(calc_rect_area3(20, 30))  # 600
```

# 2. (発展) 再帰関数

```py
# エラトステネスの篩を用いて最大公約数を求める
def gcd(x, y):
    if x == 0:
        return y
    else:
        return gcd(y % x, x)

# 三興演算子を使ってもいいですね
# def gcd(x, y):
#   return y if x == 0 else gcd(y % x, x)

print(gcd(12, 18))  # 6


# 本題 (再帰関数) から逸れますが、
# 最小公倍数は、「lcm(x, y) == x * y // gcd(x, y)」を利用すると求まります。
def lcm(x, y):
    if x == 0 and y == 0:
        return 0
    return x * y // gcd(x, y)

print(lcm(12, 18))  # 36
```

# 3. 外部ライブラリ `math` を使ってみよう

```py
import math

print("pi = {:.4}".format(math.pi))  # 3.142
print(math.log(32, 2))  # 5.0
```

外部ライブラリ `math` を使えば、円の面積を計算できます。

```py
import math


def calc_circle_area(radius):
    # * よりも ** の方が先に評価されます。
    # return math.pi * (radius ** 2) のように明示的に計算順序を書くこともできます。
    return math.pi * radius ** 2

print(calc_circle_area(10))  # 314.1592653589793
```

# 4. (超発展) Web Scraping

## 4-1. `BeautifulSoup` で Web Scraping

Static Hosting なサイトに対しては、`BeautifulSoup` のみで Web Scraping できます。
(なお、JavaScript Hosting なサイトに対しては、`selenium` + `BeautifulSoup` で Web Scraping できます。)

まずは VSCode 付属のターミナルを開き、`BeautifulSoup` の入っている `beautifulsoup4` と `requests` をインストール。

```sh
pip3 install beautifulsoup4 requests
```

```py
# https://oxylabs.io/blog/python-web-scraping
import requests
import sys
from bs4 import BeautifulSoup

url = "https://ch-random.net/authors/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# https://realpython.com/beautiful-soup-web-scraper-python/
# 以下は等価
# - soup.find("img", class_="my-portrait")
# - soup.select("img.my-portrait")

footers = soup.select("div.projects-container")

# 生成したいもの
# const authorsDict = {
#   yomog: {
#     year: 2,
#     name: "よもぎ",
#     icon: "https://ch-random.net/authors/yomog/avatar_hue523f5c0a45e10cf0e33f8e085b52548_162276_250x250_fill_lanczos_center_2.png",
#   },
#   // ...
# };
print("const authorsDict = {")

for (i, footer) in enumerate(footers[1:4]):
    print(f"  // {i + 2} 回生", file=sys.stderr)
    h4s = footer.select("h4")
    imgs = footer.select("img.my-portrait")
    for j in range(len(h4s)):
        # https://stackoverflow.com/questions/55385113/how-do-i-scrape-image-src-in-beautifulsoup
        src = str(imgs[j].get("src"))
        author = src.split("/")[2]
        print(f"  {author}: {{")
        print(f'    year: {i + 2},')
        print(f'    name: "{h4s[j].text}",')
        print(f'    icon: "https://ch-random.net{src}",')
        print("  },")

print("};")
```

# 課題

コピペ AC 可。

- (5) def [ABC083B - Some Sums](https://atcoder.jp/contests/abs/tasks/abc083_b)
- (6) sort [ABC088B - Card Game for Two](https://atcoder.jp/contests/abs/tasks/abc088_b)

# 課題の解答

- (5) def [ABC083B - Some Sums](https://atcoder.jp/contests/abs/tasks/abc083_b)

1. 関数を使わないで書いた場合。

```py
n, a, b = map(int, input().split())
ans = 0
for x in range(1, n + 1):
    sm = 0
    x2 = x
    while x2 > 0:
        sm += x2 % 10
        x2 //= 10
    if a <= sm <= b:
        ans += x
print(ans)
```

2. 関数を define (定義) して解いた場合。  
   見やすくなりましたね。

```py
def calc_sum(x):
    res = 0
    while x > 0:
        res += x % 10
        x //= 10
    return res

n, a, b = map(int, input().split())
ans = 0
for x in range(1, n + 1):
    sm = calc_sum(x)
    if a <= sm <= b:
        ans += x
print(ans)
```

- (6) sort [ABC088B - Card Game for Two](https://atcoder.jp/contests/abs/tasks/abc088_b)

1. 昇順ソートを用いた解法

```py
n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(n):
    if i % 2 == n % 2:
        ans -= a[i]
    else:
        ans += a[i]
print(ans)
```

2. 降順ソートを用いた解法

```py
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

ans = 0
for i in range(n):
    if i % 2 == 0:
        ans += a[i]
    else:
        ans -= a[i]
# 直前 6 行と等価
# ans = sum(a[::2]) - sum(a[1::2])

print(ans)
```

# 次回 (第 5 回) へのリンク

{{< post 442 >}}
