# ZB. Rút tiền ngân hàng (5 điểm)

## 📖 Problem

Ngân hàng ABC có chính sách đơn giản để cảnh báo khách hàng trong các hoạt động tín dụng được xem là bất thường. Khi một khách hàng rút tiền khỏi tài khoản một khoản tiền lớn hơn hoặc bằng
$2$
lần trung vị của
$d$
lần trước đó thì ngân hàng sẽ đưa ra cảnh báo cho khách hàng. Ví dụ một khách hàng có các lần rút tiền lần lượt là
$10$
đ
$20$
đ
$30$
đ
$40$
đ
$50$
đ và
$d= 3$
thì trong lần rút tiền thứ
$4$
ngân hàng sẽ đưa ra cảnh báo vì lần này khách hàng rút
$40$
đ nhiều gấp
$2$
lần trung vị của
$d= 3$
lần trước đó (
$3$
lần trước có trung vị là
$20$
đ), đến lần rút
$50$
đ ngân hàng không đưa ra cảnh báo vì số tiền rút chưa vượt quá
$2$
lần trung vị của
$d= 3$
lần rút trước đó.
Yêu cầu:
Cho biết
$n$
lần rút tiền của
$1$
khách hàng lần lượt là
$a1,a2, …,an$
đồng và số nguyên
$d$
, hãy cho biết ngân hàng sẽ đưa ra cảnh báo bao nhiêu lần cho các lần rút tiền từ thứ
$d+ 1$
đến thứ
$n$
.
Lưu ý:
trung vị của một dãy chẵn là trung bình cộng của hai phần tử ở giữa sau khi sắp xếp, còn trung vị dãy lẻ là phần tử giữa sau khi sắp xếp .


## 🧩 Input

Input
Dòng đầu tiên ghi
$2$
số nguyên dương
$n$
,
$d$
$(1 ≤n≤ 5 * 105, 1 ≤d≤n)$
Dòng thứ 2 ghi lần lượt các số nguyên
$a1,a2, …,an$
$(1 ≤ai≤ 1000)$


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm


## 🧠 Example

### Input

```text
9 5
2 3 4 2 3 6 8 4 5
```

### Output

```text
2
```


