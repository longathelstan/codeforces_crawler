# I. Medium way

## 📖 Problem

Cho 2 điểm trên không gian
$n$
chiều
$(x1,x2, ...,xn)$
và
$(y1,y2, ...,yn)$
$(x1≤y1,x2≤y2, ...,xn≤yn)$
. Ta sẽ xuất phát tại điểm
$(x1,x2, ...,xn)$
tại mỗi bước ta có thể chọn
$1$
chiều và tăng vị trí
$x$
của chiều đó lên
$1$
, hãy tìm số cách để tới được ô
$(y1,y2, ...,yn)$
Vì số cách có thể rất lớn hãy in đáp án chia dư cho
$109+ 7$


## 🧩 Input

Input
Gồm nhiều bộ test
$≤ 104$
, mỗi bộ test gồm.
Số
$n$
$(1 ≤n≤ 50)$
Dòng tiếp theo gồm
$n$
số
$x1,x2, ...,xn$
$(0 ≤xi≤ 500)$
Dòng tiếp theo gồm
$n$
số
$y1,y2, ...,yn$
$(0 ≤yi≤ 500)$
$0 ≤xi≤yi≤ 500$
Input sẽ kết thúc với số
$0$
ở cuối.


## 💡 Output

Output
Gồm nhiều dòng ứng với số lượng số test


## 🧠 Example

### Input

```text
2
2 1
5 5
4
0 0 0 0
1 2 3 4
5
1 2 3 4 5
8 5 6 4 8
5
0 0 0 0 0
100 100 100 100 100
0
```

### Output

```text
35
12600
19219200
257055440
```


