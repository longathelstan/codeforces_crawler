# G. Liên lạc (5 điểm)

## 📖 Problem

An có n người bạn, người bạn thứ i có độ tuổi là ai. Chúng ta có thể coi An là người bạn số 1.
Bây giờ, anh ta muốn gửi thư cho người bạn thứ $$$t$$$. Để thực hiện điều này, anh ta có thể trực tiếp gửi thư cho $$$t$$$ hoặc gửi nó thông qua vài người bạn. Khi người bạn $$$i$$$ muốn gửi thư cho người bạn $$$j$$$, do có sự chênh lệch tuổi tác nên sẽ tốn thời gian là |$$$a_i - a_j$$$|. Tuy nhiên, có $$$k$$$ cặp bạn bè thân thiết không quan tâm đến chênh lệch tuổi tác, do đó thời gian để gửi thư giữa hai cặp bạn bè này sẽ bằng 0.
Bây giờ, anh ta muốn biết với mỗi người bạn $$$t$$$ từ $$$1$$$ tới $$$n$$$, thời gian ngắn nhất để anh ta gửi thư cho người bạn này bằng bao nhiêu.


## 🧩 Input

Input
*
Dòng đầu tiên chứa hai số nguyên $$$n, k \le 2 * 10^5$$$.
*
Dòng thứ hai chứa n số nguyên mô tả dãy a. $$$(1 \le a_i \le 10^9)$$$.
*
$$$k$$$ dòng cuối, mỗi dòng chứa hai số $$$i, j$$$ ám chỉ $$$i, j$$$ là đôi bạn thân.


## 💡 Output

Output
*
In ra $$$n$$$ số, số thứ $$$i$$$ tương ứng là thời gian ngắn nhất để An gửi thư cho người bạn thứ $$$i$$$.


## 🧠 Example

### Input

```text
8 4
50 30 23 10 3 67 69 46
3 7
3 1
2 4
7 1
```

### Output

```text
0 7 0 7 14 2 0 4
```


