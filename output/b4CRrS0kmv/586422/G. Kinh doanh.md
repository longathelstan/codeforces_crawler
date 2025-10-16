# G. Kinh doanh

## 📖 Problem

Tấn là thị trưởng của một thành phố nổi tiếng với sản lượng khổng lồ các loại thuốc chống trầm cảm.
Sự gia tăng nhu cầu đối với các loại thuốc này đã thu hút
$M$
doanh nhân tham lam, được đánh số từ
$1$
đến
$M$
, từ khắp nơi trên thế giới. Có
$N$
nhà máy ở thành phố – và mỗi nhà máy thuộc sở hữu của một trong số
$M$
doanh nhân. Các nhà máy cũng được đánh số từ
$1$
đến
$N$
.
Hơn nữa, một số nhà máy phụ thuộc vào các nhà máy nhỏ hơn để lấy nguyên liệu thô. Tổng cộng có
$N- 1$
mối quan hệ phụ thuộc. Nhà máy số
$1$
là nhà máy chính và không phụ thuộc vào bất kỳ nhà máy nào khác. Đối với mỗi nhà máy từ
$2$
đến
$N$
, nó phụ thuộc vào đúng một nhà máy có chỉ số nhỏ hơn nó. Nói cách khác, mạng lưới phụ thuộc giữa các nhà máy tạo thành một cây có gốc tại
$1$
.
Mỗi năm từ
$1$
tới
$Q$
, tại năm thứ
$i$
một nhà máy
$Fi$
nhận được một khoản quyên góp
$Xi$
từ những người hào phóng. Số tiền này được phân phối theo quy tắc sau:
Cộng
$Xi$
vào
$Fi$
.
Cộng
$Xi+Di$
vào tất cả các nhà máy phụ thuộc vào
$Fi$
.
Cộng
$Xi+ 2·Di$
vào tất cả các nhà máy phụ thuộc vào các nhà máy từ bước
$(2)$
.
Nói chung, cộng
$Xi+ (K)·Di$
vào một nhà máy
$G$
nếu có
$K$
mối quan hệ phụ thuộc từ
$Fi$
đến
$G$
.
Tuy nhiên, các doanh nhân không quan tâm đến phúc lợi của công nhân trong các nhà máy. Kết quả là họ lấy hết số tiền mà một nhà máy nhận được từ quyên góp.
Mỗi doanh nhân thứ
$i$
có một giá trị
$Ci$
, thể hiện số tiền tối thiểu mà họ muốn kiếm được.
Yêu cầu:
Với
$Q$
năm báo cáo liên tiếp (các năm được đánh số từ
$1$
đến
$Q$
), hãy tìm năm nhỏ nhất mà doanh nhân thứ
$i$
đạt được ít nhất
$Ci$
,. Đưa ra
$- 1$
nếu doanh nhân đó không thể đạt được.


## 🧩 Input

Input
Dòng đầu gồm
$2$
số
$N$
và
$M$
$(1 ≤N,M≤ 105)$
Dòng tiếp theo gồm
$N- 1$
số, số thứ
$i$
thể hiện cha của nút
$i+ 1$
Dòng tiếp theo gồm
$N$
số, số thứ
$i$
thể hiện nhà máy
$i$
thuộc quyền sở hữu của doanh nhân
$Bi$
$(1 ≤Bi≤M)$
Dòng tiếp theo gồm
$M$
số, số thứ
$i$
thể hiện
$Ci$
$(1 ≤Ci≤ 1012)$
Dòng tiếp theo gồm
$Q$
$(1 ≤Q≤ 105)$
$Q$
dòng tiếp theo mỗi dòng gồm
$3$
số
$Fi$
,
$Xi$
và
$Di$
$(1 ≤Fi≤n, 1 ≤Xi,Di≤ 106)$


## 💡 Output

Output
Gồm
$M$
dòng ứng với
$M$
đáp án cần tìm


## 🧠 Example

### Input

```text
3 3
1 2
1 2 3
10 15 20
5
1 2 3
2 2 3
3 5 10
1 4 0
1 3 3
```

### Output

```text
-1
5
4
```


