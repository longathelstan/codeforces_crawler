# ZM. ĐTQG Hồ Chí Minh 2024 - Bài 6 - PIZZA (7 điểm)

## 📖 Problem

Hannah gần đây đã khám phá niềm đam mê làm bánh pizza, và quyết định mở một tiệm pizza ở trung tâm Stockholm. Cô làm điều này với sự giúp đỡ của em gái, Holly, người chịu trách nhiệm giao pizza. Tiệm pizza của họ ngay lập tức được người dân địa phương yêu thích, nhưng thật không may, tiệm liên tục bị thua lỗ. Hannah đổ lỗi cho cam kết giao hàng mà họ đưa ra khi quảng cáo tiệm:
"Bạn đang thèm một chiếc pizza ngon tuyệt? Bạn muốn nó ngay bây giờ? Hãy đặt hàng tại tiệm pizza của Hannah và chúng tôi sẽ giao pizza đến tận cửa nhà bạn. Nếu quá 20 phút kể từ lúc bạn đặt hàng cho đến khi nhận được pizza của Hannah, pizza sẽ
miễn phí
!"
Mặc dù xe giao hàng của Holly có thể chở số lượng pizza không giới hạn, nhưng cô ấy không thể theo kịp số lượng đơn đặt hàng lớn, có nghĩa là họ đã phải tặng miễn phí khá nhiều chiếc pizza vì giao trễ.
Để tìm cách khắc phục tình trạng này, Hannah đã nhờ bạn giúp phân tích các đơn hàng của ngày hôm qua. Cụ thể, nếu Holly biết trước toàn bộ các đơn hàng và áp dụng chiến lược giao hàng tối ưu, thì thời gian dài nhất mà một khách hàng phải đợi kể từ khi đặt hàng cho đến khi nhận được pizza sẽ là bao nhiêu?
Hannah cung cấp cho bạn bản đồ các con đường và các nút giao ở Stockholm. Cô ấy cũng đưa danh sách các đơn hàng của ngày hôm qua: đơn hàng $$$i$$$ được đặt lúc $$$s_i$$$, tại nút giao $$$u_i$$$, và pizza của đơn hàng này đã sẵn sàng để giao lúc $$$t_i$$$. Hannah tuân thủ nghiêm ngặt nguyên tắc "
đến trước, phục vụ trước
": nếu đơn hàng $$$i$$$ được đặt trước đơn hàng $$$j$$$ (tức $$$s_i < s_j$$$), thì pizza của $$$i$$$ sẽ ra lò trước pizza của $$$j$$$ (tức $$$t_i < t_j$$$), và pizza của $$$i$$$ phải được giao trước pizza của $$$j$$$.


## 🧩 Input

Input
Dòng đầu tiên chứa hai số nguyên $$$n$$$ và $$$m$$$ $$$(2 \le n \le 1000,\ 1 \le m \le 5000)$$$, trong đó $$$n$$$ là số nút giao ở Stockholm và $$$m$$$ là số con đường. Tiếp theo $$$m$$$ dòng, mỗi dòng chứa ba số nguyên $$$u_i, v_i, d_i$$$ $$$(1 \le u_i, v_i \le n,\ u_i \ne v_i)$$$, cho biết có một con đường hai chiều nối $$$u_i$$$ và $$$v_i$$$, mất $$$d_i$$$ đơn vị thời gian để đi qua theo cả hai hướng $$$(0 \le d_i \le 10^8)$$$. Giữa mỗi cặp nút giao có nhiều nhất một con đường.
Tiếp theo là một dòng chứa số nguyên $$$k$$$ $$$(1 \le k \le 1000)$$$ — số lượng đơn hàng. Sau đó là $$$k$$$ dòng, mỗi dòng chứa ba số nguyên $$$s_i, u_i, t_i$$$ cho biết đơn hàng được đặt lúc $$$s_i$$$, từ nút giao $$$u_i$$$ $$$(2 \le u_i \le n)$$$, và đơn hàng đã sẵn sàng để giao lúc $$$t_i$$$ $$$(0 \le s_i \le t_i \le 10^8)$$$. Các đơn hàng được cho theo thứ tự tăng dần thời gian đặt hàng, tức $$$s_i < s_j$$$ và $$$t_i < t_j$$$ với mọi $$$1 \le i < j \le k$$$.
Tiệm pizza của Hannah nằm tại nút giao số $$$1$$$, và Holly cùng xe giao hàng xuất phát từ đó lúc $$$0$$$. Luôn có thể đi từ tiệm pizza đến bất kỳ nút giao nào.


## 💡 Output

Output
Xuất ra một số nguyên duy nhất — thời gian dài nhất mà một khách hàng phải chờ từ lúc đặt hàng cho đến khi nhận pizza, giả sử Holly biết toàn bộ đơn hàng và tối ưu hóa quá trình giao hàng.


## 🧠 Example

### Input

```text
4 4
1 2 2
2 3 4
3 4 1
4 1 2
3
1 4 2
3 3 3
4 3 6
```

### Output

```text
6
```



## 📝 Note

Note
Giải thích cho ví dụ mẫu thứ nhất:
```
1-(2)-2
|     |
(2)   (4)
|     |
4-(1)-3
```
*
3: lấy pizza số 1 và 2
*
5: giao pizza số 1 (giao tại giao lộ 4)
*
6: giao pizza số 2 (giao tại giao lộ 3)
*
9: lấy pizza số 3
*
11: giao pizza số 3 (giao tại giao lộ 7)
*
6: lấy pizza số 1, 2, 3
*
8: giao pizza số 1 (giao tại giao lộ 7)
*
9: giao pizza số 2 và 3 (giao tại các giao lộ 6 và 5)
*
2: lấy pizza số 1
*
4: giao pizza số 1 (giao tại giao lộ 3)
*
6: lấy pizza số 2 và 3
*
9: giao pizza số 2 và 3 (giao tại các giao lộ 6 và 5)

