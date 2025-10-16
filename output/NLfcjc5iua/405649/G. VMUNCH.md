# G. VMUNCH

## 📖 Problem

Bessie đã chia đồng cỏ của mình là 1 vùng hình chữ nhật thành các ô vuông nhỏ với $$$R$$$ $$$(1 <= R <= 100)$$$ hàng và $$$C$$$ $$$(1 <= C <= 100)$$$ cột, đồng thời đánh dấu chỗ nào là cỏ và chỗ nào là đá. Bessie đứng ở vị trí $$$R_b, C_b$$$ và muốn ăn cỏ theo cách của mình, từng ô vuông một và trở về chuồng ở ô $$$1,1$$$ ; bên cạnh đó đường đi này phải là ngắn nhất.
Bessie có thể đi từ 1 ô vuông sang 4 ô vuông khác kề cạnh.
Dưới đây là một bản đồ ví dụ [với đá ('*'), cỏ ('.'), chuồng bò ('B'), và Bessie ('C') ở hàng 5, cột 6] và một bản đồ cho biết hành trình tối ưu của Bessie, đường đi được dánh dấu bằng chữ 'm'.
![](https://espresso.codeforces.com/7581be72c52c2a5952df5cdfc12e699f07634391.png)
Cho bản đồ, hãy tính xem có bao nhiêu ô cỏ mà Bessie sẽ ăn được trên con đường ngắn nhất trở về chuồng (tất nhiên trong chuồng không có cỏ đâu nên đừng có tính nhé)
Nếu không có đáp án thì hãy in $$$-1$$$


## 🧩 Input

Input
Dòng $$$1$$$: $$$2$$$ số nguyên cách nhau bởi dấu cách: $$$R$$$ và $$$C$$$
Dòng $$$2..R+1$$$: Dòng $$$i+1$$$ mô tả dòng $$$i$$$ với $$$C$$$ ký tự (và không có dấu cách) như đã nói ở trên.


## 💡 Output

Output
Dòng $$$1$$$: Một số nguyên là số ô cỏ mà Bessie ăn được trên hành trình ngắn nhất trở về chuồng.


## 🧠 Example

### Input

```text
5 6
B...*.
..*...
.**.*.
..***.
*..*.C
```

### Output

```text
9
```


