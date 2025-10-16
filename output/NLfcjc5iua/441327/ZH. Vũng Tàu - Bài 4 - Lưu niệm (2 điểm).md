# ZH. Vũng Tàu - Bài 4 - Lưu niệm (2 điểm)

## 📖 Problem

Bốn năm cấp hai là khoảng thời gian ghi dấu nhiều kỉ niệm nhất của tuổi học trò và những tình bạn đẹp cũng thường từ đây mà xuất hiện. Trong 4 năm qua, Hoàng và các người bạn cùng lớp 9A của mình đã có rất nhiều hình ảnh đáng nhớ! Mỗi loại bức ảnh đều có dung lượng và tính thẩm mỹ nhất định. Để lưu giữ lại những hình ảnh đẹp, Hoàng quyết định mua một chiếc thẻ nhớ ngoài dung lượng
$K$
(Gigabyte-GB) để lưu chúng.
Hoàng thấy việc này thật thú vị! và muốn tạo một hoạt động vui nhộn cùng các bạn với nội dung như sau:
*
Cho biết thông tin về số lượng các loại bức ảnh; mỗi loại sẽ có dung lượng và tính thẩm mỹ của loại đó.
*
Câu hỏi của Hoàng là: "Hãy chọn các bức ảnh của từng loại để lưu vào thẻ nhớ mà mình đã mua sao cho tổng tính thẩm mỹ thu được là lớn nhất". Biết rằng một loại ảnh có thể không được chọn hoặc chọn với số lượng không hạn chế.
Yêu cầu:
Cho biết tổng giá trị lớn nhất của tính thẩm mỹ thu được khi trả lời câu hỏi của Hoàng là bao nhiêu?


## 🧩 Input

Input
Dòng thứ nhất chứa 2 số
$N(2 ≤N≤ 1000)$
và
$K(1 ≤K≤ 4)$
. Trong đó,
$N$
là số lượng các loại ảnh của Hoàng được đánh số thứ tự từ
$1$
đến
$N$
,
$K$
là dung lượng thẻ nhớ Hoàng đã mua(tính bằng đơn bị GB)
Trong
$N$
dòng tiếp theo, dòng thứ
$i$
chứ 2 số nguyên dương
$ai(1 ≤ai≤ 1024)$
,
$bi(1 ≤bi≤ 109)$
. Trong đó
$ai$
là dung lượng của các bức ảnh loại thứ
$i$
theo đon vị Megabyte (MB) và
$bi$
là giá trị tính thẩm mỹ của bức ảnh loại thứ
$i(1 ≤i≤N)$
.
*Ghi chú:
1GB = 1024MB


## 💡 Output

Output
Một số nguyên duy nhất là kết quả tìm được


## 🧠 Example

### Input

```text
5 1
800 1000
700 690
200 30
300 40
100 50
```

### Output

```text
1100
```



## 📝 Note

Note
Giải thích ví dụ:
Có
$5$
loại ảnh, dung lượng thẻ nhớ của Hoàng là
$1$
GB(
$1024$
MB), nên sẽ chọn
$1$
ảnh loại
$1$
và
$2$
ảnh loại
$5$
để lưu giữ, có tổng giá trị thẩm mỹ
$1100$
là lớn nhất

