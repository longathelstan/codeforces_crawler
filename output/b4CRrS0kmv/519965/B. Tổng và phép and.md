# B. Tổng và phép and

## 📖 Problem

Cho $$$2$$$ số nguyên dương $$$n$$$ và $$$k$$$, bạn hãy đếm số lượng dãy số có độ dài $$$n$$$ thỏa mãn $$$3$$$ tính chất sau:
Tổng $$$and$$$ của $$$n$$$ số này bằng $$$0$$$.
Mỗi phần tử chỉ được nhận giá trị trong đoạn $$$[0,2^k-1]$$$.
Dãy có tổng lớn nhất trong tất cả dãy tạo ra được.
Ví dụ $$$n=2$$$ và $$$k=2$$$ ta có $$$4$$$ dãy: (0,3), (3,0), (2,1) (1,2) các dãy đều thỏa mãn tổng =3 là lớn nhất, các phần tử nằm trong đoạn từ $$$[0,3]$$$ và tổng and bằng $$$0$$$.


## 🧩 Input

Input
Dòng đầu là số nguyên dương $$$t$$$ là số lượng testcase $$$(1 \leq t \leq 10)$$$.
Mỗi test có định dạng sau: Một dòng gồm $$$2$$$ số nguyên dương $$$n,k$$$ $$$(1 \leq n \leq 10^5, k \leq 20)$$$.


## 💡 Output

Output
In ra số lượng dãy thỏa mãn, vì đáp án rất lớn nên in ra phần dư của chúng với $$$10^9+7$$$.


## 🧠 Example

### Input

```text
2
2 2
100000 20
```

### Output

```text
4
226732710
```


