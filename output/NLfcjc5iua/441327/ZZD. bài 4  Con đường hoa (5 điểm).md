# ZZD. bài 4 : Con đường hoa (5 điểm)

## 📖 Problem

Ở thành phố nọ, để trang trí con đường tham quan nhân dịp các ngày lễ, lãnh đạo các thành phố đã chỉ đạo trồng những cây hoa ở hai bên lề đường (có thể xem là lề đường A và lề đường B). Sau một thời gian, các cây hoa đã trường thành và có thể phục vụ cho du khách tham quan.
Trước dịp tết vừa qua, người ta thấy trong các cây hoa được trồng thì cũng có khá nhiều cây hoa không được đẹp nên lãnh đạo thành phố quyết định được ra phương án bỏ đi một số cây hoa và sắp xếp lại sao cho cảnh quan được hài hòa hơn.
Người chịu trách nhiệm công việc đó đã đánh dấu các cây hoa được đánh giá là đẹp có số
$1$
, các cây hoa còn lại là xấu được đánh số là
$- 1$
. Việc bỏ đi các cây hoa xấu có thể làm cho con đường tham quan không còn nhiều cây hoa nữa nên công việc ở đây cần làm phải đảm bảo tất cả các điều kiện sau:
*
Không được di chuyển cây hoa ở lề đường A sang lề đường B và ngược lại
*
Các cây hoa trên một lề đường không được thay đổi thứ tự vị trí của nhau
*
Một cây hoa của lề đường
$A$
và một cây hoa của lề đường
$B$
sẽ tạo thành một cặp
*
Với một cặp cây hoa được giữ lại phải luôn không được hai cây hoa cùng xấu
*
Số cặp cây hoa được giữ lại là nhiều nhất
Mỗi lề đường đều có
$n$
cây hoa, với lề đường
$A$
cây thứ
$i$
được đánh dấu là giá trị
$ai$
, với lề đường
$B$
cây thứ
$i$
được đánh dấu là giá trị
$bi$
Yêu cầu: Hãy cho biết số cặp cây hoa giữ lại nhiều nhất thỏa mãn tất cả các điều kiện nên trên là bao nhiêu?


## 🧩 Input

Input
Dòng đầu gồm
$n$
$(1 ≤n≤ 1000)$
Trong
$n$
dòng tiếp theo, dòng thứ
$i$
chứa
$2$
số
$ai$
và
$bi$
. (
$ai$
và
$bi$
có giá trị
$1$
hoặc
$- 1$
)


## 💡 Output

Output
Một số nguyên duy nhất là số lượng cặp hoa nhiều nhất được giữ lại thỏa mãn tất cả các điều kiện trên.


## 🧠 Example

### Input

```text
5
-1 -1
1 1
1 -1
-1 -1
-1 1
```

### Output

```text
4
```



## 📝 Note

Note
Với ví dụ: chọn được nhiều nhất là
$4$
cặp cây hoa
Lề đường
$A$
: gồm các cây ở vị trí
$1, 2, 3, 4$
Lề đường
$B$
: gồm các cây ở vị trí
$2, 3, 4, 5$

