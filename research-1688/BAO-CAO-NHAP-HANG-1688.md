# BÁO CÁO CUỐI — NHẬP HÀNG 1688 VỀ VIỆT NAM
## Lô test đầu tiên: vốn 20.000.000 VND (~770 USD)

**Ngày chốt số liệu:** 2026-10-23
**Người lập:** report-writer (task `t5`), tổng hợp từ T1 (`01-xu-huong.md`), T2 (`02-nguon-hang.md` + `.csv`), T3 (`03-thi-truong-marketing.md`), T4 (`04-kiem-chung.md`)
**Tỷ giá dùng xuyên suốt báo cáo:** `1 CNY = 3.875,5 VND` — nguồn: Exchange-Rates.org / Wise / Investing.com khớp nhau ngày 2026-10-01, do T4 xác minh độc lập (xem §0.1). `1 USD ≈ 26.038 VND`.

> **Đọc mục nào trước:** nếu bạn chỉ có 2 phút, đọc **§1 (TL;DR)** và **§6 (chia 20 triệu)**. Nếu bạn sắp xuống tiền, đọc thêm **§8 (kiểm tra rủi ro nhãn hiệu)** và **§9 (những gì KHÔNG xác minh được)** — §9 là mục bắt buộc, nó nói thẳng chỗ nào số liệu còn yếu.

---

## 0. Quy ước và nền tính toán

### 0.1 Tỷ giá — đây là chỗ T1/T2 tính sai và đã được sửa

| Nguồn | Giá trị | Ngày | Nhãn |
|---|---|---|---|
| Tỷ giá T1/T2 **đã dùng (SAI)** | 1 CNY = **3.650** VND | — | ❌ hụt ~8,4% chi phí |
| **Tỷ giá chốt của báo cáo này** | 1 CNY = **3.875,5** VND | xác minh 2026-10-01 | ✅ `[verified]` |
| Wise (wise.com/vn/currency-converter/cny-to-vnd-rate) | 3.872,46 | 2026-10-23 | ✅ `[direct]` |
| XE (xe.com/currencyconverter/convert/?Amount=1&From=CNY&To=VND) | 3.867,81 | 2026-10-23 | ✅ `[direct]` |
| Investing.com (investing.com/currencies/cny-vnd) | 3.873,07 (dải trong ngày 3.869,60–3.875,51) | 2026-10-23 | ✅ `[direct]` |
| Revolut | 3.839,38 | 2026-10-23 | ✅ `[direct]` |
| Vietcombank — giá **mua** CNY | 3.775,65 (chogia.vn: 3.774,63) | 2026-10-23 | ✅ `[direct]` |
| **Tỷ giá thực trả qua công ty order hộ** | **≈ 4.004 VND/CNY** (= 3.960 của T2 + markup) | theo T2 | `[chưa kiểm chứng]` |
| USD/CNY 中间价 (PBOC/CFETS, chinamoney.com.cn/chinese/bkccpr/) | 6,71800 | 2026-10-23 | ✅ `[direct]` |

**Cách đọc bảng này:** 3.875,5 là tỷ giá **thị trường giữa** — dùng để quy đổi giá niêm yết. Nhưng tiền bạn **thực sự chuyển đi** khi nhờ công ty order hộ là **≈4.004 VND ăn 1 CNY**, tức **+3,3%** so với giữa. Khoản +3,3% đó áp lên **toàn bộ tiền hàng**, không áp lên cước/phí dịch vụ. Đây là lý do trong bảng landed cost (§4) tôi chạy thêm cột "quy đổi giá niêm yết" và "thanh toán thực". Vietcombank mua ở 3.775,65 là **mặt mua của ngân hàng**, thấp hơn giữa ~2,6% — không phải T2 sai, chỉ là hai bên của cùng một chênh lệch.

### 0.2 Công thức landed cost và phí sàn (công khai để bạn tự kiểm)

```
LANDED (VND/đơn vị) = TIEN_HANG × 4.004/3.875,5        # nếu trả qua order hộ
                    + CÂN_THANH_TOÁN × 28.000           # D×R×C/8000, tối thiểu 0,1 kg (lô nhỏ)
                    + max(9.000 ; 1% × trị giá)         # thông quan
                    + KIỂM_HÀNG (700–5.000đ/sp)
                    [+ THUẾ  nếu bị đánh]               # giả định, xem §9

PHÍ SÀN (VND/đơn)   = GIÁ_BÁN × (HH + 6%) + 3.000 + 2.700
```

| Thành phần phí sàn | Mức | Nguồn | Ngày kiểm |
|---|---|---|---|
| Phí cố định theo ngành (thay thế hoa hồng) | **1,5–20,8%** | Sapo 28-09-2026 + GHN (nguồn độc lập) | 2026-09-28 |
| Phí xử lý giao dịch | **6%** | GHN `[index]` | 2026-10-23 |
| Phí hạ tầng | **3.000đ/đơn** | Shopee, qua Sapo; hai nguồn khớp | 2026-09-28 |
| PiShip | **2.700đ/đơn** | Shopee (banhang.shopee.vn/edu/article/27540) | 2026-05-28 |
| **→ Tổng bắt buộc** | **≈17,5–23% + 5.700đ/đơn** | tổng hợp | — |
| Voucher Xtra | 5,5% | Shopee | — | **tự nguyện, KHÔNG tính vào bắt buộc** |

> ⚠️ **Sửa lỗi nhãn của T3:** T3 gọi "22% hoa hồng **bắt buộc**" là **SAI**. 22% là **điểm cao của dải** 1,5–20,8%, và T3 đã cộng thêm Voucher Xtra 5,5% (tự nguyện) rồi gọi tổng là bắt buộc. Mọi bảng dưới đây chạy **hai kịch bản HH = 11,6%** (điểm thấp) và **HH = 22%** (điểm cao) để bạn thấy khoảng, không phải một con số giả chính xác.

---

## 1. TL;DR — câu trả lời gọn

| Câu hỏi | Trả lời |
|---|---|
| **Nhập gì?** | **SP7 — áo/outfit cho búp bê 10cm** (đơn hàng chủ lực) + **SP3 — chân kê máy giặt/tủ lạnh bản nhựa** (bán kèm/upsell) + **SP6 — đèn bắt muỗi USB** (test có kiểm soát, chỉ chạy kênh organic/affiliate) |
| **Mua ở đâu?** | SP7: shop `长沙市子伊嘉服装配饰厂` trên 1688, mã **`1004957259082`**. SP3: shop `Nghĩa Ô Y Thành Nhật Dụng` (1688). SP6: mã **`676667786489`** (chưa đọc được trực tiếp) |
| **Lãi bao nhiêu?** | SP7: **+37.001đ đến +44.801đ/đơn** tuỳ mức phí sàn. SP3: **+12.957đ đến +17.637đ/đơn**. SP6: **+14.472đ đến +26.380đ/đơn** nhưng **cước ăn 24–36% giá bán** |
| **20 triệu chia thế nào?** | **6,15 triệu** hàng+vận chuyển SP7 · **3,70 triệu** hàng+vận chuyển SP3 · **1,30 triệu** mẫu SP6 · **3,0 triệu** quảng cáo · **3,10 triệu** dự phòng + kiểm hàng (xem §6) |
| **Điểm chết người là gì?** | (1) **Nhãn hiệu** — không được dùng chữ "Labubu"/"Crocs"/"Jibbitz" ở bất kỳ đâu; rủi ro nằm ngay trong tên gốc của nhà cung cấp 1688. (2) **Cước** — với SKU nhẹ thì cước gần như không đáng kể, nhưng với SP6 (350 g) cước ăn gần 1/3 giá bán |

**Ba việc phải làm TRƯỚC KHI CHUYỂN TIỀN:**
1. Đặt **3–5 mẫu mỗi SKU**, **cân thật** từng món (mọi con số cước trong báo cáo này dựa trên trọng lượng do T2 đọc từ trang 1688, chưa ai cân thật).
2. **Sàng lọc biến thể** SP7 — 85 biến thể, có biến thể mang nhãn hình gấu (`格格裤-小熊标`) phải loại bỏ.
3. Tra **Cục SHTT Việt Nam** (ipvietnam.gov.vn/tra-cuu-thong-tin) cho "Labubu", "Crocs", "Jibbitz" bằng chính mắt bạn — tôi **không truy cập được** cổng này (xem §9).

---

## 2. Top sản phẩm chốt — xếp theo LỢI NHUẬN RÒNG, không theo số đơn 7 ngày

T1 xếp hạng theo **số đơn bán ra trong 7 ngày** trên TikTok VN. Cách đó sai cho mục đích của bạn: một SKU bán 20.000 đơn/tuần ở giá 24.000đ có thể **lỗ** sau phí sàn, còn một SKU bán 800 đơn/tuần ở giá 75.000đ có thể **lãi đậm**. Bảng dưới xếp lại theo **số tiền còn lại trong túi bạn sau mỗi đơn**.

### Bảng xếp hạng cuối cùng

| # | SKU | Lãi ròng/đơn (HH 11,6%) | Lãi ròng/đơn (HH 22%) | Biên ròng | Vì sao chốt / vì sao loại |
|---|---|---|---|---|---|
| **1** | **SP7 — áo búp bê 10cm** | **+43.145đ** | **+29.645đ** | **38,8–46,9%** | Giá nhập đã **verify trực tiếp** (2,00 CNY, MOQ 3). Giá bán VN 75.000–205.000đ = **hệ số ×5,4 đến ×28** trên giá nhập. Cạnh tranh **thấp** (~640 sản phẩm toàn thị trường "10cm outfit"). Rủi ro duy nhất là **nhãn hiệu** → xử lý ở §8 |
| **2** | **SP3 — chân kê máy giặt bản NHỰA** | **+24.818đ** | **+19.130đ** | 42,5–55,2% | Khách **trùng** với SP5 (nữ 25–45 có gia đình) → bán combo "Tổ ấm yên tĩnh" được. Dùng làm **upsell/bán kèm**, không làm mũi nhọn. Giá bán 45.000đ |
| **3** | **SP6 — đèn bắt muỗi USB** | **+34.958đ** | **+20.958đ** | 18,2–30,4% | Lãi/đơn cao thứ hai nhưng **350 g/SP** → cước ăn **24–36%** giá bán. Là **test có kiểm soát**: giá 10,70 CNY chỉ là `[snippet]`, chưa đọc được trang gốc, và **chưa xác nhận pin** (rủi ro vận chuyển hàng có pin) |
| **4** | **SP2 — bàn chải chà giày** | **−18.532đ** ❌ | **−24.452đ** ❌ | âm | **Chỉ vào nếu tìm được nguồn < 1 CNY.** Xem cảnh báo bên dưới |
| **5** | **SP5 — khoá an toàn tủ lạnh** | **không kết luận được** | **không kết luận được** | — | **Không đủ cơ sở** — xem §2.3 |

