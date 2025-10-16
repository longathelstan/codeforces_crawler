# ZZA. Lại là mua quà (5 điểm)

## 📖 Problem

Để đáp lại tấm lòng của Thành, Trâm cũng quyết định lấy tiền thưởng của mình để mua quà lưu niệm tặng các bạn nam lớp 12I. Trâm vào trang Web của một cửa hàng, chọn được n món hàng đưa vào danh sách sẽ mua làm quà, món hàng thứ i có giá ai, i = 1÷n. Khi em chuẩn bị chuyển danh sách hàng đã chọn vào giỏ mua thì xuất hiện thông báo về một chương trình khuyến mãi mới. Nếu giỏ hàng mua của khách có dưới 10 món hàng thì không được khuyến mãi gì, nếu có từ 10 đến 19 món hàng thì món giá thấp nhất trong số đó sẽ được nhận miễn phí, nếu giỏ hàng mua có từ 20 đến 29 món hàng thì hai món giá thấp nhất trong số đó sẽ được nhận miễn phí, nếu giỏ hàng mua có từ 30 đến 39 món hàng thì ba món giá thấp nhất trong số đó sẽ được nhận miễn phí.... Tóm lại, nếu số lượng hàng trong giỏ là m thì sẽ được miễn phí [m/10] món có giá nhỏ nhất trong giỏ đó.
Trâm không thể thay đổi trình tự hàng trong danh sách đã đăng ký mua nhưng có thể cắt danh sách thành các phần, mỗi phần gồm một dãy liên tiếp các hàng trong danh sách và bỏ vào một giỏ hàng riêng để nhận được chính sách ưu đãi đã nêu với giỏ hàng. Là một người giỏi tính toán, Trâm nhanh chóng hoàn thành các giỏ đặt hàng để tổng chi phí phải trả cho n mặt hàng muốn mua là nhỏ nhất. Yêu cầu: Hãy xác định số tiền nhỏ nhất mà Trâm phải thanh toán.


## 🧩 Input

Input
+ Dòng đầu tiên chứa một số nguyên dương
$n$
$(n≤105)$
,
+ Dòng thứ hai chứa n số nguyên dương a1, a2, . . ., an
$(ai≤109,i= 1÷n)$
.


## 💡 Output

Output
Một số nguyên là kết quả tìm được


## 🧠 Example

### Input

```text
12
4 4 5 5 5 5 5 5 5 5 5 5
```

### Output

```text
53
```


