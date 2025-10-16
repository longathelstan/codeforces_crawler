# J. Ràng buộc dãy ngoặc

## 📖 Problem

Cho số nguyên
$n$
và
$k$
, hãy in ra theo thứ tự từ điển tất cả các dãy ngoặc đúng độ dài
$n$
và không tồn tại
$k+ 1$
vị trí liên tiếp chứa toàn dãy mở. ví dụ,
$n$
=6,
$k= 2$
thì (())() là một dãy thỏa điều kiện, ((())) là dãy không thỏa. Dãy ngoặc đúng là dãy ngoặc
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
Một dòng chứa
$2$
số nguyên
$n$
và
$k$
$(1 ≤n≤ 18)$
, n là số chẵn,
$(1 ≤k≤n)$
.


## 💡 Output

Output
Gồm nhiều dòng, mỗi dòng là một dãy ngoặc đúng có độ dài
$n$
.


## 🧠 Example

### Input

```text
8 3
```

### Output

```text
((()()))
((())())
((()))()
(()(()))
(()()())
(()())()
(())(())
(())()()
()((()))
()(()())
()(())()
()()(())
()()()()
```


