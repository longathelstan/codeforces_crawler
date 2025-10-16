# D. Kế hoạch phóng tàu vũ trụ (5 điểm)

## 📖 Problem

Cơ quan hàng không vũ trụ Mĩ NASA vừa thực hiện thành công một dự án lớn. Đó là xây dựng một trạm vũ trụ trên mặt trăng. Công việc trước mắt là duy trì trạm vũ trụ này trong
$N$
ngày. Để vận hành tốt, lúc nào cũng cần có một phi hành gia ở trên trạm vũ trụ. Tuy nhiên, mỗi phi hành gia không thể ở trên trạm vũ trụ quá
$M$
ngày liên tiếp, vì vậy NASA cần lập một kết hoạc luân phiên các nhà du hành vũ trụ. Chi phí cho việc luân phiên này cũng khác nhau đối với mỗi ngày và NASA muốn tối thiểu tổng chi phí này. Nhiệm vụ của bạn là đọc các thông tin và đưa ra một kế hoạch tối ưu. Chú ý rằng ở ngày thứ
$1$
luôn cần có sự thay đổi.


## 🧩 Input

Input
Dòng thứ nhất ghi hai số
$N$
và
$M$
$(1 ≤N≤ 2 * 106, 1 ≤M≤ 104)$
.
Dòng thứ
$i$
trong
$N$
dòng sau ghi số
$Ci$
chi phí cho việc thay đổi nhà du hành vũ trụ trong ngày thứ
$i$
$(1 ≤Ci≤ 105)$
.


## 💡 Output

Output
Gồm một dòng duy nhất ghi chi phí
$S$
là chi phí tối thiểu cho việc duy trì trạm vũ trụ


## 🧠 Example

### Input

```text
6 3
1
4
3
2
5
3
```

### Output

```text
3
```


