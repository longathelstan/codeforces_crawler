# M. Bí ẩn của ADN (bản tuyệt vọng)

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
đoạn ngẫu nhiên của ADN để nguyên cứu. Họ sẽ nguyên cứu độ bí ẩn của đoạn này. Biết rằng độ bí ẩn của đoạn
$i$
là một số hiệu nguyên dương nhỏ nhất không xuất hiện trong đoạn (vì nó không xuất hiện nên đã tạo ra sự bí ẩn cho đoạn đang nguyên cứu).
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
$(1 ≤n≤ 555555, 1 ≤Q≤ 555555)$
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
gồm
$Q$
dòng, dòng
$i$
chứa
$1$
số nguyên là độ bí ẩn của đoạn
$i$
.


## 🧠 Example

### Input

```text
10 5
1 3 2 1 3 5 4 6 8 7
1 5
2 6
1 7
5 5
9 10
```

### Output

```text
4
4
6
1
1
```


