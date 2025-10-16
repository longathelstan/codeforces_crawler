# ZG. CHECKIN

## 📖 Problem

Có
$M$
người cần làm thủ tục check-in tại sân bay quốc tế Cam Ranh để đi du lịch. Tại sân bay có
$N$
bàn có thể phục vụ công việc check-in. Mỗi người chỉ cần làm thủ tục tại một bàn bất kỳ nếu bàn đó đang trống và mỗi bàn chỉ phục vụ cho một người tại một thời điểm. Do kỹ năng làm việc của nhân viên tại mỗi bàn khác nhau nên thời gian phục cho một người tại mỗi bàn là khác nhau. Bàn thứ
$i$
(
$i$
= 1 ...
$N$
) phục vụ một người mất
$Ti$
đơn vị thời gian. Thời gian chờ giữa hai người kế tiếp nhau tại mỗi bàn xem như không đáng kể.
Yêu cầu:
Bạn hãy tính thời gian ít nhất để sân bay làm xong thủ tục check-in cho
$M$
người.


## 🧩 Input

Input
+ Dòng đầu ghi hai số nguyên
$N$
(
$1$
≤
$N$
≤
$105$
) và
$M$
(
$1$
≤
$M$
≤
$109$
) cách nhau một dấu cách.
+ Dòng thứ
$i$
(
$i$
=
$1$
$...$
$N$
) trong
$N$
dòng tiếp theo, mỗi dòng ghi một số nguyên
$Ti$
(
$1$
≤
$Ti$
≤
$109$
). Các số trên cùng dòng cách nhau một dấu cách.


## 💡 Output

Output
Một số nguyên duy nhất là số đơn vị thời gian ít nhất để sân bay làm xong thủ tục check-in cho
$M$
người.


## 🧠 Example

### Input

```text
2 6
7
10
```

### Output

```text
28
```



## 📝 Note

Note
Giải thích:
Trong ví dụ thứ nhất, bàn 1 phục vụ 4 người mất 28 đơn vị thời gian. Bàn 2 phục vụ 2 người mất 20 đơn vị thời gian. Vì 2 bàn cùng phục vụ song song nên thời gian để phục vụ cho 6 người là 28 đơn vị thời gian.
Giới hạn:
• Có
$70%$
số điểm với
$M$
≤
$30000$
.
• Có
$30%$
số điểm với
$30000$
<
$M$
≤
$109$
.

