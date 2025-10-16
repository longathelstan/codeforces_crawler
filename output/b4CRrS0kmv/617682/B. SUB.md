# B. SUB

## 📖 Problem

Cho cái cây
$n$
đỉnh với gốc là đỉnh
$1$
, bạn có
$q$
truy vấn:
*
$1$
$x$
$val$
: cập nhật subtree với gốc là
$x$
lên
$val$
đơn vị
*
$2$
$x$
: tính nút có giá trị lớn nhất của subtree với gốc là
$x$
.
Yêu cầu: Với mỗi truy vân loại
$2$
$x$
hãy in ra nút có giá trị lớn nhất của subtree với gốc là
$x$
.


## 🧩 Input

Input
Dòng đầu tiên gồm số
$n$
là số đỉnh của cây
$(1 ≤n≤ 2.105)$
$n- 1$
dòng tiếp theo mỗi dòng gồm cạnh vô hướng nối
$ui$
và
$vi$
$(1 ≤ui,vi≤n)$
Dòng tiếp theo là số truy vấn
$q$
$(1 ≤q≤ 2.105)$
$q$
dòng tiếp theo là
$1$
trong
$2$
loại
*
$1$
$x$
$val$
: cập nhật subtree với gốc là
$x$
lên
$val$
đơn vị
$(1 ≤x≤n,  - 109≤val≤ 109)$
*
$2$
$x$
: tính nút có giá trị lớn nhất của subtree với gốc là
$x$
$(1 ≤x≤n)$


## 💡 Output

Output
Với mỗi truy vân loại
$2$
hãy in ra đáp án cần tìm.


## 🧠 Example

### Input

```text
5
1 2
2 3
3 4
3 5
10
1 2 4
2 5
1 3 5
2 5
1 1 5
2 5
1 4 1
2 5
1 5 3
2 5
```

### Output

```text
4
9
14
14
17
```


