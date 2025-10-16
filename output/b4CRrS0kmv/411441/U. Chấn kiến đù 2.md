# U. Chấn kiến đù 2

## 📖 Problem

Một chú kiến dạo chơi trên một hình lập phương ABCDEFGH được mô tả dưới đây:
![](https://espresso.codeforces.com/cf498476c7a34b93ffad2af96ba09f2f36ffdb9b.png)
Chú kiến muốn biết rằng có bao nhiêu con đường để đi từ một đỉnh tới một đỉnh khác cho trước, đi qua đúng k cạnh (chú kiến luôn đi hết đoạn đường từ đầu này sang đầu kia một cạnh). Nếu chú kiến đi qua một cạnh x lần, ta đếm cạnh đó x lần. Chú muốn có một hành trình thú vị, vậy nên tại mỗi bước chú sẽ không đi lại đỉnh mà mình đã thăm ở bước ngay trước đó.
Chú kiến của chúng ta không được thông minh cho lắm, chú chỉ sử dụng được các số từ 0 tới p-1, vậy nên bạn cần tính toán kết quả theo modulo p.
Hãy viết một chương trình thực hiện các công việc sau:
* đọc đỉnh xuất phát và đỉnh kết thúc trên hành trình của chú kiến, số lượng cạnh chú kiến muốn đi qua và một số p,
* tính toán số lượng hành trình thú vị thỏa mãn các yêu cầu của chú kiến, theo modulo p,
* ghi đáp án ra output chuẩn.


## 🧩 Input

Input
Dòng đầu tiên của input chuẩn chứa hai chữ cái in hoa v1 và v2, cách nhau bởi một dấu cách trống. Hai chữ cái này lần lượt thể hiện đỉnh xuất phát và đỉnh kết thúc trên hành trình của chú kiến. Dòng thứ hai chứa hai số nguyên k và p, cách nhau bởi một dấu cách trống.
* A ≤ v1, v2 ≤ H, v1 ≠ v2.
* 1 ≤ k ≤ 2 x 10^9, 2 ≤ p ≤ 10^9.


## 💡 Output

Output
Ghi ra output chuẩn một số nguyên duy nhất là đáp án.


## 🧠 Example

### Input

```text
A B
3 100
```

### Output

```text
2
```



## 📝 Note

Note
![](https://espresso.codeforces.com/25e04e22f1f22149e2f6a95de27ef23dc6d1778a.png)

