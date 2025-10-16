# ZB. 2DQ

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
: Bạn cần phải tính tổng các phần tử nằm trong hình chữ nhật có góc trái trên
$(x1,y1)$
và có phải dưới
$(x2,y2)$
.
Hãy in ra câu trả lời cho
$q$
truy vấn


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
$(1 ≤q≤ 105)$
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
$(1 ≤x1 ≤x2 ≤n)$
$(1 ≤y1 ≤y2 ≤m)$


## 💡 Output

Output
$q$
dòng cho
$q$
truy vấn


## 🧠 Example

### Input

```text
5 5 2
1 1 1 1 1
1 1 1 1 2
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
2 2 4 4
1 1 5 5
```

### Output

```text
9
26
```


