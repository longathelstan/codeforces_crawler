# ZP. Sự yêu đời

## 📖 Problem

Tấn là một bạn rất đam mê tin học, vì đã chán với bài toán quy hoạch động kinh điển là tìm dãy con có tổng lớn nhất, nên hôm nay Tấn đã nghĩ ra bài toán cải tiến của bài đó và đố các bạn.
cho $$$1$$$ hoán vị gồm $$$n$$$ phần tử, phần tử thứ $$$i$$$ có giá trị là $$$a_i$$$. Dãy con được định nghĩa là một dãy có thể đạt được nếu xóa $$$1$$$ số phần tử trong dãy ban đầu mà không làm thay đổi vị trí của chúng.
Sức mạnh của một dãy con $$$b$$$ gồm $$$k$$$ phần tử là $$$b_1 - b_2 + b_3 - b_4+b_5-b_6+...b_k$$$.
Bạn cần in ra sức mạnh của dãy con có sức mạnh lớn nhất.


## 🧩 Input

Input
Dòng đầu gồm $$$n$$$ $$$(1\leq n\leq 10^3)$$$, là số phần tử của dãy và số truy vấn.
Dòng hai gồm $$$n$$$ phần tử, phần tử thứ $$$i$$$ là giá trị của $$$a_i$$$$$$(1\leq ai \leq n)$$$, dữ liệu đảm bảo dãy $$$a$$$ là $$$1$$$ hoán vị.


## 💡 Output

Output
Gồm $$$1$$$ dòng duy nhất là đáp án cân tìm.


## 🧠 Example

### Input

```text
3
1 3 2
```

### Output

```text
3
```



## 📝 Note

Note
Ở test 1: [1,$$$3$$$,2]. Sức mạnh của dãy con lớn nhất là $$$3=3$$$.
Ở test 2: [1,$$$2$$$]. Sức mạnh của dãy con lớn nhất là $$$2 = 2$$$.
Ở test 3: [1,2,$$$5$$$,4,$$$3$$$,6,$$$7$$$]. Sức mạnh lớn nhất của dẫy con là $$$5-3+7=9$$$.
Bài này có thể giải được trong $$$O(n^2)$$$ và $$$O(nlogn)$$$ nhưng mình vẫn khuyến khích các bạn giải trong $$$O(n)$$$.

