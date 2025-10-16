# C. Cây tiên cân bằng

## 📖 Problem

Một cái cây xinh đẹp được trồng giữa một đồi xanh. Cây này có
$n$
quả tiên và
$n- 1$
cái cành nối giữa các quả tiên, mỗi quả được sẽ có màu xanh hoặc hồng.
Có
$q$
câu hỏi đưa ra, với mỗi câu hỏi bạn được đưa node
$u$
, và yêu cầu hỏi trong cây con node
$u$
có bao nhiêu node
$v$
mà từ
$u$
tới
$v$
số lượng quả tiên màu xanh bằng với số lượng quả tiên màu hồng nằm trên đường đi.


## 🧩 Input

Input
Dòng đầu tiên gồm số nguyên dương
$N$
và
$q$
$(1 ≤N≤ 5 * 105, 1 ≤q≤ 5 * 105)$
Dòng tiếp theo gồm
$n$
số nguyên dương, số thứ
$i$
bằng
$1$
nếu quả thứ
$i$
màu xanh và bằng
$0$
nếu màu hồng.
Mỗi dòng trong
$n- 1$
dòng tiếp theo, là
$2$
số nguyên dương
$u$
và
$v$
$(1 ≤u≠v≤N)$
là cạnh nối giữa hai quả tiên.
Mỗi dòng trong
$Q$
dòng tiếp theo là số nguyên dương
$u$
$(1 ≤u≤n)$
.


## 💡 Output

Output
Gồm
$Q$
dòng in ra đáp án


## 🧠 Example

### Input

```text
3 3
1 0 1
1 2
3 2
1
2
3
```

### Output

```text
1
1
0
```