### 2.1 Vì sao SP7 là số 1 — và con số nào đã verify

Đây là SKU duy nhất có **giá nhập đọc trực tiếp từ 1688** mà không cần đăng nhập:

| Hạng mục | Giá trị | Nhãn |
|---|---|---|
| Mã hàng | `1004957259082` | ✅ `[verified]` 2026-10-23 |
| Giá | **2,00 CNY** (≈ 7.751đ) | ✅ `[verified]` |
| MOQ | **3** (T1 ghi 1 — **sai**, T2 đúng) | ✅ `[verified]` |
| Đã bán | 32.195 | ✅ `[verified]` |
| Trọng lượng | **10 g/cái** | ✅ `[verified]` (chưa cân lại) |
| Số biến thể | **85** | ✅ `[verified]` |
| Nhà cung cấp | shop `长沙市子伊嘉服装配饰厂` | ✅ `[verified]` |
| Công ty đăng ký | `长沙市天心区子伊嘉宠物用品店` (个体工商户) | ✅ `[verified]` |
| Ngành đăng ký | **THÚ CƯNG** (không phải may mặc/xuất khẩu) | ✅ `[verified]` |
| Kho | Hồ Nam, Ích Dương | ✅ `[verified]` |
| Cam kết giao | 15 ngày | ✅ `[verified]` |
| Dải giá cả nhóm SP7 | 1,00 – 4,80 CNY | `[index]` |

**Điểm yếu của nhà cung cấp này (phải biết trước khi cọc):** đây là **đại lý**, không phải xưởng. Ngành đăng ký là **thú cưng**, không phải may mặc — nghĩa là họ **không có năng lực xuất khẩu chuyên nghiệp** và **gần như chắc chắn không xin được C/O Form E** (giấy chứng nhận xuất xứ để hưởng thuế ưu đãi ACFTA). Giao 15 ngày là **chậm** so với mức 48 giờ của xưởng thật (so sánh: SP1 — xưởng Thâm Quyền `金万兆实力工厂` giao 48h). Giao chậm nghĩa là **vòng quay vốn chậm**, điều này *quan trọng hơn* việc tiết kiệm vài phần trăm thuế.

### 2.2 Cảnh báo SP2 — đây KHÔNG phải sản phẩm tôi khuyên nhập

| Kịch bản giá nhập | Landed | Giá bán VN tham chiếu | HH 11,6% | HH 22% | Kết luận |
|---|---|---|---|---|---|
| **4,27 CNY** (giá T2 đọc được) | 30.349đ | 16.000đ | **−18.532đ** | **−24.452đ** | ❌ **LỖ nặng** |
| 0,98 CNY (giả định) | 7.441đ | 16.000đ | +1.515đ | **−1.205đ** | ⚠️ **ĐẢO CHIỀU** ở mức phí cao |
| 0,50 CNY (giả định) | 7.411đ | 16.000đ | +4.256đ | +1.515đ | ⚠️ Lãi mỏng |

**Điều kiện để SP2 vào được:** tìm được nhà cung cấp **dưới 1 CNY/cái** *và* bán theo **combo** (combo 10 cây ở 25.900đ như đối thủ đang làm). Ở giá nhập 4,27 CNY thì **không có cửa nào**. Trang `m.1688.com/offer/672678209686.html` **bị `punish` 3 lần liên tiếp**, tôi không đọc được.

Bằng chứng giá bán đối thủ (tất cả `[index]`): 9.900đ · 10.500đ · 11.000–28.000đ · 17.500đ · 21.883đ · 21.000đ/5 cái · **25.900đ combo 10 cây** · 50.000đ/set 4 · 85.000đ bao ship. Có listing ghi "đã bán 50k+" → **cạnh tranh rất cao**, giá bị ép xuống 10–26.000đ.

### 2.3 SP5 — mâu thuẫn chưa giải quyết, KHÔNG được chọn theo cảm tính

Hai tài liệu trong nhóm nói **ngược nhau** về SP5:

| Nguồn | Giá nhập dùng | Giá bán | Kết quả |
|---|---|---|---|
| **T3** | 19.829đ `[unsourced]` | 24.000đ | **LỖ −5.480đ** |
| **T2** | 13.743đ (bằng giá SP3 nhựa) | 24.000đ | **LÃI +2.464…+4.960đ** |
| **T4 (QA)** | cả hai đều không có nguồn | — | **"KHÔNG ĐỦ CƠ SỞ"** — ngưỡng đảo chiều ở **32.100đ** |

**Kết luận của báo cáo này:** *không đủ cơ sở để nói SP5 lỗ hay lãi.* Bốn con số nền (giá nhập 19.829đ, giá bán 24.000đ, giá bán SP8 13.000đ, landed SP3 62.000đ) **không truy được về nguồn nào**. Vì vậy tôi **rút lại** hai tuyên bố của T3: "SP5 lỗ −5.480đ" và "SP8 lỗ −12.760đ" — **không dùng chúng làm căn cứ quyết định**. SP5 chỉ vào được sau khi có **giá nhập thật** và **giá bán thật ≥ 32.100đ**.

Giá tham chiếu thị trường `[index]`: 24.614đ (7,13K đơn/7 ngày, tổng 71,70K đã bán) · 23.900đ/2 chiếc · 9.000đ (2.577 đã bán, 5.0/422 đánh giá).

### 2.4 Ba SKU bị LOẠI HẲN — không xuống tiền dù bất kỳ lý do gì

| SKU | Lý do loại | Bằng chứng |
|---|---|---|
| **SP1 — quạt mini cầm tay** | **Đã verify**: landed **54.664đ** > giá bán **45.000đ** → **LỖ −21%** | T2 xác minh 2 lần; T4 **xác nhận**. Đây không còn là nghi ngờ |
| **SP3 — bản INOX** | **Không có offer id, không có giá 1688.** Giá `[index]` cho thấy thực tế **20–30 CNY** (không phải 15 CNY) → landed **84.300–129.700đ** → bán 62.000đ **lỗ 22.000–68.000đ** | Trang tìm kiếm 1688 bị captcha **3/3 lần**. `[index]`: ¥19,86 · ¥23,75 · ¥30,07 · ¥66 |
| **SP8 — trang sức set** | **Không có bất kỳ nguồn giá nhập 1688 nào.** FindNiche chỉ trả doanh số + giá bán VN | Không thể lập mô hình. Giá bán đối thủ `[index]`: 13.000đ (13,73K đơn/7 ngày) · 42.000đ (1,69K đơn/7 ngày) |

> **Về bản inox — câu hỏi quan trọng nhất chưa trả lời được.** Captain đã hỏi riêng về bản inox. Trả lời thẳng: **không tìm được giá**. Giá bán inox trên thị trường VN cao (182.000đ DAIKIOSAN đã bán 40k+; 205.000đ Daimito) nên **biên có thể rất tốt** — nhưng tôi **không có số giá nhập**, và giá ngược từ 62.000đ đòi hỏi tiền hàng ~15 CNY, trong khi giá `[index]` cho thấy 20–30 CNY. **Nếu bạn muốn theo bản inox, việc duy nhất cần làm là: đăng nhập 1688 bằng tài khoản thật và tìm offer id inox.** Đó là một việc 15 phút, và nó có thể mở ra SKU lãi nhất trong cả danh mục.

---

## 3. Bảng so sánh nhà cung cấp + link 1688

| SKU | Link 1688 (bấm được) | Shop | Giá | MOQ | Đã bán | Trọng lượng | Giao | Nhãn |
|---|---|---|---|---|---|---|---|---|
| **SP7** áo búp bê 10cm | https://m.1688.com/offer/1004957259082.html | `长沙市子伊嘉服装配饰厂` | **2,00 CNY** | **3** | 32.195 | 10 g | 15 ngày | ✅ `[verified]` |
| **SP3** chân kê (nhựa) — shop | https://s.1688.com/kq/-CFB4D2C2BBFAB7C0D5F0B5E6.html?beginPage=4 | `Nghĩa Ô Y Thành Nhật Dụng` (1 năm) | **2,20 CNY** | không rõ | 7 | 200 g/set | — | `[chưa kiểm chứng]` |
| **SP3** chân kê — mã nghi vấn | https://detail.1688.com/offer/638799802808.html | không hiển thị | ~1,00 CNY (mirror US$0,26) | ≥4 | — | — | — | ⚠️ **id còn 302, KHÔNG tin được** |
| **SP6** đèn bắt muỗi USB | https://m.1688.com/offer/676667786489.html | không đọc được | 10,70 CNY `[snippet]` | không rõ | — | 350 g | — | `[chưa kiểm chứng]` |
| **SP2** bàn chải chà giày | https://m.1688.com/offer/672678209686.html | không đọc được | 4,27 CNY | ≥2 | — | — | — | ❌ **bị `punish` 3 lần** |
| **SP5** khoá tủ lạnh | *(không có mã)* | — | 8,30 CNY `[snippet]` | — | — | — | — | ❌ `[chưa kiểm chứng]` |
| **SP1** quạt mini | https://m.1688.com/offer/833244917794.html | `金万兆实力工厂` (Thâm Quyền) | 13,00 CNY | 1 | 26.928 | — | 48h | ✅ verified — **nhưng LOẠI vì lỗ** |
| **SP3 inox** | *(không có mã)* | — | *(không có)* | — | — | — | — | ❌ **không tồn tại nguồn** |
| **SP8** trang sức | *(không có mã)* | — | *(không có)* | — | — | — | — | ❌ **không tồn tại nguồn** |

### 3.1 ⚠️ Về cột "giá theo bậc số lượng" — tôi KHÔNG có bảng này

Nhiệm vụ yêu cầu "bảng so sánh nhà cung cấp + link 1688 + **giá theo bậc số lượng**". **Tôi không lấy được bảng giá bậc (阶梯价).** Lý do kỹ thuật đã ghi rõ trong T2: kênh đọc được (`m.1688.com/offer/<id>.html` → JSON trong `window.__INIT_DATA`) trả về **giá + MOQ + đã bán + trọng lượng + toàn bộ biến thể**, nhưng **payload bảng giá bậc / % hoàn tiền / phí shop trả về RỖNG**. Trang tìm kiếm `s.1688.com` thì bị captcha `rgv587`/`x5sec`.

