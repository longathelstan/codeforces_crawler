# ZJ. ĐTQG Hồ Chí Minh 2024 - Bài 3 - Shipper (7 điểm)

## 📖 Problem

BT mở công ty chuyên giao hàng dọc theo một tuyến đường cao tốc. Để đơn giản, ta mô tả tuyến đường cao tốc này như là một trục tọa độ. Nhằm tăng cường chất lượng dịch vụ giao hàng, công ty của BT lắp $$$n$$$ đường ống chuyển hàng nhanh dọc theo con đường. Đường ống thứ $$$i$$$ có thể chuyển một gói hàng từ vị trí $$$x_i$$$ đến vị trí $$$y_i$$$ trong thời gian $$$t_i$$$ ($$$i = 1, 2, \dots, n$$$).
Hôm nay, công ty của BT nhận được $$$m$$$ đơn hàng. Đơn hàng thứ $$$j$$$ yêu cầu chuyển một gói hàng từ vị trí $$$a_j$$$ đến vị trí $$$b_j$$$. Nếu vận chuyển thông thường (đi bộ) thì một nhân viên di chuyển $$$d$$$ đơn vị độ dài trong $$$d$$$ đơn vị thời gian. Anh ta cũng có thể sử dụng đường ống để vận chuyển đơn hàng này, tuy nhiên với mỗi đơn hàng chỉ được sử dụng đường ống không quá một lần.
Với mỗi đơn hàng, hãy giúp BT tính toán thời gian nhanh nhất để vận chuyển đơn hàng là bao nhiêu, khi không được sử dụng ống vận chuyển quá một lần.


## 🧩 Input

Input
*
Dòng đầu tiên chứa hai số nguyên dương $$$n, m$$$ ($$$1 \le n, m \le 10^5$$$).
*
Tiếp theo là $$$n$$$ dòng, dòng thứ $$$i$$$ mô tả đường ống thứ $$$i$$$ gồm ba số nguyên $$$x_i, y_i, t_i$$$.
*
Cuối cùng là $$$m$$$ dòng, dòng thứ $$$j$$$ gồm hai số nguyên $$$a_j, b_j$$$ là vị trí giao và nhận hàng của đơn hàng thứ $$$j$$$.


## 💡 Output

Output
In ra $$$m$$$ dòng, dòng thứ $$$j$$$ ghi một số nguyên là thời gian nhỏ nhất thực hiện đơn hàng thứ $$$j$$$.


## 🧠 Example

### Input

```text
2 3
0 10 1
13 8 2
1 12
5 2
20 7
```

### Output

```text
4
3
10
```


