# I. Tô màu 4

## 📖 Problem

Cho một cái cây
$n$
đỉnh,
$n- 1$
cạnh và có gốc là
$1$
, đỉnh thứ
$i$
sẽ có màu là
$ci$
.
Bạn được yêu cầu
$q$
truy vấn, truy vấn thứ
$i$
gồm
$2$
số
$vi$
và
$ki$
bạn phải đưa ra số lượng màu
$x$
trong cây con gốc
$vi$
sao màu
$x$
xuất hiện ít nhất
$ki$
lần.
Yêu cầu:
Hãy đưa ra đáp án của
$q$
truy vấn.


## 🧩 Input

Input
Dòng đầu tiên gồm số nguyên dương
$n$
và
$q$
$(1 ≤n,q≤ 5 * 105)$
.
Sau đó là
$n$
dòng, dòng thứ
$i$
là màu
$ci$
của đỉnh
$i$
$(1 ≤ci≤n)$
$n- 1$
dòng tiếp theo, mỗi dòng là số nguyên dương
$u,v$
$(1 ≤u,v≤n)$
là cạnh nối giữa
$u$
và
$v$
.
$q$
dòng tiếp theo, dòng thứ
$i$
gồm
$2$
số
$vi$
và
$ki$
$(1 ≤vi,ki≤n)$


## 💡 Output

Output
Gồm
$q$
dòng ứng với
$q$
truy vấn cần tìm


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


