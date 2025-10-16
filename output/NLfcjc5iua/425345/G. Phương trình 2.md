# G. Phương trình 2

## 📖 Problem

Cho số nguyên
$n$
, dãy số nguyên
$a1,a2, ...,an$
và
$3$
số nguyên dương
$p,q,r$
: hãy tìm số lượng bộ
$4$
$(x,y,z,w)$
sao cho thỏa mãn đồng thời các điều kiện sau:
*
$1 ≤x<y<z≤w≤n$
*
$ax+ax+ 1+ ... +ay- 1=p$
*
$ay+ay+ 1+ ... +az- 1=q$
*
$az+az+ 1+ ... +aw=r$


## 🧩 Input

Input
Dòng đầu gồm
$4$
số
$n$
,
$p$
,
$q$
,
$r$
$(1 ≤n≤ 105, 1 ≤p,q,r≤ 109)$
Dòng thứ
$2$
lần lượt là
$a1,a2, ...,an$
$(1 ≤ai≤ 109)$


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm


## 🧠 Example

### Input

```text
12 11 10 17
1 3 2 6 4 6 3 6 2 6 5 3
```

### Output

```text
1
```



## 📝 Note

Note
Có
$1$
đáp án thỏa là
$(2, 5, 7, 10)$
vì
*
$a2+a3+a4= 11$
*
$a5+a6= 10$
*
$a7+a8+a9+a10= 17$

