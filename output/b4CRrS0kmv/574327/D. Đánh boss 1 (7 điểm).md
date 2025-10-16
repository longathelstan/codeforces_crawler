# D. Đánh boss 1 (7 điểm)

## 📖 Problem

Vy cần phải đánh bại lần lượt
$n$
con quái vật
Chỉ có phù thủy Vy mới có thể xử lý điều này. Cô ấy sở hữu hai phép thuật — phép thuật nước và phép thuật lửa. Trong một giây, Vy có thể tạo ra
$w$
đơn vị mana nước và
$f$
đơn vị mana lửa. Cô ấy sẽ cần mana để thực hiện các phép thuật. Ban đầu, Vy có
$0$
đơn vị mana nước và
$0$
đơn vị mana lửa.
Mỗi con quái vật
$i$
xuất hiện từ cổng có một sức mạnh riêng, được biểu thị bằng một số nguyên dương
$si$
. Để đánh bại con quái vật
$i$
có sức mạnh
$si$
, Vy cần phải thực hiện một phép thuật nước hoặc một phép thuật lửa với sức mạnh ít nhất là
$si$
. Nói cách khác, Vy có thể chi tiêu ít nhất
$si$
đơn vị mana nước cho một phép thuật nước, hoặc ít nhất
$si$
đơn vị mana lửa cho một phép thuật lửa.
Vy có thể tạo và thực hiện phép thuật ngay lập tức. Cô ấy có thể thực hiện vô số phép thuật mỗi giây miễn là cô ấy có đủ mana để làm điều đó.
Yêu cầu:
Phù thủy muốn cứu thế giới nhanh nhất có thể, vậy hãy cho cô ấy biết cô ấy cần bao nhiêu thời gian.


## 🧩 Input

Input
Dòng đầu tiên chứa hai số nguyên
$w$
,
$f$
(
$1 ≤w,f≤ 109$
) — số lượng mana nước và mana lửa mà Vy có thể tạo ra mỗi giây.
Dòng thứ hai chứa một số nguyên duy nhất
$n$
(
$1 ≤n≤ 100$
) — số lượng quái vật.
Dòng thứ ba chứa
$n$
số nguyên
$s1,s2,s3, ...,sn$
(
$1 ≤si≤ 105$
) — sức mạnh của các quái vật.


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm


## 🧠 Example

### Input

```text
2 3
3
2 6 7
```

### Output

```text
3
```



## 📝 Note

Note
Trong ví dụ đầu tiên
Sau giây đầu tiên, Vy có thể chi tiêu
$2$
đơn vị mana lửa để tiêu diệt con quái vật đầu tiên. Dẫn tới còn
$1$
mana lửa và
$2$
mana nước
Sau giây thú hai, cô ấy có
$4$
đơn vị mana nước và
$4$
đơn vị mana lửa.
Sau giây thứ ba, cô ấy sẽ có
$6$
đơn vị mana nước và
$7$
đơn vị mana lửa sẵn có. Điều này đủ để cô ấy tiêu diệt ngay lập tức con quái vật thứ hai và thứ ba.

