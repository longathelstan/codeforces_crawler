# S. Đường đi k cạnh lớn nhất

## 📖 Problem

Bạn được cho một đồ thị với
$n$
đỉnh và
$m$
cạnh có hướng có trong số. Tìm đường đi có
$k$
cạnh với tổng trọng số lớn nhất. Một đường đi có thể đi qua một đỉnh hay cạnh nhiều lần.
Nếu không tồn tại đường đi nào có
$k$
cạnh in ra "IMPOSSIBLE"


## 🧩 Input

Input
Dòng đầu tiên gồm
$3$
số nguyên dương
$n$
,
$m$
,
$k$
$(1 ≤n≤ 100, 0 ≤m≤n* (n- 1), 1 ≤k≤ 109)$
$m$
dòng tiếp theo miêu tả các cạnh. Trong đó dòng thứ
$i$
gồm
$3$
số
$ai,bi,ci$
$(1 ≤ai,bi,n,ai≥bi,  - 109≤ci≤ 109)$
, miêu tả một cạnh có hướng nối từ
$ai$
đến
$bi$
với trọng số
$ci$
. Đồ thị trong input đảm bảo không có cạnh trùng hoặc cạnh nối cùng một đỉnh với nhau.


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm


## 🧠 Example

### Input

```text
3 4 2
1 2 12
2 3 -5
3 1 20
2 1 -1
```

### Output

```text
32
```



## 📝 Note

Note
Đường đi tối ưu nhất cho ví dụ
$1$
là:
$3$
->
$1$
->
$2$
Đường đi tối ưu nhất cho ví dụ
$2$
là:
$3$
->
$1$
->
$2$
->
$3$
->
$1$
->
$2$
![](https://espresso.codeforces.com/7f4795939aba60e35709bffc11d2fd90e00257cf.png)

