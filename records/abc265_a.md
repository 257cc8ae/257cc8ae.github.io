### [ABC265 - A](https://atcoder.jp/contests/abc265/tasks/abc265_a)

#### 指針
x * n・・・一個ずつ買った場合

y * (n // 3) + x * (n % 3)・・・三個セットとあまりは一個ずつ

の２つの場合がある。なので、２つとも計算して、大きい方を出力する。
その際に
```python
min(A,B)
```
上記のように```min``` 関数を用いると良い。
```min``` 関数ではAとBの比較し、小さい方を返す。

**関連**

```max``` 関数を使うとAとBを比較したときの大きい方の値を返す

[提出](https://atcoder.jp/contests/abc265/submissions/35698554)

2022-10-15
            