# 第 1 回 Python 勉強会 2022 | VSCode インストール、WSL 構築

# 1. 予習事項

- 「2. スクショの取り方」を実際に試してみておいてください。
- 「3. VSCode インストール」をやっておいていただけるとスムーズに進行できます。

# 2. パソコン基礎操作

## 2-1. スクショの取り方

この勉強会に限らないことですが、何か困って質問したい際に、スクショを貼ることで、自分がどういった状況かを質問相手に簡単かつ正確に伝えることができます。なお、discord の画面共有なら、さらに正確に伝えられます。

- Snipping Tool  
  `win + s` で検索窓を出して snipping tool と入力すれば見つかるはずです。
  スクショを .png 形式で保存できます。
- `win + shift + s`  
  スクショ区域を指定して、スクショした画像をクリップボードに送ります。  
  クリップボードに送られた画像は、discord や各種お絵かきソフト (クリスタ、GIMP、イラレ) 上で `ctrl + v` を入力することで貼り付けできます。

## 2-2. キーボードショートカット

| ショートカット | 機能               |
| -------------- | ------------------ |
| ctrl + c       | コピー             |
| ctrl + x       | 切り取り           |
| ctrl + v       | 貼り付け           |
| ctrl + z       | 直前動作の取り消し |
| ctrl + a       | 全選択             |
| ctrl + s       | セーブ             |

# 3. VSCode インストール

