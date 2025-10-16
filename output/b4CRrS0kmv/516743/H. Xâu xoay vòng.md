# H. Xâu xoay vòng

## 📖 Problem

Cho hai chuỗi
$s$
và
$t$
gồm các ký tự in thường từ '
$a$
' tới '
$z$
', ta có thể dịch chuyển xâu
$s$
bao nhiêu lần tuỳ thích.
Một lần dịch chuyển trên s bao gồm việc di chuyển ký tự ngoài cùng bên trái của
$s$
sang vị trí ngoài cùng bên phải.
Ví dụ: nếu s = "
$abcde$
" thì sau một lần dịch chuyển sẽ là "
$bcdea$
".
Yêu cầu:
Đưa ra YES nếu
$s$
có thể trở thành
$t$
sau một số lần dịch chuyển trên
$s$
, nếu không thì đưa ra NO.


## 🧩 Input

Input
Dòng đầu gồm xâu
$s$
Dòng hai gồm xâu
$t$
Mỗi xâu có độ dài không vượt quá
$5000$


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm


## 🧠 Example

### Input

```text
tan
ant
```

### Output

```text
YES
```



## 📝 Note

Note
Ví dụ
$1$
: ta có thể dịch chuyển xâu
$s$
một lần để được xâu
$t$
"
$tan$
" -> "
$ant$
"
Ví dụ
$1$
: ta có thể dịch chuyển xâu
$s$
hai lần để được xâu
$t$
"
$tan$
" -> "
$ant$
" -> "
$nta$
"

