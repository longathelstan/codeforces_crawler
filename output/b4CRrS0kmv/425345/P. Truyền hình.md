# P. Truyền hình

## 📖 Problem

Khi có quá nhiều kênh truyền hình với rất nhiều chương trình giải trí thú vị, bạn sẽ chọn lựa xem những chương trình nào? Đây quả là một câu hỏi khó.
Có
$n$
chương trình giải trí, chương trình thứ
$i$
( có thời điểm bắt đầu là
$si$
và thời điểm kết thúc là
$ti$
. Chương trình giải trí thứ
$i$
và chương trình giải trí thứ
$j$
$(1≤i<j≤n)$
được gọi là không phù hợp với nhau về lịch phát sóng nếu người xem không thể xem trọn vẹn nội dung của cả hai chương trình giải trí này. Nếu thời điểm kết thúc
$ti$
của chương trình
$i$
là thời điểm bắt đầu
$sj$
của chương trình
$j$
thì hai chương trình này vẫn được xem là có lịch phát sóng phù hợp với nhau.
Ví dụ: Có
$3$
chương trình giải trí như sau: Chương trình
$1$
$(s1= 7,t1= 10)$
, chương trình
$2$
$(s2= 12,t2= 15)$
, chương trình
$3$
$(s3= 10,t3= 20)$
. Chương trình
$1$
và chương trình
$2$
có lịch phát sóng phù hợp với nhau. Tương tự, chương trình
$1$
và chương trình
$3$
cũng được xem là có lịch phát sóng phù hợp với nhau. Tuy nhiên, chương trình
$2$
và chương trình
$3$
có lịch phát sóng không phù hợp với nhau.
Yêu cầu: Cho biết kế hoạch phát sóng của
$n$
chương trình giải trí, hãy xác định có bao nhiêu cặp chương trình có lịch phát sóng không phù hợp với nhau.


## 🧩 Input

Input
Dòng đầu tiên chứa một số nguyên dương
$n$
$(1 ≤n≤5 * 105)$
.
Dòng thứ
$i$
trong số
$n$
dòng tiếp theo
$(1≤i≤n)$
, mỗi dòng gồm hai số nguyên dương
$si$
và
$ti$
là thời điểm bắt đầu và thời điểm kết thúc của chương trình giải trí thứ
$i$
$(1≤si<ti≤109)$
. Các số trên cùng một dòng được ghi cách nhau bởi
$1$
khoảng trắng.


## 💡 Output

Output
Một số nguyên xác định số lượng cặp chương trình có lịch phát sóng không phù hợp với nhau.


## 🧠 Example

### Input

```text
3
7 10
12 15
10 20
```

### Output

```text
1
```


