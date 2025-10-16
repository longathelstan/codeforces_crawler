# ZL. ĐTQG Hồ Chí Minh 2024 - Bài 5 - Bấp bênh (7 điểm)

## 📖 Problem

Một dãy $$$X$$$ được gọi là dãy con của dãy $$$Y$$$ nếu như có thể xóa đi một vài phần tử của $$$Y$$$ và giữ nguyên thứ tự các phần tử còn lại thì thu được $$$X$$$.
Bây giờ cho hai dãy số nguyên $$$a$$$ và $$$b$$$ lần lượt có $$$m, n$$$ phần tử, đặt là $$$a_1, a_2, \dots, a_m$$$ và $$$b_1, b_2, \dots, b_n$$$. Ta xét các dãy con chung của hai dãy số trên mà là dãy bập bênh, trong đó dãy số nguyên $$$c_1, c_2, \dots, c_k$$$ được gọi là
bập bênh
nếu như $$$k \ge 3$$$ và thỏa mãn một trong hai điều kiện sau:
$$$$$$\, c_1 < c_2 > c_3 < c_4 > \cdots \, \text{hoặc} \, c_1 > c_2 < c_3 > c_4 < \cdots \,$$$$$$
hay nói một cách tổng quát, ta luôn có $$$(c_i - c_{i-1})(c_i - c_{i+1}) < 0$$$ với mọi $$$1 < i < k$$$.
Yêu cầu:
Xác định độ dài của dãy con chung bập bênh dài nhất của hai dãy $$$a, b$$$ đã cho.


## 🧩 Input

Input
Dòng đầu tiên chứa hai số nguyên dương $$$m, n$$$ cho biết độ dài của hai dãy con ($$$1 \le m, n \le 10^4$$$). Dòng thứ hai gồm $$$m$$$ số nguyên dương $$$a_1, a_2, \dots, a_m$$$. Dòng thứ ba gồm $$$n$$$ số nguyên dương $$$b_1, b_2, \dots, b_n$$$. Các số trong hai dãy đều không vượt quá $$$10^4$$$.


## 💡 Output

Output
Ghi ra một số nguyên duy nhất là độ dài lớn nhất của dãy con chung bập bênh, nếu không tồn tại dãy như thế thì in ra
0
.


## 🧠 Example

### Input

```text
7 6
1 3 5 4 6 2 3
1 2 5 4 3 6
```

### Output

```text
4
```



## 📝 Note

Note
*
Ví dụ 1: Dãy con chung bập bênh $$$(1,5,4,6)$$$ có độ dài $$$4$$$. Không có dãy con bập bênh dài hơn.
*
Ví dụ 2: Tất cả các dãy đều tăng hoặc giảm nên không tồn tại dãy con bập bênh nào.

