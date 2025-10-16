# J. Cây vui vẻ

## 📖 Problem

Một game show đưa ra thử thách cho bạn. Đầu tiên, bạn nhận được một cái cây. Node thứ $$$i$$$ của cây có giá trị là $$$a_i$$$ (node 1 là node gốc).
Bạn sẽ thực hiện $$$q$$$ truy vấn, mỗi cái sẽ thuộc $$$1$$$ trong $$$2$$$ loại sau:
$$$1$$$ $$$u$$$ $$$val$$$: Bạn sẽ gán tất cả các node trong cây con gốc $$$u$$$ bằng giá trị $$$val$$$ (bao gồm cả $$$u$$$) $$$(1\leq val\leq 10 ^ 5)$$$.
$$$2$$$ $$$u$$$: Bạn hãy tính tổng của tất cả các node trong cây con gốc $$$u$$$ và kiểm tra tổng có thể phân tích thành tổng của $$$2$$$ số nguyên tố được hay không (bao gồm cả $$$u$$$).


## 🧩 Input

Input
Dòng đầu tiên là số nguyên dương $$$n$$$ $$$(1 \leq n \leq 10^5)$$$.
Dòng tiếp theo là một dãy gồm $$$n$$$ số nguyên $$$a_i$$$ $$$(1 \leq a_i \leq 10^5)$$$.
Mỗi dòng trong $$$n-1$$$ dòng tiếp theo là các cạnh của cây. Dòng thứ $$$i$$$ là $$$u,v$$$ $$$(1 \leq u \neq v \leq n)$$$ là mô tả cạnh nối giữa $$$u$$$ và $$$v$$$.
Dòng tiếp theo là số nguyên dương $$$q$$$ $$$(1 \leq q \leq 10^5)$$$.
Mỗi dòng trong $$$q$$$ dòng tiếp theo là một trong hai loại truy vấn đã nêu ở bài.


## 💡 Output

Output
Gồm nhiều dòng, với mỗi dòng, tương ứng với kết quả truy vấn loại $$$2$$$. Nếu tổng phân tích được thành tổng của $$$2$$$ số nguyên tố hãy in ra $$$YES$$$ ngược lại in ra $$$NO$$$.


## 🧠 Example

### Input

```text
93 5 2 7 10 6 1 4 31 22 31 44 55 64 77 87 962 72 21 7 102 71 7 92 7
```

### Output

```text
YES
YES
YES
NO
```


