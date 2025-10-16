# D. Good Substring

## 📖 Problem

Cho xâu
$s$
gồm các ký tự in thường trong tiếng anh. Có phải từ tiếng anh được coi là tốt, còn lại là xấu.
Một xâu con
$s[l...r]$
được coi là tốt nếu nó chứa không quá
$k$
ký tự xấu.
Bạn hãy tìm số xâu con tốt riêng biệt.
$2$
xâu con
$s[x...y]$
và
$s[p...q]$
được coi là riêng biệt nếu
$s[x...y] ≠s[p...q]$


## 🧩 Input

Input
Dòng đầu gồm sâu
$s$
$(1 ≤ |s| ≤ 1500)$
Dòng tiếp theo chứa xâu
$0$
và
$1$
, độ dài của xâu là 26 ứng với độ dài bảng chữ cái tiếng anh. Vị trí thứ
$i$
trong xâu là
$1$
thể hiện tự thứ
$i$
là tốt,
$0$
nếu xấu. Ký tự thứ nhất ứng với chữ
$a$
, ký tự thứ
$2$
ứng ới chữ
$b$
...
Dòng thứ
$3$
gồm số nguyên
$k$
$(0 ≤k≤ |s|)$


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm


## 🧠 Example

### Input

```text
ababab
01000000000000000000000000
1
```

### Output

```text
5
```



## 📝 Note

Note
Ở test
$1$
:
$5$
xâu con riêng biệt thỏa là: "a", "ab", "b", "ba", "bab"

