# J. Ma trận 0 1 (5 điểm)

## 📖 Problem

Cho ma trận
$n$
x
$m$
chỉ gồm các số
$0$
hoặc
$1$
biết rằng với ma trận ban đầu từ một ô số
$1$
bất kỳ bạn luôn có thể di chuyển tới toàn bộ ô số
$1$
còn lại thông qua các ô
$1$
khác. Tại ô
$(i,j)$
bạn có thể di chuyển sang
$4$
ô kề cạnh.
Bạn phải chọn ra
$k$
ô số
$1$
khác nhau trong bảng và biến chúng thành
$0$
. Hãy in ra các ô được chọn sao cho sau khi biến chúng thành
$0$
thì từ một ô số
$1$
bất kỳ bạn vẫn có thể di chuyển tới toàn bộ ô số
$1$
còn lại.
Nếu có nhiều đáp án thì hãy in ra
$1$
đáp án bất kỳ, nếu không có đáp án thì hãy in ra "rotdoituyentinh".


## 🧩 Input

Input
Dòng đầu gồm
$3$
số
$n$
,
$m$
,
$k$
$(1≤n,m≤1000)$
$n$
dòng tiếp theo mỗi dòng gồm
$m$
số, mỗi số là
$0$
hoặc
$1$
Dữ liệu đảm bảo
$k$
sẽ luôn sẽ bé hơn số lượng số
$1$
có trong ma trận.


## 💡 Output

Output
Nếu không có đáp án hãy in "rotdoituyentinh".
Nếu có hãy in
$k$
dòng, mỗi dòng gồm
$2$
số nguyên
$(x,y)$
thể hiện ô được chọn nằm ở hàng thứ
$x$
, cột thứ
$y$


## 🧠 Example

### Input

```text
2 2 1
1 1
1 0
```

### Output

```text
1 2
```



## 📝 Note

Note
Với test
$2$
ta có thể chọn
$4$
ô như trong ảnh.
![](https://espresso.codeforces.com/fde132fecb7483e67c19bdc4a4448bff6c84029a.png)
Với test
$2$
ta có thể chọn ô
$(1, 2)$
hoặc
$(2, 1)$
và biến chúng thành
$0$
, cả
$2$
cách đều được chấp nhận. Tuy nhiên ô
$(1, 1)$
sẽ không được vì khi đó từ ô
$(1, 2)$
sẽ không thể tới ô
$(2, 1)$
và ô
$(2, 2)$
cũng sẽ không được vì ô đó không phải số
$1$
.

