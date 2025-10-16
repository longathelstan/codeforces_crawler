# B. Sao băng

## 📖 Problem

Có
$N$
tổ chức thành viên cùng tham gia thu thập các mảnh đá vũ trụ trên quỹ đạo tròn, tổ chức thành viên thứ
$i$
cần thu được ít nhất
$pi$
mảnh đá. Quỹ đạo tròn được chia thành
$M$
khu vực, trong đó khu vực
$M$
và
$1$
khu vực nằm cạnh nhau, mỗi khu vực thuộc về một trong các tổ chức thành viên.
Các nhà khoa học đã dự đoán được sự xuất hiện của
$K$
cơn mưa sao băng, cơn mưa xuất hiện vào thời điểm
$i$
sẽ giúp các khu vực có chỉ số thuộc đoạn
$[li,ri]$
tăng thêm
$ai$
mảnh đá (nếu
$li>ri$
thì đoạn
$[li,ri]$
được chia thành
$2$
đoạn
$[li,m]$
và
$[1,ri]$
).
Yêu cầu:
Với mỗi tổ chức thành viên, cho biết thời điểm sớm nhất mà tổ chức đó thu thập đủ số mảnh yêu cầu.


## 🧩 Input

Input
Dòng đầu gồm
$N$
và
$M$
$(1 ≤N,M≤ 3 * 105)$
Dòng tiếp theo gồm
$M$
số, số thứ
$i$
là
$ai$
thể hiện khu vực thứ
$i$
là của tổ chức thành viên nào
$(1 ≤ai≤N)$
Dòng tiếp theo gồm
$N$
số, số thứ
$i$
là
$pi$
thể hiện số lượng đá cần của tổ chức thành viên thứ
$i$
$(1 ≤pi≤ 1012)$
Dòng tiếp theo gồm số
$K$
$(1 ≤K≤ 3 * 105)$
$K$
dòng tiếp theo, dòng thứ
$i$
gồm
$3$
số
$li,ri,ai$
$(1 ≤li,ri≤M, 1 ≤ai≤ 1012)$


## 💡 Output

Output
Gồm
$N$
dòng ứng với
$N$
đáp án cần tìm, nếu không có đáp án hãy in
$- 1$


## 🧠 Example

### Input

```text
3 5
1 3 2 1 3
10 5 7
3
4 2 4
1 3 1
3 5 2
```

### Output

```text
3
-1
1
```



## 📝 Note

Note
Sau cơn mưa sao băng đầu, số lượng mảnh đá của
$3$
tổ chức sẽ là:
$8$
$0$
$8$
, tổ chức thứ
$3$
đủ mảnh ngay sau cơn mưa sao băng đầu.
Sau cơn mưa sao băng thứ hai, số lượng mảnh đá của
$3$
tổ chức sẽ là:
$9$
$1$
$9$
Sau cơn mưa sao băng thứ ba, số lượng mảnh đá của
$3$
tổ chức sẽ là:
$11$
$3$
$11$
, tổ chức thứ
$1$
đủ mảnh ngay sau cơn mưa sao băng thú ba.

