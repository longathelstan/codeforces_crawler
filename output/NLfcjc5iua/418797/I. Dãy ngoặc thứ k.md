# I. Dãy ngoặc thứ k

## 📖 Problem

Cho số nguyên dương
$n$
và
$k$
. Trong tất cả các dãy ngoặc đúng có độ dài là
$n$
được sắp xếp tăng dần theo thứ tự từ điển, hãy in ra dãy ngoặc đúng thứ
$k$
. Nếu không tồn tại xuất ra
$- 1$
.Dãy ngoặc đúng là dãy ngoặc
$()$
, nếu dãy
$s$
là dãy đúng thì
$(s)$
cũng là dãy đúng, nếu dãy
$t$
là dãy đúng thì
$s+t$
(phép cộng xâu) cũng là dãy đúng.
Ví dụ: một số dãy đúng (), ()(), (()()).


## 🧩 Input

Input
Một dòng duy nhất chứa
$2$
số nguyên
$n$
và
$k$
$(2 ≤n≤ 18)$
$n$
là số chẵn,
$(1 ≤k≤ 300)$
.


## 💡 Output

Output
Một dòng duy nhất chứa xâu thứ
$k$
độ dài
$n$
tìm được. Nếu không tồn tại, in ra
$- 1$
.


## 🧠 Example

### Input

```text
6 4
```

### Output

```text
()(())
```


