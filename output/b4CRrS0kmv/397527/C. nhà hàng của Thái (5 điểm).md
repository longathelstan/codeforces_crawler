# C. nhà hàng của Thái (5 điểm)

## 📖 Problem

Thái mới mở một nhà hàng và mời người bạn thân của mình là Tân qua thử món, nhà hàng của Thái có
$n$
món khác nhau và Tân muốn ăn
$m$
món khác nhau. Món thứ
$i$
sẽ có độ thỏa mãn là
$ai$
.
Nhũng món này có thể ăn kề nhau để tăng độ thõa mãn, Tân có
$k$
quy luật về
$n$
món này, mỗi quy luật mô tả rằng nếu Tân ăn món thứ
$x$
chính xác ngay trước món thứ
$y$
thì độ thỏa mãn của Tân sẽ tăng thêm
$c$
.
Vì buổi hôm nay là Do Thái mời, nên Thái muốn tìm độ thõa mãn lớn nhất mà Tân có thể đạt được.


## 🧩 Input

Input
Dòng đầu tiên gồm
$3$
số nguyên
$n$
,
$m$
,
$k$
$(1 ≤n,m≤ 18, 0 ≤k≤n* (n- 1))$
Dòng tiếp theo chứa
$n$
số
$ai$
$(0 ≤ai≤ 109)$
Tiếp theo gồm
$k$
dòng, dòng thứ
$i$
gồm
$3$
số nguyên
$xi$
,
$yi$
,
$ci$
$(1 ≤xi,yi≤n, 0 ≤ci≤ 109)$


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm


## 🧠 Example

### Input

```text
2 2 1
1 1
2 1 1
```

### Output

```text
3
```



## 📝 Note

Note
Test
$1$
: Tân chọn cả
$2$
món và ăn món thứ
$2$
trước món thứ
$1$
thì độ thõa mãn của Tân sẽ là
$1$
+
$1$
+
$1$
=
$3$
Test
$2$
: Tân chọn
$3$
món
$1$
,
$2$
và
$4$
sau đó ăn theo một trong các thứ tự
$2$
,
$1$
,
$4$
$4$
,
$2$
,
$1$
Thì độ thỏa mãn sẽ là
$1$
+
$2$
+
$4$
+
$5$
=
$12$
Lưu ý cách ăn
$2$
,
$4$
,
$1$
sẽ không thỏa quy luật vì món
$2$
phải ăn chính xác ngay trước món
$1$
.

