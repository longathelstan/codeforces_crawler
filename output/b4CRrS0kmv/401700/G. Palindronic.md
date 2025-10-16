# G. Palindronic

## 📖 Problem

Một xâu s được gọi là đối xứng
$k$
lần nếu
*
Nó là xâu đối xứng
*
Phần đối xứng bên trái đối xứng
$k- 1$
lần và phần đối xứng bên phải cũng đối xứng
$k- 1$
lần
Ví dụ xâu
$abacaba$
được gọi là đối xứng
$3$
lần nó là xâu đối xứng, xâu đối xứng bên trái
$aba$
là xâu đối xứng
$2$
lần và xâu đối xứng bên phải
$aba$
là xâu đối xứng
$2$
lần.
Một xâu đối xứng
$k$
lần cũng được coi là xâu đối xứng
$1$
,
$2$
,...
$k- 1$
lần.
Cho xâu
$s$
, với mỗi
$i$
từ
$1$
đến độ dài của xâu, hãy in ra có bao nhiêu đoạn con liên tiếp của xâu
$s$
đối xứng
$i$
lần.


## 🧩 Input

Input
Gồm xâu
$s$
$(1 ≤ |s| ≤ 4000)$


## 💡 Output

Output
Gồm
$1$
dòng duy nhất chứa
$|s|$
số.


## 🧠 Example

### Input

```text
abba
```

### Output

```text
6 1 0 0
```



## 📝 Note

Note
Test
$1$
:
Xâu con liên tiếp đối xứng
$1$
lần là:
$a$
,
$b$
,
$b$
,
$a$
,
$bb$
,
$abba$
.
Xâu con liên tiếp đối xứng
$2$
lần là:
$bb$

