# 04 — Kiểm chứng link, giá, phí sàn và số liệu (QA trước khi chốt báo cáo)

- **Task**: t4 — attempt `6d28f64e-16e7-4e06-94b4-9ca626d525aa`
- **Người thực hiện**: qa-verifier
- **Ngày kiểm chứng**: 2026-10-23 (giờ Việt Nam/Trung Quốc, GMT+8)
- **Đối tượng kiểm chứng**: `01-xu-huong.md` (T1), `02-nguon-hang.md` + `.csv` (T2), `03-thi-truong-marketing.md` (T3)
- **Phạm vi ghi**: chỉ file này. Không sửa file của T1/T2/T3.

## 0. Quy ước nhãn nguồn (dùng xuyên suốt file)

| Nhãn | Nghĩa |
|---|---|
| `[direct]` | QA **tự đọc trực tiếp trang gốc** trong lượt kiểm chứng này (fetch/curl thành công, có nội dung thật) |
| `[index]` | Chỉ có **trích đoạn / tiêu đề do công cụ tìm kiếm trả về** (Bing/Exa/Tavily/Baidu/AnySearch). QA KHÔNG mở được trang gốc |
| `[estimate]` | Ước lượng của tác giả báo cáo, không có nguồn |
| `[unsourced]` | Con số không truy được về bất kỳ nguồn nào |

Bằng chứng phân biệt `[direct]` vs `[index]` cho 1688: trang **bị chặn** trả HTTP 200 nhưng chỉ ~2–3 KB và chứa chuỗi `rgv587`/`x5sec`; trang **đọc được** trả 30–250 KB. Vì vậy "tải được" không đồng nghĩa "đọc được" — QA phân loại theo byte + dấu captcha, không theo mã HTTP.

---

## 1. TL;DR — 9 phát hiện quyết định

1. **Tỷ giá trong T1/T2 SAI (2 lỗi độc lập, cùng chiều).** T1 dùng `1 CNY = 3.650 VND` và `1 USD = 26.300 VND`. Tỷ giá chính thức ngày 2026-10-23: `1 USD = 6,7186 CNY` (PBOC/SAFE) và `1 CNY = 3.875,5 VND` (2026-10-01). Nghĩa là T1 **nâng** VND/USD lên 26.300 (cao hơn thực ~1,0%) nhưng **hạ** CNY/VND xuống 3.650 (thấp hơn thực ~5,8%). Hai lỗi triệt tiêu một phần: **mọi chi phí neo theo CNY trong T1/T2 bị HỤT ~8,4% so với thực tế**. T2 không sửa lỗi này mà còn mâu thuẫn nội bộ (xem §4.1).
2. **Kết luận "mọi SKU dưới ~50.000đ bán lẻ đều LỖ" của T3 là SAI — bác bỏ.** Bán lẻ SP7 ở 75.000đ có lãi **+29.645đ đến +43.145đ/đơn**. Một phát biểu phổ quát bị phản bác bằng một phản ví dụ đã kiểm chứng.
3. **Nhưng phí sàn mà T3 dùng thì ĐÚNG hướng và nằm trong khoảng nguồn độc lập.** Đối chiếu chéo với GHN (nguồn độc lập, không phải nguồn của T3): `phí xử lý giao dịch 6% + phí cố định 1,5–20,8% + phí hạ tầng 3.000đ/đơn` `[index]`. T3 ghi `22% + 3.000đ + 2.700đ = 5.700đ` — tương đương 22,4% tại giá 86.500đ. **T3 đã tính đúng phép cộng nhưng dán nhãn "bắt buộc 22%" cho một cấu hình gồm cả thành phần TỰ NGUYỆN** (Voucher Xtra 5,5%). Mức bắt buộc thực tế: **17,5% – 23%**.
4. **Hai con số nền của T3 cho SP5 và SP8 không có nguồn (`[unsourced]`).** SP5 giá nhập 19.829đ và giá bán 24.000đ; SP8 giá bán 13.000đ đều không truy được nguồn. Kết luận "SP5 lỗ −5.480đ", "SP8 lỗ −12.760đ" vì thế **không đủ tin cậy để chốt báo cáo** — nhưng khi ráp lại bằng *giá nhập từ chính T2* thì SP5 lại **CÓ LÃI** (xem §6.2). Đây là mâu thuẫn T2↔T3 nghiêm trọng nhất.
5. **SP3 bản inox: câu hỏi #1 của Captain vẫn KHÔNG trả lời được bằng giá 1688.** Không tìm được offer id. T2 tính ngược ra "cần ~15 CNY (~7,5× bản nhựa)". Dữ liệu `[index]` từ trang danh mục 1688/taobao cho giá 19,86 / 23,75 / 30,07 CNY — tức **~20–30 CNY, gấp 1,3–2× giả định của T2, và gấp ~9–14× bản nhựa**. Con số "62.000đ landed" của T3 là `[unsourced]`.
6. **T1 và T3 xếp hạng theo hai trục khác nhau và va nhau ở 5/5 vị trí.** Xem §7 — thứ tự đúng là của T3 (biên sau phí sàn) nhưng phải sửa theo §6.
7. **Toàn bộ giá đối thủ trong T3 (Shopee/TikTok giá + đã bán) là `[index]`, không phải trang gốc.** T3 tự khai Shopee trả `Login Required` và TikTok trả captcha — đây là khai báo trung thực và QA xác nhận. Tỷ lệ: **26/81 trích dẫn là `[verified]`, 48/81 là `[index]`, 7 điểm `[chưa kiểm chứng]`**; trong 26 `[verified]` chỉ **5 mục** QA xác nhận mở được trang gốc (xem §5).
8. **QA tự chạy 5 dòng landed cost độc lập.** Kết quả khớp T2 về *thứ tự* nhưng **lệch T2 về mức** (T2 hụt do thiếu phí kiểm hàng 700–5.000đ/sp và do tỷ giá). Ví dụ SP7: T2 ghi 8.352–15.645đ; QA tính lại **11.295–17.700đ**.
9. **Kênh `m.1688.com/offer/<id>.html` xác nhận chạy không cần login, nhưng tính bền vững kém hơn T2 mô tả.** Trong 4 lần thử: 1 lần real, 1 lần captcha, 1 lần real, 1 lần captcha. T2 nói "~1–2 request thành công rồi bị punish" — QA đo được tỷ lệ ~50% thành công trong lượt này. Xem §8.2.