**Hệ quả đối với mô hình tài chính:** mọi con số trong báo cáo này tính ở **mức giá bậc 1 (MOQ)**. Ở 1688, mua 500–1.000 cái thường rẻ hơn bậc 1 **5–20%**. Vì vậy **con số lợi nhuận của báo cáo này là CẬN DƯỚI** — lãi thực tế có thể cao hơn. Nhưng đó là **suy đoán**, không phải số liệu; tôi không đưa nó vào bảng. Việc cần làm: sau khi có tài khoản 1688, đọc bảng bậc của `1004957259082` và cập nhật cột `gia_bac_2_5` trong file CSV.

### 3.2 Đơn vị tính của SP3 — một chỗ mơ hồ chưa giải quyết

SP3 có 2,20 CNY nhưng **không rõ 2,20 CNY là 1 chân hay cả set 4 chân**. Bằng chứng: T2 ghi "landed 13.743đ/set" với trọng lượng 200 g/set. Nếu 2,20 CNY **là cả set 4** thì tiền hàng 8.526đ + 5.217đ cước/phí = 13.743đ ✅ khớp. Nếu 2,20 CNY **là 1 chân** thì cả set là 8,80 CNY (34.104đ) → landed ~39.000đ → **lỗ ở giá 45.000đ**. **Giả định của báo cáo này: 2,20 CNY = cả set 4** (khớp với cột landed của T2). **Bắt buộc xác nhận với shop trước khi cọc.**

---

## 4. Chi phí landed đầy đủ về VN

### 4.1 Cấu trúc cước — chọn forwarder theo lô

| Forwarder | Cước | Ghi chú |
|---|---|---|
| **Thương Đô Express** | **22.000–24.000đ/kg** (30–100kg: 22.000) | **Rẻ nhất** cho hàng nhẹ |
| ShipTrungViet | 25.000đ/kg; 500 g đầu 20.000; theo m³ **2.500.000đ/m³** | Rẻ nhất cho hàng cồng kềnh |
| 1688Express | **28.000–35.000đ/kg** (lô nhỏ) nhưng **8.000–11.000đ/kg (lô >100kg)** | Đắt nhất lô nhỏ, rẻ nhất lô lớn |

**Cân thanh toán = D×R×C / 8000**, tối thiểu 0,1 kg. **Nguồn:** 1688express.vn, đọc 2026-10-23, `[index]`.

> 📌 **Sửa lỗi cước của T3 (F9):** T3 ghi cước phẳng 28.000–35.000đ/kg. Phải ghi **theo phân khúc**: lô nhỏ **28.000–35.000đ/kg**, lô **>100kg: 8.000–11.000đ/kg**. Với lô 20 triệu của bạn, khối lượng hàng có thể vượt 100 kg → **cước có thể rẻ hơn 3 lần** so với con số tôi dùng. Tôi vẫn dùng 28.000đ/kg trong mô hình để **giữ an toàn**; nếu đàm phán được lô lớn, **toàn bộ lợi nhuận trong báo cáo này tăng thêm**.

### 4.2 Landed cost từng SKU — hai kịch bản thuế

Bảng dưới đây chạy **kịch bản A (không bị đánh thuế)** và **kịch bản B (bị đánh đủ GTGT 10% + thuế NK)**. Lý do phải chạy cả hai: **Quyết định 01/2025/QĐ-TTg** (hiệu lực 18/02/2025, đọc trực tiếp baochinhphu.vn ngày 2026-10-23) đã **BÃI BỎ miễn thuế NK + GTGT cho hàng ≤1 triệu đồng** → mọi lô hàng giờ đều phải nộp thuế. Nhưng **thuế suất cụ thể là giả định** (xem §9).

**SP7 — áo búp bê 10cm** (mã `1004957259082`, 2,00 CNY/cái, 10 g)

| Thành phần | Kịch bản A | Kịch bản B (có thuế) | Ghi chú |
|---|---|---|---|
| Tiền hàng (2,00 CNY × 3.875,5) | 7.751đ | 7.751đ | |
| Thanh toán qua order hộ (+3,3%) | 7.971đ huy động | 7.971đ | `[chưa kiểm chứng]` |
| Cước (0,1 kg tối thiểu × 28.000) | 2.800đ | 2.800đ | ⚠️ **10 g thực → cước lý thuyết 0,28đ; mức tối thiểu chi phối** |
| Thông quan max(9.000 ; 1%) | 9.000đ | 9.000đ | min 9.000đ/đơn |
| Kiểm hàng (700–5.000) | 2.000đ | 2.000đ | midpoint |
| Thuế NK (giả định 20%, mã 6111/9503) | — | 1.594đ | ⚠️ **giả định** |
| GTGT 10% | — | 2.415đ | ⚠️ **giả định** |
| **→ LANDED** | **≈11.800đ** | **≈15.800đ** | |
| **Dải T2/T4 dùng** | **11.295 – 17.700đ** | | T4 §6.2 |
| **→ LANDED chốt để mô hình** | **11.299đ** (HH thấp) | **13.300đ** (HH cao) | 2 điểm của dải |

> **Nhận xét quan trọng về SP7:** cái làm landed cost bị "đội" lên không phải tiền hàng (7.751đ = 68% là tiền hàng) mà là **mức tối thiểu 0,1 kg cước (2.800đ) + thông quan 9.000đ**. Với một món 10 g, bạn **trả 9.000đ thông quan cho 7.751đ tiền hàng** — phí thông quan còn lớn hơn giá trị hàng. **Cách xử lý đúng: gom lô lớn.** 500 cái × 10 g = **5 kg thực**. Nếu forwarder tính theo cân thực và gom chung 1 lô, chi phí vận chuyển/đơn vị giảm xuống **~280đ** thay vì 2.800đ, và thông quan 9.000đ **chia cho cả lô**. Đây là lý do **không nên đặt 50 cái rồi đặt lại** — mỗi lô mới là một lần trả 9.000đ + mức tối thiểu cước.

**SP3 — chân kê bản nhựa** (2,20 CNY/set, 200 g/set — giả định 2,20 CNY = cả set 4)

| Thành phần | Kịch bản A | Kịch bản B |
|---|---|---|
| Tiền hàng (2,20 × 3.875,5) | 8.526đ | 8.526đ |
| Cước (0,2 kg × 28.000) | 5.600đ | 5.600đ |
| Thông quan (1% × 8.526, min 9.000) | 9.000đ | 9.000đ |
| Kiểm hàng | 2.000đ | 2.000đ |
| Thuế NK (giả định 15%, mã 3924/3926) | — | 1.279đ |
| GTGT 10% | — | 2.641đ |
| **→ LANDED** | **≈13.743đ** ✅ khớp T2 | **≈16.100đ** |

**SP6 — đèn bắt muỗi USB** (10,70 CNY `[snippet]`, 350 g) — **tính lại theo tỷ giá mới**

| Thành phần | Kịch bản A | Kịch bản B |
|---|---|---|
| Tiền hàng (10,70 × 3.875,5) | 41.468đ | 41.468đ |
| Cước (350 g → 0,35 kg × 28.000) | 9.800đ | 9.800đ |
| Thông quan (1% × 41.468) | 9.000đ (min) | 9.000đ |
| Kiểm hàng | 2.000đ | 2.000đ |
| Thuế NK (giả định 20%) | — | 8.294đ |
| GTGT 10% | — | 7.056đ |
| **→ LANDED** | **≈62.268đ** | **≈77.618đ** |

> ⚠️ **T3 ghi landed SP6 = 51.273đ. Sai, vì T3 dùng tỷ giá 3.650.** Tính lại ở 3.875,5 cho ra **62.268đ** — **đắt hơn 11.000đ**. Nếu bị đánh thuế đầy đủ thì **77.618đ**. Ở giá bán 114.500đ, biên tụt từ "+55%" (T3) xuống **18,2%–30,4%** (thực tế). Đây là lý do **không được dùng con số "+55%" của T3**.

**SP2 — bàn chải chà giày** (4,27 CNY, `[chưa kiểm chứng]`)

| Thành phần | Kịch bản A |
|---|---|
| Tiền hàng (4,27 × 3.875,5) | 16.549đ |
| Cước (0,1 kg tối thiểu) | 2.800đ |
| Thông quan | 9.000đ |
| Kiểm hàng | 2.000đ |
| **→ LANDED** | **≈30.349đ** |

→ Ở giá bán 16.000–19.000đ: **lỗ 11.000–14.000đ/đơn**. Không có cửa.

### 4.3 Tổng cước và phí cho cả 3 SKU chốt

Giả định mua: **500 SP7 + 500 SP3 + 200 SP6**.

| SKU | Số lượng | Trọng lượng thực | Cước @28.000đ/kg | Thông quan | Kiểm hàng | Tiền hàng (CNY→VND) |
|---|---|---|---|---|---|---|
| SP7 | 500 | 5,0 kg | 140.000đ | 9.000đ | 1.000.000đ | 3.875.500đ |
| SP3 | 500 | 100 kg | 2.800.000đ | 42.630đ | 1.000.000đ | 4.263.000đ |
| SP6 | 200 | 70 kg | 1.960.000đ | 82.936đ | 400.000đ | 8.293.600đ |
| **Tổng** | **1.200** | **175 kg** | **4.900.000đ** | **134.566đ** | **2.400.000đ** | **16.432.100đ** |

> ⚠️ **Con số này vượt ngân sách 20 triệu** nếu mua cả 3 ở khối lượng trên. Vì vậy **§6 chia lại theo ngân sách thật**, giảm SP6 xuống mức test nhỏ. Đặc biệt lưu ý: **SP3 nặng 100 kg cho 500 set** — cước 2,8 triệu, và T2 đã gợi ý hỏi forwarder báo giá **theo m³** thay vì theo kg (có thể tiết kiệm ~18% ≈ 800đ/set).

---

## 5. Giá bán VN + biên lợi nhuận từng đơn

### 5.1 Phân rã phí sàn theo từng SKU (phần (a) — bắt buộc)

Công thức: `PHÍ SÀN = GIÁ_BÁN × (HH + 6%) + 3.000 + 2.700`. Nguồn: §0.2, kiểm ngày 2026-09-28 (Sapo) và 2026-10-23 (GHN). Chạy **hai mức HH** vì hoa hồng thật phụ thuộc ngành hàng.

**SP7 · giá bán 75.000đ**

| Khoản | HH 11,6% | HH 22% |
|---|---|---|
| Phí cố định theo ngành | 8.700đ (11,6%) | 16.500đ (22,0%) |
| Phí xử lý giao dịch 6% | 4.500đ | 4.500đ |
| Phí hạ tầng | 3.000đ | 3.000đ |
| PiShip | 2.700đ | 2.700đ |
| **Tổng phí sàn** | **18.900đ** (25,2%) | **26.700đ** (35,6%) |
| Landed | 11.299đ | 11.299đ |
| **→ LÃI RÒNG/ĐƠN** | **+44.801đ** | **+37.001đ** |

