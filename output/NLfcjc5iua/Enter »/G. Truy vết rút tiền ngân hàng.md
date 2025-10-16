# G. Truy vết rút tiền ngân hàng

## 📖 Problem

Tại một ngân hàng có
$n$
loại tiền mệnh giá
$a1,a1, ...,an$
với số tờ tiền mỗi loại không giới hạn. Cần chi trả cho một khách số tiền là
$M$
.
Yêu cầu: dòng
$1$
hãy cho biết cần ít nhất bao nhiêu tờ tiền để trả được số tiền là
$M$
cho khách, dòng hai gồm
$i$
số, số thứ
$i$
là số tờ tiền có mệnh giá
$ai$
cần sử dụng để ra được một cách bất kỳ sử dụng ít tờ tiền nhất để trả được số tiền là
$M$
.


## 🧩 Input

Input
Dòng đầu gồm
$N$
và
$M$
$(1 ≤n≤ 100, 1 ≤M≤ 10000)$
Dòng tiếp theo gồm
$N$
số
$(1 ≤ai≤ 10000)$
Dữ liệu đảm bảo luôn tồn tại ít nhất một cách đổi cho vị khách.


## 💡 Output

Output
Gồm hai dòng chứa đáp án cần tìm


## 🧠 Example

### Input

```text
5 98
1 5 10 20 50
```

### Output

```text
7
3 1 0 2 1
```



## 📝 Note

Note
Với ví dụ
$1$
cẩn sử dung
$3$
tờ
$1$
,
$1$
tờ
$5$
,
$0$
tờ
$10$
,
$2$
tờ
$20$
,
$1$
tờ
$50$
để trả được số tiền là
$98$

