# K. Hình vuông lớn nhất (7 điểm)

## 📖 Problem

Cho một bảng kích thước
$N$
hàng và
$M$
cột, trên các ô của bảng ghi số
$0$
hoặc
$1$
Yêu cầu:
Hãy tìm một hình vuông gồm các ô của bảng thoả mãn các điều kiện sau:
Hình vuông là đồng nhất: tức là các ô thuộc hình vuông đó phải ghi các số giống nhau (
$0$
hoặc
$1$
)
Cạnh hình vuông song song với cạnh bảng
Kích thước hình vuông là lớn nhất có thể


## 🧩 Input

Input
Dòng đầu ghi hai số
$N$
và
$M$
$(1 ≤N,M≤ 2000)$
$N$
dòng tiếp theo, dòng thứ
$i$
ghi
$M$
số mà số thứ
$j$
là số ghi trên ô
$(i,j)$
của bảng


## 💡 Output

Output
Gồm
$1$
dòng duy nhất ghi kích thước của hình vuông tìm được


## 🧠 Example

### Input

```text
11 13
0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 1 1 1 0 0 0 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0 0
0 1 1 1 1 1 1 1 1 1 0 0 0
1 1 1 1 1 1 1 1 1 1 1 0 0
0 1 1 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 1 1 1 0 0 0 0 1 1
0 0 0 0 0 1 0 0 0 0 0 1 1
```

### Output

```text
7
```



## 📝 Note

Note
Giải thích ví dụ
$1$
![](https://espresso.codeforces.com/3a0da185e77d5e0a34756ed9963bc98e04aa9fec.png)