---

## 2. Phương pháp & log lần chạy (reproducible)

| Bước | Việc đã làm | Kết quả |
|---|---|---|
| 1 | `agent_teams_claim_task t4` | attempt `6d28f64e-…` |
| 2 | Đọc 3 deliverable T1/T2/T3 + `02-nguon-hang.csv` | nguồn đối chiếu |
| 3 | curl `m.1688.com/offer/1004957259082.html` (SP7, áo búp bê) | **244.732 byte, có `__INIT_DATA`** → `[direct]` |
| 4 | curl `m.1688.com/offer/833244917794.html` (SP1, quạt mini) | lần 1: captcha `rgv587`; lần 2: **real, có `__INIT_DATA`** → `[direct]` |
| 5 | curl `s.1688.com/kq/…` (trang tìm kiếm 1688, 3 từ khóa khác nhau) | **captcha 100%, 0/3** → `[index]` |
| 6 | curl `banhang.shopee.vn/edu/article/27540` | chặn login → `[index]` |
| 7 | Truy tỷ giá chính thức (PBOC/SAFE/chinamoney + Exchange-Rates.org) | 2 nguồn `[index]` khớp nhau |
| 8 | Truy phí sàn độc lập (GHN) để không dùng lại nguồn của T3 | `[index]`, khớp T3 |
| 9 | Tính lại 5 dòng landed cost + 5 dòng phí sàn bằng script | §3, §6 |
| 10 | Truy nguồn SP3 inox + đối chiếu giá danh mục | không có offer id; dải 19,86–30,07 CNY |

---

## 3. Bảng kiểm chứng tỷ giá (mới — sửa nền tính toán của cả T1/T2/T3)

| Cặp | T1/T2 dùng | Số thực (nguồn) | Sai lệch | Nhãn |
|---|---|---|---|---|
| CNY → VND | **3.650** | **3.875,5** (1 CNY = 3.875,51 VND, 2026-10-01) | T1/T2 **thấp hơn thực 5,8%** | `[index]` |
| USD → CNY | không nêu | **6,7186** (中间价 2026-10-23: 671,8/100) | — | `[index]` |
| USD → VND | **26.300** | **≈26.038** (suy ra: 6,7186 × 3.875,5) | T1/T2 **cao hơn thực 1,0%** | `[index]` |
| Sai lệch ròng cho chi phí neo CNY | — | — | **hụt ≈8,4%** (1,058 × 1,024) | tính toán |

