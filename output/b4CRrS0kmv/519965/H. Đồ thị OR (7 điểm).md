# H. Đồ thị OR (7 điểm)

## 📖 Problem

Cho đồ thị vô hướng có
$n$
đỉnh và
$m$
cạnh, các đỉnh được đánh số từ 1 đến
$n$
. Trên mỗi cạnh được gán một số nguyên không âm là trọng số của cạnh đó. Trọng số của một đường đi được tính bằng phép toán OR.
Nói cách khác, một đường đi qua các cạnh có trọng số lần lượt là
$m1,m2, …,mk$
thì trọng số của đường đi này là
$m1$
OR
$m2$
OR ... OR
$mk$
Cho đồ thị và
$2$
đỉnh
$s$
,
$t$
, hãy tìm đường đi có trọng số nhỏ nhất từ
$s$
đến
$t$
, nếu không tìm được đường đi thì in
$- 1$
.


## 🧩 Input

Input
Dòng đầu tiên ghi 2 số nguyên
$n$
,
$m$
$(1 ≤n≤ 1000, 1 ≤m≤ 10000)$
$m$
dòng tiếp theo, mỗi dòng ghi
$3$
số nguyên
$u$
,
$v$
,
$c$
$(1 ≤u,v≤n, 1 ≤c≤ 1024)$
thể hiện có cạnh nối từ
$u$
tới
$v$
với trọng số là
$c$
.
Dòng cuối cùng ghi
$2$
số nguyên
$s,t$
$(1≤s,t≤n;s≠t)$


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án bài toán


## 🧠 Example

### Input

```text
3 4
1 2 1
1 2 1000
2 3 3
1 3 100
1 3
```

### Output

```text
3
```


