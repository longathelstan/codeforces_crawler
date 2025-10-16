# C. Cây phả hệ 1

## 📖 Problem

Cho cây phả hệ gồm $$$n$$$ người, người thứ $$$i$$$ sẽ có tối đa một cha là $$$p_i$$$, $$$p_i=0$$$ nghĩa là người đó đứng đầu cây phả hệ, có thể có nhiều người cùng đứng đầu trong cây phả hệ.
Cha thứ $$$1$$$ của $$$x$$$ được định nghĩa là cha trực tiếp của $$$x$$$
Cha thứ $$$2$$$ của $$$x$$$ được định nghĩa là cha của cha của $$$x$$$
Cha thứ $$$3$$$ của $$$x$$$ được định nghĩa là cha của cha của cha của $$$x$$$
...
Bạn có $$$q$$$ truy vấn, truy vấn thứ $$$i$$$ gồm $$$v_i$$$ và $$$k_i$$$, bạn phải xác định có bao nhiêu người có cùng cha thứ $$$k$$$ với đỉnh $$$v$$$.
Yêu cầu:
Với mỗi truy vấn, hãy đưa ra câu trả lời.


## 🧩 Input

Input
Dòng đầu tiên chứa một số nguyên dương $$$n$$$ $$$(1\leq n\leq 10 ^ 5)$$$
Dòng tiếp theo gồm $$$n$$$ số, số thứ $$$i$$$ là cha $$$p_i$$$ của người thứ $$$i$$$ $$$(0\leq p_i\leq n)$$$.
Dòng tiếp theo gồm số $$$q$$$ $$$(1\leq q\leq 10 ^ 5)$$$
$$$q$$$ dòng tiếp theo mỗi dòng gồm $$$2$$$ số $$$v_i$$$ và $$$k_i$$$ $$$(1\leq v_i, k_i\leq n)$$$


## 💡 Output

Output
Gồm $$$q$$$ dòng ứng với $$$q$$$ truy vấn cần tìm theo thứ tự đầu vào


## 🧠 Example

### Input

```text
60 1 1 0 4 471 11 22 12 24 15 16 1
```

### Output

```text
0 0 1 0 0 1 1
```