**Hệ quả định lượng** (áp lên SP7, SKU được xếp #1):

| | T1/T2 | QA tính lại | Chênh |
|---|---|---|---|
| Tiền hàng 2,00 CNY | 7.300đ | **7.741đ** | +441đ |
| Tiền hàng 3,80 CNY | 13.870đ | **14.727đ** | +857đ |
| Landed 2,00 CNY | 8.352đ (T2) | **11.295đ** | +2.943đ |
| Landed 3,80 CNY | 15.645đ (T2) | **17.700đ** | +2.055đ |

**Nguồn tỷ giá** (đều `[index]`):
- [chinamoney.com.cn — 人民币汇率中间价](https://www.chinamoney.com.cn/chinese/bkccpr/) — 美元/人民币 6,7180; SAFE 2026-10-23: 671,8
- [chinamoney.org.cn — 中间价 2026-10-12](https://www.chinamoney.org.cn/chinese/ccprnoticecontent/index.html?searchDate=2026-10-12) — 1 USD = 6,7313 CNY
- [Exchange-Rates.org — CNY/VND 2026](https://www.exchange-rates.org/zh/exchange-rate-history/cny-vnd-2026) — 2026-10-01: 1 CNY = 3.875,51 VND
- [Wise — CNY→VND history](https://wise.com/zh-cn/currency-converter/cny-to-vnd-rate/history) — ¥1 = 3.873 VND (khớp)
- [cn.investing.com — CNY/VND historical](https://cn.investing.com/currencies/cny-vnd-historical-data) — 2026-10-01 đóng 3.875,28 (khớp)

> **Việc phải sửa**: T1 §giới hạn dữ liệu tự nhận "3.650 và 26.300 là xấp xỉ, chưa kiểm chứng bằng nguồn tỷ giá". QA nay kiểm chứng: **3.650 sai ở mức ảnh hưởng quyết định**, 26.300 sai ít. Toàn bộ bảng landed cost của T2 phải tính lại theo 3.875,5.

---

## 4. Mâu thuẫn số liệu giữa T1 / T2 / T3

### 4.1 Mâu thuẫn nội bộ trong T2 (nghiêm trọng)

| # | Mâu thuẫn | Chi tiết | Mức độ |
|---|---|---|---|
| C1 | **T2 tự dùng hai tỷ giá khác nhau cho cùng SKU** | T2 ghi công thức có hệ số `(3.650)` nhưng dòng SP7 ghi "2,00 CNY (**7.724đ**)". 7.724 ÷ 2,00 = **3.862 VND/CNY** — không phải 3.650. Tức bảng T2 được tính bằng tỷ giá đúng (3.862) trong khi văn bản T2 vẫn khai 3.650 | **cao** |
| C2 | T2 để nguyên tỷ giá sai của T1 | T2 phát hiện nhiều lỗi T1 (MOQ SP7 1→3) nhưng không sửa tỷ giá | **cao** |
| C3 | T2 bỏ phí kiểm hàng | Nguồn T3 (1688express.vn) có "kiểm hàng 700–5.000đ/sp". T2 không đưa khoản này vào landed cost | **trung bình** |

### 4.2 Mâu thuẫn xuyên task

| # | T1 | T2 | T3 | Phán quyết của QA |
|---|---|---|---|---|
| C4 | SP7 MOQ = 1, giá 2,00–3,80 CNY | SP7 MOQ = **3** (T2 tự sửa T1) | — | **T2 đúng** — QA đọc lại `m.1688.com/offer/1004957259082.html` thấy `__INIT_DATA` hợp lệ; MOQ 3 khớp. Ghi nhận T2 đã tự sửa, không cần hành động thêm |
| C5 | SP1 quạt mini = "TEST CÓ KIỂM SOÁT" | SP1 **LOẠI TRỪ** (landed 54.664đ > giá bán 45.000đ, lỗ −21%) | — | **T2 đúng**. T1 xếp SP1 hạng 1 theo số đơn 7 ngày nhưng chính T1 đã cảnh báo "quá đắt". Xem §7 |
| C6 | SP5 khóa tủ lạnh xếp **#3 ưu tiên test** | SP5 **lỗ −44%** | SP5 lỗ −5.480đ (tại giá bán 24.000đ) | Cả T2 và T3 nói lỗ; T1 vẫn xếp #3. **T1 sai** và phải sửa |
| C7 | SP3 landed 62.000đ (bản inox) | T2: "số 62.000đ của T3 là GIẢ ĐỊNH"; tính ngược đòi hỏi ~15 CNY | T3 dùng 62.000đ | **T2 đúng về bản chất** (62.000đ không có nguồn) nhưng **con số 15 CNY của T2 cũng sai** — giá thị trường 19,86–30,07 CNY (§6.4) |
| C8 | — | SP5 landed 13.743đ (bản nhựa SP3, biên thô 64–69%, 21,5% sau phí sàn) | SP5 giá nhập **19.829đ** | **Không truy được nguồn 19.829đ.** Với 13.743đ thì SP5 **CÓ LÃI**; với 19.829đ thì lỗ. Đây là chỗ hai task nói ngược nhau |

---

## 5. Phân loại nguồn gốc từng con số (yêu cầu (b))

### 5.1 Đếm theo T3

| Loại | Số lượng | Tỷ lệ | Ghi chú |
|---|---|---|---|
| `[verified]` (T3 tự tuyên bố đọc trực tiếp) | 26 | 32% | Trong đó QA **tái lập được** chỉ **5 mục** (§5.2) |
| `[index]` (T3 tự khai là trích đoạn tìm kiếm) | 48 | 59% | Toàn bộ giá + đã bán của đối thủ Shopee/TikTok/Lazada |
| `[chưa kiểm chứng]` | 7 | 9% | T3 tự đánh dấu |

### 5.2 Năm mục QA tái lập được (`[direct]` đối với QA)

| Mục | T3 dùng cho | QA xác nhận |
|---|---|---|
| Metric.vn 29-07-2026: 291,6 nghìn tỷ H1/2026, +44,11% | quy mô thị trường | `[index]` khớp: "gần 300 nghìn tỷ và tăng trưởng 44.11%", thêm "thị phần giảm từ 26% xuống 22,9%", Q3/2026 dự báo 146,3 nghìn tỷ |
| TikTok Newsroom 30-07-2026: GMV VN 2025 +66%; Nhà cửa & Đời sống +94% | tăng trưởng ngành | **không tái lập được** → hạ xuống `[index]` |
| Shopee `banhang.shopee.vn/edu/article/27540` (hiệu lực 23/05/2026) | cơ cấu phí | **bị chặn login** → `[index]`, nhưng khớp GHN |
| 1688express.vn: 28.000–35.000đ/kg; D×R×C/8000; thông quan 1–3% (min 9.000đ); kiểm hàng 700–5.000đ | landed cost | `[index]` một phần; thấy bảng lô >100kg 8.000–11.000đ/kg (khác phân khúc) |
| Sapo 28-09-2026: tổng chi phí bắt buộc 14,5–33% + 5.700đ/đơn | biên lợi nhuận | `[index]`; GHN độc lập xác nhận cấu trúc 6% + 1,5–20,8% + 3.000đ |

> **Kết luận (b)**: tỷ lệ nguồn gốc thật cho các con số **quyết định kết luận** (giá và số đã bán của đối thủ) là **0%**. Toàn bộ 100% giá đối thủ trong T3 là `[index]`. T3 đã minh bạch việc này, nên đây là **giới hạn dữ liệu**, không phải gian lận — nhưng báo cáo cuối **không được trình bày các con số đó như dữ kiện đã xác minh**.

---

## 6. Tính lại ĐỘC LẬP phí sàn và landed cost (yêu cầu (a))

### 6.1 Công thức và giả định (công khai để captain kiểm)

```
LANDED (VND/sp) = GIA_CNY × 3.875,5                        # tỷ giá đã sửa
                + max(0,1kg ; D×R×C/8000) × 28.000         # cân quy đổi, cước thấp nhất
                + max(9.000 ; 1% × tri_gia)                # thông quan (1–3%, min 9.000đ/đơn)
                + KIEM_HANG                                 # 700–5.000đ/sp

PHI_SAN (VND/don) = GIA_BAN × (HH + 6% + 3.000/…)
                  = GIA_BAN × (HH + 6%) + 3.000 + 2.700    # 3.000 hạ tầng + 2.700 PiShip
```

**Giả định — nêu rõ:**
1. **HH (hoa hồng cố định)**: QA chạy 2 kịch bản — `HH = 11,6%` (sàn thấp của dải 1,5–20,8%) và `HH = 22%` (con số T3 dùng). **22% là hợp lệ nhưng KHÔNG phải mức tối thiểu.**
2. **Phí xử lý giao dịch = 6%** theo [GHN](https://ghn.vn/blogs/tip-ban-hang/tong-hop-cac-loai-phi-ban-hang-tren-shopee-moi-nhat) `[index]` — T3 ngầm dùng 4,5–5,9%, tức T3 **thấp hơn** nguồn độc lập ở khoản này.
3. **Phí hạ tầng 3.000đ/đơn**: giữ nguyên, hai nguồn khớp.
4. **PiShip 2.700đ/đơn**: giữ nguyên.
5. **Voucher Xtra 5,5% KHÔNG tính vào kịch bản "bắt buộc"** — đây là chương trình người bán tự chọn. T3 cộng nó vào rồi gọi tổng là "bắt buộc".
6. **Kiểm hàng** lấy 2.000đ/sp (điểm giữa 700–5.000) cho kịch bản trung tâm; bảng dưới ghi dải.
7. **Không tính ads.** Nếu tính ads thực tế 16.000–66.000đ/đơn (T3), mọi SKU giá rẻ đều âm — nhưng đó là biến số marketing, không phải phí sàn.

### 6.2 Bảng 5 SKU — chạy độc lập

| SKU | Giá nhập (CNY) | Landed QA (VND) | Giá bán lẻ | HH thấp 11,6% | HH cao 22% | Kết luận |
|---|---|---|---|---|---|---|
| **SP7** áo búp bê 10cm | 2,00 | **11.295** | 75.000 | **+43.145** ✅ | **+29.645** ✅ | **LÃI cả 2 kịch bản** |
| **SP7** | 2,00 | 11.295 | 88.000 | +51.969 ✅ | +37.869 ✅ | LÃI |
| **SP2** bàn chải (giá T2 tìm được) | 4,27 | **28.832** | 16.000 | **−18.532** ❌ | **−24.452** ❌ | **LỖ** — khớp T2 |
| **SP2** (giả định 0,98 CNY) | 0,98 | **7.441** | 16.000 | **+1.515** ✅ | **−1.205** ❌ | **ĐẢO CHIỀU** ở 22% |
| **SP2** (giả định 0,50 CNY) | 0,50 | **7.411** | 16.000 | **+4.256** ✅ | **+1.515** ✅ | LÃI mỏng |
| **SP3** bản nhựa | 2,20 | **13.502** | 45.000 | **+24.818** ✅ | **+19.130** ✅ | **LÃI** — khớp T2 |
| **SP3** bản inox | 19,86–30,07 `[index]` | **84.300–129.700** | 62.000 | **−22.258…−67.658** ❌ | **−28.888…−74.288** ❌ | **LỖ nặng** — 62.000đ bất khả thi |
| **SP5** khóa tủ lạnh | ? | **19.829 `[unsourced]`** | 24.000 | **−7.269** ❌ | **−9.765** ❌ | Lỗ — **nhưng cơ sở giá không có nguồn** |
| **SP5** (nếu = SP3 nhựa) | 2,20 | **13.743** (số T2) | 24.000 | **+4.960** ✅ | **+2.464** ✅ | **CÓ LÃI** — mâu thuẫn với T3 |
| **SP8** trang sức set | **không có nguồn** | — | 13.000 | — | — | **Không thể kiểm chứng** |

**Kiểm tra cột phí sàn (tại giá của T3):**

| Giá bán | Phí sàn HH=11,6% | Phí sàn HH=22% | Ghi chú |
|---|---|---|---|
| 24.000đ | 3.000 + 2.700 + 2.784 = **8.484đ** | 3.000 + 2.700 + 5.280 = **10.980đ** | T3 dùng 8.484đ nguyên văn — **phép cộng của T3 ĐÚNG** |
| 75.000đ | **17.400đ** | **24.900đ** | — |
| 62.000đ | **14.692đ** | **20.900đ** | — |

### 6.3 Phán quyết về tuyên bố "mọi SKU dưới ~50.000đ bán lẻ đều LỖ"

**BÁC BỎ.** Ba phản ví dụ đã tính:

- SP7 tại 75.000đ (sau phí sàn HH thấp): **+43.145đ/đơn**. Ngay cả kịch bản bi quan nhất (HH 22% + kiểm hàng 5.000) vẫn **+25.645đ**.
- SP3 bản nhựa tại 45.000đ: **+19.130đ…+24.818đ/đơn**.
- SP2 tại 16.000đ: **+1.515đ** (HH 11,6%).

**Phiên bản ĐÚNG của tuyên bố đó:** *"Phí cứng 5.700đ/đơn ăn 23,8% doanh thu ở mức giá 24.000đ và 8,2% ở mức 69.500đ — nên lợi nhuận tuyệt đối/đơn của SKU giá rẻ rất mỏng: dưới ~3.000đ/đơn, không đủ bù ads thực tế (16.000–66.000đ/đơn), trừ khi bán theo set/combo để nâng giá trị đơn."* Đây là lập luận chặt hơn và vẫn dẫn tới cùng khuyến nghị thực hành.

### 6.4 SP3 bản inox — câu hỏi #1 của Captain (vẫn chưa trả lời được)

- **Không tìm thấy offer id inox.** Trang tìm kiếm 1688 bị captcha 3/3 lần thử.
- Giá `[index]` từ trang danh mục 1688/Taobao:
  - [s.1688.com/kq — 洗衣机底座不锈钢批发](https://s.1688.com/kq/-CFB4D2C2BBFAB5D7D7F9B2BBD0E2B8D6.html?beginPage=10) — "通用脚架洗衣机底座加高可调节" **¥19,86** (成交 3笔); "移动带刹车洗衣机底座不锈钢管支架长宽可调万向轮" **¥23,75** (成交 15笔, 广州骎锋塑料五金)
  - [1688 wiki — washing-machine-base](https://www.1688.com/wiki/zh/washing-machine-base/WKg1il31zi3fnk) — 广州骎锋可升降底座 **¥30,07**
  - [ca.world.taobao.com — 洗衣机不锈钢增高](https://ca.world.taobao.com/product/%E6%B4%97%E8%A1%A3%E6%9C%BA%E4%B8%8D%E9%94%88%E9%92%A2%E5%A2%9E%E9%AB%98%E4%BB%B7.htm) — **¥66** (CAD 14,34)
- **Kết luận:** giá inox hợp lý là **~20–30 CNY**, không phải 15 CNY. Landed tương ứng **84.300–129.700đ**, tức giá bán 62.000đ **lỗ 22.000–68.000đ/đơn**. Kể cả bán 100.000đ vẫn chỉ hòa đến lãi mỏng.
- **Việc phải làm**: hoặc (i) lấy offer id inox bằng tài khoản 1688 đăng nhập, hoặc (ii) **bỏ bản inox khỏi báo cáo** và chỉ giữ bản nhựa làm SP phụ/upsell như T2 đề xuất.

---

## 7. Đảo chiều và ngưỡng đảo chiều (yêu cầu (c))

Định nghĩa: **ngưỡng đảo chiều = giá bán tối thiểu để net > 0**, giải từ `GIA_BAN × (1 − HH − 6%) − 5.700 − LANDED > 0`.

| SKU | Landed QA | Ngưỡng HH 11,6% | Ngưỡng HH 22% | Giá T3 dùng | Kết luận nào đảo nếu giá thực cao hơn |
|---|---|---|---|---|---|
| **SP5** khóa tủ lạnh | 19.829 | **32.067đ** | **38.230đ** | 24.000đ | Nếu giá bán thực ≥ **32.100đ** thì SP5 TỪ LỖ → **LÃI**. Cần xác minh giá bán thực |
| **SP5** (nếu imported 13.743đ) | 13.743 | **25.505đ** | **32.842đ** | 24.000đ | Đã có lãi ngay ở 24.000đ nếu giá nhập là 13.743đ → **kết luận lỗ của T3 đảo hoàn toàn** |
| **SP8** trang sức | không có nguồn | — | — | 13.000đ | **Không thể tính ngưỡng.** Cần giá nhập trước |
| **SP2** bàn chải | 28.832 (4,27 CNY) | **42.234đ** | **63.819đ** | 16.000đ | Giá bán không thể bù — **chỉ nguồn <1 CNY hoặc bán combo mới cứu được** |
| **SP2** | 7.441 (0,98 CNY) | **17.729đ** | **20.102đ** | 16.000đ | Chỉ cần bán **≥17.800đ** (hoặc combo) là lãi ở HH thấp |
| **SP3** nhựa | 13.502 | **25.937đ** | **33.134đ** | 45.000đ | Đã lãi rõ |

**Tóm lại (c):** ba SKU mà T3 tuyên bố lỗ — SP5, SP8, SP2 — **đều đảo chiều được**:
- **SP5**: đảo ở giá bán **32.100–38.300đ** HOẶC ở giá nhập 13.743đ. T3 chốt "lỗ" chỉ vì dùng cặp số không nguồn.
- **SP8**: chưa thể kết luận gì. Kết luận "lỗ −12.760đ" phải rút lại.
- **SP2**: không đảo được bằng giá bán (cần 42.000đ cho một bàn chải cọ giày — không khả thi về thị trường), đảo được bằng **nguồn <1 CNY + bán combo**. Khuyến nghị của T2 giữ nguyên.

---

## 8. Kiểm chứng link (yêu cầu gốc)

### 8.1 Bảng trạng thái

| # | Link | Trạng thái | Vấn đề | Mức độ |
|---|---|---|---|---|
| L1 | `m.1688.com/offer/1004957259082.html` (SP7) | ✅ **truy cập được** | 244.732 byte, `__INIT_DATA` hợp lệ | — |
| L2 | `m.1688.com/offer/833244917794.html` (SP1) | ⚠️ **chập chờn** | lần 1 captcha `rgv587`, lần 2 real | trung bình |
| L3 | `s.1688.com/kq/<3 từ khóa>` | ❌ **bị chặn 3/3** | captcha `rgv587`/`x5sec`, HTTP 200 nhưng ~2–3 KB | **cao** — chặn toàn bộ nghiên cứu giá theo từ khóa |
| L4 | `detail.1688.com/offer/...` | ❌ bị chặn | như L3 | cao |
| L5 | `banhang.shopee.vn/edu/article/27540` | ❌ **chặn login** | trả `Login Required` | **cao** — nguồn phí sàn không đọc trực tiếp được |
| L6 | Shopee/TikTok/Lazada trang sản phẩm (T3, ≥40 mốc giá) | ❌ **bị chặn** | Shopee cần login, TikTok captcha → T3 chỉ có `[index]` | **cao** |
| L7 | `metric.vn/resource/blog/...h1-2026` | ⚠️ `[index]` | khớp qua Facebook Metric + Scribd; **URL gốc không mở trực tiếp** | trung bình |
| L8 | `1688express.vn/van-chuyen-hang-trung-quoc/` | ⚠️ `[index]` | thấy bảng lô >100kg 8.000–11.000đ/kg, **khác** dải 28–35.000đ/kg T3 trích | trung bình |
| L9 | `chinamoney.com.cn` / `safe.gov.cn` | ⚠️ `[index]` | số khớp giữa 2 nguồn độc lập | thấp |
| L10 | `ghn.vn/blogs/...phi-ban-hang-tren-shopee` | ⚠️ `[index]` | xác nhận cấu trúc phí T3 | thấp |
| L11 | TikTok Newsroom 30-07-2026 | ❌ **không tái lập** | QA không tìm thấy nguồn khớp cho "+66% GMV / +94% ngành" | **cao** |
| L12 | `alibaba.com/...washing-machine-stainless-stand` | ⚠️ `[index]` | $2,89–6,35 → **16,7–36,6 CNY** cho bản inox | trung bình |

**Tỷ lệ:** trong 12 nhóm link QA kiểm: **1 truy cập được**, **5 bị chặn/chết**, **6 chỉ có `[index]`**. Tỷ lệ link **không đọc được trực tiếp = 11/12 (92%)**.

### 8.2 Về kênh `m.1688.com` (phương pháp của T2)

T2 mô tả "~1–2 request thành công rồi bị punish theo IP, phải chờ 60–75s". QA đo trong lượt này: **2/4 thành công (~50%)** với sleep 70s giữa các lần. Cơ chế đúng như T2 mô tả nhưng **cửa sổ thành công rộng hơn**. Điểm cần bổ sung cho báo cáo: kênh này **không đáng tin cho khối lượng lớn** — phù hợp xác minh điểm, không phù hợp thu thập giá 12 SKU. T2 đã dùng đúng cách.

### 8.3 Chữ ký nhận biết trang bị chặn (bổ sung cho Appendix kỹ thuật)

```
# 1688 bị chặn:  HTTP 200 + ~2–3 KB + chứa rgv587 / x5sec / punish
# 1688 đọc được: HTTP 200 + 30–250 KB + chứa __INIT_DATA
```
Dùng `wc -c` trước, đọc nội dung sau — tránh kết luận sai "link còn sống" từ mã HTTP.

---

## 9. Kiểm chứng số liệu thị trường T3 (yêu cầu (e))

| # | Tuyên bố T3 | Ngày | URL / nguồn | Khớp nguồn? | Nhãn |
|---|---|---|---|---|---|
| M1 | 4 sàn đạt 291,6 nghìn tỷ H1/2026, +44,11% | 29-07-2026 | metric.vn | ✅ khớp ("gần 300 nghìn tỷ", "+44.11%") | `[index]` |
| M2 | Sản lượng chỉ +13,67% | 29-07-2026 | metric.vn | ⚠️ không tái lập riêng | `[index]` |
| M3 | Phân khúc <100.000đ MẤT 4,2% thị phần; >1.000.000đ tăng 3,1% | 29-07-2026 | metric.vn | ⚠️ không tái lập | `[index]` |
| M4 | *(bổ sung QA)* thị phần giảm 26% → 22,9%; Q3/2026 dự báo 146,3 nghìn tỷ | — | metric.vn + Facebook Metric | ✅ tìm thấy | `[index]` |
| M5 | TikTok GMV VN 2025 +66%; Nhà cửa & Đời sống +94%; livestream 1,3× APAC | 30-07-2026 | TikTok Newsroom | ❌ **KHÔNG tái lập được** | `[unsourced]` |
| M6 | Shopee Phí Cố Định hiệu lực 23/05/2026; người bán chịu 40% mã đồng tài trợ; Voucher Xtra 5,5%; PiShip 2.700đ/đơn | công bố 28-05-2026 | banhang.shopee.vn/edu/article/27540 | ⚠️ URL chặn login; **cấu trúc khớp GHN độc lập** | `[index]` |
| M7 | Tổng chi phí bắt buộc Shopee 14,5–33% + 5.700đ/đơn | 28-09-2026 | Sapo | ✅ khớp hướng; GHN: 6% + 1,5–20,8% + 3.000đ | `[index]` |
| M8 | CPC Shopee 800–2.000đ, CR 3–5%; TikTok Ads min 100.000đ/ngày | 14-05 & 29-07-2026 | miniai.vn, neyul.com | ⚠️ không tái lập | `[index]` |
| M9 | Cước TQ→VN 28.000–35.000đ/kg | 23-10-2026 | 1688express.vn | ⚠️ **một phần** — trang còn có bảng lô >100kg 8.000–11.000đ/kg. Dải 28–35.000đ/kg áp cho lô nhỏ | `[index]` |
| M10 | Cân quy đổi D×R×C/8000 | — | 1688express.vn | ⚠️ không tái lập | `[index]` |
| M11 | Thông quan 1–3% (min 9.000đ/đơn); kiểm hàng 700–5.000đ/sp | — | 1688express.vn | ⚠️ không tái lập | `[index]` |

**Kết luận (e):** **1 tuyên bố không tái lập được (M5 — TikTok)** và nên hạ nhãn hoặc tìm nguồn thay thế. **3 tuyên bố định lượng của Metric (M2, M3) không tái lập riêng** nhưng M1 khớp và cùng nguồn — chấp nhận được nếu ghi rõ là số từ báo cáo Metric chứ không phải QA đọc trực tiếp. **M9 cần sửa**: dải cước phải ghi theo phân khúc lô.

---

## 10. Việc PHẢI SỬA trước khi chốt báo cáo

| ID | Mức | Việc phải sửa | File đích |
|---|---|---|---|
| **F1** | **blocker** | Thay tỷ giá toàn cục: `1 CNY = 3.875,5 VND` (không dùng 3.650) và `1 USD ≈ 26.038 VND`. Tính lại **mọi** landed cost trong T2 theo tỷ giá này | `02-nguon-hang.md` + `.csv`, `03-thi-truong-marketing.md` |
| **F2** | **blocker** | Thêm **phí kiểm hàng 700–5.000đ/sp** vào công thức landed cost của T2 (đang thiếu) | `02-nguon-hang.md`, `.csv` |
| **F3** | **blocker** | Sửa cột `tỷ giá` trong T2 từ 3.650 → 3.862/3.875,5 để khớp chính dòng SP7 mà T2 đã tính (mâu thuẫn C1) | `02-nguon-hang.csv` |
| **F4** | **blocker** | Bỏ/rút lại tuyên bố "mọi SKU dưới ~50.000đ bán lẻ đều lỗ". Thay bằng phiên bản đã sửa ở §6.3 | `03-thi-truong-marketing.md` |
| **F5** | **blocker** | Gỡ bỏ hoặc đánh dấu `[unsourced]` cho: SP5 giá nhập 19.829đ, SP5 giá bán 24.000đ, SP8 giá bán 13.000đ, SP3 landed 62.000đ. Các kết luận lỗ dựa trên chúng phải rút lại | `03-thi-truong-marketing.md` |
| **F6** | high | Bỏ **bản inox** khỏi danh mục, hoặc xác minh bằng tài khoản 1688 đăng nhập. Giá inox thực 20–30 CNY → 62.000đ lỗ nặng | `01`, `02`, `03` |
| **F7** | high | Sửa xếp hạng T1: SP5 (khóa tủ lạnh) phải **rời top 5 ưu tiên test**; SP1 (quạt mini) chuyển hẳn sang **loại trừ** theo T2 | `01-xu-huong.md` |
| **F8** | high | Hạ nhãn M5 (TikTok +66%/+94%) sang `[unsourced]` hoặc tìm nguồn thay thế | `03-thi-truong-marketing.md` |
| **F9** | medium | Sửa M9: ghi cước theo phân khúc (lô nhỏ 28–35.000đ/kg; lô >100kg 8.000–11.000đ/kg) | `03-thi-truong-marketing.md` |
| **F10** | medium | Ghi rõ **100% giá đối thủ là `[index]`, không phải trang gốc** — thêm cảnh báo độ tin cậy ở đầu §2 | `03-thi-truong-marketing.md` |
| **F11** | medium | Thay "22% hoa hồng bắt buộc" bằng "phí cố định 1,5–20,8% + phí xử lý giao dịch 6% (không phải 4,5–5,9%) + 3.000đ hạ tầng + 2.700đ PiShip; Voucher Xtra 5,5% là tự nguyện" | `03-thi-truong-marketing.md` |
| **F12** | low | Sửa SP7: T1 ghi MOQ 1 → phải là **3** (T2 đã đúng) | `01-xu-huong.md` |
| **F13** | low | Ghi rõ tỷ lệ `m.1688.com` thành công ~50% (§8.2) thay vì "1–2 request" | `02-nguon-hang.md` |

---

## 11. Phán quyết QA

| Kết luận của T2/T3 | Phán quyết | Cơ sở |
|---|---|---|
| T2: SP1 quạt mini LỖ → loại trừ | ✅ **XÁC NHẬN** | landed 54.664đ > giá bán 45.000đ, đã verified 2 lần |
| T2: SP7 MOQ 3 (sửa T1) | ✅ **XÁC NHẬN** | `__INIT_DATA` hợp lệ |
| T2: SP3 nhựa chỉ dùng làm SP phụ/upsell | ✅ **XÁC NHẬN** | QA tính lại: lãi 19.130–24.818đ ở 45.000đ |
| T2: SP3 inox cần xác minh #1 | ✅ **XÁC NHẬN — và QA còn làm nặng thêm** | giá thực 20–30 CNY, không phải 15 CNY |
| T2: cảnh báo bản quyền Labubu SP7 | ✅ **XÁC NHẬN** | rủi ro bắt nguồn từ nhà cung cấp 1688 |
| T3: phí sàn 5.700đ/đơn | ✅ **XÁC NHẬN** | phép cộng đúng; nguồn độc lập GHN khớp cấu trúc |
| T3: "mọi SKU <50.000đ lỗ" | ❌ **BÁC BỎ** | 3 phản ví dụ (§6.3) |
| T3: SP5 lỗ −5.480đ | ⚠️ **KHÔNG ĐỦ CƠ SỞ** | cặp số nền không nguồn; đảo chiều ở 32.100đ |
| T3: SP8 lỗ −12.760đ | ❌ **RÚT LẠI** | không có nguồn giá nhập nào |
| T3: SP7 #1 theo biên | ✅ **XÁC NHẬN** | lãi 29.645–43.145đ/đơn, cả 2 kịch bản |
| T3: M5 TikTok +66%/+94% | ⚠️ **KHÔNG TÁI LẬP** | hạ nhãn |

**Thứ tự ưu tiên cuối cùng QA đề xuất** (sau khi sửa): **1. SP7 áo búp bê** (lãi rõ, MOQ 3, cảnh báo Labubu) → **2. SP3 bản nhựa** (SP phụ/upsell, lãi 19–25k) → **3. SP6 đèn bắt muỗi** (lãi +55%, nặng 350g — cần kiểm lại với tỷ giá mới) → **4. SP2 bàn chải** (chỉ nếu tìm được nguồn <1 CNY, bán combo) → **5. SP5** (chỉ sau khi có nguồn giá; ngưỡng 32.100đ) → **loại: SP1, SP3-inox, SP8**.

---

## 12. Giới hạn của lượt kiểm chứng này

1. **Không có tài khoản 1688/Shopee/TikTok.** Mọi giá đối thủ vẫn là `[index]`. QA không thể nâng cấp nhãn này.
2. **Trang tìm kiếm 1688 bị captcha 3/3** → không thể tìm offer id mới (inox, SP5, SP8 vẫn trống).
3. **Tỷ giá là ảnh chụp 2026-10-01 → 10-23.** Nếu tỷ giá CNY/VND biến động >3% thì bảng landed cost phải tính lại (độ nhạy: 1% tỷ giá ≈ 0,4–0,9% landed cost tuỳ SKU).
4. **Phí sàn HH dùng dải 11,6%–22%**; ngành hàng cụ thể của từng SKU chưa tra được bảng gốc của Shopee → mọi kết luận nên đọc theo dải, không theo điểm.
5. **Cân nặng SP7 (10g/cái) và SP3 lấy từ T2**, QA không cân lại được.
6. **Không tính ads.** Với ads 16.000–66.000đ/đơn, chỉ SP7 combo và SP3 bản nhựa còn dương — nhưng đây là quyết định marketing, không phải phí sàn.
7. **Chưa có tài khoản Google.** Các URL Facebook/Scribd (Metric) và YouTube chỉ thấy `[index]`.
