# ZQ. solbin

## 📖 Problem

Spir là robot tự hành được trung tâm vũ trụ NAS phóng lên để thám hiểm bề mặt sao hỏa. Spir được trang bị một tấm pin năng lượng mặt trời dưới dạng một tấm bảng gồm
$m$
hàng và
$n$
cột, mỗi ô là một miếng pin hình vuông. Các hàng được đánh số từ trên xuống dưới lần lượt là
$1, 2, ...,m$
. Các cột được đánh số từ trái sang phải lần lượt là
$1, 2, ...,n$
. Tại thời điểm ban đầu lúc phóng lên, miếng pin tọa độ
$(i,j)$
ở hàng
$i$
cột
$j$
được thiết lập mức hấp thụ là
$aij$
. Mức hấp thụ của mảng pin hình chữ nhật bất kỳ nằm trong tấm pin bằng tổng mức của các miếng pin trong mảng đó. Các miếng pin có thể điều khiển để thay đổi mức hấp thụ, do đó mức hấp thụ của một mảng pin hình chữ nhật có thể thay đổi ở các thời điểm khác nhau.
NAS thiết kế
$2$
lệnh điều khiển
$R$
và
$D$
để điều chỉnh mức độ hấp thụ của các miếng pin. Khi nhận một lệnh
$R$
, đồng loạt các miếng pin sẽ được thiết lập sang mức hấp thụ ngay trước khi nhận lệnh này của miếng pin liền kề bên phải cùng hàng. Mỗi miếng pin cuối hàng được thiết lập hấp thụ sang mức hấp thụ của miếng pin đầu hàng đó. Khi nhận một lệnh
$D$
, đồng loạt mỗi miếng pin sẽ được thiết lập sang mức hấp thụ ngay trước khi nhận lệnh này của miếng pin liền kề bên dưới cùng cột. Mỗi miếng pin ở cuối cùng được thiết lập sang mức hấp thụ của miếng pin đầu cột đó.
Để điều khiển tấm pin của Spir, các kỹ sư NAS sử dụng các tín hiệu điều khiển chứa
$2$
số nguyên
$x$
,
$y$
tương ứng với số lệnh
$R$
và lệnh
$D$
cần áp dụng. Khi nhận được tín hiệu điều khiển, từng lệnh trong
$x$
lệnh
$R$
và sau đó từng lệnh trong
$y$
lệnh
$D$
sẽ tuần tự được thực hiện. Chú ý rằng trạng thái của tấm pin thu được sau tác động của mỗi lệnh là trạng thái tác động của lệnh kế tiếp. Trạng thái của tấm pin thu được sau mỗi tín hiệu điều khiển là trạng thái tác động của lệnh đầu tiên trong tín hiệu điều khiển tiếp theo.
Hãy giúp kỹ sư NAS tính toán mức độ hấp thụ của mảng pin hình chữ nhật mà họ quan tâm taị một số thời điểm.


## 🧩 Input

Input
Dòng thứ nhất chứa
$2$
số nguyên
$m$
và
$n$
$(1 ≤n,m≤ 500)$
lần lượt là số hàng và số cột của tấm pin đó
Dòng thứ
$i$
trong số
$m$
dòng tiếp theo chứa
$n$
số nguyên dương
$aij$
$(1 ≤aij≤ 1000)$
là mức hấp thụ được thiết lập lúc ban đầu của các miếng pin trên hàng thứ
$i$
Dòng tiếp theo chứa một số nguyên dương
$q$
$(1 ≤q≤ 105)$
là số lần gửi tín hiệu điều khiển hoặc yêu cầu tính toán của NAS;
Mỗi dòng trong
$q$
dòng tiếp theo có cấu trúc như sau:
*
Đầu tiên là số nguyên
$p$
$(0 ≤p≤ 1)$
*
Nếu
$p= 0$
, tiếp theo là
$2$
số nguyên
$x$
,
$y$
$(0 ≤x,y≤ 1000)$
mô tả tín hiệu điều khiển.
*
Nếu
$p= 1$
, tiếp theo là bốn số nguyên
$u$
,
$v$
,
$s$
,
$t$
$(1 ≤u≤s≤m, 1 ≤v≤t≤n)$
mô tả tọa độ mảng pin hình chữ nhật được yêu cầu tính toán, trong đó
$(u,v)$
là tọa độ góc trên trái và
$(s,t)$
tọa độ góc dưới bên phải


## 💡 Output

Output
Mức hấp thụ của các mảng pin hình chữ nhật tại từng thời điểm được yêu cầu tính toán tương ứng trong dữ liệu đầu vào, mỗi số trên một dòng


## 🧠 Example

### Input

```text
4 5
1 2 5 2 1
4 3 1 2 3
2 3 5 3 1
3 2 1 1 5
5
0 2 1
1 2 2 3 4
0 2 4
1 1 1 1 1
1 3 2 4 5
```

### Output

```text
15
3
17
```



## 📝 Note

Note
![](https://espresso.codeforces.com/b309e4fa615393430935ba33ff4127a542d89363.png)

