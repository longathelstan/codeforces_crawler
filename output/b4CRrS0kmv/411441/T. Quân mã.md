# T. Quân mã

## 📖 Problem

Một quân mã được đặt ở ô trái trên của bàn cờ kích thước
$8$
x
$8$
. Bạn được phép di chuyển quân mã đó tối đa
$k$
lần. Hãy đếm số đường đi có thể có với quân mã đó và in ra kết quả dưới dạng modulo cho
$232$
.
Cụ thể hơn, một đường đi là một tập các ô
$(C1,C2, ...,Cs)$
sao cho
$1 ≤s≤k+ 1$
và quân mã có thể đi từ ô
$ci$
đến ô
$Ci+ 1$
với mọi
$i$
.
(Một nước đi của quân mã trong bàn cờ vua có dạng
$1$
ô vuông theo chiều ngang và
$2$
ô vuông theo chiều dọc hoặc
$2$
ô vuông theo chiều ngang và
$1$
ô vuông theo chiều dọc)


## 🧩 Input

Input
Gồm số
$k$
$(1 ≤k≤ 1018)$


## 💡 Output

Output
In ra kết quả dưới dạng modulo cho
$232= 4294967296$


## 🧠 Example

### Input

```text
1
```

### Output

```text
3
```



## 📝 Note

Note
Với ví dụ
$1$
Quân mã có thể đứng nguyên ở ô
$(1, 1)$
hoặc có thể di chuyển tới các ô
$(2, 3)$
hoặc
$(3, 2)$
. Vậy kết quả là
$3$
.

