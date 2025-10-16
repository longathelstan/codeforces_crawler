# E. TRANSPORT

## 📖 Problem

Một mạng máy tính gồm
$N$
máy tính được đánh số thứ tự từ 1 đến
$N$
và được kết nối với nhau bằng
$N$
− 1 sợi cáp (mạng dạng hình cây) sao cho tất cả các máy tính trong mạng có thể truyền dữ liệu trực tiếp hoặc gián tiếp đến tất cả các máy tính còn lại trong mạng. Người quản lý cần truyền một file dữ liệu lớn từ một máy tính đến tất cả các máy tính khác trong mạng.
Khi một máy tính đã nhận được file dữ liệu thì nó có thể truyền file dữ liệu này đến một máy tính khác được kết nối trực tiếp với nó nếu máy tính đó chưa nhận được file và máy truyền lẫn máy nhận không được truyền hay nhận dữ liệu với những máy khác trong thời điểm này. Tuy nhiên trong lúc này có thể có những cặp máy tính khác truyền/nhận file cho nhau nếu chúng thỏa mãn điều kiện trên. Thời gian để truyền hết file dữ liệu từ một máy đến một máy khác được kết nối trực tiếp với nó là một phút.
Yêu cầu:
Ban đầu, file dữ liệu được lưu trữ tại máy tính có số thứ tự là
$a$
. Bạn hãy tính thời gian ít nhất để truyền file dữ liệu này đến tất cả các máy tính còn lại trong mạng.


## 🧩 Input

Input
+ Dòng đầu ghi hai số nguyên
$N$
(
$1$
≤
$N$
≤
$105$
) và
$a$
(1 ≤
$a$
≤
$N$
). Giữa hai số cách nhau một dấu cách.
+ Dòng thứ
$i$
(
$i$
=
$1$
...
$N−1$
) trong
$N−1$
dòng tiếp theo mỗi dòng ghi hai số nguyên
$ui$
và
$vi$
với ý nghĩa có một dây cáp nối từ máy
$ui$
đến máy
$vi$
. Giữa hai số được ghi cách nhau một dấu cách.


## 💡 Output

Output
Một số nguyên duy nhất là thời gian (số phút) ít nhất để file dữ liệu được truyền đến được tất cả các máy tính trong mạng.


## 🧠 Example

### Input

```text
6 2
1 2
2 3
2 4
1 5
5 6
```

### Output

```text
3
```



## 📝 Note

Note
Giới hạn:
• Có 50% số điểm với
$N$
≤
$1000$
• Có 50% số điểm với
$1000$
<
$N$
≤
$105$

