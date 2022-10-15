### [ABC202 - A](https://atcoder.jp/contests/abc202/tasks/abc202_a)

ある面とその反対側の面が表す整数を足すと7になるという性質を持つ。
そのことを利用すると良い。

``` python
a, b, c = map(int, input().split())
print(21 - (a + b + c))
```

が最も記述量が少なく最適と考えられる。

[提出](https://atcoder.jp/contests/abc202/submissions/35457723)

2022-10-15
            