# F. Việt Nam

## 📖 Problem

Việt Nam là một đất nước có
$n$
thành phố tuyệt đẹp và
$m$
con đường hai chiều. Giống như mọi đất nước xinh đẹp khác, Việt Nam cũng có tình trạng tắc đường.
Mỗi con đường có một giá trị đông đúc. Giá trị đông đúc của một tuyến đường được định nghĩa là giá trị đông đúc lớn nhất trong tất cả các con đường trên tuyến đó. Ví dụ, nếu các giá trị đông đúc của tất cả các con đường là
$[1, 4, 5, 6, 3]$
, thì giá trị đông đúc của tuyến đường sẽ là max(
$1, 4, 5, 6, 3$
) =
$6$
.
​Mỗi thành phố thứ
$i$
biểu thị loại tòa nhà
$Ti$
có trong thành phố đó.
Tấn vừa bắt đầu kỳ nghỉ ở Việt Nam. Anh ấy muốn đi từ thành phố
$x$
đến thành phố
$y$
. Ngoài ra, anh ấy cũng muốn nhìn thấy ít nhất
$k$
loại tòa nhà
$Ti$
khác nhau trên đường đi từ
$x$
đến
$y$
. Khi chọn một tuyến đường từ
$x$
đến
$y$
có ít nhất
$k$
loại tòa nhà khác nhau, Tấn luôn chọn tuyến đường có giá trị đông đúc nhỏ nhất.
Bạn sẽ nhận được
$q$
truy vấn. Mỗi truy vấn có dạng ba số nguyên cách nhau bởi dấu cách,
$xi$
$yi$
$ki$
biểu thị thành phố xuất phát, thành phố đích và số lượng tối thiểu các loại tòa nhà khác nhau mà Tấn muốn nhìn thấy trên đường đi.
Yêu cầu:
Với mỗi truy vấn hãy đưa ra giá trị đông đúc nhỏ nhất của tuyến đường thoả mãn. Nếu không tồn tại tuyến đường nào thỏa mãn điều kiện, in ra
$−1$
.
Lưu ý
: Một tuyến đường có thể chứa chu trình (tức là có thể đi qua cùng một con đường hoặc thành phố nhiều lần).


## 🧩 Input

Input
Dòng đầu gồm
$n$
,
$m$
,
$q$
$(1 ≤n,m,q≤ 105)$
Dòng tiếp theo gồm
$n$
số, số thứ
$i$
biểu thị loại tòa nhà
$Ti$
$(1 ≤Ti≤ 109)$
Sau đó là
$m$
dòng, dòng thứ
$i$
gồm
$3$
số
$ui$
,
$vi$
và
$ci$
thể hiện có cạnh nối từ
$ui$
tới
$vi$
với giá trị đông đúc là
$ci$
$(1 ≤ci≤ 109, 1 ≤ui,vi≤n)$
Sau đó là
$q$
dòng, dòng thứ
$i$
gồm
$3$
số
$xi$
,
$yi$
và
$ki$
$(1 ≤xi,yi,ki≤n)$


## 💡 Output

Output
Gồm
$q$
dòng ứng với
$q$
truy vấn


## 🧠 Example

### Input

```text
7 6 1
1 1 4 5 1 3 2
1 2 3
2 6 2
2 3 4
3 4 3
2 4 9
5 7 9
1 2 4
```

### Output

```text
4
```



## 📝 Note

Note
Sơ đồ dưới đây mô tả các thành phố được cung cấp trong Dữ liệu Mẫu. Các giá trị toà nhà
$Ti$
khác nhau của nó được hiển thị bằng các màu sắc khác nhau.
![](https://espresso.codeforces.com/e105314a5f42b9f81daa0b063218ec8885cf2901.png)
Đường đi cho truy vấn cuối cùng
$1$
$2$
$4$
sẽ là
$1$
->
$2$
->
$3$
->
$4$
->
$3$
->
$2$
->
$6$
->
$2$
. Tấn nhìn thấy loại tòa nhà đầu tiên của mình ở các thành phố
$1$
và
$2$
, loại tòa nhà thứ hai ở thành phố
$3$
, loại tòa nhà thứ ba ở thành phố
$4$
và loại tòa nhà thứ tư ở thành phố
$6$
.
Giá trị đông đúc cho mỗi con đường đã đi trên lộ trình này là
$[3, 4, 3, 3, 4, 2, 2]$
; giá trị lớn nhất trong số này là
$4$
. Do đó, chúng ta in
$4$
trên một dòng mới.

