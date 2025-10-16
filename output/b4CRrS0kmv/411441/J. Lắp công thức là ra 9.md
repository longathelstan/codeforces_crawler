# J. Lắp công thức là ra 9

## 📖 Problem

Xét một dãy vô hạn đuợc định nghĩa bởi
$n$
phần tử đầu tiên:
$a0,a1, ...,an- 1$
và các hệ số
$c1,c2, ...,cn$
,
$p,q,r$
. Biết rằng với mọi
$i≥n$
:
$ai= (c1*ai- 1+c2*ai- 2+ ... +cn*ai-n) +p+i*q+i2*r$
Hãy tính
$(a1+a2+ ... +ak)$
mod
$109+ 7$


## 🧩 Input

Input
Dòng đầu chứa hai số nguyên duơng
$n$
,
$k$
$(1 ≤n≤ 100, 1 ≤k≤ 1018)$
Dòng thứ hai chứa
$n$
số nguyên
$a0,a2, ...,an- 1$
$(0 ≤ai< 109+ 7)$
Dòng thứ ba chứa
$n$
số nguyên
$c1,c2, ...,cn$
$(0 ≤ci< 109+ 7)$
Dòng thứ
$4$
chứa số nguyên
$p,q,r$
$(0 ≤p,q,r< 109+ 7)$


## 💡 Output

Output
Gồm một dòng duy nhất là kết quả cần tìm


## 🧠 Example

### Input

```text
2 2
0 30
2 1
2 1 1
```

### Output

```text
98
```



## 📝 Note

Note
Ở ví dụ thứ nhất, ta có
$a0= 0,a1= 30,ai= (ai- 1* 2 +ai- 2) + 2$
Do đó
$a2= 2 *a1+a0+ 2 = 2 * 30 + 0 + 2 = 62$

