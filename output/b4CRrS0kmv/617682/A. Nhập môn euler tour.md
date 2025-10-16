# A. Nhập môn euler tour

## 📖 Problem

Bạn được cho $$$1$$$ cái cây gồm $$$n$$$ đỉnh, với đỉnh $$$1$$$ là nút gốc, và giá trị $$$a_i$$$ tương ứng của đỉnh $$$i$$$.
Nhiệm vụ của bạn là cần phải thực hiện $$$q$$$ truy vấn có dạng như sau:
- Đổi giá trị của nút $$$s$$$ thành $$$x$$$.
- Tính tổng giá trị của các nút nằm trong cây con gốc $$$s$$$.


## 🧩 Input

Input
Một dòng gồm $$$2$$$ số nguyên dương $$$n$$$ và $$$q$$$ $$$(1 \leq n,q \leq 2*10^5)$$$.
Dòng tiếp theo gồm $$$n$$$ số nguyên dương $$$a_i$$$ $$$(1 \leq a_i \leq 10^9)$$$ là giá trị của đỉnh $$$i$$$.
Mỗi dòng trong $$$Q$$$ dòng tiếp theo thuộc một trong hai loại: $$$1,s,x$$$ thay đổi $$$a_s=x$$$ và $$$2,s$$$ tính tổng giá trị.


## 💡 Output

Output
GỒm $$$Q$$$ dòng mỗi dòng là đáp án cho từng truy vấn loại $$$2$$$.


## 🧠 Example

### Input

```text
5 3
4 2 5 2 1
3 5
1 3
2 1
3 4
2 3
1 5 3
2 3
```

### Output

```text
8
10
```


