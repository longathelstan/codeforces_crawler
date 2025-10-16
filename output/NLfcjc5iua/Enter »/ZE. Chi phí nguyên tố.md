# ZE. Chi phí nguyên tố

## 📖 Problem

Cho một hình vuông có kích thước
$n$
$*$
$n$
. Trong một thao tác, bạn được phép chọn một số trong hình vuông và tăng số đó lên
$1$
. Có
$Q$
truy vấn, mỗi truy vấn cho một hình chữ nhật, tìm số lượng thao tác ít nhất cần thực hiện, để toàn bộ số trong hình chữ nhật là số nguyên tố. Các truy vấn là độc lập, không ảnh hưởng đến nhau.


## 🧩 Input

Input
Dòng đầu tiên là số nguyên dương
$n$
$(1 ≤n≤ 1000)$
và số nguyên dương
$q$
$(1 ≤q≤ 106)$
.
Mỗi dòng trong
$n$
dòng tiếp theo, dòng thứ
$i$
chứa
$n$
số nguyên dương số thứ
$j$
là
$Ai,j$
$(1 ≤Ai,j≤ 100)$
.
Mỗi dòng trong
$q$
dòng tiếp theo, là
$4$
số nguyên dương
$a,b,c,d$
.
$(a,b)$
là tọa độ trái trên của hình chữ nhật,
$(c,d)$
là tọa độ phải dưới của hình chữ nhật.


## 💡 Output

Output
Gồm
$q$
dòng mỗi dòng là đáp án cần tìm.


## 🧠 Example

### Input

```text
4 3
1 2 3 4
2 3 2 1
5 3 2 1
3 3 3 3
1 2 2 2
1 1 3 3
2 3 4 4
```

### Output

```text
0
1
2
```


