# ZH. ĐTQG Hồ Chí Minh 2024 - Bài 1 - Thu nhập tiền xu (6 điểm)

## 📖 Problem

Một trò chơi có $$$n$$$ căn phòng và $$$m$$$ đường hầm nối giữa chúng. Mỗi căn phòng chứa một số lượng xu nhất định. Hãy xác định số xu tối đa bạn có thể thu thập được khi di chuyển qua các đường hầm, trong đó bạn được tự do chọn phòng bắt đầu và phòng kết thúc.


## 🧩 Input

Input
Dòng đầu tiên chứa hai số nguyên $$$n$$$ và $$$m$$$ — số phòng và số đường hầm ($$$1 \le n \le 10^5$$$, $$$1 \le m \le 2 \cdot 10^5$$$). Các phòng được đánh số từ $$$1$$$ đến $$$n$$$.
Dòng thứ hai chứa $$$n$$$ số nguyên $$$k_1, k_2, \dots, k_n$$$ ($$$1 \le k_i \le 10^9$$$) — số xu trong từng phòng.
Tiếp theo là $$$m$$$ dòng, mỗi dòng chứa hai số nguyên $$$a$$$ và $$$b$$$ ($$$1 \le a, b \le n$$$) mô tả một đường hầm từ phòng $$$a$$$ đến phòng $$$b$$$. Mỗi đường hầm là
một chiều
.


## 💡 Output

Output
In ra một số nguyên: số xu tối đa có thể thu thập được.


## 🧠 Example

### Input

```text
4 4
4 5 2 7
1 2
2 1
1 3
2 4
```

### Output

```text
16
```


