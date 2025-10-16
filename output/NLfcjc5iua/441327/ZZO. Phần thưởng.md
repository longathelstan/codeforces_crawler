# ZZO. Phần thưởng

## 📖 Problem

Alice vừa đoạt giải quán quân trong một kỳ thi lập trình danh giá. Ban tổ chức trao thưởng thông qua một trò chơi như sau. Có
$n$
thẻ xếp trên một hàng dài, trên mỗi thẻ viết một số nguyên dương. Ban tổ chức cho phép Alice thực hiện nhiều bước để chọn ra đúng
$k$
cặp thẻ, mỗi bước thực hiện theo một trong các quy tắc sau:
*
Chọn
$2$
thẻ đầu hàng;
*
Chọn
$2$
thẻ cuối hàng
*
Chọn
$1$
thẻ đầu hàng và
$1$
thẻ cuối hàng
*
Loại
$1$
thẻ đầu hàng ra khỏi hàng
*
Loại
$1$
thẻ cuối hàng ra khỏi hàng
Sau mỗi bước nếu chọn được
$2$
thẻ thì loại
$2$
thẻ đó ra khỏi hàng và Alice nhận được số tiền thưởng bằng giá trị tuyệt đối của hiệu hai số ghi trên hai thẻ đó.
Yêu cầu: Hãy giúp Alice tìm cách chơi chọn đúng
$k$
cặp thẻ để đạt được tổng số tiền thưởng là lớn nhất.


## 🧩 Input

Input
Dòng thứ nhất chứa hai số nguyên dương
$n$
và
$k$
$($
2
$x$
k
$≤n,n≤ 300)$
Dòng thứ hai chứa
$n$
số nguyên dương là giá trị ghi trên từng thẻ, mỗi thẻ một số tương ứng lần lượt từ đầu hàng. Các số có giá trị không vượt quá
$109$
.


## 💡 Output

Output
Ghi ra một số nguyên duy nhất là tổng tiền thưởng lớn nhất tìm được.


## 🧠 Example

### Input

```text
6 2
1 3 10 2 1 4
```

### Output

```text
12
```


