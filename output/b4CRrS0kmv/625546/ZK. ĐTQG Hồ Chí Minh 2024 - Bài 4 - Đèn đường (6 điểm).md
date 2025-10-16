# ZK. ĐTQG Hồ Chí Minh 2024 - Bài 4 - Đèn đường (6 điểm)

## 📖 Problem

Trên một con đường, được coi như là một trục số dương xét từ $$$0$$$ đến $$$2^{31} - 1$$$, có hai công ty A và B nhận thi công lắp đặt đèn đường. Trong đó, công ty A nhận thi công các đèn phía bên trái, còn công ty B thi công các đèn phía bên phải.
Công ty A sẽ lắp đặt đèn đầu tiên ở vị trí $$$a$$$ và cách $$$d_1$$$ đơn vị độ dài thì đặt tiếp một cái nữa, và cứ thế lắp tại các vị trí có tọa độ $$$a, a + d_1, a + 2d_1, \dots$$$
Công ty B tương tự nhưng sẽ lắp đặt đèn đầu tiên ở vị trí $$$b$$$ và cách $$$d_2$$$ đơn vị độ dài thì đặt tiếp một cái nữa, và cứ thế lắp tại các vị trí có tọa độ $$$b, b + d_2, b + 2d_2, \dots$$$ (trong đó $$$a, b, d_1, d_2$$$ đều là các số nguyên dương).
Để rèn luyện sức khỏe, bạn Lan muốn chạy bộ trên con đường này, xuất phát tại một vị trí $$$L$$$ nguyên tùy ý nào đó thuộc $$$[0; 10^5]$$$ và chạy đến vị trí $$$L + k$$$ với $$$k$$$ nguyên.
Do chạy vào lúc bình minh, lúc đèn đường không quá sáng nên bạn Lan chỉ thấy rõ cảnh vật hai bên đường ở vị trí $$$x$$$ mà tại đó đều có đèn của cả hai bên trái và bên phải.
Bạn hãy chọn vị trí xuất phát thích hợp để chạy qua được nhiều nhất những nơi có thể ngắm được cảnh hai bên đường.


## 🧩 Input

Input
Một dòng duy nhất chứa $$$d_1, a, d_2, b, k$$$ ($$$1 \le d_1, a, d_2, b, k \le 10^9$$$).


## 💡 Output

Output
In ra một số nguyên duy nhất — số lượng lớn nhất các vị trí mà Lan có thể ngắm cảnh.


## 🧠 Example

### Input

```text
2 1 2 2 2024
```

### Output

```text
0
```



## 📝 Note

Note
*
Ví dụ 1: Công ty A chỉ lắp đèn tại vị trí lẻ, còn công ty B lắp ở vị trí chẵn nên không có vị trí nào có đèn của A lẫn B (với mọi cách chọn $$$L$$$).
*
Ví dụ 2: Công ty A lắp đèn ở vị trí chia hết cho 2, công ty B lắp đèn ở vị trí chia hết cho 4 kể từ 1000, nên Lan có thể xuất phát từ vị trí 1000 để đi qua được 507 vị trí chia hết cho 4 từ 1000 đến 3024.
*
Ví dụ 3: Lan có thể xuất phát tại vị trí 1 và sẽ đi qua các vị trí chia cho 6, do cả 2 bên đều có đèn ở những vị trí đó. Số lần gặp tối đa sẽ là $$$\frac{k}{\mathrm{lcm}(d_1, d_2)}$$$.

