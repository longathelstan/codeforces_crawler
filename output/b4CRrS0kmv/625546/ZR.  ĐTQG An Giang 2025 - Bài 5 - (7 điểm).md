# ZR.  ĐTQG An Giang 2025 - Bài 5 - (7 điểm)

## 📖 Problem

Thành phố được biểu diễn như một bảng hình chữ nhật kích thước $$$m \times n$$$. Mỗi ô $$$(i, j)$$$ của bảng ứng với một lô đất hình vuông có độ dài cạnh là 1 và có giá trị $$$a_{ij}$$$ (đơn vị: đồng).
Một nhà tài phiệt đang có trong tay $$$T$$$ đồng. Ông ta muốn đầu tư bằng cách chọn ra chính xác $$$k$$$ lô đất hình vuông sao cho:
Các lô đất không giao nhau (không chọn trùng một ô).
Tổng giá trị các lô đất không vượt quá $$$T$$$.
Tổng diện tích là lớn nhất có thể.
Hãy xác định diện tích lớn nhất mà nhà tài phiệt có thể đầu tư được.


## 🧩 Input

Input
Đọc từ file
LAND.INP
có cấu trúc như sau:
*
Dòng đầu tiên có ba số nguyên $$$m, n$$$ và $$$k$$$.
*
Dòng thứ hai có một số nguyên không âm $$$T$$$ $$$(T \le 10^9)$$$.
*
$$$m$$$ dòng tiếp theo, dòng thứ $$$i$$$ có $$$n$$$ số nguyên không âm $$$a_{ij}$$$ $$$(a_{ij} \le 10^9)$$$.


## 💡 Output

Output
Ghi ra file
LAND.OUT
một số nguyên duy nhất – tổng diện tích lớn nhất có thể đạt được.


## 🧠 Example

### Input

```text
4 5 1
30
2 2 2 2 2
2 1 1 1 2
2 1 1 1 2
2 2 2 2 2
```

### Output

```text
16
```


