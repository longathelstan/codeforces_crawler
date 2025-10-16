# F. Truy vết Thanh và kỳ nghỉ

## 📖 Problem

Thanh là một người rất thích đi du lịch, Thanh muốn đi khắp mọi nơi từ Bắc vào Nam và đợt này Thanh sẽ đi du lịch ở một hòn đảo tại Khánh Hòa.
Kì nghỉ của Thanh gồm
$n$
ngày, để phục vụ cho thú vui tao nhã của mình thì Thanh đã nghĩ ra
$3$
hoạt động để làm mỗi ngày đó là:
$1$
: Đi bơi. Nếu Thanh đi bơi ở ngày thứ
$i$
thì độ vui mà Thanh nhận được ngày hôm đó là
$ai$
.
$2$
: Bắt bọ. Nếu Thanh bắt bọ ở ngày thứ
$i$
thì độ vui mà Thanh nhận được ngày hôm đó là
$bi$
.
$3$
: Xây lâu đài cát. Nếu Thanh xây lâu đài cát ở ngày thứ
$i$
thì độ vui mà Thanh nhận được ngày hôm đó là
$ci$
.
Do thời gian có hạn nên mỗi ngày Thanh chỉ được làm
$1$
trong
$3$
hoạt động trên. Vì là một người dễ chán nên Thanh sẽ không làm lại hoạt động mà mình đã làm ngày hôm trước.
Yêu cầu:
Dòng một đưa ra độ vui lớn nhất mà Thanh có thể nhận được trong
$n$
ngày nghỉ, dòng hai gồm
$n$
số cách nhau bởi dấu cách số thứ
$i$
là hành động Thanh sẽ làm ở ngày thứ
$i$
sao cho tổng độ vui sau
$n$
ngày là lớn nhất, số thứ
$i$
là
$1$
nếu đi bơi,
$2$
nếu bắt bọ,
$3$
nếu xây lâu đài cát, nếu có nhiều cách hãy in ra một cách bất kỳ.


## 🧩 Input

Input
Dòng đầu gồm
$n$
$(1 ≤n≤ 105)$
, là số ngày trong kì nghỉ của Thanh.
Dòng thứ
$i$
trong
$n$
dòng tiếp theo gồm
$ai$
,
$bi$
,
$ci$
$(0 ≤ai,bi,ci≤ 109)$
, lần lượt là độ vui vẻ Thanh nhận được nếu đi bơi, bắt bọ, xây lâu đài cát trong ngày thứ
$i$
.


## 💡 Output

Output
Gồm hai dòng ứng với đáp án cần tìm


## 🧠 Example

### Input

```text
2
0 2 3
0 2 4
```

### Output

```text
6
2 3
```



## 📝 Note

Note
Ở test
$1$
:
Cách tối ưu nhất là: Bắt bọ ở ngày thứ nhất, xây lâu đài cát ở ngày thứ hai. Tổng độ vui nhận được là
$2 + 4 = 6$
.
Thanh không thể đi xây lâu đài cát ở cả
$2$
ngày vì nếu vậy sẽ không thỏa không có
$2$
ngày liên tiếp làm cùng
$1$
hoạt động.
Ở test
$2$
:
Cách tối ưu nhất là: xây lâu đài cát ở ngày thứ nhất, bắt bọ ở ngày thứ hai, xây lâu đài cát ở ngày thứ ba. Tổng độ vui nhận được là
$70 + 50 + 90 = 210$
.
Ở test
$3$
:
Cách tối ưu nhất là: xây lâu đài cát -> đi bơi -> bắt bọ -> đi bơi -> xây lâu đài cát -> bắt bọ -> đi bơi. Tổng độ vui nhận được là
$8 + 8 + 5 + 7 + 8 + 3 + 7 = 46$
.

