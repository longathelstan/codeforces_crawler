# C. Đếm (7 điểm)

## 📖 Problem

Cho mảng
$a$
gồm
$n$
phần tử.
Yêu cầu:
đếm số lượng đoạn con liên tiếp
$[l,r]$
mà mọi giá trị trong dãy con đó đều có số lần xuất hiện không vượt quá (
$(r-l+ 1) / 2$
làm tròn xuống)


## 🧩 Input

Input
Dòng đầu gồm
$n$
$(1 ≤n≤ 5000)$
Dòng tiếp theo gồm
$n$
số, số thú
$i$
là giá trị của
$ai$
$(1 ≤ai≤ 5000)$


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm


## 🧠 Example

### Input

```text
4
2 1 1 3
```

### Output

```text
3
```



## 📝 Note

Note
Ở ví dụ
$1$
có
$3$
đoạn thoả:
$[l,r]$
:
$[1, 2]$
,
$[1, 4]$
,
$[3, 4]$

