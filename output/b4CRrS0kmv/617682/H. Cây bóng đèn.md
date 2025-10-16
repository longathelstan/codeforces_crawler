# H. Cây bóng đèn

## 📖 Problem

Bạn được giao một cái cây $$$n$$$ nút và nút $$$1$$$ đặt làm gốc của cây, trên mỗi nút của cây treo một cái bóng đèn, ban đầu trạng thái của bóng đèn $$$i$$$ là $$$t_i$$$ $$$(0 \leq t_i \leq 1)$$$. Bạn thực hiện $$$q$$$ tác vụ mỗi tác vụ sẽ có một trong $$$2$$$ loại sau:
1 pow v $$$(1 \leq v \leq n)$$$ : chuyển trạng thái của mọi bóng đèn trong cây con gốc $$$v$$$ (chuyển trạng thái tức là từ tắt thành bật và ngược lại)
2 get v $$$(1 \leq v \leq n)$$$: Đếm số lượng bóng đèn đang bật $$$(t_x=1)$$$ trong cây con gốc $$$v$$$.
Bạn hãy xây dựng chương trình giải quyết vấn đề trên


## 🧩 Input

Input
Dòng đầu tiên gồm số nguyên dương $$$n$$$ $$$(1 \leq n \leq 2*10^5)$$$
Dòng tiếp theo gồm $$$n-1$$$ số nguyên dương $$$p_i$$$ $$$(2 \leq i \leq n)$$$ $$$p_i$$$ là nút cha của $$$i$$$.
Dòng tiếp theo gồm $$$n$$$ số nguyên dương $$$t_i$$$ $$$(0 \leq t_i \leq 1)$$$.
Dòng tiếp gồm số nguyên dương $$$q$$$ $$$(1 \leq q \leq 2*10^5)$$$ số lượng tác vụ
Mỗi dòng trong $$$q$$$ dòng cuối là một trong hai tác vụ.


## 💡 Output

Output
In ra đáp án ứng với mỗi tác vụ loại $$$2$$$.


## 🧠 Example

### Input

```text
41 1 11 0 0 19get 1get 2get 3get 4pow 1get 1get 2get 3get 4
```

### Output

```text
20012110
```


