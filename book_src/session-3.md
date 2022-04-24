# 第 3 回 Python 勉強会 2022 | 型、配列 (list)、ループ (for, while)

# 0. 予習事項

「1. 型とは？」を読んでおいてください。

# 1. 型とは？

- `bool` 型  
  if の中に入れるやつで、`True` (=1) と `False` (=0) の二値しか取りません。
- `int` 型  
  整数。ちなみに、C++ と異なり何桁でも無限に取れます (多倍長整数と言います)。
- `float` 型  
  小数。
- `str` 型  
  文字列。`str` は string の略で、文字列の意。

```py
x = True
print(x)  # True
print(type(x))  # bool

print(type(3.0))  # float?
print(type(3))  # int
print(3.0 == 3)  # True

print(type("3"))  # str
print("3" == 3)  # False (型が違います)

print(True + True)  # 2 (True の実態は 1 です)
```

# 2. 配列 (list)

プログラミングで最も使われるデータ構造は `list` です。
なお、`list` に付属の関数は表の通りです。
さらに詳しくは、[［解決！Python］リスト（配列）の使い方まとめ](https://atmarkit.itmedia.co.jp/ait/articles/2012/25/news023.html) を参照してください。

| メソッド名 | 説明               | 使い方 (リストの変数名が li のとき) |
| ---------- | ------------------ | ----------------------------------- |
| append(x)  | 末尾に x を追加    | li.append(6)                        |
| pop(i=-1)  | i 番目の要素を削除 | li.pop()とか li.pop(2)              |
| count(x)   | 出現数を数える     | li.count(1)                         |
| sort()     | ソートする         | li.sort()                           |
| reverse()  | 逆順にする         | li.reverse()                        |

```py
# いちいち変数を作るのは面倒
# num0 = 3
# num1 = 1
# num2 = 4
# num3 = 1
# num4 = 5

# 配列 (list) にしましょう。配列とは、数個の変数を 1 つとしてもつもののことです。
nums = [3, 1, 4, 1, 5]

print(nums)  # [3, 1, 4, 1, 5]
# 配列の前に * (アスタリスク) を付けると配列の中身を展開してくれます
print(*nums)  # 3 1 4 1 5
print(nums[0])  # 3
```

```py
planets = ["Mercury", "Venus", "Earth", "Malacandra", "Jupiter", "Saturn", "Uranus", "Neptune"]
print(planets.pop())  # Pluto
print(planets)
planets.index("Jupiter")  # 4 (index を返す)
```

## 2-1. (発展) ソート関数 `li.sort()` と `sorted(li)` の違い

| 使い方     | 破壊的か？   | 出自               |
| ---------- | ------------ | ------------------ |
| li.sort()  | 破壊的       | 型 list のメソッド |
| sorted(li) | 破壊的でない | 組み込み関数       |

ちなみに、どのプログラミング言語でも、デフォルトのソートは昇順ソートです。

- 昇順ソート: [3, 1, 4, 1, 5] -> [1, 1, 3, 4, 5] のように小さい順に並べる意。
- 降順ソート: [3, 1, 4, 1, 5] -> [5, 4, 3, 1, 1] のように大きい順に並べる意。

```py
nums = [3, 1, 4, 1, 5]
nums.sort()  # nums にソート結果を代入
print(nums)  # [1, 1, 3, 4, 5]
```

```py
nums = [3, 1, 4, 1, 5]
nums2 = sorted(nums)  # nums は不変
print(nums2)  # [1, 1, 3, 4, 5]
```

# 3. 組み込み関数 `range`

繰り返し実行機能である `for` 文を学習する前に、まずは組み込み関数 `range` を紹介します。
1 つ目の要素が 1 ではなく 0 (`0-indexed` という。) であることに注意。

| 使い方                   | 対応する配列                      | 対応する半開区間               | 具体例                                     |
| ------------------------ | --------------------------------- | ------------------------------ | ------------------------------------------ |
| range(stop)              | [0, 1, ..., stop - 1]             | $[0, stop)$                    | range(5) は、配列 [0, 1, 2, 3, 4] に対応。 |
| range(start, stop)       | [start, start + 1, ..., stop - 1] | $[start, stop)$                | range(2, 5) は、配列 [2, 3, 4] に対応。    |
| range(start, stop, step) | [start, start + step, ...]        | $[start, stop)$ の step 個飛び | range(0, 5, 2) は、配列 [0, 2, 4] に対応。 |

```py
# list でラップしないと生の range が出力されます
print(range(5))  # range(0, 5)

# 以下では list でラップします
print(list(range(5)))  # [0, 1, 2, 3, 4]
print(list(range(1, 5)))  # [1, 2, 3, 4]
print(list(range(0, 4)))  # [0, 1, 2, 3]
print(list(range(1, 4)))  # [1, 2, 3]
print(list(range(0, 5, 2)))  # [0, 2, 4]
```

# 4. 一定回数を繰り返す (`for`, `while`)

1. `for i in range(n)` 型

i は index の頭文字です。

```py
# 先述の通り range(5) は [0, 1, 2, 3, 4] の意です
for i in range(5):
    print(i)
    # 0
    # 1
    # 2
    # 3
    # 4
```

2. `for x in range(nums)` 型

```py
nums = [3, 1, 4, 1, 5]
for x in nums:
    print(x)
    # 3
    # 1
    # 4
    # 1
    # 5
```

3. (発展) 組み込み関数 `enumerate`
```py
nums = [3, 1, 4, 1, 5]
for i in range(len(nums)):
    print(f"nums[{i}] = {nums[i]}")
    # nums[0] = 3
    # nums[1] = 1
    # nums[2] = 4
    # nums[3] = 1
    # nums[4] = 5

# 組み込み関数 enumerate を使ってもよい
nums = [3, 1, 4, 1, 5]
for i, x in enumerate(nums):
    print(f"nums[{i}] = {x}")
    # nums[0] = 3
    # nums[1] = 1
    # nums[2] = 4
    # nums[3] = 1
    # nums[4] = 5
```

## 4-1. for で配列 (list) を構築する構文

```py
nums = [3, 1, 4, 1, 5]
# 配列 nums 内のそれぞれの要素を 2 乗する
nums2 = [num**2 for num in nums]
print(nums2)  # [9, 1, 16, 1, 25]
```

```py
planets = ["Mercury", "Venus", "Earth", "Malacandra", "Jupiter", "Saturn", "Uranus", "Neptune"]
# 各 planet の 0 文字目を集めた配列 planets2 を作る
planets2 = [planet[0] for planet in planets]
print(planets2)  # ['M', 'V', 'E', 'M', 'J', 'S', 'U', 'N']
```

```py
planets = ["Mercury", "Venus", "Earth", "Malacandra", "Jupiter", "Saturn", "Uranus", "Neptune"]
# 各 planet の末尾に感嘆符 (!) を付けた配列 planets3 を作る
planets3 = [
    planet.upper() + '!'
    for planet in planets
    if len(planet) < 6
]
print(planets3)  # ['VENUS!', 'EARTH!', 'MARS!']
```

```py
# 平方数
square_number = [n ** 2 for n in range(10)]
print(square_number)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

# 5. 配列 (list) の要素の総和を求める (for)

```py
a = [1, 2, 3, 4]
tot = 0
for i in range(len(a)):
    tot += a[i]
    print("tot =", tot)
    # tot: 1
    # tot: 3
    # tot: 6
    # tot: 10
print(tot)  # 10
```

別解として、組み込み関数 `sum` を使う方法もあります。
組み込み関数とは、デフォルトで (つまり import せずに) 使用可能な、標準搭載の関数のことです。

```py
a = [1, 2, 3, 4]
print(sum(a))  # 10
```

# 6. (while 文の説明をここに)

(工事中)

# 課題

コピペ AC 可。

- (2) for [C081A - Placing Marbles](https://atcoder.jp/contests/abs/tasks/abc081_a)
- (3) for, while [ABC081B - Shift only](https://atcoder.jp/contests/abs/tasks/abc081_b)
- (4) for [ABC087B - Coins](https://atcoder.jp/contests/abs/tasks/abc087_b)

# 課題の解答

- (2) for [C081A - Placing Marbles](https://atcoder.jp/contests/abs/tasks/abc081_a)

```py
s = input()
ans = 0
for c in s:
    if c == "1":
        ans += 1
print(ans)
```

- (3) for, while [ABC081B - Shift only](https://atcoder.jp/contests/abs/tasks/abc081_b)

```py
n = int(input())
a = list(map(int, input().split()))
ans = 0
while True:
    cnt = 0
    for i in range(n):
        if a[i] % 2 == 0:
            cnt += 1
    if cnt < n:
        break
    for i in range(n):
        a[i] //= 2
    ans += 1
print(ans)
```

- (4) for [ABC087B - Coins](https://atcoder.jp/contests/abs/tasks/abc087_b)

```py
a = int(input())
b = int(input())
c = int(input())
x = int(input())
# 上 4 行と等価
# a, b, c, x = [int(input()) for _ in range(4)]

ans = 0
for i in range(a + 1):
    for j in range(b + 1):
        for k in range(c + 1):
            tot = 500 * i + 100 * j + 50 * k
            if tot == x:
                ans += 1
print(ans)
```

# 次回 (第 4 回) へのリンク

{{< post 441 >}}
