# J. Alyona

## 📖 Problem

Tấn có
$1$
cái cây
$n$
đỉnh với gốc là
$1$
. Mỗi đỉnh có
$1$
số nguyên dương viết trên chúng, đỉnh thứ
$i$
được viết số nguyên dương
$ai$
. Hơn thế nữa, mỗi cạnh của đồ thị đều có trọng số, cạnh thứ
$i$
có trọng số nguyên dương
$wi$
.
Định nghĩa
$dist(v,u)$
là tổng trọng số của các cạnh trên đường đi từ
$v$
->
$u$
.
Đỉnh
$v$
được gọi là kiểm soát đỉnh
$u$
nếu
$u$
nằm trong cây con gốc
$v$
và
$dist(v,u) ≤au$
Tấn muốn biết với mỗi đỉnh
$v$
có bao nhiêu đỉnh
$u$
sao cho
$v$
kiểm soát
$u$
.


## 🧩 Input

Input
Dòng đầu tiên gồm số nguyên dương
$n$
$(1 ≤n≤ 2.105)$
Dòng tiếp theo gồm
$n$
số
$a1,a2, ...,an$
$(1 ≤ai≤ 109)$
$n- 1$
dòng tiếp theo, dòng thứ
$i$
chứa
$3$
số nguyên dương
$ui,vi,pi$
thể hiện có cạnh nối giữa
$2$
đỉnh
$ui$
và
$vi$
với trọng số
$wi$
.
$(1 ≤ui,vi≤n, 1 ≤wi≤ 109)$


## 💡 Output

Output
In ra
$1$
dòng chứa
$n$
số, số thứ
$i$
là đáp án cần tìm của đỉnh
$i$
, các số cách nhau bởi dấu " ".


## 🧠 Example

### Input

```text
5
2 5 1 4 6
1 2 7
1 3 1
3 4 5
3 5 6
```

### Output

```text
1 0 1 0 0
```



## 📝 Note

Note
Ví dụ đầu, đỉnh
$1$
kiểm soát đỉnh
$3$
, đỉnh
$3$
kiểm soát đỉnh
$5$
.

