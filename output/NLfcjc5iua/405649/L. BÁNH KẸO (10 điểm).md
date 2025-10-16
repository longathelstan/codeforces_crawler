# L. BÁNH KẸO (10 điểm)

## 📖 Problem

Công ty bánh kẹo
$ABC$
chuẩn bị xây dựng hệ thống đại lý để giao bánh kẹo đến tất cả địa điểm trong thành phố. Hàng ngày, từ mỗi đại lý các nhân viên dùng K loại xe với trọng lượng lần lượt là
$P1,P2, ...,PK$
chuyên chở bánh kẹo đến các địa điểm còn lại. Thành phố có
$N$
địa điểm (đánh số từ
$1$
đến
$N$
) và
$M$
con đường hai chiều nối trực tiếp giữa các địa điểm, trên mỗi con đường có ghi một số nguyên dương cho biết trọng lượng tối đa của xe được phép di chuyển trên con đường này. Giữa 2 địa điểm bất kì có thể có nhiều con đường nối trực tiếp.
Để có thể giao hàng đến N địa điểm, công ty tìm cách chọn một số địa điểm để đặt đại lý. Chi phí mỗi cách chọn phụ thuộc vào số lượng địa điểm được chọn làm đại lý, số địa điểm càng ít thì chi phí càng thấp.
Yêu cầu: Hãy cho biết cách chọn có chi phí thấp nhất sẽ có số lượng địa điểm đặt đại lý là bao nhiêu.


## 🧩 Input

Input
Dòng
$1$
gồm ba số nguyên dương
$N$
$(1≤N≤1000),M(1≤M≤100000),K(1≤K≤20)$
.
Dòng
$2$
gồm
$K$
số nguyên dương
$P1,P2, ...,PK$
$(1≤Pi≤500)$
$M$
dòng tiếp theo, dòng thứ
$i$
gồm ba số nguyên dương
$Ai$
,
$Bi$
,
$Ti$
$(1≤Ti≤500)$
, cho biết con đường nối giữa địa điểm
$Ai$
đến
$Bi$
chịu được trọng lượng tối đa là
$Ti$
. Các số ghi trên cùng một dòng cách nhau bởi ít nhất một kí tự trắng.


## 💡 Output

Output
Một dòng với số nguyên duy nhất cho biết số lượng địa điểm ít nhất.


## 🧠 Example

### Input

```text
5 6 3
5 3 4
1 2 2
1 3 1
2 3 3
3 4 2
4 5 2
4 5 4
```

### Output

```text
3
```



## 📝 Note

Note
Công ty có ba loại xe với trọng lượng 5,3, 4
Bằng cách chọn ba địa điểm 1, 3, 5 để đặt đại lý. Công ty có thể giao bánh kẹo đến tất cả các địa điểm.

