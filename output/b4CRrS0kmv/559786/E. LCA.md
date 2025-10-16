# E. LCA

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
Đưa ra số cặp
$(i,j)$
thỏa
$aLCA(i,j)=ai*aj$
$(1 ≤i<j≤n)$


## 🧩 Input

Input
Dòng đầu tiên gồm số nguyên dương
$n$
$(1 ≤n≤ 2 * 105)$
.
$n- 1$
dòng tiếp theo, mỗi dòng là số nguyên dương
$u,v$
$(1 ≤u,v≤n)$
là cạnh nối giữa
$u$
và
$v$
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


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm


## 🧠 Example

### Input

```text
7
1 2
1 3
2 4
2 5
5 6
5 7
6 8 3 2 8 2 4
```

### Output

```text
4
```


