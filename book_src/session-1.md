# 第 1 回 Python 勉強会 2022 | VSCode インストール、WSL 構築

# 1. 予習事項

- 「2. スクショの取り方」を実際に試してみておいてください。
- 「3. VSCode インストール」をやっておいていただけるとスムーズに進行できます。

# 2. スクショの取り方

この勉強会に限らないことですが、何か困って質問したい際に、スクショを貼ることで、自分がどういった状況かを質問相手に簡単かつ正確に伝えることができます。

- Snipping Tool  
  `win + s` で検索窓を出して snipping tool と入力すれば見つかるはずです。
  スクショを .png 形式で保存できます。
- `win + shift + s`  
  スクショ区域を指定して、スクショした画像をクリップボードに送ります。  
  クリップボードに送られた画像は、discord や各種お絵かきソフト (クリスタ、GIMP、イラレ) 上で `ctrl + v` を入力することで貼り付けできます。

# 3. VSCode インストール

Windows 向けの説明しか行いません。すいませんが、Mac ユーザーの方々は各自で環境を構築してください。
まず、[VSCode 公式のダウンロードページ](https://code.visualstudio.com/download) から DL して、インストールしてください。
Vim 派の人もいるかもですが、VSCode に Vim を載せれるらしいので、よければ VSCode をインストールしてください。

# 4. (任意) WSL を有効化しよう

ちなみに、WSL は Windows Subsystem for Linux の略です。

## 4-1. なぜ WSL が必要か

- Ubuntu には、非公式リポジトリ [PPA](https://launchpad.net/ubuntu/+ppas) があり、自作 CLI ツールを PPA に登録すると、`add-apt-repository` コマンドで、そのリポジトリをマシンに登録できるので、他のユーザーが `apt` コマンドでそのプログラムを使えるようになります。
- 対して Windows では、自作 CLI ツールを公開する仕組みがないため、技術が発展していません。

従って、**Ubuntu 上の便利な CLI ツールを使うため**に、WSL が必要です。

## 4-2. WSL を入れよう

本勉強会では Python・C++ を WSL にインストールします。  
[Visual Studio Code で競プロ環境構築(導入編)](https://qiita.com/AokabiC/items/e9312856f588dd9303ed) をブラウザ上の別タブで開いてください。  
一応、実行すべき行為を置いておきます。

1. デフォルトの Windows では、スタートアップ時に WSL が起動しません。  
   以下の A, B いずれかを行い、WSL を有効化します。  
   A. (GUI で有効化) [Windows Subsystem for Linux (WSL1) をインストールしてみよう！](https://qiita.com/Aruneko/items/c79810b0b015bebf30bb) を読んでください。  
   B. (CUI で有効化) Windows PowerShell にて、WSL を有効化しましょう。  
   この設定により NoxPlayer などのエミュレーターが動かなくなることがありますが、元の設定に戻せば、また動かせます。

```sh
# Windows PowerShell にて、以下を実行。ただし、先頭の $ は入力しないでください。
# 今回の例でいえば、「Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux」のみを入力して Enter してください。
$ Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

2. WSL を起動させるために、PC を再起動。
3. Microsoft Store で Ubuntu 22.04 LTS (2022-04-21 リリース) を入れる (「ubuntu」で検索すると、下の方に出てきます)。
   - LTS (Long Time Support, 長期サポート) は「安定版」の意です。
   - Ubuntu 22.04 LTS のバージョン違いとして Ubuntu, Ubuntu 20.04 LTS がありますが、ほぼ同じように扱えますので、すでに Ubuntu を入れていた方は新規にインストールする必要はありません。
4. Ubuntu 22.04 LTS を起動し以下を実行。

```sh
# コマンドの先頭に sudo (スードゥー) を付けると、ルート権限でコマンドを実行できます。
$ sudo sed -i -e 's%http://.*.ubuntu.com%http://ftp.jaist.ac.jp/pub/Linux%g' /etc/apt/sources.list
```

```sh
$ sudo apt update
$ sudo apt -y upgrade
```

```sh
$ sudo apt install -y software-properties-common
$ sudo add-apt-repository universe

# build-essential, gdb: C++ 向け
# python3, flake8: Python 向け
# pkg-config:
#   これがないとバグるツールが結構あるので
#   まとめてインストールしえおきましょう。
$ sudo apt install -y build-essential gdb python3 flake8 pkg-config
```

```sh
$ sudo apt update
$ sudo apt install -y python3-pip
# Linter の black をインストール
$ sudo pip install autopep8
# Formatter の black をインストール
$ sudo pip3 install black

# (参考) インストール済みパッケージのアップデートを行うには、
# --upgrade あるいは -U を付けます。
# $ sudo pip install --upgrade autopep8
# $ sudo pip3 install --upgrade black
```

# 5. (余談) プログラミング用フォルダは `~` 下に置くといいよ、という話

(「(任意) WSL を有効化しよう」をやってくださった方向けです。)  
WSL を入れ終わった方は、エクスプローラーを開き、パンくずリストが書かれた窓に `\\wsl$\Ubuntu-20.04\home` と打って Enter を押してください。
`YOUR_NAME` (YOUR_NAME は自分の入力した名前) というフォルダがあるはずです。
(以下、`\\wsl$\Ubuntu-20.04\home\YOUR_NAME` を `~` と略記します。)  
実は、`Remote-WSL` (VSCode の拡張機能) を使う場合は、 `C:\` や `D:\` に作業フォルダを置くより、`~` 以下に作業フォルダを置いた方が、Windows と Ubuntu 間のシステムのやり取りがないため、ファイル読み書きの動作が速いです。  
具体的に書くと、 `~/compro` というフォルダを `Remote-WSL` で開くと、比較的ファイル読み書きの動作が軽い、ということです。  
ちなみに、compro というのは競プロ (Competitive Programming) の意です。

- 参考資料 [WSL2 で Git などのファイル操作が重い問題を解決した方法](https://www.orzs.tech/how-to-solve-the-problem-that-file-operations-such-as-git-are-heavy-with-wsl2/)

# 6. `cd`, `ls` コマンドを知っておこう

Ubuntu を使うにあたって必須のコマンドが `cd`, `ls` コマンドです。機能は下票の通りです。  
(下記表で、「ディレクトリ」は「フォルダ」と同義です。)

| コマンド名 | コマンド名の由来 | 機能                                         | 使い方                   |
| ---------- | ---------------- | -------------------------------------------- | ------------------------ |
| cd         | change directory | カレントディレクトリの変更                   | `cd PATH/TO/YOUR/FOLDER` |
| ls         | list segments    | カレントディレクトリ配下のファイル一覧を表示 | `ls`                     |

1. `cd` の引数 (ひきすう) に絶対パスを指定して移動  
   絶対パスとは、Windows のエクスプローラーのパンくずリストの窓をクリックした時に現れるパスです。

```sh
# WSL 20.04 LTS にて以下を実行。
$ cd ~  # フォルダ ~ に移動
# ls に対する出力と、エクスプローラーで開いた \\wsl$\Ubuntu-20.04\home\YOUR_NAME に見えているフォルダ内とを見比べて、
# 正常に cd 出来ているかを確認してみましょう。。
$ ls
```

```sh
$ cd /mnt/c  # フォルダ /mnt/c に移動
$ ls
```

2. `cd` の引数に相対パスを指定して移動  
   相対パスとは、基準となるフォルダからの差分のパスです。

| カレントディレクトリが (絶対パス) のとき (絶対パス) は             | (相対パス)    |
| ------------------------------------------------------------------ | ------------- |
| カレントディレクトリが `~/compro` のとき `~/compro/src/test.py` は | `src/test.py` |
| カレントディレクトリが `~` のとき `~/compro` は                    | `compro`      |
| カレントディレクトリが `~` のとき `~/compro/src` は                | `compro/src`  |
| カレントディレクトリが `~/compro` のとき `~` は                    | `..`          |
| カレントディレクトリが `~/compro` のとき `~/.bashrc` は            | `../.bashrc`  |
| カレントディレクトリが `~/compro/src` のとき `~` は                | `../..`       |

```sh
# WSL 20.04 LTS にて以下を実行。
$ cd ..  # 親フォルダへ
$ ls
```

```sh
$ cd YOUR_FOLDER  # 子フォルダ YOUR_FOLDER に移動
$ ls
```

# 7. 勉強会用フォルダにて各種準備をしよう

## 7-1. py ファイルを準備しよう

1. `D:\YOUR_FOLDER` や `~/YOUR_FOLDER` のいずれかの場所に、勉強会用フォルダを作成してください。(以下、このフォルダを `YOUR_FOLDER` として統一して言及する。)
2. エクスプローラー上で `YOUR_FOLDER/main.py` (ファイル名 (つまり `main` の部分) は自由でいいです) を作成。

## 7-2. VSCode で `Remote-WSL` で `YOUR_FOLDER` を開こう

1. VSCode を立ち上げる。
2. `フォルダを開く` を押し、フォルダ `YOUR_FOLDER` を選択して開く。
3. VSCode の下リボンの一番左にある、ルーン文字感の漂う ${}_>{}^<$ マークを押し、`Reopen Folder in WSL` を選択。

# 8. 四則演算

「整数・小数の四則計算 (+ - \* \*\* / // %) (int float)」をしてみましょう。

| 演算子 | 機能               | 実際の使い方     |
| ------ | ------------------ | ---------------- |
| +      | 加算               | print(1 + 2)     |
| -      | 減算               | print(2 - 1)     |
| \*     | 乗算               | print(2 \* 3)    |
| \*\*   | 累乗               | print(6 \*\* 10) |
| /      | 除算               | print(2 / 3)     |
| //     | 除算の商、切り捨て | print(31 // 7)   |
| %      | 除算の余り         | print(31 % 7)    |

main.py に以下を記載。

```py
print(1 + 2)  # 3
print(2 - 1)  # 1
print(2 * 3)  # 6
print(6 ** 10)  # 60466176
print(2 / 3)  #  0.6666666666666666
print(31 // 7)  # 4
print(31 % 7)  # 3
```
下記コマンドで main.py を実行可能です。
```sh
# VSCode 付属のターミナルにて以下を実行。
$ python3 main.py
```

# 9. VSCode に拡張機能を入れよう

- LOCAL に入れるべき
  - `Japanese Language Pack for Visual Studio Code`
  - `Remote - Containers`
- WSL:Ubuntu-20.04 に入れるべき
  - `Python`  
    `Pylance` (Linter) が入っています。
  - `Python Indent`  
    .py ファイルを綺麗にインデントできます。
  - `Highlight Trailing White Spaces`

# 10. AtCoder 入門
## 10-1. AtCoder に登録してみよう

AtCoder は毎週土曜 21:00-22:40 に競技プログラミングのコンテストを行っているサイトです。
(競技プログラミングとは何かについて知りたい方は、[競プロのすすめ](https://ch-random.net/post/246/) を参照してください。)

1. [AtCoder の Register ページ](https://atcoder.jp/register) から新規登録してください。
2. また、AtCoder 上の問題一覧を見れるサイト、[AtCoder Problems](https://kenkoooo.com/atcoder/#/table/) (ちなみに fanmade のサイトです) をブックマークしておきましょう。

## 10-2. AtCoder Easy Test を導入してみよう

[AtCoder Easy Test を支える技術](https://qiita.com/magurofly/items/4b60dc02283e70230f71) を参考に。

## 10-3. 課題 0 を AC してみよう

コピペ AC してみましょう。

```py
a = int(input())
b, c = map(int, input().split())
s = input()
print(a + b + c, s)
```

# 11. (発展) 各種 VSCode の機能の紹介
## 11-1. 設定を弄ってみよう

設定ファイル `settings.json` に到達する手順は以下の通りです。

1. `左リボンの一番下にある歯車アイコン` > `設定` を押すと設定が開きます。  
   (ちなみに、コマンド `ctrl + ,` でも設定画面が開くことができます。)
2. 右上の小さなアイコン群のうち、ホバーで見れるテキストが `設定 (JSON) を開く` のアイコンを押すと到達できます。

- [よもぎの settings.json](https://github.com/moyomogi/python_2022_md/tree/master/jsons)  
  良ければコピペしてください！　元々何か書かれていた場合は、元の状態に戻したくなるかもしれないので、元データを他の場所に一時退避しておいてください。

## 11-2. スニペットを使ってみよう

python スニペットファイル `python.json` に到達する手順は以下の通りです。

1. `左リボンの一番下にある歯車アイコン` > `ユーザースニペット` を押すと VSCode 内部にウィンドウが開きます。
2. `python.json (Python)` を選択すると到達できます。

- [よもぎの python.json](https://github.com/moyomogi/python_2022_md/tree/master/jsons)  
  良ければコピペしてください！

## 11-3. (超発展) マルチカーソルを使ってみよう

Home/End キー (行頭/行末に移動) 程度で満足してはなりません。マルチカーソルを使うと、同時に複数個所の編集が可能です。  
詳しくは、[VSCode のマルチカーソル練習帳](https://qiita.com/TomK/items/3b1f5be07d708d7bd6c5) が実際の編集映像付きで分かりやすいので読んでみてください。

# 12. 補遺

- 大学のプログラミングの授業では C 言語が使われるはずなので、C とその後継である C++ を実行できる環境も構築しています。
- 他人のコードを読むことがプログラミング学習に最適な手段です。すなわち、プログラミングを効率よく学ぶには、AtCoder などにて他人のコードを日常的に見ることが必要です。(再掲)
- なお、課題は [AtCoder に登録したら次にやること ～ これだけ解けば十分闘える！過去問精選 10 問 ～](https://qiita.com/drken/items/fd4e5e3630d0f5859067) を用います。(再掲)

# 課題

- (0) [PracticeA - Welcome to AtCoder](https://atcoder.jp/contests/abs/tasks/practice_1)

# 課題の解答

- (0) 掲載済みのため略。

# 次回 (第 2 回) へのリンク

{{< post 439 >}}
