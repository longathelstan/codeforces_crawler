# J. Tàu cao tốc

## 📖 Problem

Có
$n$
điểm tập trung dân cư đông đúc. Các điểm này được đánh số từ
$1$
đến
$n$
$(1 ≤n≤ 105)$
. Mạng lưới giao thông công cộng là
$m$
đường xe lửa cao tốc một ray, mỗi đường nối một cặp điểm dân cư và chạy một chiều, mỗi đường nối một cặp điểm
$(0 ≤m≤ 105)$
. Mỗi cặp điểm dân cư có thể có hơn một đường tàu mỗi chiều, và
$n$
điểm tập trung dân cư cũng nằm trên một vùng liên thông.
Để thuận tiện cho việc đi lại của mọi người và công tác vận hành người ta quyết định, trong trường hợp cần thiết, xây dựng thêm một số ít nhất các tuyến đường mới để đảm bảo từ một điểm bất kỳ có thể đi tới điểm bất kỳ khác bằng tàu cao tốc.
Yêu cầu:
Xác định số lượng tối thiểu các đường cần xây dựng thêm.


## 🧩 Input

Input
Dòng đầu tiên chứa
$2$
số nguyên
$n$
và
$m$
.
Mỗi dòng trong
$m$
dòng tiếp theo chứa
$2$
số nguyên
$a$
và
$b$
là đường nối từ
$a$
tới
$b$
.


## 💡 Output

Output
Một số nguyên chứa số lượng đường tối thiểu cần xây.


## 🧠 Example

### Input

```text
5 4
1 2
2 3
1 4
4 5
```

### Output

```text
2
```



## 📝 Note

Note
Cần xây dựng thêm ít nhất hai đường mới, chẳng hạn 5->3, 3->1.
![](https://espresso.codeforces.com/97ed774f17d059177db98591b13ed7012d581a4b.png)

