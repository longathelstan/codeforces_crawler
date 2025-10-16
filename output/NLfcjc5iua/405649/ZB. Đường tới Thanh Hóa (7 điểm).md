# ZB. Đường tới Thanh Hóa (7 điểm)

## 📖 Problem

Đường từ Nha Trang tới Thanh Hóa có thể được mô tả dưới ma trận
$n$
x
$m$
với Nha Trang ở ô
$(1, 1)$
và Thanh Hóa ở ô
$(n,m)$
, vì bảo mật ở đây rất nghiêm nên sẽ có
$k$
chốt chặn trên đường đi, chốt chặn thứ
$i$
sẽ có vị trí tại ô
$(xi,yi)$
với bán kính chặn là
$ri$
. Một ô
$(xj,yj)$
gọi là bị chặn nếu khoảng cách từ ô đó tới
$1$
chốt chặn bất kỳ thỏa
$(xi-xj)2+ (yi-yj)2≤r2$
.
Bạn sẽ xuất phát từ Nha Trang và điểm tới bạn sẽ là Thanh Hóa, tại mỗi lượt bạn có thể bước tới
$1$
trong
$4$
ô kề cạnh nếu ô đó không bị chặn. Hãy tìm số bước ít nhất để bạn tới được Thanh Hóa. Nếu không có đường đi nào hãy in
$- 1$


## 🧩 Input

Input
Dòng đầu gồm
$3$
số nguyên
$n$
,
$m$
và
$k$
$(1 ≤n,m≤ 1000, 1 ≤k≤ 105)$
$k$
dòng tiếp theo mỗi dòng gồm
$3$
số nguyên
$xi,yi$
và
$ri$
là tọa độ và bán kính chặn của chốt chặn thứ
$i$
$(1 ≤xi≤n, 1 ≤yi≤m, 0 ≤ri≤n+m)$
.


## 💡 Output

Output
Gồm một dòng duy nhất là đường đi ngắn nhất cần tìm


## 🧠 Example

### Input

```text
3 5 2
1 5 1
3 1 1
```

### Output

```text
6
```



## 📝 Note

Note
$1$
: là ô bị chặn
$0$
: là ô trống
Test ví dụ
$1$
$00011$
$10001$
$11000$
Đường đi ngắn nhất là:
$(1, 1)$
->
$(1, 2)$
->
$(2, 2)$
->
$(2, 3)$
->
$(2, 4)$
->
$(3, 4)$
->
$(3, 5)$
Test ví dụ
$2$
$00100$
$01110$
$00100$
Test ví dụ
$3$
$00111$
$00111$
$10011$
$11000$
$11100$

