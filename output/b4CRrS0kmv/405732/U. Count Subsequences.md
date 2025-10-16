# U. Count Subsequences

## 📖 Problem

Cho xâu
$s$
chỉ gồm các ký tự 'a', 'b', 'c'và dấu '?'
Bạn có thể thế dấu '?' thành 'a','b','c'. Hãy đếm xem tổng có bao nhiêu xâu con 'abc' trong mọi cách điền xâu
$s$
có thể.
Vì đáp án có thể rất lớn hãy in chia dư cho
$109+ 7$


## 🧩 Input

Input
Dòng đầu gốm
$n$
$(3 ≤n≤ 2 * 105)$
Dòng tiếp theo gồm xâu
$s$
có độ dài
$n$
chỉ gồm
$4$
ký tự 'a', 'b', 'c' và '?'.


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm


## 🧠 Example

### Input

```text
6
ac?b?c
```

### Output

```text
24
```



## 📝 Note

Note
Có 9 cách điền:
"acabac" — 2 xâu con "abc"
"acabbc" — 4 xâu con "abc"
"acabcc" — 4 xâu con "abc"
"acbbac" — 2 xâu con "abc"
"acbbbc" — 3 xâu con "abc"
"acbbcc" — 4 xâu con "abc"
"accbac" — 1 xâu con "abc"
"accbbc" — 2 xâu con "abc"
"accbcc" — 2 xâu con "abc"
2+4+4+2+3+4+1+2+2=24.

