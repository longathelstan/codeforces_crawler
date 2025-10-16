# B. QueryTwo

## 📖 Problem

Cho $$$n$$$ phần tử, phần tử thứ $$$i$$$ có giá trị là $$$a_i$$$.
Cho $$$q$$$ truy vấn, truy vấn thứ $$$i$$$ gồm số $$$x_i$$$, với mỗi truy vấn thứ $$$i$$$ hãy in số $$$a_j$$$ lớn nhất sao cho $$$x_i \ge a_j$$$, nếu không có $$$a_j$$$ nào thỏa mãn thì in $$$-1$$$


## 🧩 Input

Input
Dòng đầu gồm số $$$n$$$ $$$(1\leq n \leq 10^5)$$$.
Dòng hai gồm $$$n$$$ số, số thú $$$i$$$ là giá trị của $$$a_i$$$ $$$(1\leq a_i \leq 10^5)$$$.
Dòng ba gồm $$$q$$$ $$$(1\leq q \leq 10^5)$$$ là số truy vấn.
Dòng thứ $$$i$$$ trong $$$q$$$ dòng tiếp theo mỗi dòng gồm $$$x_i$$$ $$$(1\leq x_i\leq 10^5)$$$.


## 💡 Output

Output
Gồm $$$q$$$ dòng, dòng thứ $$$i$$$ là đáp án của truy vấn thứ $$$i$$$.


## 🧠 Example

### Input

```text
5
2 4 6 8 10
6
1
3
5
7
9
11
```

### Output

```text
-1
2
4
6
8
10
```


