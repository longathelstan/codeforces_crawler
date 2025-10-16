# I. Bán bánh (5 điểm)

## 📖 Problem

![](https://espresso.codeforces.com/99a84493e4f86e9332ee712ecda552b5b65bb040.png)
Hải quyết định mở một tiệm bánh. Vào ngày khai trương, anh ấy đã nướng
$n$
chiếc bánh để bán. Giá thông thường của một chiếc bánh là
$a$
xu, nhưng để thu hút khách hàng, Hải đã tổ chức chương trình khuyến mãi như sau:
*
Hải chọn một số nguyên
$k$
$(0 ≤k≤min(n,b))$
.
*
Hải bán
$k$
chiếc bánh đầu tiên với giá đã được điều chỉnh. Cụ thể, giá của chiếc bánh thứ
$i$
$(1 ≤i≤k)$
được tính theo công thức:
$(b-i+ 1)$
xu.
*
Các chiếc bánh còn lại
$(n-k)$
sẽ được bán với giá
$a$
xu mỗi chiếc.
Lưu ý:
rằng Hải có thể chọn
$k= 0$
, trong trường hợp này, tất cả bánh sẽ được bán với giá
$a$
xu mỗi chiếc.
Yêu cầu:
giúp Hải xác định lợi nhuận tối đa mà anh ấy có thể đạt được khi bán hết
$n$
chiếc bánh.


## 🧩 Input

Input
Dòng đầu tiên chứa một số nguyên duy nhất
$t$
$(1 ≤t≤ 104)$
là số lượng truy vấn
Mỗi truy vấn gồm
$3$
số
$n$
,
$a$
,
$b$
$(1 ≤n,a,b≤ 109)$
— số lượng bánh, giá thông thường của một chiếc bánh, và giá của chiếc bánh đầu tiên được bán với giá đã điều chỉnh.


## 💡 Output

Output
Gồm
$t$
dòng ứng với
$t$
truy vấn


## 🧠 Example

### Input

```text
7
4 4 5
5 5 9
10 10 5
5 5 11
1000000000 1000000000 1000000000
1000000000 1000000000 1
1000 1 1000
```

### Output

```text
17
35
100
45
1000000000000000000
1000000000000000000
500500
```


