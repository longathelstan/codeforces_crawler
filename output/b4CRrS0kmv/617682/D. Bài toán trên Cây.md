# D. Bài toán trên Cây

## 📖 Problem

Bạn được cho 1 cây gồm $$$n$$$ nút, gốc tại nút 1. Ban đầu mỗi nút trên cây có 1 màu. Có $$$q$$$ truy vấn thuộc 1 trong 2 loại:
1. Đổi màu nút $$$u$$$ thành $$$c$$$.
2. Truy vấn số màu khác nhau trong cây con gốc $$$u$$$.


## 🧩 Input

Input
Dòng đầu tiên gồm 2 số nguyên $$$n$$$ và $$$q$$$ $$$(1 \leq n, q \leq 4 \cdot 10^5)$$$ — lần lượt là số lượng nút trên cây và số lượng truy vấn.
Dòng thứ 2 gồm $$$n$$$ số nguyên $$$c_i$$$ $$$(1 \leq c_i \leq 60)$$$ — màu ban đầu của nút i.
$$$n-1$$$ dòng tiếp theo, mỗi dòng chứa 2 số nguyên $$$x_j, y_j$$$ $$$(1 \leq x_j, y_j \leq n)$$$ — các cạnh trên cây của mình. Đảm bảo rằng đồ thị là một cây.
$$$q$$$ dòng cuối cùng mô tả các truy vấn của mình. Mỗi dòng bắt đầu bằng số nguyên $$$t_k$$$ $$$(1 \leq t_k \leq 2)$$$ — loại của truy vấn thứ k:
*
Với $$$t_k = 1$$$, theo sau đó là 2 số nguyên $$$u_k, c_k$$$ $$$(1 \leq u_k \leq n, 1 \leq c_k \leq 60)$$$ — đổi màu nút $$$u_k$$$ thành $$$c_k$$$.
*
với $$$t_k = 2$$$, theo sau đó là 1 số nguyên $$$u_k$$$ $$$(1 \leq u_k \leq n)$$$ — truy vấn số màu khác nhau trong cây con gốc $$$u_k$$$.


## 💡 Output

Output
Với mỗi truy vấn loại 2, in ra 1 số nguyên trên 1 dòng là kết quả cho truy vấn đấy.


## 🧠 Example

### Input

```text
6 10
1 2 1 2 1 2
1 2
1 3
2 4
2 5
2 6
2 1
2 2
2 4
1 5 3
2 2
1 4 1
2 2
2 1
1 3 5
2 1
```

### Output

```text
2
2
1
2
3
3
4
```


