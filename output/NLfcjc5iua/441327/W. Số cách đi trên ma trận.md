# W. Số cách đi trên ma trận

## 📖 Problem

Có một lưới với
$H$
hàng và
$W$
cột. Gọi
$(i,j)$
là ô ở hàng thứ
$i$
từ trên xuống và cột thứ
$j$
từ trái sang. Ô
$(i,j)$
được mô tả bởi ký tự "." nếu nó trống, ký tự "#" nếu nó bị chặn . Dữ liệu đảm bảo rằng ô
$(1, 1)$
và
$(H,W)$
là hình ô trống.
Tấn sẽ bắt đầu từ ô
$(1, 1)$
và đến ô
$(H,W)$
bằng cách liên tục di chuyển sang phải hoặc xuống ô trống liền kề.
Tìm số đường đi của Tấn từ ô (1,1) đến ô (H,W). Vì đáp án có thể rất lớn hãy in chia dư cho
$109+ 7$


## 🧩 Input

Input
Dòng đâù gồm
$H,W$
$(1 ≤H≤W≤ 1000)$
Sau đó là ma trận có kích thước
$H$
x
$W$
.


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm.


## 🧠 Example

### Input

```text
3 4
...#
.#..
....
```

### Output

```text
3
```



## 📝 Note

Note
Với test
$1$
có
$3$
cách đi như hình:
![](https://espresso.codeforces.com/f8c334ab6da1c7587b2afd6c816f5728c034c9a7.png)

