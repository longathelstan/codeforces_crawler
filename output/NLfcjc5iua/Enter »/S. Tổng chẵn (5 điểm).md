# S. Tổng chẵn (5 điểm)

## 📖 Problem

Trên giá sách của thư viện trường THPT chuyên Phan Bội Châu có
$N$
quyển sách được đánh số thứ tự
$1, 2, ...,N$
. Mỗi quyển sách có số lượng trang tương ứng
$a1,a2, ...,an$
.
Yêu cầu: Tính số lượng tất cả các sách để có thể lấy
$2$
quyển sách trong số
$N$
quyển sách, sao cho tổng số lượng trang sách trong
$N- 2$
quyển sách còn lại trên giá là một số chẵn.


## 🧩 Input

Input
Dòng thứ nhất chứa số nguyen
$N$
$(2 <N≤ 106)$
.
Dòng thứ hai chứa
$N$
số nguyên
$a1,a2, ...,an$
$(ai≤ 104, 1 ≤i≤N)$
các số cách nhau ít nhất một dấu cách trống.


## 💡 Output

Output
Gồm một dòng duy nhất chứa một số nguyên là số cách có thể chọn.


## 🧠 Example

### Input

```text
5
36 58 27 64 75
```

### Output

```text
4
```



## 📝 Note

Note
Giải thích:
Có
$4$
cách chọn là
Cách
$1$
: Lấy quyển
$1$
và quyển
$2$
thì tổng số trang sách của các quyển còn lại là
$27 + 64 + 75 = 166$
là số chẵn
Cách
$2$
: Lấy quyển
$1$
và quyển
$4$
thì tổng số trang sách của các quyển còn lại là
$58 + 27 + 75 = 160$
là số chẵn
Cách
$3$
: Lấy quyển
$2$
và quyển
$4$
thì tổng số trang sách của các quyển còn lại là
$36 + 27 + 75 = 138$
là số chẵn
Cách
$4$
: Lấy quyển
$3$
và quyển
$5$
thì tổng số trang sách của các quyển còn lại là
$36 + 58 + 64 = 158$
là số chẵn

