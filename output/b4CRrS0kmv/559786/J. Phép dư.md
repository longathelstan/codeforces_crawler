# J. Phép dư

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
hãy đưa số lượng số
$K$
nguyên dương sao cho tất cả các đỉnh trong cây con gốc
$i$
khi lấy giá trị của từng đỉnh chia dư cho
$K$
thì sẽ ra cùng số dư, nếu tất cả các nút trong cây con gốc
$i$
đều có cùng giá trị hãy đưa ra
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
$(1 ≤ai≤ 2 * 106)$
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
23 15 25 27 15 15 23
1 2
1 3
2 4
2 5
5 6
5 7
```

### Output

```text
2
3
-1
-1
4
-1
-1
```


