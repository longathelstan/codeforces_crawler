# ZC. 2DA

## 📖 Problem

Cho ma trận
$a$
kích thước
$n$
x
$m$
, bạn có
$q$
truy vấn, mỗi truy vấn có dạng
*
$x1$
,
$y1$
,
$x2$
,
$y2$
,
$val$
: Bạn cần phải cập nhật các giá trị của hình chữ nhật có góc trái trên
$(x1,y1)$
và có phải dưới
$(x2,y2)$
trong ma trận
$a$
thêm
$val$
đơn vị
Hãy in ra ma trận
$a$
cuối cùng sau khi thực hiện
$q$
truy vấn.


## 🧩 Input

Input
Dòng đầu tiên gồm
$n$
,
$m$
,
$q$
lần lượt là số dòng, số cột, số truy vấn
$(1 ≤n,m≤ 500)$
$(1 ≤q≤ 106)$
$n$
dòng tiếp theo mỗi dòng gồm
$m$
số mô tả giá trị của
$ai,j$
$( - 109≤ai,j≤ 109)$
$q$
dòng tiếp theo gồm
$x1$
,
$y1$
,
$x2$
,
$y2$
,
$val$
$(1 ≤x1 ≤x2 ≤n)$
$(1 ≤y1 ≤y2 ≤m)$
$( - 109≤val≤ 109)$


## 💡 Output

Output
Ma trận
$a$
sau khi thực hiện
$q$
truy vấn.


## 🧠 Example

### Input

```text
5 5 3
1 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
2 2 4 4 5
1 1 2 2 10
1 1 5 5 1
```

### Output

```text
12 11 1 1 1 
11 16 6 6 1 
1 6 6 6 1 
1 6 6 6 1 
1 1 1 1 1
```


