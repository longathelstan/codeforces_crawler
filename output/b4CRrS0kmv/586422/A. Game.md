# A. Game

## 📖 Problem

Có
$N$
học sinh và
$M$
trò chơi vi tính. Mỗi học sinh chỉ thích chơi một trò duy nhất và mỗi trò chơi có ít nhất một học sinh thích. Nhà trường tổ chức kết nối mạng Lan cho các máy tính trong
$Q$
phút, phút thứ
$i$
nối
$2$
máy của học sinh
$Ui$
và
$Vi$
(coi như đồ thị vô hướng). Tất cả những học sinh thích chơi cùng một loại game sẽ bắt đầu chơi khi máy tính của họ liên thông (có thể đi qua các đỉnh chứa game khác). Hỏi thời gian bắt đầu chơi của mỗi game.
Nếu game chỉ có
$1$
người thích thì sẽ bắt đầu vào phút thứ
$0$
Nếu
$1$
loại game không thế liên thông sau
$Q$
phút thì in ra
$- 1$
ứng với game đó


## 🧩 Input

Input
Dòng đầu gồm
$N,M,Q$
$(1 ≤M≤N≤ 105, 1 ≤Q≤ 2 * 105)$
Dòng hai gồm
$N$
số, số thứ
$i$
là
$Ai$
miểu tả trò chơi mà học sinh thứ
$i$
thích
$Q$
dòng tiếp theo: mỗi dòng gồm
$2$
số
$Ui$
và
$Vi$


## 💡 Output

Output
Gồm
$M$
dòng, dòng thứ
$i$
là thời điểm bắt đầu chơi của game thứ
$i$


## 🧠 Example

### Input

```text
5 2 4
1 2 2 2 1
1 2
2 3
1 5
4 5
```

### Output

```text
3
4
```


