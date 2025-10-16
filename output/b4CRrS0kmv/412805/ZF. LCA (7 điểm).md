# ZF. LCA (7 điểm)

## 📖 Problem

Cho cái cây
$n$
đỉnh và
$n- 1$
cạnh với gốc ban đầu là
$1$
. Có
$q$
truy vấn, mỗi truy vấn thuộc
$1$
trong
$2$
loại
*
$!$
$root$
$(1 ≤root≤n)$
: Chọn
$root$
làm gốc của cây
*
$?$
$u$
$v$
$(1 ≤u,v≤n)$
: Tìm tổ tiên chung gần nhất của
$u$
và
$v$
Yêu cầu:
Với mỗi truy vấn dạng
$?$
hãy đưa ra câu trả lời.


## 🧩 Input

Input
Dòng đầu gồm
$n$
$(1 ≤n≤ 2 * 105)$
$n- 1$
dòng tiếp theo mỗi dòng gồm
$2$
đỉnh
$u$
và
$v$
Dòng tiếp theo gồm
$q$
$(1 ≤q≤ 2 * 105)$
$q$
dòng tiếp theo mỗi dòng thuộc
$1$
trong
$2$
loại truy vấn mô tả phía trên.


## 💡 Output

Output
Gồm các dòng ứng với đáp án của các truy vấn
$?$


## 🧠 Example

### Input

```text
9
1 2
1 3
2 4
2 5
3 6
3 7
6 8
6 9
7
? 4 5
? 5 6
? 8 7
! 6
? 4 5
? 5 6
? 8 7
```

### Output

```text
2
1
3
2
6
6
```



## 📝 Note

Note
Cây với gốc là
$1$
![](https://espresso.codeforces.com/8387d5cce25ee514ace5334609f8290087b77545.png)
Cây với gốc là
$6$
![](https://espresso.codeforces.com/36ae5eaa802e1dd3dacec333733f52458fbbcc2e.png)

