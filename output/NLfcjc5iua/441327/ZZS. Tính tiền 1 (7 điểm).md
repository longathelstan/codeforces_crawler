# ZZS. Tính tiền 1 (7 điểm)

## 📖 Problem

Tấn đến cửa hàng tiện lợi mua
$n$
món đồ bỏ vào xe đẩy và đi đến quầy tính tiền để thanh toán. Mỗi mặt hàng được mô tả bằng giá
$ci$
và thời gian
$ti$
tính bằng giây mà nhân viên thanh toán chi cho mặt hàng này. Trong khi người nhân viên thanh toán đang bận rộn với mặt hàng đang thanh toán, Tấn có thể lấy trộm một số mặt hàng khác từ xe đẩy của mình. Để lấy trộm một món đồ Tấn cần đúng 1 giây.
Yêu cầu
: Hãy tính số tiền tối thiểu Tấn sẽ phải trả cho nhân viên thu ngân là bao nhiêu? Xin hãy nhớ rằng chính Tấn là người xác định thứ tự các món hàng cho nhân viên thanh toán.


## 🧩 Input

Input
Dòng đầu gồm
$n$
$n$
dòng sau, dòng thứ
$i$
gồm
$2$
số mô tả
$ti$
và
$ci$
$(0 ≤ti≤ 2000, 1 ≤ci≤ 109)$


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm


## 🧠 Example

### Input

```text
4
2 10
0 20
1 5
1 3
```

### Output

```text
8
```



## 📝 Note

Note
Với ví dụ
$1$
:
Tấn sẽ đưa nhân viên món hàng số
$4$
, trong thời gian
$1$
giây mà nhân viên thanh toán món hàng đó, Tấn sẽ lấy trộm món hàng số
$2$
.
Sau đó Tấn sẽ đưa nhân viên món hàng số
$3$
, trong thời gian
$1$
giây mà nhân viên thanh toán món hàng đó, Tấn sẽ lấy trộm món hàng số
$1$
.
Vậy số tiền Tấn phải trả là tổng số tiền món số
$3$
và
$4$
với tổng là
$8$
Với ví dụ
$2$
:
Do tất cả món hàng đều cần
$0$
giây để thanh toán, nên Tấn sẽ không thể lấy trộm món hàng nào.
Với ví dụ
$3$
:
Tấn sẽ đưa nhân viên món hàng số
$1$
, trong thời gian
$2$
giây mà nhân viên thanh toán món hàng đó, Tấn sẽ lấy trộm món hàng số
$2$
và
$3$
.

