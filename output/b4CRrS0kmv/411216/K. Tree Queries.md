# K. Tree Queries

## 📖 Problem

Cho cái cây
$n$
đỉnh với gốc là
$1$
. Mỗi đỉnh có màu là
$ci$
, bạn cần trả lời
$m$
truy vấn:
*
$v$
$k$
: đếm số màu
$x$
thỏa số lần xuất hiện của màu
$x$
$≥k$
trong cây con gốc
$v$
.


## 🧩 Input

Input
Dòng đầu tiên gồm
$2$
số
$n$
,
$m$
là số đỉnh của cây và số lượng truy vấn
$(1 ≤n,q≤ 105)$
.
Dòng tiếp theo gồm
$n$
số nguyên dương
$ci$
là màu của đỉnh
$i$
$(1 ≤ci≤ 105)$
$n- 1$
dòng tiếp theo mỗi dòng gồm cạnh vô hướng nối
$ui$
và
$vi$
$(1 ≤ui,vi≤n)$
$m$
dòng tiếp theo gồm
$vi$
và
$ki$
thể hiện truy vấn thứ
$i$
$(1 ≤vi≤n, 1 ≤k≤ 105)$


## 💡 Output

Output
Gồm
$m$
dòng là đáp án ứng với
$m$
truy vấn


## 🧠 Example

### Input

```text
8 5
1 2 2 3 3 2 3 3
1 2
1 5
2 3
2 4
5 6
5 7
5 8
1 2
1 3
1 4
2 3
5 3
```

### Output

```text
2
2
1
0
1
```


