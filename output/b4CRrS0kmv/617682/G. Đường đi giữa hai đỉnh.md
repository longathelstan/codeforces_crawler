# G. Đường đi giữa hai đỉnh

## 📖 Problem

Cho một cái cây có $$$n$$$ đỉnh, và $$$n-1$$$ cạnh có trọng số là số nguyên dương. Bạn được yêu cầu xử lý hai truy vấn:
$$$1$$$ $$$x$$$ $$$y$$$: Thay đổi trọng số cạnh $$$x$$$ thành $$$y$$$. $$$(1 \leq x \leq n-1,1 \leq y \leq 10^9)$$$.
$$$2$$$ $$$a$$$ $$$b$$$: in ra tổng trọng số đường đi từ $$$a$$$ đến $$$b$$$ $$$(1 \leq a,b \leq n)$$$.


## 🧩 Input

Input
Dòng đầu tiên gồm số nguyên dương $$$n$$$ $$$(1 \leq n \leq 2*10^5)$$$.
$$$n-1$$$ dòng tiếp theo, mỗi dòng là số nguyên dương $$$u,v$$$ $$$(1 \leq u,v \leq n)$$$ là cạnh nối giữa $$$u$$$ và $$$v$$$.
Dòng tiếp theo là số nguyên dương $$$q$$$ $$$(1 \leq q \leq 2*10^5)$$$
$$$n-1$$$ dòng tiếp theo, mỗi dòng là một truy vấn $$$1$$$ trong $$$2$$$ loại $$$1,x,y$$$ hoặc $$$2,a,b$$$.


## 💡 Output

Output
In ra đáp án của mỗi truy vấn loại $$$2$$$.


## 🧠 Example

### Input

```text
5
1 2 3
1 3 6
1 4 9
4 5 10
4
2 2 3
2 1 5
1 3 1
2 1 5
```

### Output

```text
9
19
11
```


