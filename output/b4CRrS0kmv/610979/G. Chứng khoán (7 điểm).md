# G. Chứng khoán (7 điểm)

## 📖 Problem

Chứng khoán là một trong những kênh đầu tư rất nhiều rủi ro. Nhà đầu tư cần phân tích nhiều yếu tố thị trường để quyết định đầu tư vào một cổ phiếu. Một trong những tham số được nhiều nhà đầu tư quan tâm là tính ổn định của một cổ phiếu. Xét giá bán của một cổ phiếu trong nhiều phiên giao dịch. Cổ phiếu được xem là có ổn định trong một khoảng thời gian nếu khoảng chênh lệch của giá bán cao nhất và giá bán thấp nhất của cổ phiếu đó trong khoảng thời gian trên không vượt quá ngưỡng ổn định giá
$T$
cho trước.
Yêu cầu: Cho biết giá bán cổ phiếu trong
$N$
phiên giao dịch. Hãy tính chương trình tính số phiên giao dịch dài nhất mà cổ phiếu có giá ổn định.


## 🧩 Input

Input
Dòng đầu chứa
$2$
số nguyên
$T$
$(0 ≤T≤ 2 * 109)$
và
$N$
lần lượt cho biết ngưỡng ổn định giá và số phiên giao dịch.
Dòng thứ hai chứa
$N$
số nguyên
$Gi$
$(1 ≤Gi≤ 2.109)$
lần lượt cho biết giá bán của cổ phiếu trong
$N$
phiên giao dịch.


## 💡 Output

Output
Một số nguyên là phiên giao dịch dài nhất mà cổ phiếu có giá ổn định


## 🧠 Example

### Input

```text
5 10
5 7 9 20 15 13 20 12 11 1
```

### Output

```text
3
```


