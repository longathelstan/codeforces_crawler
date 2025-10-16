# J. Khoảng cách gần nhất

## 📖 Problem

![](https://espresso.codeforces.com/20ffb160689f2ca2ec8d597cc52fe6ab151c32c6.png)
Mặc dù không còn quen nhau nhưng hằng ngày Nhân vẫn luôn nhớ về Linh, sau khi lên đại học Nhân thuê trọ ở toạ độ
$A(xA,yA)$
và Linh thuê trọ ở toạ độ
$C(xC,yC)$
, hằng ngày Nhân tới trường ở toạ độ
$B(xB,yB)$
và Linh tới trường ở toạ độ
$D(xD,yD)$
. Hay nói cách khác Nhân sẽ di chuyển từ
$A$
tới
$B$
và Linh sẽ di chuyển từ
$C$
tới
$D$
.
Vì còn duyên nợ nên ngày nào hai người cùng xuất phát tại cùng một lúc , tới trường tại cùng một thời điểm và vận tộc của từng người sẽ không thay đổi trong quá trình di. Nhân luôn tự hỏi khoảng cách Euclid gần nhau nhất của hai người là bao nhiêu trong quá trình đi nhà tới trường.
Yêu cầu:
Hãy đưa ra câu trả lời cho Nhân, đáp án của bạn sẽ được coi là đúng nếu lệch với kết quả của bài toán
$< 10- 6$


## 🧩 Input

Input
Dòng đầu tiên chứa một số nguyên duy nhất
$t$
$(1 ≤t≤ 104)$
là số lượng truy vấn
Mỗi truy vấn gồm
$8$
số
$xA,yA,xB,yB,xC,yC,xD,yD$
$(0 ≤xA,yA,xB,yB,xC,yC,xD,yD≤ 103)$


## 💡 Output

Output
Gồm
$t$
dòng ứng với
$t$
truy vấn cần tìm


## 🧠 Example

### Input

```text
3
0 0 5 0 5 5 5 0
0 0 5 5 10 10 6 6
0 0 5 0 10 1 1 1
```

### Output

```text
0.000000
1.414214
1.000000
```