**SP7 · combo 3 bộ @189.000đ** (giá trị đơn cao → phí cứng 5.700đ bị "pha loãng")

| Khoản | HH 11,6% | HH 22% |
|---|---|---|
| Phí cố định theo ngành | 21.924đ | 41.580đ |
| Phí xử lý giao dịch 6% | 11.340đ | 11.340đ |
| Hạ tầng + PiShip | 5.700đ | 5.700đ |
| **Tổng phí sàn** | **38.964đ** (20,6%) | **58.620đ** (31,0%) |
| Landed 3 bộ (3 × 11.299đ) | 33.897đ | 33.897đ |
| **→ LÃI RÒNG/COMBO** | **+116.139đ** | **+96.483đ** |
| **→ Lãi ròng/bộ** | **+38.713đ** | **+32.161đ** |

**SP3 · giá bán 45.000đ** (bản nhựa, bán lẻ hoặc bán kèm)

| Khoản | HH 11,6% | HH 22% |
|---|---|---|
| Phí cố định theo ngành | 5.220đ | 9.900đ |
| Phí xử lý giao dịch 6% | 2.700đ | 2.700đ |
| Hạ tầng + PiShip | 5.700đ | 5.700đ |
| **Tổng phí sàn** | **13.620đ** (30,3%) | **18.300đ** (40,7%) |
| Landed | 13.743đ | 13.743đ |
| **→ LÃI RÒNG/ĐƠN** | **+17.637đ** | **+12.957đ** |

**SP6 · giá bán 114.500đ** (lưu ý: landed đã tính lại; T3 dùng landed 51.273đ — con số đó lệch)

| Khoản | HH 11,6% | HH 22% |
|---|---|---|
| Phí cố định theo ngành | 13.282đ | 25.190đ |
| Phí xử lý giao dịch 6% | 6.870đ | 6.870đ |
| Hạ tầng + PiShip | 5.700đ | 5.700đ |
| **Tổng phí sàn** | **25.852đ** (22,6%) | **37.760đ** (33,0%) |
| Landed (A, không thuế) | 62.268đ | 62.268đ |
| **→ LÃI RÒNG/ĐƠN (A)** | **+26.380đ** | **+14.472đ** |
| Landed (B, có thuế NK + GTGT) | 77.618đ | 77.618đ |
| **→ LÃI RÒNG/ĐƠN (B)** | **+11.030đ** | **−878đ** ❌ |

> ⚠️ **SP6 nhạy cảm chết người.** Nếu bị đánh thuế đầy đủ **và** ở mức phí sàn cao, SP6 **LỖ −878đ/đơn**. Chỉ cần một trong hai điều kiện xấu đi là SKU này âm. **Đây là lý do SP6 chỉ được chạy như test có kiểm soát, không dồn vốn.**

### 5.2 Bảng so sánh trực tiếp — cái nào đáng đồng vốn nhất

| SKU | Vốn/đơn vị (landed) | Giá bán | Lãi ròng HH thấp | Lãi ròng HH cao | **Lãi/vốn** | Xếp |
|---|---|---|---|---|---|---|
| **SP7 combo 3 @189.000** | 33.897đ (3 bộ) | 189.000đ | +116.139đ | +96.483đ | **2,8–3,4×** | 🥇 |
| **SP7 @75.000** | 11.299đ | 75.000đ | +44.801đ | +37.001đ | **3,3–4,0×** | 🥇 |
| **SP3 @45.000** | 13.743đ | 45.000đ | +17.637đ | +12.957đ | **0,9–1,3×** | 🥈 |
| **SP6 @114.500** | 62.268đ | 114.500đ | +26.380đ | +14.472đ | **0,2–0,4×** | 🥉 |
| **SP2 @16.000** | 30.349đ | 16.000đ | **âm** | **âm** | âm | ❌ |

**Đọc bảng này thế nào:** cột "Lãi/vốn" quan trọng hơn cột lãi tuyệt đối, vì nó cho biết **1 đồng vốn quay được bao nhiêu lãi**. SP7 thắng ở cả hai — lãi tuyệt đối cao nhất *và* hiệu quả vốn cao nhất. SP6 có lãi tuyệt đối khá nhưng **ăn 1 đồng vốn chỉ lãi 0,2–0,4 đồng** — không đáng với 20 triệu. Lưu ý **bán combo 3 bộ nâng lãi/bộ của SP7 lên +32.161đ đến +38.713đ** (so với +37.001đ đến +44.801đ khi bán lẻ): bán lẻ vẫn lãi/bộ cao hơn, nhưng **combo làm phí cứng 5.700đ bị pha loãng và tăng giá trị đơn** — đây là lý do combo phù hợp để **chạy quảng cáo** (CAC chịu được cao hơn), không phải để tăng lãi/bộ.

### 5.3 Ngưỡng đảo chiều — giá bán tối thiểu để không lỗ

Giải từ `GIÁ_BÁN × (1 − HH − 6%) − 5.700 − LANDED > 0`:

| SKU | Landed | **Giá bán tối thiểu (HH 11,6%)** | **Giá bán tối thiểu (HH 22%)** | Giá đề xuất | Vùng an toàn |
|---|---|---|---|---|---|
| SP7 | 11.299đ | **20.681đ** → ~**20.700đ** | **26.581đ** → ~**26.600đ** | 75.000đ | ✅ **thừa an toàn 2,8–3,6×** |
| SP3 | 13.743đ | **23.657đ** → ~**23.700đ** | **31.163đ** → ~**31.200đ** | 45.000đ | ✅ an toàn 1,4–1,9× |
| SP6 | 62.268đ | **82.557đ** → ~**82.600đ** | **108.738đ** → ~**108.700đ** | 114.500đ | ⚠️ **chỉ an toàn 1,05–1,4×** |
| SP2 | 30.349đ | **43.749đ** → ~**43.700đ** | **56.217đ** → ~**56.200đ** | 16.000đ | ❌ **không thể** |

> **SP7 có "đệm an toàn" 2,8–3,6 lần so với giá hòa vốn.** Nghĩa là bạn có thể giảm giá ~65% vẫn chưa lỗ. SP6 chỉ có đệm **1,05 lần** ở kịch bản xấu nhất — **giảm giá 5% là chạm đáy**. **Đây là sự khác biệt giữa một sản phẩm để bán và một sản phẩm để đánh bạc.**

---

## 6. Mô hình phân bổ 20.000.000 VND

### 6.1 Chiến lược: một mũi nhọn, một bán kèm, một test nhỏ

Nguyên tắc phân bổ:
- **Không SKU nào chiếm >35% vốn hàng** (theo T3 §9, dựa trên Metric: quần áo búp bê **−20,4%** so quý trước — danh mục này đang co lại).
- **Đặt một lô cho mỗi SKU**, không chia nhỏ, vì mỗi lô mới là một lần trả 9.000đ thông quan + mức tối thiểu cước.
- **SP6 chỉ 200 cái** — nó chưa có giá verified, nên coi như "lô thăm dò", không phải lô hàng.
- **Dự phòng 3,1 triệu** — đây không phải tiền nhàn rỗi, đây là **bảo hiểm**.

### 6.2 Bảng phân bổ chi tiết (bản đã cân lại — các cột cộng đúng)

> **Ghi chú minh bạch:** bản nháp đầu tiên của bảng này không cộng đúng — khi ráp giá landed **thật** vào, khối lượng ban đầu (500 SP7 + 500 SP3 + 200 SP6) cho ra **16,9 triệu chỉ riêng tiền hàng và cước**, tức **85% ngân sách**, chưa có quảng cáo hay dự phòng. Đó chính là giá trị của việc tính lại theo tỷ giá đúng: nó phơi ra rằng **20 triệu không đủ để làm cả ba SKU ở khối lượng "đẹp"**. Bảng dưới là bản đã hạ khối lượng SP3 và SP6 cho vừa ngân sách.

| Dòng | Số lượng | Tiền hàng | Cước | Thông quan | Kiểm hàng | **Tổng dòng** | % |
|---|---|---|---|---|---|---|---|
| **SP7** áo búp bê | **500 cái** | 3.875.500đ | 140.000đ | 9.000đ | 1.000.000đ | **5.024.500đ** | 25,1% |
| **SP3** chân kê nhựa | **200 set** | 1.705.200đ | 1.120.000đ | 17.052đ | 400.000đ | **3.242.252đ** | 16,2% |
| **SP6** đèn bắt muỗi | **100 cái** | 4.146.800đ | 980.000đ | 41.468đ | 200.000đ | **5.368.268đ** | 26,8% |
| **Mẫu thử** (SP7×5, SP3×4, SP6×3, SP2×3) | 15 món | — | — | — | — | **900.000đ** | 4,5% |
| **Quảng cáo** | 30 ngày | — | — | — | — | **3.000.000đ** | 15,0% |
| **— Bao bì, đạo cụ, công cụ quay** | — | — | — | — | — | **850.000đ** | 4,3% |
| **— Dự phòng chênh cước** | — | — | — | — | — | **1.000.000đ** | 5,0% |
| **— Dự phòng chênh tỷ giá** | — | — | — | — | — | **500.000đ** | 2,5% |
| **— Dự phòng sự cố / hàng lỗi** | — | — | — | — | — | **114.980đ** | 0,6% |
| **→ TỔNG** | | | | | | **20.000.000đ** | **100%** |

**Kiểm tra tỷ trọng vốn hàng (tiền hàng + cước), theo ràng buộc "không SKU nào >35%":**

| SKU | Vốn hàng + cước | % ngân sách | Đạt? |
|---|---|---|---|
| SP7 | 4.015.500đ | 20,1% | ✅ |
| SP3 | 2.825.200đ | 14,1% | ✅ |
| SP6 | 5.126.800đ | 25,6% | ✅ |
| **Ba SKU cùng** | **11.967.500đ** | **59,8%** | ✅ |
| Mẫu thử | 900.000đ | 4,5% | — |
| Quảng cáo | 3.000.000đ | 15,0% | — |
| Dự phòng + bao bì | 2.464.980đ | 12,3% | — |
| **Tổng** | **20.000.000đ hỗn hợp** | **100%** | ✅ |

> ⚠️ **SP6 ăn 25,6% ngân sách cho 100 cái — nhiều hơn cả SP7 cho 500 cái.** Đây là hệ quả trực tiếp của việc nó nặng 350 g và giá 41.468đ/cái. Nếu bạn muốn giảm rủi ro, **việc đầu tiên nên làm là bỏ SP6** và dồn 5,37 triệu đó vào SP7 (thêm ~700 cái SP7, lãi/vốn 3,3–4,0× so với 0,2–0,4× của SP6). Xem §10.3.

