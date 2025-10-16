# ZA. Robot

## 📖 Problem

Bằng phương pháp quét sóng âm các nhà khảo cổ học có thể xác định được không gian rỗng bên trong một hang sâu, từ đó xác lập khả năng tiếp cận bên trong hang sâu để thám hiểm hoặc nghiên cứu. Để cho an toàn các nhà khảo cổ học sẽ lập một tấm bản đồ hình chữ nhật kích thước gồm
$MxN$
$(0 <M,N< 51)$
ô vuông. Trên bản đồ đó ghi số
$0$
biểu thị không gian rỗng có thể đi qua được, số
$1$
biểu thị không gian không đi qua được, hai ô vuông ghi số
$0$
kề nhau chung đỉnh hoặc chung cạnh thì rô bốt có thể đi qua được. Vị trí hàng
$1$
, cột
$1$
của bản đồ luôn bắt đầu là số
$0$
, là nơi đầu tiên đặt rô bốt khởi hành. Sau đó rô bốt thám hiểm sẽ tìm đường tiếp cận đến các vị trí bên trong của hang mà nó có thể đến được để làm nhiệm vụ dò đường.
Hãy viết chương trình tính tổng số ô vuông trong hang sâu mà rô bốt có thể đi qua được.


## 🧩 Input

Input
- Dòng đầu tiên ghi hai số
$M$
và
$N$
, cách nhau một khoảng trắng.
-
$M$
dòng tiếp theo, mỗi dòng ghi
$N$
số
$0$
hoặc
$1$
, các số cách nhau một khoảng trắng.


## 💡 Output

Output
- Dòng đầu tiên ghi tổng số ô vuông mà rô bốt sẽ đi qua được.
- Các dòng tiếp theo, mỗi dòng ghi hai số cách nhau một khoảng trắng, là hàng và cột của ô vuông cuối cùng trong mỗi nhánh đường đi theo thứ tự tăng dần theo hàng, nếu các ô vuông có số hàng bằng nhau thì ghi tăng dần theo cột (ô vuông cuối cùng trong mỗi nhánh đường đi có nghĩa là khi rô bốt đứng tại đó nó không thể tiến thêm được nữa).


## 🧠 Example

### Input

```text
5 8
0 1 1 0 0 1 1 0
1 0 1 0 1 0 1 0
0 0 0 1 1 0 0 1
0 1 1 1 0 1 1 1
1 0 0 1 1 0 0 1
```

### Output

```text
19
1 8
5 3
5 7
```


