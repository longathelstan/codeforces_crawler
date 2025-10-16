# ZZT. Trò chơi chọn số (6 điểm)

## 📖 Problem

Tí là một học sinh rất chăm ngoan, học giỏi đặc biệt rất yêu thích môn lập trình. Để động viên tinh thần học tập của cậu bé cũng như phát huy tư duy lập trình của con, ba cậu bé đã đưa cho Tí một bài toán như sau:
Cho một bảng số có kích thước
$n$
x
$2$
, hàng được đánh số thứ tự từ
$1$
đến
$n$
, cột được đánh số thú tự từ
$1$
đến
$2$
. Ô thuộc hàng
$i$
, cột
$j$
được quy định bởi một số nguyên
$ai,j$
$(|ai,j| ≤ 109)$
,
$ai,j$
được gọi là giá trị của ô
$(i,j)$
Quy trắc trò chơi
:
*
Mỗi ô chỉ được chọn tối đa
$1$
lần
*
Không được chọn
$2$
ô trên cùng một cột trong
$2$
lần chọn liên tiếp; ô chọn sau phải có chỉ số hàng lớn hơn chỉ số hàng của ô chọn trước đó
*
Cần chọn ít nhất một ô
*
Giá trị phần thưởng của trò chơi chính bằng tổng giá trị các ô mà Tí đã chọn
Yêu cầu:
Giúp Tí tính tổng giá trị lớn nhất của phần thưởng mà Tí có thể chọn đảm bảo các quy tắc của trò chơi.


## 🧩 Input

Input
Dòng đầu chứa số nguyên dương
$n$
$(n≤ 106)$
Dòng thứ
$i$
trong
$n$
dòng tiếp theo chứa
$2$
số nguyên
$ai, 1$
,
$ai, 2$
cách nhau bởi ký tự trắng.


## 💡 Output

Output
Một số nguyên duy nhất là đáp án của bài toán


## 🧠 Example

### Input

```text
4
2 5
-8 1
-2 -2
3 6
```

### Output

```text
9
```



## 📝 Note

Note
Danh sách các ô được chọn với phần thưởng có giá trị lớn nhất bao gồm các ô:
$(1, 2)$
;
$(3, 1)$
;
$(4, 2)$
có tổng giá trị là
$5 + ( - 2) + 6 = 9$

