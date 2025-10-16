# S. SEQ 198

## 📖 Problem

Con số
$198$
có gợi cho bạn điều gì không? Khi học lịch sử Việt Nam, Vinh biết rằng ngày
$19 - 8 - 1945$
là ngày Tổng khởi nghĩa, ngày nhân dân cả nước ta nhất tề đứng lên làm cuộc Cách mạng Tháng Tám vĩ đại. Hiện nay,
$198$
được đặt tên cho nhiều bệnh viện, công viên, đường phố trong cả nước. Con số này đã gợi ý cho Vinh khảo sát dãy số
$SEQ98$
sau đây: Dãy số nguyên không âm
$a1,a2, ...,an$
được gọi là dãy
$SEQ198$
nếu không tồn tại hai chỉ số
$i$
và
$j$
$(1≤i,j≤n)$
mà
$ai-aj$
hoặc là bằng
$1$
hoặc là bằng
$8$
hoặc là bằng
$9$
.
Ví dụ:
Dãy số nguyên
$1$
,
$3$
,
$5$
,
$7$
là dãy
$SEQ198$
.
Dãy số nguyên
$7, 3, 5, 1, 9, 21$
không phải là dãy
$SEQ198$
bởi vì có hai phần tử
$1$
và
$9$
có hiệu
$9 - 1 = 8$
. Tuy nhiên, sau khi xóa bớt phần tử
$1$
, ta thu được dãy
$7, 3, 5, 9, 21$
là một dãy
$SEQ198$
.
Vinh quan tâm tới bài toán sau đây: Cho dãy số nguyên không âm
$b1,b2, ...,bm$
, hãy tìm cách loại bỏ một số ít nhất phần tử của dãy để được dãy còn lại là
$SEQ198$
.


## 🧩 Input

Input
Dòng đầu chứa số nguyên dương
$m$
$(1 ≤m≤ 20)$
Dòng thứ hai chứa
$m$
số nguyên không âm
$b1,b2, ...,bm$
$(bi≤109)$


## 💡 Output

Output
Ghi ra số nguyên
$k$
là số phần tử bị loại bỏ. Ghi số
$0$
nếu dãy đã cho là
$SEQ198$
.


## 🧠 Example

### Input

```text
6
7 3 5 1 9 21
```

### Output

```text
1
```


