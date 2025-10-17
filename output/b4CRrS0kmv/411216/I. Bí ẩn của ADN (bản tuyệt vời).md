# I. Bí ẩn của ADN (bản tuyệt vời)

## 📖 Problem

Các nhà khoa học hiện tại đang nghiên cứu ADN của sinh vật lạ độ dài
$n$
, vị trí thứ
$i$
mang
$1$
số hiệu nguyên dương
$Ai$
. các nhà khoa học sẽ lần lượt bốc ra
$Q$
đoạn ngẫu nhiên của ADN để nguyên cứu kỹ. Điều mà họ nguyên cứu là độ bí ẩn của đoạn này. Biết rằng độ bí ẩn của đoạn
$i$
là một số hiệu nguyên dương nhỏ nhất không xuất hiện trong đoạn (vì nó không tồn tại nên đã tạo ra sự bí ẩn cho đoạn đang nguyên cứu).
Yêu cầu:
với mỗi đoạn
$i$
hãy tìm độ bí ẩn của đoạn.


## 🧩 Input

Input
Dòng đầu tiên là một số nguyên
$n$
và
$Q$
$(1 ≤n≤ 105, 1 ≤Q≤ 105)$
.
Dòng tiếp theo là
$n$
số nguyên
$Ai$
$(1 ≤Ai≤n)$
là số hiệu mà vị trí
$i$
mang.
$Q$
dòng tiếp theo, dòng gồm hai số nguyên
$Li$
và
$Ri$
$(1 ≤Li≤Ri≤n)$
.


## 💡 Output

Output
Gồm
$Q$
dòng, dòng thứ
$i$
là độ bí ẩn của đoạn
$i$
.


## 🧠 Example

### Input

```text
7 4
2 1 1 3 2 1 4
1 5
4 7
2 4
1 4
```

### Output

```text
4
5
2
4
```


