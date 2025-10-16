# H. Trò chơi (4 điểm)

## 📖 Problem

Hôm nay, các coder chơi trò chơi xếp hình chữ nhật với các que diêm như sau: Có
$n$
que diêm, que thứ
$i$
có độ dài di. Người chơi cần chọn ra
$4$
que diêm để có thể xếp thành một hình chữ nhật, giả sử
$4$
que diêm mà người chơi chọn có độ dài lần lượt là
$a$
,
$b$
,
$c$
,
$d$
$(a≤b≤c≤d)$
, khi đó có thể xếp được thành một hình chữ nhật nếu
$a=b$
và
$c=d$
. Người chơi xếp được hình chữ nhật có diện tích càng lớn sẽ càng được điểm cao.
Yêu cầu: Cho
$d1,d2, ..,dn$
là độ dài của
$n$
que diêm. Hãy tìm cách chọn
$4$
que diêm để xếp được thành một hình chữ nhật có diện tích lớn nhất.


## 🧩 Input

Input
Dòng đầu tiên ghi số nguyên dương
$K$
là số lượng bộ dữ liệu
$(1 ≤K≤ 10)$
. Tiếp đến là
$K$
nhóm dòng,
mỗi nhóm tương ứng với một bộ dữ liệu có cấu trúc như sau:
Dòng thứ nhất ghi một số nguyên dương n
$(1 ≤n≤ 105)$
;
Dòng tiếp theo chứa n số nguyên dương
$d1,d2, ...,dn(1 ≤di≤n)$
Các số trên cùng một dòng được ghi cách nhau ít nhất một dấu cách.


## 💡 Output

Output
Ghi
$K$
dòng, mỗi dòng ghi một số nguyên là diện tích của hình chữ nhật xếp được tương ứng với bộ dữ liệu trong file dữ liệu vào (ghi -1 nếu không tồn tại cách chọn nào xếp được hình chữ nhật).


## 🧠 Example

### Input

```text
2
5
5 3 1 5 1
4
1 2 3 4
```

### Output

```text
5
-1
```


