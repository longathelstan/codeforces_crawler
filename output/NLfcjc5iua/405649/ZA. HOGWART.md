# ZA. HOGWART

## 📖 Problem

Cho một ma trận $$$n.m$$$, mỗi ô trong ma trận có thể là $$$1$$$ trong $$$3$$$ trường hợp sau:
$$$'.'$$$ nếu trống.
$$$'\#'$$$ nếu bị chặn.
$$$'@'$$$ nếu không thể bị chặn.
Chi phí để chặn $$$1$$$ ô $$$.$$$ là $$$1$$$, bạn hãy tìm cách chặn có chi phí thấp nhất sao cho không có đường đi từ $$$(1,1)$$$ tới ô $$$(n,m)$$$. In ra $$$-1$$$ nếu không có cách chặn nào.


## 🧩 Input

Input
Bài toán gồm nhiều testcase
$$$2$$$ số đầu của testcase là $$$n$$$,$$$m$$$. Nếu $$$n$$$ và $$$m$$$ là $$$0$$$ thì ngưng chương trình $$$(1\leq n.m\leq 10^6)$$$
$$$n$$$ dòng tiếp theo mỗi dòng gồm $$$m$$$ ký tự dính liền, ký tự thứ $$$i$$$ có thể là $$$1$$$ trong $$$3$$$ trường hợp sau
$$$'.'$$$ nếu trống.
$$$'\#'$$$ nếu bị chặn.
$$$'@'$$$ nếu không thể bị chặn.
Tổng của $$$r.c$$$ ở các testcase $$$\leq$$$ 10^6


## 💡 Output

Output
$$$1$$$ số duy nhất là chi phí ít nhất cần tìm


## 🧠 Example

### Input

```text
4 4
@..#
....
....
#..@
4 4
@..#
..#.
.#..
#..@
0 0
```

### Output

```text
2
0
```


