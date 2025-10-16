# F. Mua vé 2

## 📖 Problem

Bạn đã lên kế hoạch đi tàu trước cho
$n$
ngày. Danh sách đó được thể hiện dưới mảng
$d$
, trong đó nếu
$di= 1$
thì bạn cần đi tàu vào ngày thứ
$i$
, còn
$di= 0$
nếu không cần. Vé tàu được bán theo ba cách khác nhau:
*
Vé 1 ngày được bán với giá
$a$
*
Thẻ 7 ngày được bán với giá
$b$
*
Thẻ 30 ngày được bán với giá
$c$
Thẻ cho phép đi lại nhiều ngày liên tục.
Ví dụ: nếu chúng ta nhận được thẻ
$7$
ngày vào ngày thứ
$2$
thì chúng ta có thể đi tàu trong
$7$
ngày:
$2, 3, 4, 5, 6, 7$
và
$8$
.
Hãy tính số tiền tối thiểu bạn cần để thực hiện đúng kế hoạch đi tàu mà bạn đã đề ra trong
$n$
ngày.


## 🧩 Input

Input
Dòng đầu gồm
$n$
,
$a$
,
$b$
,
$c$
$(1 ≤n≤ 106, 1 ≤a<b<c≤ 106)$
Dòng tiếp theo gồm
$n$
, số thứ
$i$
là giá trị
$di$
thể hiện có cần đi tàu vào ngày thứ
$i$
không (
$0 ≤di≤ 1)$


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm


## 🧠 Example

### Input

```text
8 2 7 15
1 0 0 1 0 1 1 1
```

### Output

```text
9
```



## 📝 Note

Note
Với ví dụ
$1$
:
Ta có thể mua vé
$1$
ngày vào ngày thứ nhất, mua thẻ
$7$
ngày vào ngày thứ tư
Với ví du
$2$
:
Ta có thể mua thẻ
$30$
ngày vào ngày thứ nhất

