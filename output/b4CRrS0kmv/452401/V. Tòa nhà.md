# V. Tòa nhà

## 📖 Problem

Thành phố nơi Alice sinh sống có
$n$
toà nhà. Trên bản thiết kế, mặt bằng nền mỗi tòa nhà đều là hình chữ nhật có các cạnh song song với trục tọa độ, với các đỉnh đều có tọa độ nguyên trên hệ trục tọa độ. Hai tòa nhà gọi là liền kề nếu có hai đường biên của hai hình chữ nhật mặt nền tương ứng hai tòa nhà đó có ít nhất một điểm chung. Để thuận tiện đi lại giữa các tòa nhà, người ta xây dựng một lối đi tắt hai chiều giữa mỗi cặp tòa nhà liền kề.
Alice rất thích thú với cách thiết kế các tòa nhà của thành phố và thường xuyên đi lại giữa các tòa nhà thông qua các lối đi tắt này. Sau một thời gian khám phá, Alice nhận thấy có một số lối đi tắt là độc đạo. Một lối đi tắt giữa hai tòa nhà
$u$
và
$v$
gọi là độc đạo nếu như sau khi đi từ
$u$
sang
$v$
qua lối đi này thì không có cách đi nào quay trở lại
$u$
thông qua các lối đi tắt khác ngoài lối đi tắt từ
$v$
về
$u$
.
Với mỗi cặp tòa nhà
$(u,v)$
có lối đi tắt là độc đạo, Alice tiếp tục khám phá nếu như đóng cửa lối đi độc đạo này thì xuất phát từ
$u$
Alice có thể tham quan được tối đa
$du$
tòa nhà, và nếu xuất phát từ
$v$
Alice có thể tham quan được tối đa
$dv$
tòa nhà. Khoảng chênh lệch giữa
$du$
và
$dv$
là giá trị
$|du-dv|$
.
Yêu cầu:
Biết tọa độ các đỉnh hình chữ nhật mặt nền tương ứng của các tòa nhà, hãy giúp Alice tìm cặp tòa nhà
$(u,v)$
có lối đi tắt độc đạo sao cho khoảng chênh lệch giữa
$du$
và
$dv$
là nhỏ nhất.


## 🧩 Input

Input
Dòng thứ nhất chứa một số nguyên dương
$n$
là số lượng tòa nhà cao tầng
$(1 ≤n≤ 105)$
;
Dòng thứ
$i$
trong số
$n$
dòng tiếp theo chứa
$4$
số nguyên không âm
$xi$
,
$yi$
,
$pi$
,
$qi$
với
$(xi,yi)$
là tọa độ của đỉnh trái trên và
$(pi,qi)$
là tọa độ của đỉnh phải dưới của hình chữ nhật biểu thị mặt nền tòa nhà thứ
$i$
trên bản đồ quy hoạch. Dữ liệu đảm bảo
$xi$
<
$pi$
và
$yi$
>
$qi$
và hai hình chữ nhật bất kỳ có thể tiếp xúc nhưng không giao nhau.


## 💡 Output

Output
Một số nguyên duy nhất là khoảng chênh lệch nhỏ nhất tìm được. Nếu không tồn tại lối đi tắt độc đạo thì in ra số
$- 1$
.


## 🧠 Example

### Input

```text
6
1 3 4 1
4 1 8 0
6 2 9 1
4 4 8 2
5 6 7 4
6 7 9 6
```

### Output

```text
2
```



## 📝 Note

Note
![](https://espresso.codeforces.com/e543f0691679a2075b0e2c9c1ab4f1fc82346bfd.png)

