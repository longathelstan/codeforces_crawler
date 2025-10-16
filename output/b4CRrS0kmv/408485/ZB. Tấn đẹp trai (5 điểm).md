# ZB. Tấn đẹp trai (5 điểm)

## 📖 Problem

Cho đồ thị có hướng
$n$
đỉnh,
$m$
cạnh, cạnh thứ
$i$
nối giữa
$2$
đỉnh
$ui$
và
$vi$
với trọng số là
$wi$
. Bạn muốn đi đường đi ngắn nhất từ đỉnh
$1$
tới đỉnh
$2$
.
Với mỗi cạnh thứ
$i$
hãy đưa ra:
*
TAN: Nếu đảo hướng cạnh thứ
$i$
giúp đường đi ngắn nhất từ
$1$
tới
$2$
ngắn hơn so với ban đầu
*
DEP: Nếu đảo hướng cạnh thứ
$i$
giúp đường đi ngắn nhất từ
$1$
tới
$2$
không thay đổi so với ban đầu
*
TRAI: Nếu đảo hướng cạnh thứ
$i$
làm đường đi ngắn nhất từ
$1$
tới
$2$
xa hơn so với ban đầu hoặc làm cho việc đi từ
$1$
tới
$2$
không còn khả thi.


## 🧩 Input

Input
Dòng đầu gồm
$n$
và
$m$
$(1 ≤n≤ 105, 1 ≤m≤ 5 * 105)$
$m$
dòng tiếp theo, mỗi dòng gồm
$3$
số
$ui$
,
$vi$
và
$wi$
$(1 ≤ui,vi≤n,ui≠vi, 1 ≤wi≤ 105)$
Dữ liệu đảm bảo luôn tồn tại ít nhất một đường đi từ
$1$
tới
$2$
trong đồ thị ban đầu


## 💡 Output

Output
Gồm
$m$
dòng chứa đáp án cần tìm


## 🧠 Example

### Input

```text
4 5
1 3 5
3 4 6
4 2 7
2 1 18
2 3 12
```

### Output

```text
TRAI
TRAI
TRAI
DEP
TAN
```


