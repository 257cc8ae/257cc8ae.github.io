俺氏（Twitter:@257cc8ae, AtCoder:N257cc8ae)の競技プログラミング精進記録

## [ABC202 B - Everyone is Friends](https://atcoder.jp/contests/abc272/tasks/abc272_b)
［指針］
すべての組み合わせを作って、その2つの要素が各舞踏会に含まれているかを確認すると良い。
なお、組み合わせの生成にはintertoolsのcombination関数を用いるのが適切と考えられる。

[提出](https://atcoder.jp/contests/abc272/submissions/35532197)

2022-10-09

## [ABC202 A - 484558](`https://atcoder.jp/contests/abc271/tasks/abc271_a)
ある面とその反対側の面が表す整数を足すと7になるという性質を持つ。
そのことを利用すると良い。

``` python
a, b, c = map(int, input().split())
print(21 - (a + b + c))
```

が最も記述量が少なく最適と考えられる。

[公式の解説](https://atcoder.jp/contests/abc202/editorial/1857)

2022-10-08