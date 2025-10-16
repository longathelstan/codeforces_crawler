# F. Ebola

## 📖 Problem

Một cơ quan có n nhân viên được đánh số thứ tự từ 1 đến n. Mỗi người có một phòng làm việc riêng của mình. Do nhu cầu công việc, hàng ngày mỗi nhân viên có thể phải tiếp xúc với một số nhân viên khác. Vào một ngày làm việc bình thường, có một nhân viên bị nhiễm bệnh Ebola, nhưng do không biết nên người này vẫn đi làm. Đến cuối ngày làm việc người ta mới phát hiện ra người nhiễm bệnh Ebola đầu tiên, Khả năng lây lan của Ebola rất nhanh chóng: một người nhiễm bệnh nếu tiếp xúc với một người khác có thể sẽ truyền bệnh cho người này.
Yêu cầu: Hãy giúp các bác sĩ kiểm tra xem cuối ngày hôm đó, có tối đa bao nhiêu người có thể sẽ nhiễm bệnh và đó là những người nào để còn cách ly. Người có tiếp xúc với người nhiễm bệnh được coi là người nhiễm bệnh.
Lưu ý: Nếu
$a$
tiếp xúc với
$b$
thi chưa chắc
$b$
đã tiếp xúc với
$a$
.


## 🧩 Input

Input
Dòng đầu tiên ghi
$2$
số tự nhiên
$n$
,
$k$
$(1 ≤n≤ 105, 1 ≤k≤n)$
tương ứng là số lượng người làm việc trong toà nhà và số hiệu của nhân viên đã nhiễm Ebola đầu tiên.
Dòng thứ
$i$
trong
$n$
dòng tiếp theo ghi danh sách những người có tiếp xúc với người thứ
$i$
theo cách sau: số đầu tiên
$m$
của dòng là tổng số nhân viên đã gặp người thứ
$i$
, tiếp theo là
$m$
số tự nhiên lần lượt là số hiệu của các nhân viên đó. Nếu
$m= 0$
có nghĩa rằng không ai đã tiếp xúc với người thứ
$i$
.
Dữ liệu được cho đảm bảo tổng số lần tiếp xúc của tất cả nhân viên trong cơ quan không vượt quá
$106$


## 💡 Output

Output
Dòng đầu tiên ghi số s là tổng số người có thể bị lây nhiễm Ebola
Dòng thứ
$2$
liệt kê tất cả nhân viên có thể bị lây nhiễm Ebola cần cách ly, danh sách cần được sắp theo thứ tự tăng dần của số hiệu nhân viên.


## 🧠 Example

### Input

```text
5 1
2 2 3
2 1 3
2 1 2
1 5
1 4
```

### Output

```text
3
1 2 3
```


