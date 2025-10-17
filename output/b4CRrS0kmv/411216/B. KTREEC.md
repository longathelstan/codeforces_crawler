# B. KTREEC

## 📖 Problem

Cho đồ thị liên thông
$n$
đỉnh và
$n- 1$
cạnh, có
$C$
loại màu, mỗi đỉnh được tô màu
$ci$
bạn có
$q$
truy vấn. Mỗi truy vấn có dạng
$v$
$c$
bạn cần trả về khoảng cách gần nhất từ
$1$
đỉnh có màu
$c$
tới
$v$
.
Nếu không có đỉnh nào có màu
$c$
hãy in ra
$- 1$
.


## 🧩 Input

Input
Dòng đầu tiên gồm số nguyên
$n$
$(1 ≤n≤ 105)$
$n- 1$
dòng sau mỗi dòng gồm
$2$
số nguyên thể hiện có cạnh nối giữa
$2$
đỉnh
$u$
và
$v$
$(1 ≤u,v≤n)$
Dòng tiếp theo gồm
$C$
là số màu
$(1 ≤C≤n)$
Dòng tiếp theo gồm
$n$
số nguyên, số thứ
$i$
thể hiện màu
$ci$
của đỉnh thứ
$i$
$(1 ≤ci≤n)$
Dòng tiếp theo gồm số nguyên
$q$
là số lượng truy vấn
$(1 ≤q≤ 105)$
$q$
dòng tiếp theo mỗi dòng gồm
$2$
số nguyên
$v$
và
$c$
$(1 ≤v≤n)$
$(1 ≤c≤C)$


## 💡 Output

Output
Gồm
$q$
dòng ứng với đáp án của
$q$
truy vấn theo thứ tự input


## 🧠 Example

### Input

```text
8
1 2
1 3
2 7
2 8
3 4
4 5
4 6
4
1 2 4 2 3 1 3 2
8
1 4
2 4
3 4
4 4
5 4
6 4
7 4
8 4
```

### Output

```text
1
2
0
1
2
2
3
3
```


