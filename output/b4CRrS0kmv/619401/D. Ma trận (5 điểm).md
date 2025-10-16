# D. Ma trận (5 điểm)

## 📖 Problem

Cho một hình chữ nhật có kích thước
$N×M$
gồm
$N$
hàng và
$M$
cột được chia thành các ô vuông con. Các hàng được đánh số từ
$1$
đến
$N$
từ trên xuống dưới. Các cột được đánh số từ
$1$
đến
$M$
từ trái qua phải. Ô
$(i,j)$
được định nghĩa là ô vuông giao giữa hàng thứ
$i$
, cột thứ
$j$
với
$1 ≤i≤N$
,
$1 ≤j≤M$
.
Tuấn xuất phát tại một ô bất kì trên dòng 1. Mỗi bước đi, Tuấn chỉ có thể di chuyển từ ô hiện tại sang ô
liền kề bên phải
hoặc ô
liền kề bên trái
, hoặc
ô liền kề phía dưới
, và
không được phép quay lại một ô đã đi qua
. Giá trị của một tuyến đường bằng tổng các ô nằm trên đường đi đó.
Yêu cầu:
Tìm giá trị lớn nhất của đường đi xuất phát tại một ô nào đó trên dòng 1 và kết thúc tại một ô nào đó ở dòng
$N$
.


## 🧩 Input

Input
Dòng đầu tiên chứa 2 số nguyên
$N,M$
$(1 ≤N,M≤ 105)$
.
Dòng thứ
$i$
trong
$N$
dòng tiếp theo chứa
$M$
số nguyên
$ai1,ai2, ...,aiM$
$(|aij| ≤ 109)$
.


## 💡 Output

Output
Gồm một dòng ghi một số nguyên là giá trị đường đi lớn nhất tìm được


## 🧠 Example

### Input

```text
3 3
1 -6 3
4 7 -6
1 10 2
```

### Output

```text
24
```


