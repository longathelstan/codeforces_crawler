# A. Substr

## 📖 Problem

Cho xâu
$A$
và xâu
$B$
chỉ gồm các chữ cái thường. Xâu
$B$
được gọi là xuất hiện tại vị trí
$i$
của xâu
$A$
nếu: A[i] = B[1], A[i+1] = B[2], ..., A[i+length(B)-1] = B[length(B)].
Hãy tìm tất cả các vị trí mà
$B$
xuất hiện trong
$A$
.


## 🧩 Input

Input
Dòng
$1$
: xâu
$A$
gồm các ký tự tin thường từ a đến z.
Dòng
$2$
: xâu
$B$
gồm các ký tự tin thường từ a đến z.
Độ dài
$A$
,
$B$
không quá
$106$


## 💡 Output

Output
Ghi ra các vị trí tìm được trên
$1$
dòng (thứ tự tăng dần). Nếu
$B$
không xuất hiện trong
$A$
thì bỏ trắng.


## 🧠 Example

### Input

```text
aaaaa
aa
```

### Output

```text
1 2 3 4
```