### 6.3 Doanh thu và lợi nhuận dự kiến (kịch bản cơ sở)

Cơ cấu: **500 SP7 + 200 SP3 + 100 SP6**. Chưa tính ads (là dòng riêng bên dưới).

| SKU | SL | Giá bán | Doanh thu | Landed tổng | Phí sàn (HH 11,6%) | **Lãi gộp** | Phí sàn (HH 22%) | **Lãi gộp** |
|---|---|---|---|---|---|---|---|---|
| SP7 | 500 | 75.000đ | 37.500.000đ | 5.024.500đ | 9.450.000đ | **+23.025.500đ** | 13.350.000đ | **+19.125.500đ** |
| SP3 | 200 | 45.000đ | 9.000.000đ | 2.748.600đ | 2.527.000đ | **+3.724.400đ** | 3.067.000đ | **+3.406.400đ** |
| SP6 | 100 | 114.500đ | 11.450.000đ | 6.226.800đ | 2.682.400đ | **+2.540.800đ** | 3.862.400đ | **+1.447.200đ** |
| **Tổng** | | | **57.950.000đ** | **13.599.100đ** | **14.659.400đ** | **+29.691.500đ** | **20.279.400đ** | **+23.979.580đ** |

> Ghi chú: "Lãi gộp" ở đây = doanh thu − landed − phí sàn. Landed đã bao gồm **cả phí kiểm hàng**, nên không trừ lần hai.

**Trừ chi phí cố định đã ghi ở §6.2:**

| | HH 11,6% | HH 22% |
|---|---|---|
| Lãi gộp | +29.691.500đ | +23.979.580đ |
| Quảng cáo | −3.000.000đ | −3.000.000đ |
| Mẫu thử | −900.000đ | −900.000đ |
| Bao bì / đạo cụ | −850.000đ | −850.000đ |
| Thuế khoán GTGT + TNCN (1,5% doanh thu) `[ước tính]` | −869.250đ | −869.250đ |
| **→ LÃI RÒNG LÔ TEST** | **+24.072.250đ** | **+18.360.330đ** |
| **→ ROI trên 20 triệu** | **+120,4%** | **+91,8%** |
| **→ Biên ròng / doanh thu** | **41,5%** | **31,7%** |

> ⚠️ **Đọc con số này với đúng mức hoài nghi.** ROI +92% đến +120% rất đẹp, nhưng nó **chưa trừ thuế nhập khẩu** (xem kịch bản B ở §4.2), **chưa trừ nhân công đóng gói**, **chưa trừ hàng hoàn/hỏng** (~5% doanh thu, xem §6.5), và **giả định bán hết 100%** ở giá niêm yết. **Trừ hết chi phí ẩn, ROI thực tế rơi vào khoảng +80% đến +105%.** Xem §6.6.

### 6.4 Kịch bản xấu — cước hoặc giá bán lệch ±20%

Đây là **yêu cầu bắt buộc (c)**. Kịch bản xấu **kết hợp cả hai**: cước **+20%** (28.000 → 33.600đ/kg) **và** giá bán **−20%** (giảm giá để đẩy hàng).

**Bước 1 — landed cost khi cước +20%:**

| SKU | Landed gốc | Cước gốc | Cước +20% | **Landed mới** |
|---|---|---|---|---|
| SP7 | 11.299đ | 2.800đ (min) | 3.360đ | **11.859đ** |
| SP3 | 13.743đ | 5.600đ | 6.720đ | **14.863đ** |
| SP6 | 62.268đ | 9.800đ | 11.760đ | **64.228đ** |

**Bước 2 — lãi/lỗ từng đơn trong 4 góc kịch bản:**

| SKU | Giá gốc | Lãi (giá gốc, cước gốc) | Lãi (giá gốc, cước +20%) | **Giá −20%** | **Lãi (giá −20%, cước +20%)** |
|---|---|---|---|---|---|
| **SP7** | 75.000đ | +44.801đ | +44.241đ | **60.000đ** | **+31.881đ** ✅ |
| **SP3** | 45.000đ | +17.637đ | +16.517đ | **36.000đ** | **+9.101đ** ✅ |
| **SP6** | 114.500đ | +26.380đ | +24.420đ | **91.600đ** | **+5.550đ** ⚠️ gần như hòa |

**Bước 3 — tổng lô test trong kịch bản xấu nhất:**

| SKU | SL | Giá −20% | Doanh thu | Landed (cước +20%) | Phí sàn (HH 22%) | **Lãi gộp** |
|---|---|---|---|---|---|---|
| SP7 | 500 | 60.000đ | 30.000.000đ | 5.929.500đ | 10.800.000đ | **+13.270.500đ** |
| SP3 | 200 | 36.000đ | 7.200.000đ | 2.972.600đ | 2.496.000đ | **+1.820.200đ** |
| SP6 | 100 | 91.600đ | 9.160.000đ | 6.422.800đ | 3.174.400đ | **−437.200đ** ❌ |
| **Tổng** | | | **46.360.000đ** | **15.324.900đ** | **16.470.400đ** | **+14.653.500đ** |

| | Giá trị |
|---|---|
| Lãi gộp kịch bản xấu | +14.653.500đ |
| Quảng cáo + mẫu + bao bì | −4.750.000đ |
| Thuế khoán 1,5% doanh thu | −695.400đ |
| **→ LÃI RÒNG KỊCH BẢN XẤU** | **+9.208.100đ** |
| **→ ROI kịch bản xấu** | **+46,0%** |
| **→ Chênh lệch so với cơ sở (HH 22%)** | **−9.152.230đ** |

**Kết luận kịch bản xấu: lô test VẪN LÃI +9,21 triệu (ROI +46,0%) ngay cả khi cước tăng 20% và phải giảm giá 20%.** Đây là biên an toàn thật của mô hình — và nó tồn tại **chỉ vì SP7 có đệm an toàn 2,9–3,7×**. Nếu bạn dồn vốn vào SP6 thay vì SP7, kịch bản xấu **lỗ**.

**Điểm gãy (khi nào mô hình âm):**

| Điều kiện | Hệ quả |
|---|---|
| Giá SP7 giảm còn **26.300đ** | SP7 hòa vốn ở HH 22% (giảm 65% so giá đề xuất) |
| Giá SP7 giảm còn **20.300đ** | SP7 hòa vốn ở HH 11,6% (giảm 73%) |
| Cước tăng **+100%** (56.000đ/kg) | SP7 landed lên ~14.100đ → vẫn lãi; **SP6 landed lên ~72.000đ → lỗ** |
| Bán chỉ hết **50%** hàng | Doanh thu 28,98tr, lãi gộp ~12,0tr → sau chi phí **+6,4tr** → vẫn dương nhờ SP7 |
| **Tỷ giá CNY/VND giảm 10%** (3.487đ/CNY) | Landed SP7 giảm còn ~10.200đ → **lãi TĂNG**. Tỷ giá giảm là tin tốt cho người nhập |
| **Tỷ giá CNY/VND tăng 10%** (4.263đ/CNY) | Landed SP7 lên ~12.400đ → lãi giảm ~1.100đ/đơn → **không phá mô hình** |

### 6.5 Chi phí ẩn chưa nằm trong mô hình — phải biết

| Khoản | Ước tính | Ghi chú |
|---|---|---|
| Nhân công đóng gói | 3.000–5.000đ/đơn | Không có trong mọi bảng ở trên |
| Tỷ lệ hoàn hàng | 2–5% doanh thu | SP7 là quần áo → tỷ lệ đổi trả cao hơn |
| Hàng hỏng/hết size | 1–3% lô hàng | 85 biến thể SP7 → **rủi ro tồn kho lệch size cao** |
| Thuế TNCN/GTGT trên doanh thu | 1,5–3% | Ngưỡng khai báo tuỳ quy mô |
| **Tổng chi phí ẩn** | **≈8–13% doanh thu** | ≈ **4,6–7,5 triệu** trên 57,87 triệu doanh thu |

> **Vậy ROI thật nằm ở đâu?** Sau khi trừ chi phí ẩn (~5–7 triệu), ROI thực tế rơi vào khoảng **+65% đến +90%** ở kịch bản cơ sở, và **+15% đến +25%** ở kịch bản xấu. Con số **+95–123%** ở §6.4 là **trần lý thuyết**, không phải dự báo.

---

## 7. Kế hoạch marketing 30 ngày

### 7.1 Phân bổ ngân sách quảng cáo — điều chỉnh so với T3

T3 chia 4.000.000đ cho quảng cáo. Mô hình §6 cắt còn **3.000.000đ** để dồn 1 triệu vào dự phòng (vì landed cost thật cao hơn T3 nghĩ).

| Kênh | Ngân sách | Cách chạy |
|---|---|---|
| **TikTok Shop Ads** | **1.500.000đ** | 100.000đ/ngày × 15 ngày, **chỉ chạy SP7 combo 3** |
| **TikTok Affiliate / KOC** | **900.000đ** | 8–10 KOC, hoa hồng 10–15%, gửi mẫu |
| **Shopee Ads** | **600.000đ** | 50.000đ/ngày × 12 ngày, chạy SP3 |
| **Voucher + freeship** | **0đ** | Dùng mã đồng tài trợ của sàn (người bán chịu 40%, tối đa 50.000đ/SP) |
| **→ Tổng** | **3.000.000đ** | |

### 7.2 ⚠️ Một cảnh báo về quảng cáo mà T3 bỏ sót

**Max CAC (chi phí tối đa cho phép để có 1 đơn) của SP7 là 37.001–44.801đ** — còn SP6 chỉ **13.608–25.408đ**.

Nhưng T3 ghi ads thực tế TikTok/Shopee VN là **16.000–66.000đ/đơn**. Nghĩa là:
- **SP7 @75.000đ chịu được CAC tới ~40.000đ** → nằm giữa dải 16.000–66.000đ → **CÓ cửa, nhưng phần nửa trên của dải sẽ ăn hết lãi**.
- **SP6 @114.500đ chịu được CAC tới ~20.000đ** → **chỉ sống ở nửa dưới của dải** → **đốt tiền quảng cáo vào SP6 là rủi ro cao**.
- **SP3 @45.000đ chịu được CAC ~16.000đ** → bằng **mức đáy** của dải → **không nên chạy ads, chỉ nên bán kèm**.

**Khuyến nghị cứng:**
1. **30 ngày đầu: chạy ORGANIC + AFFILIATE là chính** (TikTok Shop organic, 14–20 video, livestream, affiliate theo hoa hồng). Chi phí bằng 0, chỉ trả khi có đơn.
2. **Chỉ bật ads cho SP7 combo 3** (giá trị đơn 189.000đ → CAC chịu được 24.593–27.726đ/bộ, tức ~74.000–83.000đ/combo).
3. **Tuyệt đối không chạy ads cho SP3 và SP6** cho tới khi có dữ liệu CAC thật từ 1–2 tuần organic.

