# G. Software (7 điểm)

## 📖 Problem

Tâm rất yêu thích lập trình tạo phần mềm. Vào dịp rãnh rỗi Tâm đã thiết kế một phần mềm đơn giản. Màn hình phần mềm gồm
$N$
địa điểm (đánh số từ 1 đến N), trong đó mỗi địa điểm có đặt một bóng đèn ở trạng thái sáng hoặc tắt.
Có
$N- 1$
con đường một chiều nối trực tiếp giữa các cặp địa điểm. Mỗi lần Tâm trạm tay vào địa điểm
$Xi$
di chuyển theo các con đường một chiều, cuối cùng kết thúc tại địa điểm
$1$
. Robot không thay đổi địa điểm ở trạng thái đèn ở địa điểm
$Xi$
và địa điểm
$1$
, các địa điểm còn lại robot đã đi qua thì đèn ở địa điểm đó sẽ thay đổi sang trạng thái ngược lại (sáng thành tắt, tắt thành sáng)
Yêu cầu: Hãy cho biết khi Tâm thực hiện
$K$
lần chạm chạm tay (mỗi lần chạm tay vào một địa điểm) thì sau đó sẽ có tất cả bao nhiêu địa điểm có đèn sáng. Biết rằng robot xuất phát từ địa điểm bất kì luôn có thể di chuyển theo các con đường một chiều đến địa điểm
$1$
.


## 🧩 Input

Input
Dòng đầu tiên gồm
$2$
số nguyên dương
$N$
và
$K$
lần lượt là số địa điểm, số lần chạm tay
$(1 ≤N,K≤ 105)$
Dòng thứ
$2$
gồm
$N$
số nguyên cho biết trạng thái đèn ở
$N$
địa điểm , lần lượt theo thứ tự từ địa điểm
$1$
đến địa điểm
$N$
. Trạng thái đèn tắt là
$0$
, sáng là
$1$
.
Dòng thứ
$i$
trong
$N- 1$
dòng tiếp theo gồm
$2$
số nguyên dương
$Ai$
và
$Bi$
$(1 ≤Ai,Bi≤n)$
cho biết có con đường một chiều nối trực tiếp từ địa điểm
$Ai$
đến
$Bi$
Dòng cuối cùng gồm
$K$
số nguyên dương, trong đó số nguyên thứ
$i$
là
$Xi$
$(1 ≤Xi≤N)$
cho biết địa điểm thứ
$i$
mà tâm thực hiện chạm tay.


## 💡 Output

Output
Số nguyên duy nhất là kết quả cần tìm.


## 🧠 Example

### Input

```text
5 3
1 0 0 0 0
2 1
4 2
3 2
5 4
4 5 4
```

### Output

```text
3
```



## 📝 Note

Note
Giải thích test ví dụ
$1$
: Tâm chạm tay
$3$
lần
Lần
$1$
ở địa điểm
$4$
: robot đi qua các địa điểm
$4, 2, 1$
và thay đổi trạng thái đèn ở địa điểm
$2$
.
Kết quả trạng thái
$5$
đèn theo thứ tự lần lượt là:
$1$
$1$
$0$
$0$
$0$
Lần
$2$
ở địa điểm
$5$
: robot đi qua các địa điểm
$5, 4, 2, 1$
và thay đổi trạng thái đèn ở địa điểm
$4, 2$
.
Kết quả trạng thái
$5$
đèn theo thứ tự lần lượt là:
$1$
$0$
$0$
$1$
$0$
Lần
$3$
ở địa điểm
$4$
: robot đi qua các địa điểm
$4, 2, 1$
và thay đổi trạng thái đèn ở địa điểm
$2$
.
Kết quả trạng thái
$5$
đèn theo thứ tự lần lượt là:
$1$
$1$
$0$
$1$
$0$
Sau
$3$
lần chạm tay, có
$3$
địa điểm có đèn sáng là địa điểm
$1$
,
$2$
,
$4$

