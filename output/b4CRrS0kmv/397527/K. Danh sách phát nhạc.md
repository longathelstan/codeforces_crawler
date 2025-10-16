# K. Danh sách phát nhạc

## 📖 Problem

Tấn có một danh sách phát bao gồm
$n$
bài hát được đánh số từ
$1$
đến
$n$
. Bài hát thứ
$i$
có thể loại
$gi$
và nhà tác giả
$wi$
. Tấn muốn tạo một danh sách phát theo cách mà mọi cặp bài hát liền kề đều có cùng tác giả hoặc cùng thể loại (hoặc cả hai). Anh ấy gọi một danh sách nhạc như vậy là thú vị. Cả hai
$gi$
và
$wi$
là các chuỗi có độ dài không quá
$104$
.
Không phải lúc nào cũng có thể tạo danh sách phát thú vị bằng cách sử dụng tất cả các bài hát, vì vậy quá trình xáo trộn diễn ra theo hai bước. Đầu tiên, một số bài hát (có thể là
$0$
) sẽ bị xóa và sau đó các bài hát còn lại trong danh sách sẽ được sắp xếp lại để tạo danh sách phát thú vị.
Vì Tấn không thích khi các bài hát bị xóa khỏi danh sách phát của mình nên anh ấy muốn xoá càng ít bài hát càng tốt.
Yêu cầu:
Hãy giúp anh ấy tìm ra số lần xóa tối thiểu cần thực hiện để có thể sắp xếp lại các bài hát còn lại sao cho danh sách phát trở nên thú vị.


## 🧩 Input

Input
Dòng đầu tiên chứa một số nguyên
$n$
$(1 ≤n≤ 16)$
Sau đó
$n$
dòng tiếp theo, dòng thứ
$i$
trong số đó chứa hai chuỗi chữ cái viết thường
$gi$
và
$wi$
$(1 ≤ |gi|, |wi| ≤ 104)$


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm


## 🧠 Example

### Input

```text
1
pop taylorswift
```

### Output

```text
0
```



## 📝 Note

Note
Ví dụ đầu, danh sách phát đã thú vị sẵn.
Ví dụ hai, nếu bạn xếp các bài hát theo thứ tự
$4, 3, 1, 2$
thì danh sách phát sẽ trở nên thú vị nên bạn không cần phải xóa bất kỳ bài hát nào.
Ví dụ ba, bạn có thể xóa các bài hát
$4, 5, 6, 7$
. Sau đó là danh sách thú vị sẽ là các bài hát theo thứ tự
$1, 2, 3$
.