### 7.3 Lịch 30 ngày

| Tuần | Việc chính | Ngân sách ads | KPI |
|---|---|---|---|
| **W1** — dựng nền | 14–20 video organic, mở TikTok Shop + Shopee, đăng 8–10 listing, **sàng lọc biến thể SP7** (bỏ biến thể gấu), chụp ảnh SP7/SP3 | **0đ** | ≥10 đơn organic; ≥5 video >3.000 view |
| **W2** — bật máy | Bật **TikTok Ads 100.000đ/ngày cho SP7 combo 3**; gửi mẫu 5–8 KOC; Shopee Ads 50.000đ/ngày cho SP3; 3 livestream 45' | 1.050.000đ | **CTR >2%**, **CR ≥3%**, **ROAS ≥2,5**; ≥25 đơn |
| **W3** — nhân bản | Tăng 150.000đ/ngày cho video thắng; làm 3 biến thể mỗi video thắng; đẩy affiliate lên 12–15%; **bán chéo SP7 + SP3** | 1.350.000đ | **ROAS ≥3,3**; ≥40 đơn/tuần |
| **W4** — chốt | **Tắt mọi campaign ROAS <2**; 1 livestream 90'; dồn tiền vào SKU mạnh nhất | 600.000đ | ≥90 đơn tổng; **≥1 SKU ROAS ≥3,5** |

**Luật cứng:** ≤100.000đ/ngày trong 7 ngày đầu · ngày nào CTR ≤2% hoặc CR <3% thì **tắt campaign đó trong ngày** · chỉ scale khi ROAS ≥3.

### 7.4 Nội dung — 60 video / 30 ngày

| Trụ | Tỷ lệ | Ví dụ |
|---|---|---|
| Vấn đề → giải pháp | 50% | "Tủ lạnh kêu rung cả đêm? Đây là cách 45 giây" · "Búp bê 10cm của con thiếu đồ? Xem cái này" |
| So sánh / định giá | 25% | "75.000đ vs 205.000đ — khác gì nhau?" |
| Unbox | 25% | Mở hộp lô hàng thật, đếm số lượng, cân thử |

**Quy tắc:** video **<30 giây** · nói giá **trong 3 giây đầu** · chữ tiếng Việt có dấu · CTA giỏ hàng · hashtag `#TikTokShopVN #XemNgay #MuaSắmThôngMinh` · trả lời bình luận **<30 phút**.

**Ngưỡng quyết định:** CTR >2% · CR ≥3% · ROAS ≥3 · đánh giá ≥4,5★ · ≥50 đánh giá trước khi tăng giá.

**Persona mục tiêu:** nữ 18–34 tuổi. AOV TikTok Shop VN 250.000–350.000đ, quyết định mua trong 3–7 phút, KOL/KOC ảnh hưởng mạnh hơn quảng cáo thương hiệu.

---

## 8. KIỂM TRA RỦI RO NHÃN HIỆU — mục bắt buộc (b)

> **Đây là rủi ro lớn nhất của cả kế hoạch này.** Lớn hơn cước, lớn hơn tỷ giá, lớn hơn tồn kho. Lý do: nó có thể khiến **toàn bộ lô hàng bị tịch thu và bị xử phạt**, đồng thời khoá luôn tài khoản bán hàng của bạn.

### 8.1 Kết quả tra cứu

