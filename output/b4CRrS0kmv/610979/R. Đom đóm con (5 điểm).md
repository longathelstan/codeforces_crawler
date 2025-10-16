# R. Đom đóm con (5 điểm)

## 📖 Problem

Jack sắp biểu diễn show ca nhạc tại Khánh Hoà, có
$n$
người đang đứng xếp hàng đợi mua vé xem Jack biểu diễn, biết chiều cao của người thứ
$i$
là
$ai$
.
![](https://espresso.codeforces.com/0586d82e65d5917e4edca27afcc006f279139418.png)
Hai người
$i$
,
$j$
sẽ quan sát được nhau nếu hai người đứng cạnh nhau hoặc
$max(ai+ 1, ...,aj- 1) ≤min(ai,aj)$
Yêu cầu:
Hãy đếm số cặp
$(i,j)$
$(1 ≤i<j≤n)$
sao cho hai người có thể thấy được nhau.


## 🧩 Input

Input
Dòng đầu gồm
$n$
$(1 ≤n≤ 2 * 106)$
Dòng tiếp theo gồm
$n$
số nguyên dương
$ai$
$(1 ≤ai≤ 109)$
.


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm


## 🧠 Example

### Input

```text
9
2 2 2 1 2 1 2 2 2
```

### Output

```text
25
```


