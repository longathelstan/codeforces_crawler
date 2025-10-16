# ZZE. Dãy con chung không liền kề dài nhất

## 📖 Problem

Dãy
$C$
=
$c1,c2, ...,ck$
là dãy con không liền kề của dãy
$A=a1,a2, ...,am$
nếu
$C$
có thể nhận được bằng cách chọn một dãy các phần tử không liền kề của
$A$
, nghĩa là tìm dược dãy các chỉ số
$i1,i2, ...,ik$
sao cho:
*
$1≤i1,i2, ...,ik≤m$
;
*
$i1<i2- 1,i2<i3- 1, ...,ik- 1<ik- 1$
;
*
$c1=ai1,c2=ai2,ck=aik$
.
Ta gọi độ dài của dãy số là số phần tử của nó.
Cho hai dãy:
$A=a1,a2, ...,am$
và
$B=b1,b2, ...,bn$
Dãy
$C$
được gọi là dãy con chung không liền kề của hai dãy
$A$
và
$B$
nếu như nó vừa là dãy con không liền kề của
$A$
, vừa là dãy con không liền kề của
$B$
.
Cho hai dãy số
$A$
và
$B$
. Hãy tìm độ dài của dãy con chung không liền kề dài nhất của hai dãy đã cho.


## 🧩 Input

Input
Dòng đầu tiên chứa hai số nguyên dương
$m$
và
$n$
$(2≤m,n≤103)$
được ghi cách nhau bởi dấu cách, lần lượt là số lượng phần tử của dãy
$A$
và dãy
$B$
.
Dòng thứ
$2$
gồm
$m$
số, số thứ
$i$
là số nguyên không âm
$ai$
$(ai≤104)$
Dòng thứ
$3$
gồm
$n$
số, số thứ
$j$
là số nguyên không âm
$bj$
$(bj≤104)$


## 💡 Output

Output
Ghi ra trên một dòng duy nhất độ dài của dãy con chung không liền kề dài nhất của hai dãy A và B.


## 🧠 Example

### Input

```text
4 5
4 9 2 4
1 9 7 3 4
```

### Output

```text
2
```