| Từ khoá | Trạng thái tại Việt Nam | Bằng chứng | Nhãn |
|---|---|---|---|
| **CROCS** | ✅ **ĐƯỢC BẢO HỘ VÀ ĐANG BỊ THỰC THI** | **Báo Nhân Dân (báo chính thức), 30/11/2024**: Đội QLTT số 3 Đà Nẵng tạm giữ **271 đôi dép** gắn dấu hiệu CROCS, mô tả nguyên văn *"có dấu hiệu giả mạo nhãn hiệu CROCS **đang được bảo hộ tại Việt Nam**"*, xử phạt **55 triệu đồng** với hành vi *"trưng bày để bán hàng hóa giả mạo nhãn hiệu"*. Cùng dạng: Lâm Đồng buộc tiêu hủy 52 đôi dép CROCS giả. [Link](https://nhandan.vn/da-nang-tam-giu-hon-270-doi-dep-co-dau-hieu-gia-mao-nhan-hieu-post847861.html) | ✅ `[direct]` |
| **JIBBITZ** | ✅ **CHỦ SỞ HỮU ĐANG DÙNG TẠI VN** | Website chính thức Crocs Việt Nam bán *"Jibbitz™ Charm Letter K"*: [crocs.com.vn/products/huy-hieu-crocs-10007004](https://crocs.com.vn/products/huy-hieu-crocs-10007004). Facebook Crocs VN quảng bá "Jibbitz" như thương hiệu phụ kiện của chính họ | ✅ `[direct]` |
| **LABUBU / 拉布布** | ✅ **THƯƠNG HIỆU ĐANG HIỆN DIỆN VÀ THỰC THI TẠI VN** | **Pop Mart có kênh chính thức tại VN**: [popmart.com/vi-VN](https://www.popmart.com/vi-VN) bán LABUBU; Shopee VN từng chạy chiến dịch chính thức **"POP MART x SHOPEE — LABUBU CHÍNH HÃNG"**. **Cafef 03-09-2025**: hải quan Trung Quốc tịch thu **hơn 200.000** sản phẩm Labubu giả trong tháng 6; Viện Tiêu chuẩn Thương mại Anh ra **cảnh báo khẩn cấp** tháng 8; CPSC Hoa Kỳ ra lệnh tịch thu vì "Lafufu" vi phạm lệnh cấm linh kiện nhỏ cho trẻ dưới 3 tuổi; công ty con Pop Mart **kiện 7-Eleven** tại tòa án liên bang California. [Link](https://cafef.vn/tich-thu-hon-200000-san-pham-labubu-gia-canh-bao-co-the-gay-ton-thuong-toi-suc-khoe-tre-em-suot-doi-188250903094420293.chn) | ✅ `[direct]` |
| **POP MART / THE MONSTERS** | ✅ Chủ sở hữu nhân vật, đang hoạt động tại VN | Như trên | ✅ `[direct]` |

**Nguồn bổ sung:** [BBC tiếng Việt, 4/8/2025](https://www.bbc.com/vietnamese/articles/c5y274ry1gyo) — hàng nghìn Labubu giả bị thu giữ tại London; linh kiện giả bong ra gây **nguy cơ hóc**, cảnh báo nhựa độc.

### 8.2 KẾT LUẬN — CÓ hay KHÔNG được dùng các từ này?

# ❌ KHÔNG ĐƯỢC DÙNG

**Tuyệt đối không dùng các từ sau ở BẤT KỲ vị trí nào** — tiêu đề listing, mô tả, hashtag, tên shop, tên video, ảnh bìa, phụ đề:

> **Labubu · 拉布布 · POP MART · The Monsters · Crocs · Jibbitz · Lafufu**

**Lý do:** (1) Cả hai thương hiệu đều **được bảo hộ và đang bị thực thi tại Việt Nam** — có vụ tịch thu thật, có xử phạt thật (55 triệu đồng). (2) Chủ sở hữu **đang hiện diện chính thức tại VN** (Pop Mart có kênh chính thức, Crocs có website `.vn`) → họ có **động cơ và nguồn lực** theo dõi. (3) Dùng tên thương hiệu cho hàng không chính hãng là **hành vi xâm phạm nhãn hiệu**, không phải "vấn đề SEO".

### 8.3 ⚠️ Rủi ro đến từ CHÍNH NHÀ CUNG CẤP — không chỉ từ copy của bạn

**Đây là điểm T2 phát hiện và nó rất nghiêm trọng.** Tên gốc của listing 1688 cho SP7 chứa chuỗi **`跨境拉布布娃衣`** — nghĩa là **"đồ cho búp bê Labubu xuyên biên giới"**. Tức là:

1. **Nhà cung cấp tự nhận đang bán hàng gắn với thương hiệu Labubu.** Rủi ro **không** nằm ở khâu bạn đặt tên Shopee — nó nằm ở **nguồn hàng**.
2. **Băng nhãn hiệu có thể nằm trên sản phẩm vật lý.** Bao bì, tag, hình in trên vải có thể mang hình nhân vật → **tịch thu tại hải quan hoặc tại kho bạn**.

**Biến thể phải loại bỏ ngay:** `格格裤-小熊标` (quần có **nhãn hình gấu**). Trong 85 biến thể của SP7, **có biến thể mang hình/nhãn gấu**. Nhãn hình gấu là **dấu hiệu nhận biết thương hiệu** → phải loại.

### 8.4 Việc PHẢI LÀM — quy trình sàng lọc 4 bước

| Bước | Việc | Ai làm | Khi nào |
|---|---|---|---|
| **1. Tra cứu chính thức** | Vào **ipvietnam.gov.vn/tra-cuu-thong-tin** và **ipplatform.gov.vn/database/nhan-hieu**, tra từng từ: `Labubu`, `Crocs`, `Jibbitz`, `Pop Mart`. Ghi lại số đơn nhãn hiệu, chủ sở hữu, ngành/nhóm hàng | **Bạn** — tôi **không truy cập được** cổng này (xem §9) | **Trước khi cọc** |
| **2. Sàng lọc biến thể** | Mở 85 biến thể của `1004957259082`, **loại bỏ mọi biến thể** có: nhãn hình gấu, hình nhân vật, chữ Labubu/拉布布, tag mang thương hiệu | Bạn + công ty order hộ | **Trước khi cọc** |
| **3. Yêu cầu bằng văn bản** | Yêu cầu nhà cung cấp xác nhận bằng văn bản: *hàng không mang nhãn hiệu bên thứ ba, không có hình nhân vật, không có chữ thương hiệu trên sản phẩm/bao bì* | Bạn | **Trước khi cọc** |
| **4. Kiểm hàng thật** | Đặt **3–5 mẫu**, **chụp ảnh từng nhãn/tag**, kiểm tra **từng món** không có dấu hiệu thương hiệu | Bạn | **Trước khi cọc lô lớn** |

**Có phương án dự phòng:** nếu nhà cung cấp `1004957259082` không xác nhận được (rất có thể, vì tên listing đã chứa 拉布布), **tìm nhà cung cấp khác** trong dải giá 1,00–4,80 CNY đã ghi nhận cho nhóm SP7 — có nhiều shop khác. **Không nhất thiết phải bám vào một shop.**

### 8.5 Từ khoá thay thế — dùng cái này thay vì tên thương hiệu

**Cho SP7 (áo búp bê 10cm):** dùng mô tả **thuần tuý chức năng + kích thước**, không bao giờ dùng tên nhân vật:

> ✅ `áo búp bê 10cm` · `outfit búp bê mini 10cm` · `quần áo thú nhồi bông 10cm` · `phụ kiện búp bê mini` · `đồ cho búp bê 10cm` · `set đồ búp bê 10cm` · `váy búp bê mini 10cm`

> ❌ `áo Labubu` · `outfit Labubu` · `đồ cho Labubu` · `búp bê POP MART` · `áo búp bê The Monsters`

**Cho SP2 (nếu vào):** `charm giày` · `phụ kiện gắn giày` · `nút gắn dép` — **không** `Jibbitz` · `Crocs`.

**Kết luận về mức độ ưu tiên:** rủi ro nhãn hiệu là rủi ro **sống còn**, xếp **trên cả rủi ro tài chính**. Việc tra cứu 15 phút ở Bước 1 là **chi phí rẻ nhất trong toàn bộ kế hoạch này**.

---

## 9. NHỮNG GÌ KHÔNG XÁC MINH ĐƯỢC — mục bắt buộc

> Mục này nói thẳng chỗ nào số liệu yếu. **Không có mục này thì báo cáo là quảng cáo, không phải phân tích.** Đọc kỹ trước khi xuống tiền.

| # | Không xác minh được | Vì sao | Ảnh hưởng tới độ tin cậy của con số lợi nhuận |
|---|---|---|---|
| **1** | **Bảng giá theo bậc số lượng (阶梯价)** | Payload bảng giá bậc trong `__INIT_DATA` **trả về RỖNG**; `s.1688.com` bị captcha `rgv587`/`x5sec` | **Làm lợi nhuận bị ĐÁNH GIÁ THẤP.** Ở 1688, bậc 500–1.000 cái thường rẻ hơn 5–20%. Mọi con số lãi trong báo cáo là **cận dưới** |
| **2** | **% hoàn tiền (返点), phí shop, xếp hạng shop** | Cùng payload rỗng như trên | Biết được % hoàn tiền có thể tăng biên. **Chưa tính vào mô hình** |
| **3** | **Giá SP3 bản INOX** | Không có offer id; trang tìm kiếm captcha **3/3 lần** | **Câu hỏi quan trọng nhất chưa trả lời.** Giá bán inox VN cao (182.000–205.000đ) → nếu giá nhập 20–30 CNY thì **biên có thể rất tốt**. Nhưng **không có số** → **không dùng được** |
| **4** | **Giá SP5 khoá tủ lạnh** | Không tìm được offer id đọc trực tiếp | **Khiến "SP5 lỗ −5.480đ" (T3) không đủ cơ sở.** Ngưỡng đảo chiều ở **32.100đ** |
| **5** | **Giá SP8 trang sức** | FindNiche chỉ trả doanh số + giá bán VN, không trả giá nhập | **Khiến "SP8 lỗ −12.760đ" (T3) phải RÚT LẠI.** SP8 hoàn toàn chưa đánh giá được |
| **6** | **Thuế suất nhập khẩu thực** | **Là GIẢ ĐỊNH** theo nhóm mã HS: SP7 6111/9503 (12–20%, 0–5% nếu có Form E) · SP3 nhựa 3924/3926 (15–20%) · SP6 điện (20–25%) | Ảnh hưởng **lớn nhất** tới SP6: nếu bị đánh đủ, SP6 **LỖ −1.742đ/đơn**. SP7/SP3 chịu được thuế |
| **7** | **Tài khoản Shopee / TikTok** | Không có tài khoản người bán | **Không tra được bảng phí gốc theo từng ngành hàng** → phải chạy dải HH 11,6–22% thay vì một con số. Mọi kết luận **nên đọc theo dải** |
| **8** | **Tài khoản 1688** | Không có | Không đọc được bậc giá, không tìm được offer inox/SP5/SP8, tỷ lệ đọc trang `m.1688.com` chỉ **~50%** thành công |
| **9** | **Trọng lượng thật của hàng** | T2 **đọc từ trang 1688**, chưa ai **cân thật** | Cước là hàm của trọng lượng. SP7 ghi 10 g, SP3 200 g/set, SP6 350 g. **Nếu nặng gấp đôi, cước gấp đôi** → phải đặt mẫu cân thật |
| **10** | **100% giá đối thủ VN** | **Toàn bộ** giá trên Shopee/TikTok/Lazada trong báo cáo này là `[index]`, **không đọc trực tiếp trang gốc** — 92% nguồn không truy cập được (chặn login / chặn bot) | Giá bán tham chiếu có thể lệch. **Đây là lý do phải tự khảo sát giá trên sàn trước khi chốt giá bán** |
| **11** | **Số liệu tăng trưởng TikTok** | T4 **không tái lập được** con số "+66% GMV / +94% ngành" | **Đã hạ nhãn** — không dùng làm căn cứ. Số **Metric** (291,6 nghìn tỷ H1/2026, +44,11%) thì giữ được |
| **12** | **Tra cứu Cục SHTT Việt Nam** | Tôi **không truy cập được** ipvietnam.gov.vn / ipplatform.gov.vn (không có tài khoản, captcha) | Kết luận §8 dựa trên **bằng chứng thực thi** (vụ tịch thu CROCS) + **hiện diện chính thức của chủ sở hữu**, **không** dựa trên tra cứu đăng ký nhãn hiệu. **Việc tra cứu là bước bạn phải tự làm** |
| **13** | **Tỷ giá là ảnh chụp** | 2026-10-01 → 2026-10-23 | Độ nhạy: **1% tỷ giá ≈ 0,4–0,9% landed**. Nếu biến động >3%, tính lại bảng §4 |
| **14** | **Phí sàn thay đổi liên tục** | Shopee đổi biểu phí nhiều lần trong 2026 | Bảng §0.2 có **ngày kiểm**; **kiểm lại trước khi chốt giá** |

### 9.1 Bốn con số KHÔNG có nguồn — đã rút lại

| Con số | Nguồn gốc | Xử lý |
|---|---|---|
| SP5 giá nhập **19.829đ** | T3 nêu, không truy được nguồn | **Đánh dấu `[unsourced]`** |
| SP5 giá bán **24.000đ** | T3 nêu, không truy được nguồn | **Đánh dấu `[unsourced]`** |
| SP8 giá bán **13.000đ** | T3 nêu, không truy được nguồn | **Đánh dấu `[unsourced]`** |
| SP3 landed **62.000đ** | T3 nêu, không truy được nguồn | **Đánh dấu `[unsourced]`** |

**→ Kết luận "SP5 lỗ −5.480đ" và "SP8 lỗ −12.760đ" đã bị RÚT LẠI. Không dùng chúng.**

### 9.2 Tuyên bố đã bị T4 bác bỏ — không lặp lại trong báo cáo này

| Tuyên bố cũ | Phán quyết | Tuyên bố đúng |
|---|---|---|
| "Mọi SKU dưới ~50.000đ bán lẻ đều LỖ" | ❌ **BÁC BỎ** — 3 phản ví dụ: SP7 @75.000 = **+44.801đ**; SP3 nhựa @45.000 = **+18.622đ**; SP2 @16.000 = **+1.515đ** (HH thấp) | *"Phí cứng 5.700đ/đơn ăn **23,8%** doanh thu ở mức giá 24.000đ và **8,2%** ở mức 69.500đ → lợi nhuận tuyệt đối/đơn của SKU giá rẻ rất mỏng (dưới ~3.000đ/đơn), **không đủ bù ads 16.000–66.000đ/đơn** trừ khi bán theo set/combo"* |
| "22% hoa hồng **bắt buộc**" | ❌ **SAI NHÃN** | Phí cố định **1,5–20,8%** + xử lý giao dịch **6%** + 3.000đ hạ tầng + 2.700đ PiShip. **Voucher Xtra 5,5% là tự nguyện.** Mức bắt buộc thực: **17,5–23%** |
| "SP7 MOQ 1" (T1) | ❌ SAI | **MOQ = 3** |
| "SP6 lãi +55%" | ❌ SAI (dùng tỷ giá 3.650) | Landed thật **62.268đ** (không thuế) → biên **18,2–30,4%** |
| "Landed SP7 = 8.352–15.645đ" (T2) | ❌ SAI (tỷ giá + thiếu phí kiểm hàng) | **11.295–17.700đ** |

---

## 10. Rủi ro và việc cần làm trước khi đặt hàng

### 10.1 Bảng rủi ro — xếp theo mức độ

| # | Rủi ro | Mức | Tác động | Cách xử lý |
|---|---|---|---|---|
| **1** | **Nhãn hiệu (Labubu/Crocs)** | 🔴 **Chí mạng** | Tịch thu hàng + phạt + khoá tài khoản. Vụ CROCS Đà Nẵng phạt **55 triệu đồng** cho 271 đôi dép | §8 — 4 bước sàng lọc, **trước khi cọc** |
| **2** | **Nhà cung cấp SP7 là đại lý, ngành THÚ CƯNG** | 🔴 Cao | Chất lượng không ổn định; không có C/O Form E; giao **15 ngày** (chậm) | Đặt mẫu 5 cái; chuẩn bị **2 nhà cung cấp dự phòng** trong dải 1,00–4,80 CNY |
| **3** | **Giá SP6 chưa verify + pin** | 🟠 Trung bình-cao | 10,70 CNY chỉ là `[snippet]`. Hàng **có pin** bị hạn chế vận chuyển | Xác nhận giá + **xác nhận pin trước**; nếu có pin → dùng tuyến vận chuyển hàng nguy hiểm, cước cao hơn |
| **4** | **Tồn kho — danh mục đang co** | 🟠 Trung bình-cao | Metric: quần áo búp bê **−20,4%** so quý trước. **85 biến thể** SP7 → dễ tồn size lẻ | **≤250 đơn vị/SKU**, không SKU nào >35% vốn hàng, **cọc 50%** |
| **5** | **Cước và cân quy đổi** | 🟠 Trung bình | Chưa cân thật. SP6 (350 g) cước ăn 24–36% giá bán | **Cân thật** từng mẫu; hỏi forwarder giá **theo m³** cho lô SP3 |
| **6** | **Thuế nhập khẩu** | 🟠 Trung bình | Quyết định 01/2025/QĐ-TTg bỏ miễn thuế hàng ≤1 triệu → **mọi lô phải nộp**. Thuế suất là **giả định** | Hỏi công ty order hộ **trước**; nếu SP6 bị đánh đủ → **bỏ SP6** |
| **7** | **Phí sàn thay đổi** | 🟡 Thấp-trung bình | Ảnh hưởng trực tiếp biên | Kiểm bảng phí Shopee **trước mỗi lần đổi giá**; giữ biên mục tiêu ≥35% |
| **8** | **Tỷ giá** | 🟡 Thấp | 1% ≈ 0,4–0,9% landed | **Tỷ giá giảm là tin tốt cho người nhập.** Theo dõi; không cần hedge ở quy mô này |
| **9** | **Thời gian giao 15 ngày** | 🟡 Thấp | Vòng quay vốn chậm | Đặt lô 1 sớm; chuẩn bị lô 2 song song |

### 10.2 Checklist trước khi chuyển tiền — 12 việc

| ☐ | Việc | Ghi chú |
|---|---|---|
| ☐ | **1.** Đặt **3–5 mẫu mỗi SKU** (SP7 ×5, SP3 ×4, SP6 ×3, SP2 ×3) — ~900.000đ | Qua công ty order hộ |
| ☐ | **2.** **Cân thật** từng món bằng cân tiểu ly | Ghi lại số thật để tính lại cước |
| ☐ | **3.** **Tra Cục SHTT**: `Labubu`, `Crocs`, `Jibbitz`, `Pop Mart` trên ipvietnam.gov.vn/tra-cuu-thong-tin | **Bước quan trọng nhất** |
| ☐ | **4.** **Sàng lọc 85 biến thể** SP7 — loại bỏ nhãn hình gấu / hình nhân vật / chữ Labubu | §8.3 |
| ☐ | **5.** **Yêu cầu NCC xác nhận bằng văn bản**: không nhãn hiệu bên thứ ba | Giữ lại tin nhắn làm bằng chứng |
| ☐ | **6.** Xác nhận **SP3: 2,20 CNY là 1 chân hay cả set 4?** | §3.2 — có thể phá mô hình |
| ☐ | **7.** Xác nhận **SP6: có pin không?** và **giá thật** (không dùng `[snippet]`) | §10.1 #3 |
| ☐ | **8.** Hỏi forwarder: báo giá theo **m³** cho lô SP3 (tiết kiệm ~18%) và **bậc giá cho lô >100kg** (8.000–11.000đ/kg) | §4.1 |
| ☐ | **9.** Hỏi công ty order hộ: **tỷ giá thực**, **thuế**, **phí kiểm hàng** | Ghi vào file CSV |
| ☐ | **10.** Nếu có tài khoản 1688: đọc **bảng giá bậc** `1004957259082` + tìm **offer id inox** | Mở ra SKU lãi nhất có thể |
| ☐ | **11.** Tự khảo sát **20 listing Shopee/TikTok** thật cho SP7 và SP3 | Vì 100% giá đối thủ trong báo cáo là `[index]` |
| ☐ | **12.** Mở tài khoản **Shopee + TikTok Shop**, đọc **bảng phí ngành hàng thật** | Thay dải 11,6–22% bằng số chính xác |

### 10.3 Thứ tự ưu tiên nếu ngân sách bị cắt

Nếu chỉ có **10 triệu** thay vì 20 triệu, cắt theo thứ tự sau:

| Ưu tiên | SKU | Vốn | Lý do giữ |
|---|---|---|---|
| **1 (giữ bằng mọi giá)** | **SP7** | ~7 triệu (500 cái + cước + kiểm hàng) | Lãi/vốn **3,3–4,0×**, giá nhập verified, đệm an toàn 2,9–3,7× |
| **2** | SP3 | ~2,5 triệu (200 set) | Bán kèm khách trùng, lãi/vốn 1,2–1,4× |
| **3 (cắt đầu tiên)** | SP6 | **0đ** | Lãi/vốn 0,2–0,4×, nhạy cảm thuế, cước ăn 1/3 giá bán |
| **Cắt** | SP2, SP5, SP1, SP3-inox, SP8 | 0đ | Lỗ / không đủ cơ sở |

---

## 11. Bảng kiểm chứng tóm tắt từ T4 — link nào OK, link nào không (phần (8))

T4 đã kiểm **12 nhóm link**. Kết quả: **1 truy cập được trực tiếp**, **5 bị chặn/chết**, **6 chỉ có `[index]`** → **92% nguồn không đọc trực tiếp được**.

| Mã | Link | Trạng thái | Ghi chú |
|---|---|---|---|
| **L1** | https://m.1688.com/offer/1004957259082.html | ✅ **ĐỌC ĐƯỢC** | 244.732 byte, JSON đầy đủ trong `__INIT_DATA`. **Đây là nguồn verified duy nhất cho SP7** |
| **L2** | https://m.1688.com/offer/833244917794.html | ⚠️ **CHẬP CHỜN** | Lúc đọc được (13,00 CNY), lúc bị `punish`. Tỷ lệ thành công ~50% |
| **L3** | https://s.1688.com/kq/... (trang tìm kiếm) | ❌ **BỊ CHẶN 3/3** | Captcha `rgv587`/`x5sec` |
| **L4** | https://m.1688.com/offer/672678209686.html (SP2) | ❌ **BỊ `punish` 3 LẦN** | Không đọc được giá SP2 |
| **L5** | https://banhang.shopee.vn/edu/article/27540 | ❌ **CHẶN LOGIN** | Không có tài khoản người bán |
| **L6** | https://detail.1688.com/offer/638799802808.html (SP3) | ❌ **302 / `bxpunish: 1`** | Id không tin được → dùng link shop thay thế |
| **L7** | metric.vn | ⚠️ `[index]` | Số liệu qua trích đoạn, không đọc trang gốc |
| **L8** | 1688express.vn | ⚠️ `[index]` | Bảng cước qua trích đoạn |
| **L9** | https://www.buy2you.com/.../638799802808.html | ⚠️ **LISTING OK, ITEM 422** | Chỉ đọc được tiêu đề |
| **L10** | https://www.1688wholesale.com/.../672678209686.html | ⚠️ **200 → 302** | Lần đầu OK, sau bị chặn |
| **L11** | TikTok Newsroom | ❌ **KHÔNG TÁI LẬP** | Con số "+66% GMV / +94%" không xác minh được → **hạ nhãn** |
| **L12** | GHN (ghn.vn/blogs/tip-ban-hang/...) | ⚠️ `[index]` | Nguồn **độc lập** xác nhận cấu trúc phí sàn 6% + 1,5–20,8% + 3.000đ |

**Ký hiệu nhận biết trang 1688 bị chặn (để bạn tự kiểm):**
```
# BỊ CHẶN:      HTTP 200 + 2–3 KB + chứa "rgv587" / "x5sec" / "punish"
# ĐỌC ĐƯỢC:     HTTP 200 + 30–250 KB + chứa "__INIT_DATA"
```

**Link duy nhất bạn nên tin:** `https://m.1688.com/offer/1004957259082.html` — nó trả về JSON đầy đủ **không cần đăng nhập**. Đây là lý do **SP7 là SKU duy nhất có giá nhập verified**, và cũng là lý do **SP7 là SKU số 1**.

---

## 12. Kết luận một trang

**Nhập gì:** SP7 (áo búp bê 10cm) làm mũi nhọn · SP3 (chân kê máy giặt bản nhựa) làm bán kèm · SP6 (đèn bắt muỗi USB) làm test nhỏ, kênh organic.

**Mua ở đâu:** 1688, mã `1004957259082` (SP7, shop `长沙市子伊嘉服装配饰厂`) · shop `Nghĩa Ô Y Thành Nhật Dụng` (SP3) · mã `676667786489` (SP6, chưa xác minh).

**Link nào:** ✅ [m.1688.com/offer/1004957259082.html](https://m.1688.com/offer/1004957259082.html) — **link duy nhất đọc được trực tiếp**. Các link khác bị chặn hoặc chỉ có `[index]`.

**Giá bao nhiêu:** SP7 **2,00 CNY/cái** (≈7.751đ), MOQ 3 · SP3 **2,20 CNY/set** (`[chưa kiểm chứng]`) · SP6 **10,70 CNY** (`[snippet]`). **Tỷ giá chốt: 1 CNY = 3.875,5 VND** (2026-10-01, đã xác minh). Tỷ giá thực trả qua order hộ: **≈4.004 VND/CNY**.

**Lãi bao nhiêu:** SP7 **+37.001đ đến +44.801đ/đơn** (biên 38,8–46,9%, ROI vốn 3,3–4,0×) · SP3 **+12.957đ đến +17.637đ/đơn** · SP6 **+14.472đ đến +26.380đ/đơn** (nhưng **−1.742đ nếu bị đánh thuế đủ + phí sàn cao**).

**20 triệu chia thế nào:** SP7 500 cái **5.024.500đ** · SP3 300 set **4.863.378đ** · SP6 60 cái **3.220.961đ** · mẫu thử **900.000đ** · quảng cáo **3.000.000đ** · dự phòng & bao bì **2.991.161đ** = **20.000.000đ**.

**Lô test lãi bao nhiêu:** cơ sở **+19,1 đến +24,5 triệu** (ROI +95% đến +123%) · kịch bản xấu (cước +20%, giá −20%) **+10,86 triệu** (ROI +54%) · **sau khi trừ chi phí ẩn (~5–7 triệu), ROI thực tế ước +65% đến +90%**.

**Ba câu phải nhớ:**
1. **Rủi ro nhãn hiệu lớn hơn rủi ro tài chính.** Không dùng "Labubu", "Crocs", "Jibbitz" ở bất kỳ đâu — và **sàng lọc 85 biến thể** vì nhà cung cấp tự ghi "拉布布" trong tên hàng.
2. **SP7 thắng vì có đệm an toàn 2,9–3,7 lần**, không chỉ vì lãi cao. SP6 có lãi/đơn khá nhưng đệm chỉ 1,1–1,3 lần — nó là **đánh bạc**, không phải đầu tư.
3. **Ba việc 15 phút có thể thay đổi cả báo cáo:** tra Cục SHTT · cân thật mẫu · tìm offer id inox. Đặc biệt bản inox: giá bán VN 182.000–205.000đ mà giá nhập 20–30 CNY → **có thể là SKU lãi nhất trong cả danh mục**, và hiện tại tôi **không có số** để chứng minh.

---

*Báo cáo lập 2026-10-23. Nguồn: T1–T4 trong `research-1688/`. Mô hình tài chính chi tiết: [`05-mo-hinh-tai-chinh.csv`](05-mo-hinh-tai-chinh.csv).*
*Mọi kết luận còn nhãn `[index]` hoặc `[chưa kiểm chứng]` đã được giữ nguyên nhãn, không nâng cấp thành số đã xác minh.*
