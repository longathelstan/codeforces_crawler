# D. Cặp xâu đối xứng

## 📖 Problem

Cho một danh sách gồm $$$n$$$ xâu, mỗi xâu chỉ bao gồm các ký tự in thường. Bạn hãy đếm số cặp (i,j) thỏa mãn $$$i<j$$$ sao cho ta tiến hành gán $$$t=s_i+s_j$$$, sau đó ta sắp xếp lại chữ cái $$$t$$$ ta sẽ tạo ra được một xâu palindrome.
Ví dụ:
$$$s_i=aba$$$ và $$$s_j=aa$$$ ta tiến hành gán $$$t=s_i+s_j=abaaa$$$ sau đó sắp xếp lại $$$t$$$ ta được xâu đối xứng $$$aabaa$$$ nên ta nói $$$i,j$$$ là một cặp xâu đối xứng.


## 🧩 Input

Input
Dòng đầu tiên gồm số nguyên dương $$$n$$$ $$$(1 \leq n \leq 10^5)$$$ là số lượng xâu.
Mỗi dòng trong $$$n$$$ dòng, là một xâu $$$s_i$$$. Input đảm bảo tổng số lượng ký tự của $$$n$$$ xâu không vượt quá $$$10^6$$$.


## 💡 Output

Output
In ra đáp án của bài.


## 🧠 Example

### Input

```text
6
aab
abcac
dffe
ed
aa
aade
```

### Output

```text
6
```



## 📝 Note

Note
aab + abcac = aababcac →aabccbaa
aab + aa = aabaa
abcac +aa =abcacaa →aacbcaa
dffe +ed =dffeed → fdeedf
dffe +aade = dffeaade → adfaafde
ed +aade =edaade → aeddea

