# AtCoder Recode by N257cc8ae
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
