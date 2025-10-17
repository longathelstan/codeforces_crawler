# A. Dãy số và phép and

## 📖 Problem

Cho một dãy số có $$$n$$$ số nguyên, số thứ $$$i$$$ là $$$A_i$$$. Bạn được thực hiện thao tác sau vô số lần, mỗi lần bạn chọn một đoạn $$$[l,r]$$$ sau đó tiến hành với mọi $$$i$$$ sao cho $$$(0 \leq i \leq r-l)$$$, ta gán $$$A_{l+i}=A_{l+i}$$$ & $$$A_{r-i}$$$. Với ký hiệu dấu & là phép and trong bitwise.
Hãy tìm cách thức hiện các thao tác sao cho số lớn nhất của dãy là nhỏ nhất có thể!!


## 🧩 Input

Input
Dòng đầu tiên gồm số nguyên dương $$$t$$$ $$$(1 \leq t \leq 100)$$$ là số lượng testcase. Mỗi test trong $$$t$$$ test ta có định dạng sau:
Số đầu tiên là một số nguyên dương $$$n$$$ $$$(1 \leq n \leq 100)$$$ là số lượng phần tử
Dòng tiếp theo gồm $$$n$$$ số nguyên $$$A_i$$$ $$$(0 \leq A_i \leq 10^9)$$$.


## 💡 Output

Output
In ra số nhỏ nhất có thể của số lớn nhất trong dãy sau một số thao tác thực hiện.


## 🧠 Example

### Input

```text
4
2
1 2
3
1 1 3
4
3 11 3 7
5
11 7 15 3 7
```

### Output

```text
0
1
3
3
```


