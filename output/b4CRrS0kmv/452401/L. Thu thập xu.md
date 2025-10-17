# L. Thu thập xu

## 📖 Problem

Một trò chơi có
$n$
căn phòng và
$m$
đường hầm nối giữa các phòng. Mỗi căn phòng chứa một số lượng xu nhất định.
Yêu cầu:
Tìm số lượng xu lớn nhất mà bạn có thể thu thập được khi di chuyển qua các đường hầm, với điều kiện bạn được tự do chọn phòng bắt đầu và phòng kết thúc.


## 🧩 Input

Input
*
Dòng đầu tiên chứa hai số nguyên
$n$
và
$m$
$(1 ≤n≤ 105, 1 ≤m≤ 2.105)$
: số lượng căn phòng và số đường hầm. Các phòng được đánh số từ
$1, 2, ...,n$
.
*
Dòng thứ hai chứa
$n$
số nguyên
$k1,k2, ...,kn$
$(1 ≤ki≤ 109)$
: số xu có trong mỗi căn phòng.
*
Sau đó là
$m$
dòng, mỗi dòng chứa hai số nguyên
$a$
và
$b$
$(1 ≤a,b≤n)$
: biểu diễn một đường hầm một chiều đi từ phòng
$a$
tới phòng
$b$
.


## 💡 Output

Output
Gồm một dòng duy nhất là kết quả cần tìm


## 🧠 Example

### Input

```text
4 4
4 5 2 7
1 2
2 1
1 3
2 4
```

### Output

```text
16
```


