# F. GOPQUA

## 📖 Problem

Trong ngày trao thưởng cho các lập trình viên nhí, ban tổ chức đã chuẩn bị trước rất nhiều món quà trong đó có
$n$
món quà (được đánh số từ 1 đến
$n$
) được bày sẵn trên sân khấu, món quà thứ
$i$
có giá trị
$ai$
(1 ≤
$ai$
≤
$106$
; i = 1 ...
$n$
).
Có
$m$
lập trình viên nhí được nhận quà trong đợt này, các lập trình viên được đánh số từ 1 đến
$m$
. Ban tổ chức gọi lần lượt từng người lên nhận quà, người thứ
$i$
được nhận món quà có số thứ tự từ
$li$
đến
$ri$
(1 ≤
$li$
≤
$ri$
≤ n). Khi người thứ
$i$
nhận quà xong, các vị trí từ
$li$
đến
$ri$
sẽ được bổ sung các món quà khác có cùng giá trị.
Giả sử một lập trình viên nhận các món quà có giá trị
$b1,b2, ...,bk$
, khi gộp các món quà lại thì giá trị món quà mà người này nhận được là
$s12$
× 1 +
$s22$
× 2 +
$s32$
× 3 + ... +
$s1062$
×
$106$
, trong đó
$si$
(
$i$
= 1 ...
$106$
) là số lần xuất hiện của
$i$
trong
$b1,b2, ...,bk$
.
Yêu cầu
: Hãy cho biết giá trị của món quà mà mỗi lập trình viên nhận được.


## 🧩 Input

Input
+ Dòng đầu tiên ghi 2 số nguyên dương
$n$
,
$m$
(1 ≤
$n$
,
$m$
≤
$2×105$
).
+ Dòng thứ 2 ghi lần lượt các số
$a1,a2, ...,an$
.
+ Dòng thứ
$i$
trong
$m$
dòng tiếp theo, mỗi dòng ghi 2 số nguyên
$li,ri$
.


## 💡 Output

Output
Gồm
$m$
số tương ứng với giá trị món quà sau khi gộp của
$m$
lập trình viên nhận được. Mỗi số ghi trên một dòng.


## 🧠 Example

### Input

```text
6 3
1 2 3 1 1 3
1 6
2 4
3 6
```

### Output

```text
23
6
16
```



## 📝 Note

Note
Giới hạn
:
Có
$25%$
số test tương ứng với
$25%$
số điểm có:
$n,m≤2000, 1≤ai≤10$
.
Có
$25%$
số test khác tương ứng với
$25%$
số điểm có:
$n,m≤2×105, 1≤ai≤10$
.
Có
$25%$
số test khác tương ứng với
$25%$
số điểm có:
$n,m≤2000, 1≤ai≤106$
.
Có
$25%$
số test khác tương ứng với
$25%$
số điểm có:
$n,m≤2×105, 1≤ai≤106$
.

