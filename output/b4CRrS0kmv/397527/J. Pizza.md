# J. Pizza

## 📖 Problem

Tấn muốn mở một số cửa hàng pizza tại một số địa điểm. Bánh pizza sẽ cung cấp cho mọi khách hàng nằm trong hình tròn bán kính
$R$
với tâm là các địa điểm được chọn.
Yêu cầu:
Xác định số khách hàng lớn nhất có thể phục vụ.


## 🧩 Input

Input
Dòng đầu là hai số
$K$
,
$R$
là số nhà hàng có thể được mở và bán kính phục vụ của mỗi nhà hàng
$(1 ≤K≤ 10, 1 ≤R≤ 500)$
Dòng thứ hai là
$M$
là số địa điểm có thể đặt nhà hàng
$(1 ≤K≤M≤ 20)$
$M$
dòng tiếp theo, mỗi dòng là
$2$
số nguyên
$X$
và
$Y$
$( - 1000 ≤X,Y≤ 1000)$
Dòng tiếp theo gồm
$N$
là số khu nhà
$(1 ≤N≤ 100)$
.
Mỗi dòng tiếp theo là
$N$
dòng tiếp theo là
$3$
số nguyên
$X$
,
$Y$
,
$S$
là tọa độ và số người ở khu nhà đó.
$( - 1000 ≤X,Y≤ 1000, 1 ≤S≤ 100)$
Khu nhà nằm trong bán kính của nhà hàng nếu khoảng cách giữa chúng
$≤R$
. Không có
$2$
ngôi nhà tại cùng một địa điểm và không có
$2$
địa điểm có thể đặt nhà hàng trùng nhau.


## 💡 Output

Output
Ghi ra số người tối đa có thể được phục vụ.


## 🧠 Example

### Input

```text
2 2
3
1 0
4 0
7 0
4
0 0 1
3 0 7
5 0 9
8 0 1
```

### Output

```text
18
```


