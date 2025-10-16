# K. Dãy ngoặc tối ưu

## 📖 Problem

Hãy tìm một dãy ngoặc đúng có độ dài
$n$
, biết rằng tại vị trí
$i$
nếu đặt dấu mở thì tốn phí
$Ai$
ngược lại, dấu đóng thì tốn
$Bi$
. Dãy ngoặc đúng là dãy ngoặc
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
Yêu cầu:
In ra chi phí nhỏ nhất để xây dựng một dãy ngoặc đúng có độ dài
$n$
.


## 🧩 Input

Input
Một dòng chứa số nguyên
$n$
là độ dài của dãy ngoặc
$(1 ≤n≤ 18)$
,
$n$
là số chẵn.
$n$
dòng tiếp theo, mỗi dòng gồm 2 số nguyên
$Ai$
và
$Bi$
$(1 ≤Ai,Bi≤ 106)$
là chi phí để đặt dấu mở hoặc đóng vào vị trí
$i$
.


## 💡 Output

Output
Một dòng duy nhất chứa số nguyên là đáp án của bài


## 🧠 Example

### Input

```text
4
2 1
1 4
5 3
2 2
```

### Output

```text
8
```


