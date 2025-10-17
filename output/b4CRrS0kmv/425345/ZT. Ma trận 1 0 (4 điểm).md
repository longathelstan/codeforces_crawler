# ZT. Ma trận 1 0 (4 điểm)

## 📖 Problem

Cho một lưới ma trận nhị phân m x n trong đó mỗi ô là 0 (trống) hoặc 1 (có người sử dụng).
Bạn được cung cấp các tem có kích thước
$H$
x
$W$
. Nhiệm vụ của bạn là muốn điều chỉnh các tem sao cho chúng tuân theo các hạn chế và yêu cầu đã cho:
*
Che tất cả các ô trống.
*
Không che bất kỳ ô nào bị chiếm đóng.
*
Chúng ta có thể dán bao nhiêu tem tùy thích.
*
Tem có thể chồng lên nhau.
*
Tem không được phép xoay.
*
Tem phải nằm hoàn toàn bên trong lưới.
Trả về "YES" nếu có thể vừa với tem trong khi tuân theo các hạn chế và yêu cầu đã cho. Nếu không, trả về "NO"


## 🧩 Input

Input
Dòng đầu gồm
$q$
là số lượng số test
$(1 ≤q≤ 1000)$
, mỗi test có dang
Dòng đầu gòm
$4$
số
$n$
,
$m$
,
$H$
,
$W$
$(1 ≤n.m≤ 106, 1 ≤H,W≤ 106)$
Dữ liệu đảm bảo tổng
$n.m≤ 106$


## 💡 Output

Output
Gồm
$q$
dòng ứng với
$q$
đáp án cần tìm.


## 🧠 Example

### Input

```text
2
5 4 4 3
1 0 0 0
1 0 0 0
1 0 0 0
1 0 0 0
1 0 0 0
4 4 2 2
1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
```

### Output

```text
YES
NO
```



## 📝 Note

Note
Với test
$1$
:
![](https://espresso.codeforces.com/f2e0f407e6db3f45b1095719e045182623722cbb.png)
Đặt
$2$
con tem, các ô được đánh số 1 là ô đó được đặt tem
$1$
, số
$2$
là được đặt tem
$2$
, cả
$1$
và
$2$
là được đặt lên bởi cả
$2$
con tem.
Với test
$2$
![](https://espresso.codeforces.com/35ecc5857d0a37926d5323e77cf6d3539b55f60c.png)
Không có cách nào để đặt.