Windows 向けの説明しか行いません。すいませんが、Mac ユーザーの方々は各自で環境を構築してください。
まず、[VSCode 公式のダウンロードページ](https://code.visualstudio.com/download) からダウンロードして、インストールしてください。
Vim 派の人もいるかもですが、VSCode に Vim を載せれるらしいので、よければ VSCode をインストールしてください。

# 4A. (任意) WSL を入れよう

ちなみに、WSL は Windows Subsystem for Linux の略です。

## 4A-1. (余談) なぜ WSL が必要か

- Ubuntu には、非公式リポジトリ [PPA](https://launchpad.net/ubuntu/+ppas) があり、自作 CLI ツールを PPA に登録すると、`add-apt-repository` コマンドで、そのリポジトリをマシンに登録できるので、他のユーザーが `apt` コマンドでそのプログラムを使えるようになります。
- 対して Windows では、`apt` に当たるものとして `choco` ([Chocolatey](https://chocolatey.org)) がありますが、GUI ツールばかりで、高性能な CLI ツールがあまりないです。(参考: [Chocolatey Community Repository](https://community.chocolatey.org/packages))

従って、**Ubuntu 上の便利な CLI ツールを使うため**に、WSL が必要です。

## 4A-2. WSL を有効化しよう

本勉強会では Python・C++ を WSL にインストールします。

- Windows 11 の人は、これだけ実行すればいいらしいです。  
  もしダメなら、

```ps1
wsl --install
```

- Windows 10 以前の人は、以下 1. ～ 6. を実行。

1. デフォルトの Windows では、スタートアップ時に WSL が起動しません。  
   以下の A, B いずれかを行い、WSL を有効化します。  
   A. (GUI で有効化) [Windows Subsystem for Linux (WSL1) をインストールしてみよう！](https://qiita.com/Aruneko/items/c79810b0b015bebf30bb) をブラウザ上の別タブで開いてください。  
   B. (CUI で有効化) Windows PowerShell にて、WSL を有効化しましょう。  
   この設定により NoxPlayer などのエミュレーターが動かなくなることがありますが、元の設定に戻せば、また動かせます。

```sh
# Windows PowerShell にて、以下を実行。ただし、先頭の $ は入力しないでください。
# 今回の例でいえば、「Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux」のみを入力して Enter してください。
$ Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

2. WSL を起動させるために、PC を再起動。
3. [以前のバージョンの WSL の手動インストール手順](https://docs.microsoft.com/ja-jp/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package) にて、`手順 4 - Linux カーネル更新プログラム パッケージをダウンロードする` にある `x64 マシン用 WSL2 Linux カーネル更新プログラム パッケージ` をダウンロードし、実行。

4. Microsoft Store で Ubuntu 20.04 LTS を入れる (「ubuntu」で検索すると、出てきます)。
   - LTS (Long Time Support, 長期サポート) は「安定版」の意です。
   - 2022-04-21 リリースの Ubuntu 22.04 もありますが、設定が面倒なので、ここでは古いバージョンである Ubuntu 20.04 をインストールします。
5. Ubuntu 20.04 LTS を起動。  
   以下のように、username と password を設定するように促されるので、それに従って入力。

```sh
Installing, this may take a few minutes...
Please create a default UNIX user account. The username does not need to match your Windows username.
For more information visit: https://aka.ms/wslusers
# YOUR_USERNAME は自由に決めたものに読み替えてください。
# 先述しましたが、入力が終わったら Enter を押しましょう。
# (ただし、a-z, 0-9 のみで構成するといいと思います。)
Enter new UNIX username: YOUR_USERNAME
# 以降の行において、YOUR_USERNAME は自分で決めてください。
# ここで設定したパスワードは、以降で使うので覚えておくように。
New password: YOUR_PASSWORD
# 上の行で入力した YOUR_PASSWORD と全く同じものを入力。
Retype new password: YOUR_PASSWORD
```

6. Ubuntu 20.04 LTS にて以下を実行。

```sh
# コマンドの先頭に sudo (superuser do; スードゥー) を付けると、ルート権限でコマンドを実行できます。
# なお、なにも表示されないです。
$ sudo sed -i -e 's%http://.*.ubuntu.com%http://ftp.jaist.ac.jp/pub/Linux%g' /etc/apt/sources.list
```

```sh
# 「インストール可能なコマンドの一覧」を更新する。
# 実際のコマンドのインストールは行わない。
# sudo apt -y upgrade をしないと何も起こらない。
$ sudo apt update
# 「インストール可能なコマンドの一覧」を参照し、
# - 既インストールで新バージョンが
#   公開されてたらアップグレード。
# - 未インストールならインストール。
# 事前に sudo apt update をする必要がある。
$ sudo apt -y upgrade
```

```sh
# コマンド add-apt-repository の入っている
# software-properties-common をインストール。
$ sudo apt install -y software-properties-common
$ sudo add-apt-repository universe

# build-essential, gdb: C++ 向け
# python3, flake8: Python 向け
# pkg-config:
#   これがないとバグるツールが結構あるので
#   まとめてインストールしておきましょう。
$ sudo apt install -y build-essential gdb python3 flake8 pkg-config
```

```sh
$ sudo apt update
$ sudo apt install -y python3-pip
# Linter の autopep8 をインストール
$ sudo pip install autopep8
# Formatter の black をインストール
$ sudo pip3 install black

# (参考) インストール済みパッケージのアップグレードを行うには、
# --upgrade あるいは -U を付けます。
# $ sudo pip install --upgrade autopep8
# $ sudo pip3 install --upgrade black
```

# 4A-3. (余談) プログラミング用フォルダは `~` 下に置くといいよ、という話

(「WSL を有効化しよう」をやってくださった方向けです。)  
WSL を入れ終わった方は、エクスプローラーを開き、パンくずリストが書かれた窓に `\\wsl$\Ubuntu-20.04\home` と打って Enter を押してください。
`YOUR_NAME` (YOUR_NAME は自分の入力した名前) というフォルダがあるはずです。
(以下、`\\wsl$\Ubuntu-20.04\home\YOUR_NAME` を `~` と略記します。)  
実は、`Remote-WSL` (VSCode の拡張機能) を使う場合は、 `C:\` や `D:\` に作業フォルダを置くより、`~` 以下に作業フォルダを置いた方が、Windows と Ubuntu 間のシステムのやり取りがないため、ファイル読み書きの動作が速いです。  
具体的に書くと、 `~/compro` というフォルダを `Remote-WSL` で開くと、比較的ファイル読み書きの動作が軽い、ということです。  
ちなみに、compro というのは競プロ (Competitive Programming) の意です。

- 参考資料 [WSL2 で Git などのファイル操作が重い問題を解決した方法](https://www.orzs.tech/how-to-solve-the-problem-that-file-operations-such-as-git-are-heavy-with-wsl2/)

# 4A-4. `cd`, `ls` コマンドを知っておこう

Ubuntu を使うにあたって必須のコマンドが `cd`, `ls` コマンドです。機能は下表の通りです。  
(下表で、「ディレクトリ」は「フォルダ」と同義です。)

| コマンド名 | コマンド名の由来 | 機能                                         | 使い方                   |
| ---------- | ---------------- | -------------------------------------------- | ------------------------ |
| cd         | change directory | カレントディレクトリの変更                   | `cd PATH/TO/YOUR/FOLDER` |
| ls         | list segments    | カレントディレクトリ配下のファイル一覧を表示 | `ls`                     |

1. `cd` の引数 (ひきすう) に絶対パスを指定して移動  
   絶対パスとは、Windows のエクスプローラーのパンくずリストの窓をクリックした時に現れるパスです。

```sh
# WSL 20.04 LTS にて以下を実行。
$ cd ~  # フォルダ ~ に移動
# ls に対する出力と、エクスプローラーで開いた
# \\wsl$\Ubuntu-20.04\home\YOUR_NAME に見えているフォルダ内とを見比べて、
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

# 4B. WSL なしで VSCode 上に Python 環境を構築

1. [Download Python](https://www.python.org/downloads/) にて Python 3.10.4 をダウンロードし、インストール。
2. VSCode の左のタブにて、Python をインストール。

# 5. 勉強会用フォルダにて各種準備をしよう

## 5-1. py ファイルを準備しよう

1. `D:\YOUR_FOLDER` や `~/YOUR_FOLDER` のいずれかの場所に、勉強会用フォルダを作成してください。(以下、このフォルダを `YOUR_FOLDER` として統一して言及する。)
2. エクスプローラー上で `YOUR_FOLDER/main.py` (ファイル名 (つまり `main` の部分) は自由でいいです) を作成。

## 5-2. (WSL を入れた人用) VSCode で `Remote-WSL` で `YOUR_FOLDER` を開こう

1. VSCode を立ち上げる。
2. `フォルダを開く` を押し、フォルダ `YOUR_FOLDER` を選択して開く。
3. VSCode の下リボンの一番左にある、ルーン文字感の漂う「 ${}_>{}^<$ 」マークを押し、`Reopen Folder in WSL` を選択。

# 6. 四則演算

「整数・小数の四則計算 (+ - \* \*\* / // %) (int float)」をしてみましょう。

| 演算子 | 機能                      | 実際の使い方     |
| ------ | ------------------------- | ---------------- |
| +      | 加算                      | print(1 + 2)     |
| -      | 減算                      | print(2 - 1)     |
| \*     | 乗算                      | print(2 \* 3)    |
| \*\*   | 累乗                      | print(6 \*\* 10) |
| /      | 除算                      | print(2 / 3)     |
| //     | 除算の商 (つまり切り捨て) | print(31 // 7)   |
| %      | 除算の余り                | print(31 % 7)    |

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

# 7. VSCode に拡張機能を入れよう

- LOCAL に入れるべき
  - `Japanese Language Pack for Visual Studio Code`  
    日本語化。
  - `Remote - Containers`
  - `Code Runner`  
    Python や C++ のファイルの実行を手軽に行えます。
- WSL:Ubuntu-20.04 に入れるべき  
  (WSL 入れなかった人は LOCAL に入れて下さい)
  - `Python`
  - `C/C++`  
    C++ 言語使うなら。
  - `Highlight Trailing White Spaces`

# 8. AtCoder 入門

## 8-1. AtCoder に登録してみよう

AtCoder は毎週土曜 21:00-22:40 に競技プログラミングのコンテストを行っているサイトです。
(競技プログラミングとは何かについて知りたい方は、[競プロのすすめ](https://ch-random.net/post/246/) を参照してください。)

1. [AtCoder の Register ページ](https://atcoder.jp/register) から新規登録してください。
2. また、AtCoder 上の問題一覧を見れるサイト、[AtCoder Problems](https://kenkoooo.com/atcoder/#/table/) (ちなみに fanmade のサイトです) をブックマークしておきましょう。

## 8-2. AtCoder Easy Test を導入してみよう

[AtCoder Easy Test を支える技術](https://qiita.com/magurofly/items/4b60dc02283e70230f71) を参考に。

## 8-3. 課題 0 を AC してみよう

コピペ AC してみましょう。

```py
a = int(input())
b, c = map(int, input().split())
s = input()
print(a + b + c, s)
```

# 9. (発展) 各種 VSCode の機能の紹介

## 9-1. 設定を弄ってみよう

設定ファイル `settings.json` に到達する手順は以下の通りです。

1. `左リボンの一番下にある歯車アイコン` > `設定` を押すと設定が開きます。  
   (ちなみに、コマンド `ctrl + ,` でも設定画面が開くことができます。)
2. 右上の小さなアイコン群のうち、ホバーで見れるテキストが `設定 (JSON) を開く` のアイコンを押すと到達できます。

- [よもぎの settings.json](https://github.com/moyomogi/python_2022_md/tree/master/jsons)  
  良ければコピペしてください！　元々何か書かれていた場合は、元の状態に戻したくなるかもしれないので、元データを他の場所に一時退避しておいてください。

## 9-2. スニペットを使ってみよう

python スニペットファイル `python.json` に到達する手順は以下の通りです。

1. `左リボンの一番下にある歯車アイコン` > `ユーザースニペット` を押すと VSCode 内部にウィンドウが開きます。
2. `python.json (Python)` を選択すると到達できます。

- [よもぎの python.json](https://github.com/moyomogi/python_2022_md/tree/master/jsons)  
  良ければコピペしてください！

## 9-3. (超発展) マルチカーソルを使ってみよう

Home/End キー (行頭/行末に移動) 程度で満足してはなりません。マルチカーソルを使うと、同時に複数個所の編集が可能です。  
詳しくは、[VSCode のマルチカーソル練習帳](https://qiita.com/TomK/items/3b1f5be07d708d7bd6c5) が実際の編集映像付きで分かりやすいので読んでみてください。

# 10. 補遺

- VSCode のフォントは [RictyDiminished](https://github.com/edihbrandon/RictyDiminished) がお薦めです。`Code` ボタンから `Download ZIP` すると、ttf 形式のフォントが手に入るので、インストール。
- 大学のプログラミングの授業では C 言語が使われるはずなので、C とその後継である C++ を実行できる環境も構築しています。
- 他人のコードを読むことがプログラミング学習に最適な手段です。すなわち、プログラミングを効率よく学ぶには、AtCoder などにて他人のコードを日常的に見ることが必要です。(再掲)

# 課題

- (0) [PracticeA - Welcome to AtCoder](https://atcoder.jp/contests/abs/tasks/practice_1)

# 課題の解答

- (0) 掲載済みのため略。

# 次回 (第 2 回) へのリンク

{{< post 439 >}}
