# P. Kế hoạch cải tổ

## 📖 Problem

Mạng giao thông của thành phố NB có
$N$
nút giao thông và
$M$
đoạn đường phố hai chiều nối các nút giao thông. Các nút giao thông được đánh số từ
$1$
đến
$N$
. Các đoạn đường phố được đánh số từ
$1$
đến
$M$
. Mạng giao thông của thành phố có tính chất sau đây:
Giữa hai nút giao thông bất kỳ có không quá một đoạn đường phố nối chúng;
Không có đoạn đường phố nào nối một nút giao thông với chính nó.
Vấn đề giao thông là thách thức với chính quyền thành phố từ nhiều năm. Với mong muốn đảm bảo việc đi lại thuận lợi hơn cho người dân, chính quyền thành phố quyết định tiến hành cải tổ mạng giao thông, trước hết nhằm đảm bảo có thể đi từ một nút giao thông bất kỳ đến tất cả các nút còn lại. (Lưu ý là mạng giao thông trước khi cải tổ có thể không đảm bảo yêu cầu này). Tuy nhiên, do hạn hẹp về nguồn kinh phí, trước mắt kế hoạch cải tổ chỉ có thể bao gồm
$2$
công việc:
Loại bỏ một đoạn đường phố hiện có khỏi mạng giao thông;
Xây dựng một đoạn đường chưa từng có trước đó nối hai nút giao thông khác nhau.
Đồng thời, sau khi thực hiện cải tổ, mạng giao thông phải đảm bảo có thể đi từ một nút giao thông bất kỳ đến tất cả các nút còn lại.
Yêu cầu:
Giúp chính quyền thành phố xác định xem có bao nhiêu cách khác nhau để thực hiện kế hoạch cải tổ thỏa mãn các yêu cầu đặt ra. (Hai kế hoạch cải tổ là khác nhau nếu có ít nhất một trong hai đoạn đường được lựa chọn loại bỏ hay xây dựng mới là khác nhau.)


## 🧩 Input

Input
Dòng đầu tiên chứa hai số nguyên
$N$
và
$M$
$(1 ≤N≤ 2 * 105, 1 ≤M≤ 105)$
M dòng tiếp theo, mỗi dòng gồm 2 số nguyên
$u$
và
$v$
$(1 ≤u,v≤N,u≠v)$
biểu thị đoạn đường phố hai chiều nối 2 nút
$u$
và
$v$


## 💡 Output

Output
Ghi ra một số nguyên là số cách thực hiện kế hoạch cải tổ mạng giao thông thỏa mãn các yêu cầu đặt ra.


## 🧠 Example

### Input

```text
4 4
1 2
2 3
2 4
3 4
```

### Output

```text
8
```



## 📝 Note

Note
![](https://espresso.codeforces.com/985ac6620ae9da3c3809100bd71feae06c408479.png)
![](https://espresso.codeforces.com/c8b07ff266614776526e5e9c394ce50db9d390a9.png)

