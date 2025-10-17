# ZW. Light

## 📖 Problem

Một giàn đèn trang trí kích thước
$m$
x
$n$
, các hàng được đánh số từ
$1$
đến
$m$
từ trên xuống dưới, các cột đánh số từ
$1$
đến
$n$
từ trái sang phải. Ô nằm giao giữa hàng r và cột c gọi là ô
$(r,c)$
.
Trên mỗi ô có một bóng đèn, mỗi bóng đèn có ba trạng thái: hoặc tắt, hoặc bật sáng màu xanh, hoặc bật sáng màu đỏ. Có
$k$
ô phân biệt
$(r1,c1), (r2,c2), ..., (rk,ck)$
của giàn đèn, mỗi ô có một công tắc điều khiển. Khi tác động vào công tắc của ô
$(ri,ci)$
thì những đèn nằm trong các ô thuộc hình chữ nhật có ô trái trên là
$(ri,ci)$
và ô phải dưới là
$(xi,yi)$
sẽ đổi trạng thái
$(t= 1, 2, ...,k)$
. Cụ thể, các đèn nằm trong các ô
$(u,v)$
mà
$ri≤u≤ci$
và
$ci≤v≤yi$
sẽ thay đổi theo qui tắc: nếu đèn đang ở trong trạng thái tắt sẽ chuyển sang trạng thái bật sáng màu xanh,nếu đèn đang ở trạng thái bật sáng màu xanh sẽ chuyển sang trạng thái bật sáng màu đỏ, còn nếu đèn đang ở trạng thái bật sáng màu đỏ sẽ chuyển sang trạng thái tắt. Mỗi công tắt có thể tác động nhiều lần.
Cho thông tin trạng thái ban đầu của đèn trên giàn và công tắt. Hãy tìm cách đưa tất cả các đèn về cùng một trạng thái bật sáng màu xanh hoặc bật sáng màu đỏ với số lần tác động là ít nhất.


## 🧩 Input

Input
Dòng đầu chứa
$3$
số nguyên dương
$m$
,
$n$
,
$k$
$(1 ≤k≤m.n≤ 105)$
Dòng thứ
$i$
trong số
$m$
dòng tiếp theo chứa
$n$
số nguyên nhận giá trị
$0$
,
$1$
hoặc
$2$
. Số thứ
$j$
$(j= 1, 2, ...,n)$
mô tả trạng thái đèn ở ô
$(i,j)$
là tắt, bật sáng màu xanh hoặc bật sáng màu đỏ tương ứng với các giá trị
$0$
,
$1$
hoặc
$2$
Dòng thứ
$i$
trong số
$k$
dòng tiếp theo chứa bốn số nguyên dương
$ri$
,
$ci$
,
$xi$
,
$yi$
$(1 ≤ri≤xi≤m)$
$(1 ≤ci≤yi≤n)$


## 💡 Output

Output
Số lần tác động ít nhất để các đèn về cùng một trạng thái sáng màu xanh hoặc sáng màu đỏ, nếu không tồn tại cách tác động thì in ra
$- 1$
.


## 🧠 Example

### Input

```text
2 3 3
2 1 0
2 1 0
1 1 2 3
1 2 2 3
1 3 2 3
```

### Output

```text
2
```



## 📝 Note

Note
Trước tiên tác động vào công tắc ở ô
$(1, 3)$
, sau đó tác động vào công tắt ở ô
$(1, 2)$
, khi đó tất cả các đèn trên giàn đều sáng màu đỏ.

