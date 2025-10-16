# A. Lục Vân Tiên (7 điểm)

## 📖 Problem

Dạo này tivi cũng đang chiếu phim
Lục Vân Tiên
, sẵn tiện lấy luôn làm tiêu đề.
Lục Vân Tiên cũng giống như
Samurai Jack
, bị Quan Thái Sư đẩy vào vòng xoáy thời gian và bị chuyển tới tương lai của những năm 2777.
Ở thời đại này, tráng sĩ phải là người thông thạo máy tính, gõ bàn phím lia lịa như đấu sĩ thời xưa múa kiếm vậy, và phải qua một cuộc thi lập trình mới được phong danh hiệu.
Để vượt qua vòng loại, Vân Tiên cần tham gia cuộc thi sát hạch. Ban Giám Khảo cuộc thi sát hạch gồm có
$N$
người, họ đều là các cao thủ trong giới IT. Các thành viên trong Ban Giám Khảo được đánh số từ
$1$
đến
$N$
, và mỗi người lại có một chỉ số sức mạnh gọi là APM (Actions Per Minute). Các giám khảo sẽ xếp hàng lần lượt từ
$1$
đến
$N$
.
Mỗi thí sinh sẽ phải đấu với
$K$
vị giám khảo, và
$K$
vị giám khảo này phải đứng liền nhau thành một đoạn (tức là các vị giám khảo
$i,i+ 1,i+ 2, ...,i+K- 1$
). Chỉ cần thắng một vị giám khảo trong số đó thì sẽ vượt qua vòng loại. Tuy nhiên, thí sinh không được chọn xem sẽ đấu với những giám khảo nào.
Vân Tiên rất lo lắng vì lỡ đụng độ với những vị giám khảo "khó nhằn" thì sẽ tiêu mất. Nên chiến thuật của Vân Tiên là tập trung hạ vị giám khảo có chỉ số APM thấp nhất trong số
$K$
vị.
Bạn hãy lập trình để giúp Lục Vân Tiên xác định được ở tất cả các phương án, thì chỉ số APM thấp nhất trong mỗi nhóm giám khảo sẽ là bao nhiêu. Có tất cả
$N-K+ 1$
phương án:
*
Phương án 1: Vân Tiên phải đấu với vị giám khảo
$1$
->
$K$
*
Phương án 2: Vân Tiên phải đấu với vị giám khảo
$2$
->
$K+ 1$
*
...
*
Phương án
$N-K+ 1$
: Vân Tiên phải đấu với vị giám khảo
$N-K+ 1$
->
$N$


## 🧩 Input

Input
Dòng 1: Gồm hai số nguyên dương
$N$
và
$K$
$(1 ≤K≤N≤ 3 * 106)$
— số lượng giám khảo và số lượng giám khảo mà Vân Tiên phải đối đầu trong một lượt.
Dòng 2: Gồm
$N$
số nguyên dương
$A1,A2, ...,AN$
$(1 ≤Ai≤ 109)$
— chỉ số APM của từng giám khảo.


## 💡 Output

Output
Gồm một dòng duy nhất là đáp án cần tìm


## 🧠 Example

### Input

```text
4 2
3 2 4 1
```

### Output

```text
2 2 1
```


