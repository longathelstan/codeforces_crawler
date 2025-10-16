# I. toán lớp 5 (7 điểm)

## 📖 Problem

Cho
$2$
chiếc xe, một chiếc ở vị trí
$0$
và một chiếc ở vị trí
$l$
. Chiếc xe ở vị trí
$0$
sẽ di chuyển theo chiều xuôi và chiếc xe ở vị trí
$l$
sẽ di chuyển theo chiều ngược. Ban đầu cả
$2$
chiếc đều có vận tốc là
$1$
.
Sẽ có
$n$
vị trí
$ai$
mà khi đi qua đó vận tốc của chiếc xe sẽ tăng lên
$1$
. Hãy tìm thời gian để
$2$
chiếc xe gặp nhau.


## 🧩 Input

Input
Dòng đầu gồm số nguyên
$n$
và
$l$
$(1 ≤n≤ 105, 1 ≤l≤ 109)$
Dòng tiếp theo gồm
$n$
số nguyên
$a1,a2, ...,an$
$(1 ≤a1<a2< ... <an<l)$


## 💡 Output

Output
Hãy in ra đáp thời gian để
$2$
chiếc xe gặp nhau, đáp án của bạn sẽ được coi là đúng nếu lệch với đáp án của đề bài
$≤ 10- 6$


## 🧠 Example

### Input

```text
2 10
1 9
```

### Output

```text
3.000000000
```



## 📝 Note

Note
Với test ví dụ
$1$
,
$2$
xe sẽ gặp nhau ở vị trí số
$5$
sau thời gian là
$3$
.
Xe thứ nhất sẽ tốn
$1$
s để đi tới vị trí thứ
$1$
sau đó vận tốc của xe thứ nhất sẽ tăng lên
$1$
tức là
$2$
. Sau
$2$
s tiếp vị trí của xe thứ nhất sẽ là
$5$
.
Cụ thể hơn
$0$
->
$1$
->
$3$
->
$5$
Xe thứ hai sẽ tốn
$1$
s để đi tới vị trí thứ
$9$
sau đó vận tốc của xe thứ hai sẽ tăng lên
$1$
tức là
$2$
. Sau
$2$
s tiếp vị trí của xe thứ hai sẽ là
$5$
.
Cụ thể hơn là
$10$
->
$9$
->
$7$
->
$5$
Với test ví dụ
$2$
, các xe không nhất thiết phải gặp nhau ở các tọa độ nguyên.

