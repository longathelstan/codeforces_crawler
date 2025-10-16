# W. Card war

## 📖 Problem

Tấn và Tân đang chơi
$1$
thể loại trò chơi về bài, trò chơi sẽ có
$n$
lá bài có giá trị riêng biệt từ
$1$
->
$n$
, Tấn sẽ bốc ngẫu nhiên
$n/ 2$
lá và Tân sẽ bốc phần còn lại.
Trò chơi sẽ bao gồm
$n/ 2$
lượt được đánh số từ
$1$
->
$n/ 2$
.
Tại các lượt chơi lẻ Tấn sẽ chọn
$1$
lá bài có giá trị là
$x$
trên tay và Tân sẽ chọn
$1$
lá bài có giá trị là
$y$
. Nếu
$x>y$
thì trò chơi sẽ kết thúc và Tấn thắng, còn không thì
$2$
lá bài đó sẽ bị cho ra ngoài và sẽ tới lượt của Tân.
Tương tự tại các lượt chơi chẵn, Tân sẽ chọn
$1$
lá bài có giá trị là
$x$
trên tay và Tấn sẽ chọn
$1$
lá bài có giá trị là
$y$
. Nếu
$x>y$
thì trò chơi sẽ kết thúc và Tân thắng, còn không thì
$2$
lá bài đó sẽ bị cho ra ngoài và sẽ tới lượt của Tấn.
Nếu hết
$n/ 2$
lượt vẫn chưa có ai thắng, trò chơi sẽ kết thúc với việc hòa.
Giả sử cả
$2$
đều chơi tối ưu hãy đếm số cách mà Tấn có thể thắng chia dư cho
$998244353$


## 🧩 Input

Input
Dòng đầu gồm số
$T$
là số lượng số test
$(1 ≤T≤ 50)$
Dòng tiếp theo gồm
$n$
$(n%2 = 0, 1 ≤n≤ 100)$
là số lượng lá bài của trò chơi.


## 💡 Output

Output
Gồm
$T$
dòng ứng với
$T$
đáp án cần tìm.


## 🧠 Example

### Input

```text
2
2
4
```

### Output

```text
1
3
```



## 📝 Note

Note
Test
$1$
: Tấn sẽ thắng nếu Tấn nhận được lá bài có giá trị
$2$
Test
$2$
: Tấn sẽ thắng nếu như Tấn nhận được
$2$
lá bài có giá trị: [3,4] , [2,4], [1,4].

