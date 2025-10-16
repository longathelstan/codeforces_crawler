# ZA. Cấp số cộng 2 (5 điểm)

## 📖 Problem

Cho mảng
$a$
gồm
$n$
phần tử và
$q$
truy vấn, mỗi truy vấn có dạng
$l$
$r$
$x$
, bạn phải cập nhật
$al$
tăng thêm
$x$
,
$al+ 1$
tăng thêm
$x+ 1$
, ...,
$ar$
tăng thêm
$x+r-l$
.
Hãy in ra mảng
$a$
sau khi thực hiện
$q$
truy vấn.


## 🧩 Input

Input
Dòng đầu gồm
$n$
$(1 ≤n≤ 106)$
Dòng thứ hai gồm
$n$
số
$a1,a2, ...,an$
$(1 ≤ai≤ 109)$
Dòng tiếp theo gồm
$q$
$(1 ≤q≤ 106)$
$q$
dòng tiếp theo mỗi dòng gồm
$3$
số
$l$
,
$r$
và
$x$
$(1 ≤l≤r≤n, 1 ≤x≤ 109)$


## 💡 Output

Output
Gồm một dòng chứa
$n$
số trong mảng
$a$
sau khi cập nhật
$q$
truy vấn, các số cách nhau bởi dấu cách.


## 🧠 Example

### Input

```text
5
0 0 0 0 1
2
2 4 2
1 5 3
```

### Output

```text
3 6 8 10 8
```


