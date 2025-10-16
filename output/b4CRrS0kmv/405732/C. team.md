# C. team

## 📖 Problem

Một cuộc thi có toán học giữa các trường sắp diễn ra, nhưng không phải trường nào cũng sẽ đi thi và không phải học sinh nào của các trường cũng đi thi. Bạn biết rằng có
$N$
trường và sẽ có
$A$
trường tham gia và bạn cũng biết rằng mỗi trường có chính xác
$B$
học sinh và sẽ có chính xác
$D$
học sinh mỗi trường sẽ tham gia.
Hãy đếm số cách kết hợp các học sinh để tham gia.
Ví dụ:
$n= 2,A= 1,B= 2,D= 1$
, nghĩa là sẽ có
$1$
trường tham gia trong
$2$
trường, mỗi trường sẽ có
$2$
học sinh và trong đó có
$1$
học sinh tham gia.
Sẽ có
$4$
cách:
Trường
$1$
tham gia với học sinh số
$1$
Trường
$1$
tham gia với học sinh số
$2$
Trường
$2$
tham gia với học sinh số
$1$
Trường
$2$
tham gia với học sinh số
$2$
Vì số cách có thể rất lớn hãy chia dư cho
$109+ 7$


## 🧩 Input

Input
Gồm nhiều dòng tối đa là
$104$
, mỗi dòng gồm
$4$
số
$N$
,
$A$
,
$B$
,
$D$
$(1 ≤A≤N≤ 106)$
$(1 ≤D≤B≤ 106)$


## 💡 Output

Output
Với mỗi test gồm một dòng ứng với đáp án của test đó.


## 🧠 Example

### Input

```text
2 1 2 2
2 2 2 1
2 1 2 1
4 3 3 2
4 2 1 1
10 4 12 7
50 30 44 20
```

### Output

```text
2
4
4
108
6
625817778
154746653
```


