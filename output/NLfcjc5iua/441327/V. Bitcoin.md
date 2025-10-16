# V. Bitcoin

## 📖 Problem

Cho giá giao dịch
$n$
ngày của bitcoin, mỗi ngày bạn có thể chọn mua
$1$
lần hoặc bán
$1$
lần hoặc không làm gì cả, việc bán và mua không diễn ra cùng
$1$
ngày, để bán được bitcoin thì bạn phải mua bitcoin ở những ngày trước đó, mỗi lần mua hoặc bán bạn phải trả phí là
$1%$
bằng số tiền bỏ vào.
Ví dụ bạn bỏ
$5000$$
lúc mua bitcoin giá
$20k$$
và bán bitcoin ở giá
$30k$$
. Thì tổng số phí phải trả là
$5000$.1%$
(lúc mua) +
$5000$.1%$
(lúc bán) =
$100$$
. Số tiền của bạn sau khi mua và bán là
$5000$$
*
$(30k$ / 20k$)$
-
$100$$
(tiền phí) =
$7400$$
.
Cho trước giá giao dịch
$n$
ngày của bitcoin và số tiền
$x$$
bạn hiện có, hãy tìm số tiền lớn nhất bạn có thể đạt được nếu bạn chơi một cách tối ưu.
Đáp án của bạn được coi là đúng nếu độ lệch với đáp án gốc
$≤ 10- 5$


## 🧩 Input

Input
Dòng đầu tiên là số lượng số test
$q$
$(1 ≤q≤ 104)$
, mỗi test có cấu trúc:
Dòng đầu tiên gồm
$2$
số
$n$
và
$x$
$(2 ≤n≤ 50, 1 ≤x≤ 5000)$
Dòng tiếp theo gồm
$n$
số
$a1,a2, ...an$
$(20000 ≤ai≤ 30000)$


## 💡 Output

Output
Gồm một dòng duy nhất là số tiền lớn nhất cần tìm.


## 🧠 Example

### Input

```text
3
2 5000
20000 30000
2 5000
20000 20001
4 123
20000 25000 22000 30000
```

### Output

```text
7400.00000
5000.00000
203.27875
```


