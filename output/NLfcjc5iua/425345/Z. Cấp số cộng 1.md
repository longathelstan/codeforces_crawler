# Z. Cấp số cộng 1

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
, bạn phải cập nhật
$al$
tăng thêm
$1$
,
$al+ 1$
tăng thêm
$2$
, ...,
$ar$
tăng thêm
$(r-l+ 1)$
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
$2$
số
$l$
và
$r$
$(1 ≤l≤r≤n)$


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
1 2 1 2 1
2
2 4
1 5
```

### Output

```text
2 5 6 9 6
```


