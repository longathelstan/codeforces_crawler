# B. Frog 1

## 📖 Problem

Cho
$n$
viên đá, viên đá thứ
$i$
có độ cao là
$hi$
.
Con ếch đang đứng tại viên đá thứ nhất. Tại vị trí thứ
$i$
con ếch có thể nhảy sang hòn đá thứ
$i+ 1$
hoặc hòn đá thứ
$i+ 2$
với chi phí nhảy là
$|hi-hj|$
với
$j$
là vị trí đáp của chú ếch.
Hãy tìm chi phí ngắn nhất để chú ếch tới được hòn đá thứ
$n$
.


## 🧩 Input

Input
Dòng đầu gồm
$n$
là số lượng hòn đá
$(1 ≤n≤ 105)$
Dòng sau gồm
$n$
số, số thứ
$i$
thể hiện
$hi$
là chiều cao của viên đá thứ
$i$
$(1 ≤hi≤ 104)$


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm


## 🧠 Example

### Input

```text
4
10 30 40 20
```

### Output

```text
30
```



## 📝 Note

Note
Ở ví dụ
$1$
chú ếch sẽ nhảy
$1$
->
$2$
->
$4$
với chi phí là |10 - 30| + |30 - 20| = 30

