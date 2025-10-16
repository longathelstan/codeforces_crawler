# O. Độ yếu và độ nghèo

## 📖 Problem

Bạn được cho một dãy gồm $$$n$$$ số nguyên $$$a_1, a_2, \dots, a_n$$$.
Độ yếu
của một dãy số là giá trị lớn nhất của
độ nghèo
trên tất cả các đoạn con liên tiếp của dãy số đó.
Độ nghèo
của một đoạn con được định nghĩa là
giá trị tuyệt đối
của tổng các phần tử trong đoạn đó.
Yêu cầu:
Hãy xác định một số thực $$$x$$$ sao cho
độ yếu
của dãy số $$$a_1 - x, a_2 - x, \dots, a_n - x$$$ là nhỏ nhất có thể.


## 🧩 Input

Input
Dòng đầu tiên chứa một số nguyên $$$n$$$ $$$(1 \leq n \leq 200000)$$$, độ dài của dãy số.
Dòng thứ hai chứa $$$n$$$ số nguyên $$$a_1, a_2, \dots, a_n$$$ $$$(|a_i| \leq 10000)$$$.


## 💡 Output

Output
In ra một số thực duy nhất biểu diễn giá trị nhỏ nhất có thể của độ yếu của dãy số đã biến đổi. Đáp án của bạn sẽ được chấp nhận nếu sai số tương đối hoặc tuyệt đối không vượt quá $$$10^{-6}$$$.


## 🧠 Example

### Input

```text
31 2 3
```

### Output

```text
1.000000000000000
```



## 📝 Note

Note
Ví dụ 1:
Giá trị tối ưu của $$$x$$$ là $$$2$$$, dãy số trở thành: $$$-1, 0, 1$$$ Độ nghèo lớn nhất xảy ra tại đoạn $$$-1$$$ hoặc $$$1$$$, nên đáp án là $$$1$$$.
Ví dụ 2:
Giá trị tối ưu của $$$x$$$ là $$$2.5$$$, dãy số trở thành: $$$-1.5, -0.5, 0.5, 1.5$$$ Độ nghèo lớn nhất xảy ra tại đoạn $$$-1.5, -0.5$$$ hoặc $$$0.5, 1.5$$$, nên đáp án là $$$2$$$.

