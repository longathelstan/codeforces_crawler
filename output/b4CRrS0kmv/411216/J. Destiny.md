# J. Destiny

## 📖 Problem

Tấn có một dãy $$$a$$$ có độ dài là $$$n$$$. Tấn hỏi bạn $$$q$$$ truy vấn, mỗi truy vấn có dạng $$$l$$$ $$$r$$$ $$$k$$$, bạn hãy trả về giá trị $$$a_i$$$ nhỏ nhất sau cho $$$l\leq i\leq r$$$ và số lần xuất hiện của $$$a_i > \frac{r - l + 1}{k}$$$ trong đoạn $$$[l,r]$$$. Nếu không có thì in $$$-1$$$.


## 🧩 Input

Input
Dòng đầu gồm số $$$n$$$ và $$$q$$$ là số phần tử của dãy và số truy vấn $$$(1\leq n , q\leq3.10^5)$$$
Dòng tiếp theo gồm $$$n$$$ số nguyên dương mô tả phần tử $$$a_i$$$ $$$(1\leq a_i\leq n)$$$
$$$q$$$ dòng tiếp theo mỗi dòng chứa ba số $$$l$$$,$$$r$$$,$$$k$$$ $$$(1\leq l\leq r\leq n, 1\leq k\leq 5)$$$ mô tả truy vấn.


## 💡 Output

Output
Đáp án với mỗi truy vấn


## 🧠 Example

### Input

```text
4 2
1 1 2 2
1 3 2
1 4 2
```

### Output

```text
1
-1
```


