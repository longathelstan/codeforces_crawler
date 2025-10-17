# S. Chênh lệch

## 📖 Problem

Cho một dãy số gồm
$n$
số nguyên dương
$a1,a2, ...,an$
. Bạn có
$q$
truy vấn, với mỗi truy vấn gồm một cặp số
$(u,v)$
bạn hãy tìm độ chênh lệch bé nhất khi chia đoạn con
$[au..av]$
thành hai phần.
Ví dụ dãy
$a$
:
$3$
$1$
$4$
$2$
$5$
, và
$(u,v)$
=
$(2, 5)$
bạn cần tìm chênh lệch nhỏ nhất khi chia đoạn này ra hai phần. Có các cách chia sau: (1) và (4,2,5); (1,4) và (2,5); (1,4,2) và (5); (1,4,2,5) và (); Khi đó chênh lệch bé nhất là 2 – Tương ứng với cặp (1,4) (2,5).


## 🧩 Input

Input
Dòng đầu tiên là hai số nguyên dương
$n$
,
$q$
$(1≤n,q≤105)$
Dòng tiếp theo là
$n$
số nguyên dương trong dãy
$a$
$(ai≤109)$
$q$
dòng tiếp theo mỗi dòng là
$2$
số nguyên dương
$(u,v)$
$(1 ≤u≤v≤n)$
. Mỗi cặp số là một truy vấn cần bạn trả lời.


## 💡 Output

Output
Gồm
$q$
dòng, dòng thứ
$i$
là giá trị chênh lệch nhỏ nhất tìm được ứng với truy vấn
$i$
.


## 🧠 Example

### Input

```text
5 1
3 1 4 2 5
2 5
```

### Output

```text
2
```


