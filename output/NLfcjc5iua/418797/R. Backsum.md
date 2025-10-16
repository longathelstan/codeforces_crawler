# R. Backsum

## 📖 Problem

Cho hai số nguyên
$n$
và
$x$
. Tìm dãy phép tính
$A$
gồm
$n$
số có dạng
$A1$
$?$
$A2$
$?$
...
$?$
$An$
.
$(1 ≤Ai≤ 5,$
?={+,-}
$)$
sao cho đáp án của phép tính đó
$x$
.
Lưu ý:
Phép tính có phân biệt vị trí tức là
$2$
phép
${[2 + 2 + 3]}$
và
$[2 + 3 + 2]$
được tính là
$2$
phép tính khác nhau.
Yêu cầu:
In ra tất cả dãy
$A$
tìm được theo thứ tự từ điển (
$+$
ưu tiên hơn
$-$
).


## 🧩 Input

Input
Một dòng duy nhất chứa
$2$
số nguyên
$n$
và
$x$
$(1 ≤n≤ 8,  - 5 * (n- 1) + 1 ≤x≤ 5 *n)$
.


## 💡 Output

Output
Gồm nhiều dòng, mỗi dòng là
$1$
dãy
$A$
thỏa mãn điều kiện đề bài. Giữa số và dấu có một khoảng trắng.


## 🧠 Example

### Input

```text
2 6
```

### Output

```text
1 + 5 
2 + 4 
3 + 3 
4 + 2 
5 + 1
```


