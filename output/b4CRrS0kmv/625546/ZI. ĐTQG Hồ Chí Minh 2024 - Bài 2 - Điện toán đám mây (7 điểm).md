# ZI. ĐTQG Hồ Chí Minh 2024 - Bài 2 - Điện toán đám mây (7 điểm)

## 📖 Problem

Johnny đang thành lập Bytecomp, một công ty cung cấp sức mạnh tính toán trên nền tảng điện toán đám mây. Các công ty thuộc lĩnh vực này thường sở hữu nhiều máy tính mạnh có thể thực hiện các phép tính của khách hàng.
Johnny vẫn chưa mua máy nào. Anh ấy đến một cửa hàng máy tính và nhận được danh sách gồm tất cả $$$n$$$ máy tính hiện có. Mỗi máy tính được mô tả bởi số lượng lõi xử lý (processor cores) $$$c_i$$$, xung nhịp $$$f_i$$$, và giá bán $$$v_i$$$. Một máy tính như vậy chứa $$$c_i$$$ lõi riêng biệt không can thiệp lẫn nhau, nên có thể dùng cho các tác vụ khác nhau.
Khi khách hàng đặt hàng tài nguyên tính toán, họ chỉ định số lõi cần thiết $$$C_j$$$ và xung nhịp tối thiểu cần có $$$F_j$$$. Một đơn hàng cũng bao gồm số tiền $$$V_j$$$ mà khách hàng sẵn sàng trả. Nếu đơn hàng được chấp nhận, Bytecomp phải cung cấp quyền truy cập độc quyền vào tài nguyên tính toán yêu cầu bởi khách hàng. Johnny cần chọn $$$C_j$$$ lõi (có thể từ các máy tính khác nhau), mỗi lõi có xung nhịp ít nhất là $$$F_j$$$. Những lõi này không thể được sử dụng cho bất kỳ đơn hàng nào khác.
Hãy giúp Johnny kiếm được nhiều tiền nhất có thể: chọn một tập con các đơn hàng để chấp nhận và một tập con các máy tính từ cửa hàng để đáp ứng tất cả các đơn hàng đã chấp nhận. Mục tiêu của bạn là tối đa hóa tổng lợi nhuận, tức là chênh lệch giữa doanh thu từ việc cung cấp tài nguyên cho khách hàng và chi phí mua máy tính.


## 🧩 Input

Input
Dòng đầu tiên chứa một số nguyên $$$n$$$ $$$(1 \leq n \leq 2000)$$$ — số lượng máy tính có trong cửa hàng. Mỗi một trong $$$n$$$ dòng tiếp theo chứa ba số nguyên cách nhau bởi dấu cách $$$c_i$$$, $$$f_i$$$, và $$$v_i$$$ $$$(1 \leq c_i \leq 50, 1 \leq f_i \leq 10^9, 1 \leq v_i \leq 10^9)$$$ — số lõi, xung nhịp, và giá của máy tính.
Dòng tiếp theo chứa một số nguyên $$$m$$$ $$$(1 \leq m \leq 2000)$$$ — số lượng đơn hàng. Mỗi một trong $$$m$$$ dòng tiếp theo chứa ba số nguyên cách nhau bởi dấu cách $$$C_j$$$, $$$F_j$$$, và $$$V_j$$$ $$$(1 \leq C_j \leq 50, 1 \leq F_j \leq 10^9, 1 \leq V_j \leq 10^9)$$$ — số lõi cần thiết, xung nhịp tối thiểu, và số tiền khách hàng sẵn sàng trả.


## 💡 Output

Output
In ra một số nguyên duy nhất — tổng lợi nhuận tối đa có thể đạt được.


## 🧠 Example

### Input

```text
4
4 2200 700
2 1800 10
20 2550 9999
4 2000 750
3
1 1500 300
6 1900 1500
3 2400 4550
```

### Output

```text
350
```



## 📝 Note

Note
Có bốn máy tính sẵn có và ba đơn hàng. Phương án tối ưu là mua hai máy tính bốn lõi với giá 700 và 750 (tổng cộng 1450) và sau đó chấp nhận hai đơn hàng đầu tiên để thu về $$$300 + 1500 = 1800$$$. Lúc này ta có bốn lõi với xung nhịp 2000 và bốn lõi với xung nhịp 2200. Ta có thể gán sáu lõi bất kỳ cho đơn hàng thứ hai (yêu cầu xung nhịp 1900) và một lõi cho đơn hàng đầu tiên (yêu cầu xung nhịp 1500). Một lõi sẽ không được sử dụng, điều này được phép.
Lợi nhuận tổng cộng là $$$1800 - 1450 = 350$$$.

