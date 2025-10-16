# ZZJ. Chất nhờn

## 📖 Problem

Có
$n$
chất nhờn, chất nhờ thứ
$i$
có độ lớn là
$ai$
, bạn phải ghép
$2$
chất nhờn bất kỳ với nhau thành một chất nhờn to hơn tới khi chỉ còn một chất nhờn duy nhất.
Mỗi lần ghép bạn có thể chọn
$2$
chất nhờ ở bên
cạnh nhau
và ghép chúng lại để được cục nhờn có độ lớn
$x+y$
với
$x,y$
là độ lớn của
$2$
chất nhờn được ghép. Sau khi ghép vị trí của chất nhờn sẽ không thay đổi. Mỗi lần ghép như vậy bạn sẽ tốn
$x+y$
đồng.
Hãy tìm số tiền ít nhất để ghép các chất nhờn thành một chất nhờn duy nhất.


## 🧩 Input

Input
Dòng đầu tiêm gồm số
$n$
$(2 ≤n≤ 400)$
Dòng tiếp theo gồm
$n$
số
$a1,a2, ...an$
$(1 ≤ai≤ 109)$


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm


## 🧠 Example

### Input

```text
4
10 20 30 40
```

### Output

```text
190
```



## 📝 Note

Note
Test
$1$
:
Một trong những cách tối ưu nhất là:
(
10,20
,30,40) -> (
30
,30,40)
(
30,30
,40) -> (
60
,40)
(
60,40
) -> (100)
Tổng chi phí là
$10 + 20 + 30 + 30 + 60 + 40 = 190$
Test
$2$
Một trong những cách tối ưu nhất là:
(10,
10,10
,10,10) -> (10,
20
,10,10)
(10,20,
10,10
) -> (10,20,
20
)
(
10,20
,20) -> (
30
,20)
(
30,20
) -> (
50
)
Tổng chi phí là
$10 + 10 + 10 + 10 + 10 + 20 + 30 + 20 = 120$

