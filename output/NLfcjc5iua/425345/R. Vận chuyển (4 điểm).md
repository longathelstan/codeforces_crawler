# R. Vận chuyển (4 điểm)

## 📖 Problem

Tuấn là quản lý của một Công ty chuyên vận chuyển hàng hóa liên tỉnh bằng đường bộ. Công ty cần chuyển một gói hàng từ Hà Nội đến Sài Gòn, do không có chuyến chuyển thẳng từ Hà Nội đến Sài Gòn mà phải qua trạm trung chuyển tại Huế.
Có
$N$
chuyến vận chuyển từ Hà Nội đến Huế, chuyến thứ
$i$
xuất phát vào thời điểm
$ai$
và các chuyến vận chuyển đều có thời gian là
$Ta$
Có
$M$
chuyến vận chuyển từ Huế đến Sài Gòn, chuyến thứ
$j$
xuất phát vào thời điểm
$bj$
và các chuyến vận chuyển đều có thời gian là
$Tb$
Nếu công ty sử dụng chuyển vận chuyển thứ
$i$
xuất phát từ Hà Nội đến Huế, sau đó sử dụng chuyến vận chuyển thứ
$j$
xuất từ Huế tới Sài Gòn thì phải thỏa mãn
$bj≥ai+Ta$
Công ty luôn muốn chọn phương án vận chuyển để gói hàng có thể đến Sài Gòn sớm nhất. Tuy nhiên, vì gói hàng bị lỗi nên Tuấn lại muốn gói hàng không thể đến được nơi nhận nhằm mục đích khắc phục lỗi hoặc nếu luôn tồn tại cách vận chuyển gói hàng đến Sài Gòn thì phải đến muộn nhất có thể để Tuấn tăng thêm thời gian xử lý. Tuấn được phép hủy tối đa
$K$
chuyến vận chuyển trong tất cả
$N+M$
chuyến để thực hiện mong muốn trên.
Yêu cầu: Hãy xác định thời điểm gói hàng đến Sài Gòn khi Tuấn hủy các chuyến vận chuyển khiến gói hàng đến muộn nhất có thể hoặc thông báo hàng không thể đến được nơi nhận.


## 🧩 Input

Input
Dòng đầu gồm
$5$
số nguyên dương
$N,M,Ta,Tb,K$
$(1 ≤N,M≤ 106, 1 ≤Ta,Tb≤ 109, 0 ≤K≤N+M)$
Dòng thứ hai gồm
$N$
số nguyên dương
$a1,a2, ...,aN$
$(1 ≤a1<a2< ... <aN≤ 109)$
Dòng thứ ba gồm
$M$
số nguyên dương
$b1,b2, ...,bM$
$(1 ≤b1<b2< ... <bM≤ 109)$
Các số trên cùng một dòng cách nhau bởi dấu cách trống.


## 💡 Output

Output
Một số nguyên là thời điểm đến nơi nhận khi Tuấn hủy các chuyến vận chuyển khiến gói hàng đến Sài Gòn muộn nhất có thể hoặc thông báo gói hàng không thể đến được. Nếu gói hàng không thể đến nơi được thì ghi
$- 1$


## 🧠 Example

### Input

```text
4 5 1 1 2
1 3 5 7
1 2 3 9 10
```

### Output

```text
11
```



## 📝 Note

Note
Ví dụ
$1$
:
Tuấn được phép hủy tối đa
$2$
chuyến
Tuấn hủy chuyến thời điểm
$a1$
, gói hàng phải đi chuyến thời điểm
$a2$
và đến Huế thời gian là
$4$
. Tiếp tục hủy chuyến thời điểm
$b4$
và di chuyển thời điểm
$b5$
, khi đó thời gian tới Sài Gòn là:
$b5+Tb= 10 + 1 = 11$
Ví dụ
$2$
:
Tuấn được phép huy tối đa
$3$
chuyến
Tuấn hủy chuyến thời điểm
$a1$
và chuyến thời điểm
$a2$
, khi đó gói hàng không thể đến được Sài Gòn
Ví dụ
$3$
:
Tuấn được phép hủy tối đa
$1$
chuyến
Gói hàng được gửi theo chuyến thời điểm
$a1$
. Tuấn hủy chuyến thời điểm
$b1$
, gói hàng phải di chuyển thời điểm
$b2$
và đến Sài Gòn là:
$b2+Tb= 7 + 2 = 9$

