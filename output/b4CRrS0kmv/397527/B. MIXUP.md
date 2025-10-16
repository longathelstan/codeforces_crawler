# B. MIXUP

## 📖 Problem

Mỗi trong
$N$
cô bò
$(4 <  =N<  = 16)$
của bác John có một số seri phân biệt
$Si$
$(1 <  =Si<  = 25, 000)$
. Các cô bò tự hào đến nỗi mỗi cô đều đeo một chiếc vòng vàng có khắc số seri của mình trên cổ theo kiểu các băng đảng giang hồ.
Các cô bò giang hồ này thích nổi loạn nên đứng xếp hàng chờ vắt sữa theo một thứ tự gọi được gọi là 'hỗn loạn'.
Một thứ tự bò là 'hỗn loạn' nếu trong dãy số seri tạo bởi hàng bò, hai số liên tiếp khác biệt nhau nhiều hơn
$K$
$(1 <  =K<  = 3400)$
. Ví dụ, nếu
$N= 6$
và
$K= 1$
thì
$1, 3, 5, 2, 6, 4$
là một thứ tự 'hỗn loạn' nhưng
$1, 3, 6, 5, 2, 4$
thì không (vì hai số liên tiếp
$5$
và
$6$
chỉ chênh lệch
$1$
).
Hỏi có bao nhiêu cách khác nhau để
$N$
cô bò sắp thành thứ tự 'hỗn loạn'?.


## 🧩 Input

Input
Dòng
$1$
: Hai số
$N$
và
$K$
cách nhau bởi khoảng trắng.
Dòng
$2..N+ 1$
: Dòng
$i+ 1$
chứa một số nguyên duy nhất là số seri của cô bò thứ
$i$
:
$Si$


## 💡 Output

Output
Dòng
$1$
: Một số nguyên duy nhất là số cách để N cô bò sắp thành thứ tự 'hỗn loạn'. Kết quả đảm bảo nằm trong phạm vi kiểu số nguyên 64-bit.


## 🧠 Example

### Input

```text
4 1
3
4
2
1
```

### Output

```text
2
```


