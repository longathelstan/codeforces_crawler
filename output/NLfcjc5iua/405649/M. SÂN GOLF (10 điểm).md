# M. SÂN GOLF (10 điểm)

## 📖 Problem

Sân golf được biểu diễn bởi một lưới kích thước
$M$
x
$N$
$(1≤M,N≤500)$
. Mỗi ô của lưới có độ cao trong khoảng
$0$
đến
$109$
so với mực nước biển.
Tại một vài ô trong lưới này là các vị trí có đặt lỗ, tức là nơi vận động viên sẽ đánh bóng rơi vào đó và bắt buộc sẽ đi đến đó để nhặt bóng.
Ban tổ chức của Olympics muốn đánh giá độ chênh lệch độ cao
$D$
của sân golf bằng cách làm như sau:
Cho một nhân viên bắt đầu di chuyển từ một vị trí đặt lỗ bất kỳ đến một trong bốn ô kề cạnh với ô đang đứng, có trị tuyệt đối chênh lệch độ cao không quá D. Tại ô mới này, anh ta lại di chuyển tiếp sang một trong bốn ô kề cạnh có trị tuyệt đối chênh lệch độ cao không quá D. Cứ thế tiếp tục cho đến khi có thể đến được tất cả các lỗ.
Yêu cầu: Hãy xác định độ chênh lệch độ cao D nhỏ nhất mà từ một lỗ bất kỳ có thể đến được tất cả các lỗ còn lại.


## 🧩 Input

Input
Dòng 1: chứa 2 số nguyên M, N.
M dòng tiếp theo: mỗi dòng chứa N số nguyên là độ cao của ô.
M dòng tiếp theo: mỗi dòng chứa N giá trị là 0 hoặc 1, trong đó ô có giá trị 1 cho biết tại vị trí đó có lỗ, ngược lại thì tại đó không có lỗ. Các số ghi trên cùng một dòng cách nhau bởi ít nhất một kí tự trắng.


## 💡 Output

Output
Gồm 1 dòng duy nhất ghi số nguyên dương D cần tìm.


## 🧠 Example

### Input

```text
3 5
25 21 18 76 15
19 22 20 16 26
18 17 40 60 80
1 0 0 0 1
0 0 0 0 0
0 0 0 0 1
```

### Output

```text
20
```



## 📝 Note

Note
-Với
$D$
=
$20$
: từ lỗ
$(1, 1)$
ta đến được các lỗ
$(1, 5)$
,
$(3, 5)$
hoặc theo hướng ngược lại.
-Với
$D$
=
$19$
, từ lỗ
$(1, 1)$
hoặc lỗ
$(1, 5)$
ta không thể đi đến được lỗ
$(3, 5)$
.

