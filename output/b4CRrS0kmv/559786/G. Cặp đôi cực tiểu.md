# G. Cặp đôi cực tiểu

## 📖 Problem

Cho một cái cây
$n$
đỉnh,
$n- 1$
cạnh và có gốc là
$1$
, đỉnh thứ
$i$
sẽ có giá trị là
$ai$
.
Yêu cầu:
Với mỗi đỉnh
$i$
hãy đưa
$|au-av|$
nhỏ nhất với
$u$
và
$v$
nằm trong cây con gốc
$i$
$(u≠v)$
, nếu
$i$
là nút lá hãy đưa ra
$- 1$
.


## 🧩 Input

Input
Dòng đầu tiên gồm số nguyên dương
$n$
$(1 ≤n≤ 2 * 105)$
.
Sau đó là
$n$
dòng, dòng thứ
$i$
là giá trị
$ai$
của đỉnh
$i$
$(1 ≤ai≤ 109)$
$n- 1$
dòng tiếp theo, mỗi dòng là số nguyên dương
$u,v$
$(1 ≤u,v≤n)$
là cạnh nối giữa
$u$
và
$v$
.


## 💡 Output

Output
Gồm
$n$
dòng chứa đáp án của
$n$
đỉnh theo thứ tự từ
$1$
tới
$n$


## 🧠 Example

### Input

```text
7
6 8 15 2 5 100 1000
1 2
1 3
2 4
2 5
5 6
5 7
```

### Output

```text
1
3
-1
-1
95
-1
-1
```


