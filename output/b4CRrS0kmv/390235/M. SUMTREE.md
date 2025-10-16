# M. SUMTREE

## 📖 Problem

Cây trong lý thuyết đồ thị là một đồ thị vô hướng, có trọng số, liên thông không chu trình. Một cây gồm N đỉnh sẽ có N-1 cạnh nối giữa chúng.
Cho một cây N đỉnh, bạn hãy tính tổng khoảng cách từ các đỉnh của đồ thị đến các đỉnh còn lại, Tức là với mỗi đỉnh u (1 ≤ u ≤ N), bạn phải tính tổng khoảng cách từ đỉnh u đến các đỉnh v của đồ thị (1 ≤ v ≤ N).


## 🧩 Input

Input
Dòng đầu tiên chứa một số nguyên
$T$
- số lượng test case. Mỗi test case có cấu trúc như sau:
Dòng đầu tiên chứa một số nguyên dương N
$(1≤N≤105)$
$N- 1$
dòng tiếp theo, mỗi dòng chứa
$3$
số nguyên u, v, w biểu diễn cạnh nối giữa
$2$
đỉnh
$u,v$
có trọng số là
$w$
.
$(1≤u,v≤N,u≠v, 1≤w≤106)$
.
Dữ liệu đảm bảo tổng giá trị N trong các test case không vượt quá
$2 * 106$
.


## 💡 Output

Output
Với mỗi test case, xuất ra trên N dòng, dòng thứ i là tổng khoảng cách từ đỉnh i đến các đỉnh trên đồ thị.


## 🧠 Example

### Input

```text
3
4
1 4 7
2 3 5
4 2 6
4
1 2 2
3 1 4
4 3 5
4
1 2 5
2 3 1
3 4 3
```

### Output

```text
38
24
34
24
15
19
15
25
20
10
10
16
```



## 📝 Note

Note
Với test case thứ nhất:
- Từ đỉnh
$1$
: khoảng cách đến
$2$
là
$13$
, đến
$3$
là
$18$
, đến
$4$
là
$7$
. Tổng khoảng cách là
$13 + 18 + 7 = 38$
- Từ đỉnh
$2$
: khoảng cách đến
$1$
là
$13$
, đến
$3$
là
$5$
, đến
$4$
là
$6$
. Tổng khoảng cách là
$24$
- Từ đỉnh
$3$
: khoảng cách đến
$1$
là
$18$
, đến
$2$
là
$5$
, đến
$4$
là
$11$
. Tổng khoảng cách là
$34$
- Từ đỉnh
$4$
: khoảng cách đến
$1$
là
$7$
, đến
$2$
là
$6$
, đến
$3$
là
$11$
. Tổng khoảng cách là
$24$

