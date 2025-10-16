# ZA. Trò chơi thoát hiểm

## 📖 Problem

Nhâm Tấn đang tham gia một gameshow thử thách. Hệ thống đưa anh tới một khu gồm
$n$
đỉnh núi và
$m$
cây cầu nối giữa
$2$
đỉnh núi. Ở một số cây cầu, được treo một cái chìa khóa để mở cổng thoát hiểm. Cổng thoát hiểm được đặt ở đỉnh núi
$b$
(có thể trùng với đỉnh núi Tấn đang đứng). Nhiệm vụ của anh là lấy chìa khóa và mở cổng. Tuy nhiên, đời đâu như mơ, những cây cầu chỉ có thể đi qua 1 lần, sau khi đi qua nó sẽ bị phá hủy (
Lưu ý:
Một khi đã đi thì sẽ đi hết cây cầu không đi ra lấy chìa khóa xong quay lại).
Yêu cầu:
Viết chương trình thông báo có tồn tại cách để Nhâm Tấn dành chiến thắng không !


## 🧩 Input

Input
Dòng đầu tiên chứa
$2$
số nguyên
$n$
và
$m$
$(1 ≤n≤ 3 * 105, 1 ≤m≤ 3 * 105)$
lần lượt là số đỉnh núi và số cây cầu.
$m$
dòng tiếp theo, mỗi dòng chứa
$3$
số nguyên
$ui$
,
$vi$
,
$zi$
$(1 ≤ui,vi≤n, 0 ≤zi≤ 1)$
cho biết có cây cầu nối giữa
$ui$
và
$vi$
.
$zi= 1$
thì cây cầu này có treo chìa khóa và ngược lại
$zi= 0$
là không có chìa khóa trên cầu.
Dòng cuối chứa 2 số nguyên
$a$
và
$b$
$(1 ≤a,b≤n)$
lần lượt là đỉnh núi Nhâm Tấn bắt đầu và đỉnh núi chứa cổng thoát hiểm


## 💡 Output

Output
Một dòng duy nhất là
$YES$
nếu tồn tại cách để Nhâm Tấn dành chiến thắng và ngược lại in ra
$NO$


## 🧠 Example

### Input

```text
6 7
1 2 0
2 3 0
3 1 0
3 4 1
4 5 0
5 6 0
6 4 0
1 6
```

### Output

```text
YES
```


