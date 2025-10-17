# E. DQuery

## 📖 Problem

Cho một dãy số $$$n$$$ phần tử $$$a_1, a_2, ...,a_n$$$ và một số các truy vấn $$$d$$$. Một truy vấn $$$d$$$ là một cặp $$$(i , j)$$$ $$$(1\leq i\leq j\leq n)$$$. Với mỗi truy vấn $$$(i,j )$$$, bạn cần trả về số phần tử phân biệt nằm trong dãy con $$$a_i, a_{i+1}, ...,a_j$$$ .


## 🧩 Input

Input
Dòng $$$1$$$: $$$n$$$ $$$(1\leq n\leq 2 * 10^5)$$$.
Dòng $$$2$$$: $$$n$$$ số $$$a_1, a_2, ...,a_n$$$ $$$(1 \leq a_i \leq 10^6)$$$.
Dòng $$$3$$$: $$$q$$$ $$$(1\leq q\leq 2 * 10^5)$$$, số lượng truy vấn $$$d$$$.
Trong $$$q$$$ dòng sau, mỗi dòng chứa $$$2$$$ số $$$i,j$$$ biểu thị một truy vấn d $$$(1\leq i\leq j\leq n)$$$.


## 🧠 Example

### Input

```text
5
1 1 2 1 3
3
1 5
2 4
3 5
```

### Output

```text
3
2
3
```


