# L. WATER

## 📖 Problem

Tấn có một cái cây
$n$
đỉnh, mỗi đỉnh là một cái hồ có thể rỗng hoặc chứa nước. Các đỉnh được đánh số từ
$1$
tới
$n$
với gốc của cây là đỉnh
$1$
. Các đỉnh được nối với nhau bằng một cái ống có thể giúp nước lưu thông xuống các hồ của đỉnh con khi cho nước vào hồ của đỉnh đó. Tấn có thể thực hiện
$1$
trong
$3$
truy vấn:
*
$1$
$v$
: Đổ nước vào hồ của đỉnh
$v$
, tất cả các hồ của subtree
$v$
đều nhận được nước.
*
$2$
$v$
: Lấy nước ra khỏi hồ
$v$
. Tất cả các hồ của tổ tiên của
$v$
cũng bị lấy nước ra khỏi hồ
*
$3$
$v$
: Xác định hồ của đỉnh
$v$
còn nước không.
Ban đầu tất cả các hồ nước của các đỉnh đều không có nước. Hãy giúp Tấn xác định kết quả với mỗi truy vấn
$3$
.


## 🧩 Input

Input
Dòng đầu tiên gồm số
$n$
là số đỉnh của cây
$(1 ≤n≤ 2.105)$
$n- 1$
dòng tiếp theo mỗi dòng gồm cạnh vô hướng nối
$ui$
và
$vi$
$(1 ≤ui,vi≤n)$
Dòng tiếp theo là số truy vấn
$q$
$(1 ≤q≤ 2.105)$
$q$
dòng tiếp theo là
$1$
trong
$3$
loại
*
$1$
$v$
: Đổ nước vào hồ của đỉnh
$v$
, tất cả các hồ của subtree
$v$
đều nhận được nước.
$(1 ≤v≤n)$
*
$2$
$v$
: Lấy nước ra khỏi hồ
$v$
. Tức cả các hồ của tổ tiên của
$v$
cũng bị lấy nước ra khỏi hồ.
$(1 ≤v≤n)$
*
$3$
$v$
: Xác định hồ của đỉnh
$v$
còn nước không.
$(1 ≤v≤n)$


## 💡 Output

Output
Với mỗi truy vấn
$3$
, in ra
$1$
nếu hồ của đỉnh
$v$
có chứa nước.
$0$
nếu không chứa.


## 🧠 Example

### Input

```text
5
1 2
5 1
2 3
4 2
12
1 1
2 3
3 1
3 2
3 3
3 4
1 2
2 4
3 1
3 3
3 4
3 5
```

### Output

```text
0
0
0
1
0
1
0
1
```


