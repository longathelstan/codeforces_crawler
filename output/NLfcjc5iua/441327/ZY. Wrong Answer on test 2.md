# ZY. Wrong Answer on test 2

## 📖 Problem

Cho một mảng $$$a$$$ gồm $$$n$$$ phần tử. Độ đẹp của mảng là tổng
đoạn con liên tiếp
có tổng lớn nhất của mảng đó.
Bạn có thể chọn
nhiều nhất một
(có thể không) đoạn con liên tiếp và nhân các phần tử trong đoạn con đó lên $$$x$$$ đơn vị. Hãy tìm độ đẹp lớn nhất của mảng.


## 🧩 Input

Input
Dòng đầu là số tượng số test $$$(1\leq q\leq 20)$$$, mỗi test sẽ có dạng:
Dòng đầu là $$$2$$$ số nguyên $$$n$$$ và $$$x$$$ $$$(1\leq n\leq 10^5 , -100\leq x\leq 100)$$$
Dòng tiếp theo gồm $$$n$$$ số $$$a_1,a_2,...a_n$$$ $$$(-10^9\leq a_i\leq 10^9)$$$
Tổng $$$n$$$ của $$$q$$$ test $$$\leq 5.10^5$$$


## 💡 Output

Output
$$$q$$$ dòng ứng với đáp án của $$$q$$$ test theo thứ tự input


## 🧠 Example

### Input

```text
3
5 -2
-3 8 -2 1 -6
12 -3
1 3 3 7 1 3 3 7 1 3 3 7
5 10
-1 -2 -3 -4 -5
```

### Output

```text
22
42
0
```



## 📝 Note

Note
Test $$$1$$$: Chọn $$$[-2,1,-6]$$$ và nhân lên $$$-2$$$, mảng mới sẽ thành $$$[-3 , \bf{8,4,-2,12}]$$$ có độ đẹp là $$$22$$$.
Test $$$2$$$: Không cần chọn đoạn con liên tiếp để nhân với $$$x$$$.
Test $$$3$$$: Không chọn gì luôn là đáp án tối ưu nhất.

