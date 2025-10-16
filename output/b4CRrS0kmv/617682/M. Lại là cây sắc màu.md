# M. Lại là cây sắc màu

## 📖 Problem

Cho một cái cây đa sắc có $$$n$$$ đỉnh có gốc ở đỉnh $$$1$$$. Mỗi đỉnh trong cây được gán một màu là $$$c_i$$$.
Có $$$Q$$$ truy vấn, mỗi truy vấn gồm $$$2$$$ loại sau:
$$$1$$$ $$$s$$$ $$$k$$$ $$$(1 \leq s \leq n, 1 \leq k \leq n)$$$: thay đổi màu sắc của đỉnh $$$s$$$ sang màu $$$k$$$.
$$$2$$$ $$$s$$$ $$$(1 \leq s \leq n)$$$: In ra số lượng màu riêng biệt trong cây con gốc $$$s$$$.


## 🧩 Input

Input
Dòng đầu tiên gồm số nguyên dương $$$n,q$$$ $$$(1 \leq n,q \leq 2*10^5)$$$
Dòng tiếp theo gồm $$$n$$$ số nguyên dương $$$c_i$$$ $$$(1 \leq c_i \leq 2*10^5)$$$.
Mỗi dòng trong $$$n-1$$$ dòng tiếp theo, mỗi dòng gồm số nguyên dương $$$u,v$$$ $$$(1 \leq u,v \leq n)$$$ là cạnh nối giữa $$$u$$$ và $$$v$$$.
Dòng tiếp theo gồm số nguyên dương $$$Q$$$ $$$(1 \leq Q \leq 2*10^5)$$$
Mỗi dòng trong $$$Q$$$ dòng cuối cùng, gồm một trong hai loại truy vấn.


## 💡 Output

Output
In ra đáp án tương ứng với mỗi truy vấn loại $$$2$$$.


## 🧠 Example

### Input

```text
7 4
1 2 3 4 3 2 1
1 2
1 3
1 4
4 5
4 6
4 7
2 4
2 1
2 2
2 7
```

### Output

```text
4
4
1
1
```


