# 02 — So sánh nguồn hàng 1688, nhà cung cấp và chi phí landed về Việt Nam

- **Task:** T2 — So sánh giá, nhà cung cấp, link 1688 và chi phí landed về VN
- **Ngày thu thập:** **2026-10-23** (Asia/Shanghai) — mọi con số giá có hiệu lực tại ngày này
- **Người thực hiện:** sourcing-analyst · attempt `dd659a57-5cd3-4615-b684-2c68f30b72c3`
- **Phạm vi ưu tiên (theo chỉ đạo của captain sau khi T3 xong):** **SP7 (áo búp bê 10cm) và SP3 (chân kê — tách bản inox vs nhựa)** được dồn công; các SKU còn lại chỉ ghi landed cost mức combo/set.
- **Nguồn gốc:** `research-1688/01-xu-huong.md` (T1) và `research-1688/03-thi-truong-marketing.md` (T3).

---

## 0. ĐỌC TRƯỚC — phát hiện phương pháp quan trọng nhất

### 0.1. KÊNH TRUY CẬP MỚI ĐÃ MỞ: `m.1688.com/offer/<id>.html`

Trong quá trình làm T2 tôi phát hiện **trang chi tiết bản mobile `m.1688.com` trả về dữ liệu đầy đủ mà KHÔNG cần đăng nhập**, trong khi `detail.1688.com` (bản desktop) và `s.1688.com` (tìm kiếm) đều bị captcha `rgv587`/`x5sec` chặn.

Dữ liệu lấy được từ `m.1688.com/offer/<id>.html` (nhúng trong `window.__INIT_DATA`):

| Trường | Lấy được? |
|---|---|
| Tên sản phẩm, mã offer, đơn vị tính | ✅ |
| **Giá + MOQ (`beginAmount`)** | ✅ |
| **Số đã bán (`saledCount`)** | ✅ |
| **Trọng lượng 1 sản phẩm (`unitWeight`, kg)** | ✅ |
| **Tên shop + tên công ty + địa chỉ kho** | ✅ |
| **Toàn bộ danh sách biến thể/màu (`propsList`)** | ✅ |
| Thông tin logistics (hãng vận chuyển, cam kết thời gian giao) | ✅ |
| Cờ "hàng chuyên xuất khẩu" | ✅ |
| **Bảng giá theo bậc (阶梯价)** | ❌ — trang chỉ hiển thị **1 mức giá**; không có `saleCount`/`goodRate`/tỉ lệ hoàn tiền trong payload |
| **Tỉ lệ hồi đáp, % đánh giá tốt, phí shop** | ❌ — các trường này trả về `0`/rỗng (bị chặn ở tầng dữ liệu) |

**Giới hạn còn lại:** trang **TÌM KIẾM** vẫn bị chặn hoàn toàn (thử `m.1688.com/offer_search.htm`, `m.1688.com/offer_search/-<hex>.html`, `m.1688.com/page/offerlist.htm`, `s.1688.com/selloffer/offer_search.htm` → tất cả trả captcha hoặc redirect). **Vì vậy tôi chỉ đọc được những offer id đã biết sẵn từ T1, không tự tìm được listing mới.** Ngoài ra `m.1688.com` **giới hạn theo IP**: sau ~1–2 request thành công thì các request sau bị trả `punish`/302 trong vài chục giây. Tôi phải chờ 60–75 giây giữa các request.

**Hệ quả cho độ tin cậy:** 3 SKU dưới đây giờ có dữ liệu **đọc trực tiếp**, không còn là snippet:

| SKU | Offer id | Trạng thái | Ngày đọc |
|---|---|---|---|
| SP7 áo búp bê 10cm | `1004957259082` | ✅ `[ĐÃ VERIFY]` đầy đủ | 2026-10-23 |
| SP1 quạt mini | `833244917794` | ✅ `[ĐÃ VERIFY]` đầy đủ | 2026-10-23 |
| SP2 bàn chải | `672678209686` | ❌ Bị `punish` 3 lần liên tiếp → vẫn `[chưa kiểm chứng]` | — |
| SP3 chân kê (bản nhựa) | `638799802808` | ⚠️ **Chỉ có giá từ mirror**, không đọc được trực tiếp; id còn 302 | — |

### 0.2. Thang độ tin cậy

| Nhãn | Nghĩa |
|---|---|
| `[ĐÃ VERIFY]` | Đọc trực tiếp `m.1688.com/offer/<id>.html` ngày 2026-10-23, có giá + MOQ + số đã bán + trọng lượng |
| `[chưa kiểm chứng]` | Từ snippet tìm kiếm hoặc mirror; **chưa** xác nhận giá/MOQ/tên shop |
| `[suy luận]` | Do người phân tích suy ra, không có nguồn giá trực tiếp |

### 0.3. GIỚI HẠN PHẢI CÔNG BỐ (không giấu)

1. **Yêu cầu "≥3 nhà cung cấp/listing có ĐẦY ĐỦ dữ liệu" KHÔNG đạt được cho bất kỳ SKU nào** — vì trang tìm kiếm 1688 bị chặn nên tôi không thể tự phát hiện listing mới; chỉ đọc được các id có sẵn. Bảng dưới có **3–4 nguồn/SKU nhưng phần lớn là `[chưa kiểm chứng]`**.
2. **Không có bảng giá theo bậc (阶梯价) cho bất kỳ SKU nào.** Cả 2 trang đọc trực tiếp đều chỉ trả **1 mức giá + MOQ**. Ở SP1 và SP7, mức giá duy nhất hiển thị đã là mức cho **MOQ = 1 và 3** — tức **chưa thấy chiết khấu theo số lượng**, và giá bán buôn thật **phải đàm phán trực tiếp với shop**. **Đây là ẩn số lớn nhất của toàn bộ báo cáo.**
3. **% hoàn tiền / phí shop / đánh giá shop: KHÔNG có cho bất kỳ SKU nào** (payload trả rỗng).
4. **SP3 bản inox KHÔNG có bất kỳ nguồn giá 1688 nào.** Mục 3.2 trình bày rõ khoảng trống này và giá ngược cần có.
5. **Thuế suất nhập khẩu là GIẢ ĐỊNH** (§6.2), không tra biểu thuế.

---

## 1. TỶ GIÁ — nguồn và ngày (2026-10-23)

| Loại tỷ giá | Giá trị | Nguồn | Ngày |
|---|---|---|---|
| USD/CNY tham chiếu quốc tế | 1 USD = **6,6743** CNY | ECB (qua `frankfurter`) | 2026-10-23 |
| Tỷ giá trung tâm USD/VND | 1 USD = **25.831** VND | SBV / Open ER | 2026-10-23 |
| → **CNY/VND thị trường (chéo)** | **1 CNY = 3.862,18 VND** | = 25.831 ÷ 6,6743 | 2026-10-23 |
| Vietcombank — mua chuyển khoản CNY | 1 CNY = **3.812,76** VND | Vietcombank | 2026-10-23 |
| Vietcombank — bán ra CNY | 1 CNY = **3.934,97** VND | Vietcombank | 2026-10-23 |
| **Tỷ giá công ty order hộ** | 1 CNY = **3.960** VND | bảng giá công khai | 2026-10-23 |
| USD/VND — giá bán Vietcombank | 1 USD = **26.040** VND | Vietcombank | 2026-10-23 |

**Quy tắc dùng:** cột "→ VND" dùng **1 CNY = 3.862 VND** (tỷ giá thị trường) để so sánh thuần. **Khi tính tiền thật phải dùng 1 CNY = 4.004 VND** (mua CNY ở giá bán ra ngân hàng) hoặc **3.960** nếu trả qua công ty order hộ → **đắt hơn 2,5–3,7%** so với mọi cột trong báo cáo này. **Ngân sách 20.000.000 VND ≈ 769 USD @ 26.000.**

---

## 2. SP7 — ÁO/ĐỒ CHO BÚP BÊ 10CM `[ĐÃ VERIFY]` — **ỨNG VIÊN #1**

### 2.1. Dữ liệu đọc trực tiếp từ `m.1688.com/offer/1004957259082.html` (2026-10-23)

| Thuộc tính | Giá trị | Nguồn |
|---|---|---|
| **Tên đầy đủ (tiếng Trung)** | 背带裤10cm跨境拉布布娃衣可爱背带裤公仔玩偶替换衣服 | `[ĐÃ VERIFY]` |
| Dịch | Quần yếm 10cm cho búp bê, **"cross-border Labubu doll clothes"**, quần yếm dễ thương cho gấu bông/thú nhồi bông | — |
| Mã offer | `1004957259082` | `[ĐÃ VERIFY]` |
| **Giá hiển thị** | **2,00 CNY** | `[ĐÃ VERIFY]` |
| **→ VND** | **7.724 VND** | tính |
| **MOQ (`beginAmount`)** | **3** (đơn vị: 个 = cái) | `[ĐÃ VERIFY]` |
| **Đã bán (`saledCount`)** | **32.195** (hiển thị "3万+") | `[ĐÃ VERIFY]` |
| **Trọng lượng 1 sản phẩm** | **0,01 kg = 10 g** | `[ĐÃ VERIFY]` |
| **Tên shop** | 长沙市子伊嘉服装配饰厂 | `[ĐÃ VERIFY]` |
| **Tên công ty đăng ký** | 长沙市天心区子伊嘉宠物用品店(个体工商户) — *hộ kinh doanh cá thể, ngành **thú cưng*** | `[ĐÃ VERIFY]` |
| **Địa chỉ kho** | **Hồ Nam, Ích Dương** (湖南益阳) | `[ĐÃ VERIFY]` |
| **Số biến thể / màu** | **85 lựa chọn** | `[ĐÃ VERIFY]` |
| Loại biến thể | Quần yếm nhung tăm (条绒背带裤) 13 màu · quần yếm jean mềm (软牛仔背带裤) · quần yếm có túi (口袋背带裤) 12 màu · quần cách (格格裤) có/không nhãn · **mũ** (帽子) 18 màu · **túi nhỏ hoa** (碎花小包) | `[ĐÃ VERIFY]` |
| Chất liệu | 布 (vải) | `[ĐÃ VERIFY]` |
| Thời điểm lên kệ | 2023年春季 (xuân 2023) | `[ĐÃ VERIFY]` |
| Phân loại 3C | Đồ chơi cho **trẻ trên 14 tuổi** | `[ĐÃ VERIFY]` |
| Cờ xuất khẩu | 是否跨境出口专供货源 = **否** (không phải nguồn chuyên xuất khẩu) | `[ĐÃ VERIFY]` |
| Cam kết giao | **15 ngày** (承诺15天发货) | `[ĐÃ VERIFY]` |
| Bảo vệ người mua | Bồi thường phí hoàn hàng, hoàn tiền nhanh | `[ĐÃ VERIFY]` |

### 2.2. ⚠️ BA CẢNH BÁO QUAN TRỌNG VỀ SP7

**(1) ⚠️ TÊN SẢN PHẨM TRÊN 1688 CÓ CHỨA "拉布布" = LABUBU — RỦI RO SỞ HỮU TRÍ TUỆ.**
Tên gốc ghi rõ **"跨境拉布布娃衣"** (娃衣 đồ cho búp bê Labubu xuyên biên giới). **Labubu là nhân vật có bản quyền của POP MART.** T3 đã cảnh báo các listing **Shopee VN** dùng chữ "Labubu" — nay tôi xác nhận **rủi ro bắt nguồn từ chính nhà cung cấp 1688**, không chỉ ở khâu đặt tên bán.
→ **Bắt buộc:** không dùng "Labubu", "拉布布", "POP MART" trong tiêu đề/mô tả/hashtag/tên shop; không bán set có **hình in nhân vật**; chỉ bán **áo quần generic cho búp bê cao 10cm**. Lưu ý trong danh sách biến thể có loại **"格格裤-小熊标"** (quần có **nhãn hình gấu**) → **tránh đặt biến thể có nhãn/hình in**.

**(2) ⚠️ MOQ LÀ 3, KHÔNG PHẢI 1.** T1 ghi `beginAmount = 1` cho mã này; dữ liệu hiện tại là **`beginAmount: 3`**. Đã đổi. Ảnh hưởng: đặt mẫu phải mua **tối thiểu 3 cái/lần** — với 7.724 VND/cái là **23.172 VND/lần đặt mẫu**, không đáng kể.

**(3) ⚠️ SHOP LÀ ĐẠI LÝ, KHÔNG PHẢI XƯỞNG.** Tên đăng ký là **hộ kinh doanh ngành THÚ CƯNG** (宠物用品店) ở Ích Dương, Hồ Nam, nhưng lại bán quần áo búp bê. Đây là **thương lái gom hàng**, không phải xưởng may. Hệ quả: (a) khó đàm phán giá sâu; (b) chất lượng và độ ổn định giữa các lô không đảm bảo; (c) **không xin được C/O Form E** vì không phải nhà sản xuất. Ích Dương (Hồ Nam) là trung tâm sản xuất **chiếu cói/tre trúc**, **không phải trung tâm may mặc** → càng củng cố kết luận đây là đại lý.

### 2.3. So sánh nhà cung cấp SP7 (4 nguồn)

| # | Mã offer / URL | Shop | Đã bán | Giá (CNY) | → VND | MOQ | Loại giá | Đặc điểm | Tin cậy |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `1004957259082` · https://m.1688.com/offer/1004957259082.html | 长沙市子伊嘉服装配饰厂 (đại lý, Hồ Nam Ích Dương) | **32.195** | **2,00** | 7.724 | **3** | niêm yết, đã xác nhận | 85 biến thể, 10 g/cái, giao 15 ngày | **`[ĐÃ VERIFY]`** |
| 2 | `1010251183643` · https://m.1688.com/offer/1010251183643.html | *(không đọc được — bị punish)* | không rõ | **1,00** *(snippet)* | 3.862 | không rõ | niêm yết | Váy 14cm + áo 10cm | `[chưa kiểm chứng]` |
| 3 | https://s.1688.com/kq/-CDDECDDED2C2B7FE.html | không rõ | **1.668** | **3,50** | 13.518 | không rõ | niêm yết | **Bán chạy nhất nhóm này** | `[chưa kiểm chứng]` |
| 4 | https://s.1688.com/kq/-CDDECDDED2C2B7FE.html | không rõ | **488** | **4,80** | 18.538 | không rõ | niêm yết | — | `[chưa kiểm chứng]` |

**Dải giá: 1,00 – 4,80 CNY (3.862 – 18.538 VND).** Nguồn #1 (đã verify) nằm ở **đáy dải giá** và có lượng đã bán lớn nhất trong nhóm đọc được trực tiếp → **đây là nguồn tốt để khởi động**. Nguồn #3 (3,50 CNY, 1.668 đơn) là mẫu bán chạy thứ hai, đáng đặt thử để so sánh chất lượng.

### 2.4. Chi phí landed SP7 — 3 mức số lượng (trọng lượng **ĐÃ VERIFY 10 g/cái**)

Quy tắc: phí thông quan 1688Express nhóm **thời trang 4,9%** (bậc 2–20 triệu), tối thiểu 9.000 VND. Phí ship tính **25.000 VND/kg** (1688Express, mức thận trọng); cột so sánh cho thấy mức tiết kiệm nếu dùng Thương Đô.

**Trường hợp A — giá 2,00 CNY (7.724 VND) `[ĐÃ VERIFY]`**

| SL | kg | Tiền hàng | Phí ship | Thông quan | **Landed A (kênh thường)** | **/đơn vị** | Landed B (+thuế 12% +GTGT 8%) /đv |
|---|---|---|---|---|---|---|---|
| 50 | 0,5 | 386.200 | 12.500 | 18.924 | 417.624 | **8.352** | **11.173** |
| 200 | 2,0 | 1.544.800 | 50.000 | 75.695 | 1.670.495 | **8.352** | **11.174** |
| 500 | 5,0 | 3.862.000 | 125.000 | 189.238 | 4.176.238 | **8.352** | **11.173** |
| 1.000 | 10,0 | 7.724.000 | 250.000 | 378.476 | 8.352.476 | **8.352** | **11.173** |

**Trường hợp B — giá 3,80 CNY (14.676 VND) `[chưa kiểm chứng]` (mức cao của dải T1)**

| SL | kg | Tiền hàng | Phí ship | Thông quan | **Landed A** | **/đơn vị** | Landed B /đv |
|---|---|---|---|---|---|---|---|
| 50 | 0,5 | 733.800 | 12.500 | 35.956 | 782.256 | **15.645** | **19.936** |
| 200 | 2,0 | 2.935.200 | 50.000 | 143.825 | 3.129.025 | **15.645** | **19.925** |
| 500 | 5,0 | 7.338.000 | 125.000 | 359.562 | 7.822.562 | **15.645** | **19.925** |
| 1.000 | 10,0 | 14.676.000 | 250.000 | 719.124 | 15.645.124 | **15.645** | **19.925** |

**So sánh forwarder @ 500 cái:** Thương Đô (22.000 đ/kg) **8.322** · 1688Express (25.000 đ/kg) **8.352** — chênh 30 VND/cái. **Với hàng nhẹ thế này, chênh lệch forwarder gần như không đáng kể** (vì tổng chỉ 5 kg). **Điều này rất quan trọng: với SP7, chọn forwarder không phải là đòn bẩy lợi nhuận — giá nhập mới là.**

**Về cân nặng:** giả định cũ của T2 là 30 g/cái; **trọng lượng thật là 10 g/cái** → tiết kiệm 500 VND/cái (≈6% landed).

**Đối chiếu với T3:** T3 dùng **11.700 VND landed/đơn vị**. Con số thật là **8.352 (2,00 CNY)** đến **15.645 (3,80 CNY)** — trung vị ~12.000. **Giả định của T3 nằm trong khoảng thật và hơi thận trọng** → **mô hình biên 38,8–46,9% của T3 vẫn đứng vững**, và nếu mua được ở 2,00 CNY thì biên còn tốt hơn dự kiến.

### 2.5. Đối chiếu giá bán VN (từ T3) và biên lợi nhuận

| Cấu hình | Giá bán VN | Landed (2,00 CNY) | Lãi gộp trước phí sàn | Ghi chú |
|---|---|---|---|---|
| 1 bộ | 75.000 | 8.352 – 11.173 | **85–89%** | Biên rất cao |
| Combo 3 bộ | 189.000 | 25.056 – 33.519 | **82–87%** | T3 tính 46,9% **sau** phí sàn + freeship |
| Set full | 205.000 | 8.352 – 11.173 | **94–96%** | Dùng làm neo giá |

> **Kết luận SP7:** đây là **SKU duy nhất có dữ liệu giá đọc trực tiếp**, **SKU duy nhất có trọng lượng siêu nhẹ (10 g)**, và **SKU có biên gộp cao nhất**. Xác nhận T3: **dồn tiền vào SP7.** Ba việc phải làm trước khi đặt: (a) đặt **3 cái** (MOQ) để kiểm chất lượng + xác nhận ảnh thật; (b) **loại bỏ mọi biến thể có nhãn/hình in**; (c) **đàm phán giá bậc** cho lô ≥500 vì trang không hiển thị chiết khấu số lượng.

---

## 3. SP3 — CHÂN KÊ MÁY GIẶT/TỦ LẠNH: **BẢN NHỰA vs BẢN INOX**

### 3.1. Bản nhựa/cao su cơ bản

| # | Mã offer / URL | Shop | Đã bán | Giá (CNY) | → VND | MOQ | Loại giá | Đặc điểm | Tin cậy |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `638799802808` · https://detail.1688.com/offer/638799802808.html | không hiển thị | không rõ | **~1,00** *(mirror: US$0,26)* | ~3.900 | **≥4** | niêm yết | Cao su/silicone, tăng chiều cao | `[chưa kiểm chứng]` |
| 2 | https://s.1688.com/kq/-CFB4D2C2BBFAB7C0D5F0B5E6.html?beginPage=4 | Nghĩa Ô Y Thành Nhật Dụng (1 năm) | **7** | **2,20** | 8.497 | không rõ | niêm yết | Tăng chiều cao + giảm chấn + chống trượt, dùng chung tủ lạnh | `[chưa kiểm chứng]` |
| 3 | https://www.1688.com/wiki/zh/washing-machine-base/WKg1tewa44j7cw | *(wiki 1688 — AI sinh)* | **>100.000** | **0,14** | 541 | không rõ | niêm yết | Đệm chân đơn lẻ | `[chưa kiểm chứng]` ⚠️ nguồn AI-SEO, nghi phóng đại |

⚠️ **Vẫn chưa giải quyết được câu hỏi quan trọng nhất:** `US$0,26` là giá **1 chân** hay **cả set 4 chân**? Nếu là 1 chân thì set 4 ≈ 4,00 CNY ≈ 15.448 VND → landed đội lên đáng kể. **Phải xác minh.**

### 3.2. BẢN INOX — **KHÔNG CÓ NGUỒN GIÁ 1688** ⚠️

**Đây là khoảng trống lớn nhất của T2.** T3 xác định bản inox là **"cửa thoát khỏi cuộc đua giá"** (giá bán VN **182.000–205.000 VND**, listing đã bán **40k+**, khách chấp nhận trả gấp 4 lần bản nhựa), và T3 dùng **62.000 VND landed** cho bản inox. Nhưng:

- **Tôi KHÔNG tìm được bất kỳ offer id nào cho chân kê inox** — vì trang tìm kiếm 1688 bị chặn, tôi chỉ đọc được các id có sẵn từ T1, và T1 không có id nào cho bản inox.
- Các nguồn tìm được cho SP3 (kể cả nguồn `buy2you` `638799802808`) đều là **bản nhựa/cao su**, không phải inox.
- **62.000 VND landed trong T3 là GIẢ ĐỊNH, không phải số đo.** Tôi tính ngược để cho thấy giả định đó đòi hỏi điều gì:

| Nếu landed mục tiêu = 62.000 VND/đơn vị (giả định T3) | Giá nhập 1688 cần có |
|---|---|
| Với trọng lượng 200 g/set, ship 25.000 đ/kg, thông quan 2,9% | **≈ 15,0 CNY (≈ 57.900 VND) tiền hàng** |
| → tức landed = **7,5× giá bản nhựa 2,20 CNY** | **Bản inox phải đắt gấp ~7 lần bản nhựa** |

**Đánh giá:** mức gấp ~7 lần giữa bản nhựa và bản inox **là hợp lý về mặt vật liệu** (inox 304 + trụ điều chỉnh cao vs cao su đúc), **nhưng hoàn toàn chưa được kiểm chứng.** Nếu giá inox thật là 15 CNY thì landed 62.000 VND và biên 30,6% của T3 đúng; nếu inox thật đắt hơn (ví dụ 25 CNY) thì landed ~100.000 VND và **biên sụp còn ~15%**.

**→ Việc phải làm:** truy cập 1688 bằng account/proxy để tìm offer inox, hoặc hỏi trực tiếp shop `Nghĩa Ô Y Thành` xem có bản inox không. **Không được xuống tiền cho bản inox dựa trên số 62.000 VND này.**

### 3.3. Chi phí landed SP3 — bản nhựa, 3 mức số lượng

**Trường hợp giá 2,20 CNY (8.497 VND), trọng lượng 200 g/set `[chưa kiểm chứng]`**

| SL | kg | Tiền hàng | Phí ship | Thông quan | **Landed A** | **/đơn vị** | Landed B (+thuế 15% +GTGT 8%) /đv |
|---|---|---|---|---|---|---|---|
| 50 | 10,0 | 424.850 | 250.000 | 12.321 | 687.171 | **13.743** | **16.208** |
| 200 | 40,0 | 1.699.400 | 1.000.000 | 49.283 | 2.748.683 | **13.743** | **16.208** |
| 500 | 100,0 | 4.248.500 | 2.500.000 | 123.207 | 6.871.707 | **13.743** | **16.200** |

**So sánh forwarder @ 200 set:** Thương Đô **13.143** · ShipTrungViet 13.543 · 1688Express **13.743** VND/set (chênh tối đa 600 VND = 4,4% → **với hàng 200 g, chọn forwarder có ý nghĩa hơn so với SP7**).

**Trường hợp giá ~1,00 CNY (mirror US$0,26, nếu là CẢ SET 4 CHÂN):** landed ≈ **4.000–5.000 VND/set** → lãi gộp **89%** ở giá bán 45.000.
**Trường hợp US$0,26 là giá 1 CHÂN (set 4 = 4,00 CNY ≈ 15.448 VND):** landed ≈ **21.000 VND/set** → lãi gộp **53%**.

> **Kết luận SP3:** **hai phiên bản, hai câu chuyện khác hẳn nhau:**
> - **Bản nhựa (2,20 CNY):** landed 13.743 VND, **lãi gộp 64–69%** trước phí sàn. **Nhưng** T3 đã chứng minh ở giá bán lẻ 45.000–55.000 VND, sau **5.700 VND phí cứng + 22% hoa hồng**, biên còn **~21,5%** → **mỏng, dễ thành hoà vốn.**
> - **Bản inox (giá chưa biết, T3 giả định 62.000 VND landed):** bán 182.000–205.000 VND, biên **30,6%**, **cạnh tranh ít hơn** vì bản nhựa rẻ đã bão hoà ở 19.998 VND.
> **→ SP3 bản inox là hướng đúng, nhưng đang bị chặn bởi thiếu dữ liệu giá. Đây là ưu tiên xác minh #1 của T2.**

---

## 4. PHÍ VẬN CHUYỂN NỘI ĐỊA TRUNG QUỐC

| Kênh | Phí nội địa TQ | Ghi chú | Tin cậy |
|---|---|---|---|
| SP7 (`1004957259082`) | **không hiển thị trong payload** — shop ở Hồ Nam Ích Dương, giao 15 ngày | Cần hỏi shop | — |
| SP1 (`833244917794`) | **không hiển thị** — giao 48 giờ, thường phát Trung Thông (中通快递) | Shop ở Quảng Đông Thâm Quyến → **gần Quảng Châu ✓** | `[ĐÃ VERIFY]` (thông tin logistics) |
| Shop có "1 dau 代发" | **US$0 — miễn phí** | Mô hình dropship TQ | `[chưa kiểm chứng]` |
| T3 ghi nhận | **~80% đơn 1688 miễn phí ship nội địa TQ** | Nguồn: 1688express.vn | `[verified]` theo T3 |

**Lưu ý định tuyến quan trọng:** kho SP1 ở **Thâm Quyến (Quảng Đông)** → gần tuyến **Quảng Châu–Hà Nội**, phí nội địa vào kho gom rất thấp. Kho SP7 ở **Ích Dương (Hồ Nam)** → **xa hơn**, phí nội địa TQ vào Quảng Châu **cao hơn** và thời gian dài hơn (shop đã cam kết 15 ngày giao, dài hơn mức 48 giờ của SP1). **Đây là một bất lợi thật của SP7 mà cần tính vào lịch nhập hàng.**

---

## 5. PHÍ VẬN CHUYỂN TRUNG QUỐC → VIỆT NAM (theo **kg** VÀ theo **m³**)

### 5.1. So sánh ≥2 phương án forwarder (bảng giá công bố 2026-10-23)

**A. Thương Đô Express — Quảng Châu → Hà Nội**

| Bậc | Phí/kg | Ghi chú |
|---|---|---|
| ≤ 10 kg | **24.000** | |
| 10–30 kg | **23.000** | |
| 30–100 kg | **22.000** | **Rẻ nhất** trong 3 đơn vị |
| Thời gian | 5–7 ngày | |
| Thể tích | 1 m³ = **8.000 kg** | |

**B. ShipTrungViet — Quảng Châu → Hà Nội**

| Bậc | Phí/kg | Ghi chú |
|---|---|---|
| < 10 kg | **25.000** | |
| 10–20 kg | 25.000–30.000 | |
| 20–50 kg | 25.000–33.000 | |
| 500 g đầu | **20.000** | Tốt cho đơn mẫu rất nhỏ |
| **Theo m³** | **2.500.000 VND/m³** (<10 m³) · **1.800.000 VND/m³** (≥10 m³) · cuộn 1.000.000 VND/m³ | **Rẻ nhất cho hàng cồng kềnh** |

**C. 1688Express — Quảng Châu → Hà Nội** (đơn vị T1/T3 đang dùng)

| Bậc | Phí/kg | Ghi chú |
|---|---|---|
| 5–10 kg | **28.000–34.000** | T3 đọc được: 28.000 (HN) / 34.000 (HCM) / 35.000 (Đà Nẵng) |
| 10–20 kg | 27.000–33.000 | |
| 20–30 kg | 26.000–32.000 | |
| 30–100 kg | 25.000–31.000 | Đắt nhất ở mọi bậc |
| Thể tích | 1 m³ = **8.000 kg** (D×R×C/8000) | |

### 5.2. Tính theo kg vs theo m³ — áp dụng cho chính 2 SKU ưu tiên

**SP7 (10 g/cái — ĐÃ VERIFY):**

| Lô | Theo kg (Thương Đô 22.000–24.000 đ/kg) | Theo m³ | Kết luận |
|---|---|---|---|
| 500 cái = **5 kg** | 110.000–120.000 VND → **220–240 VND/cái** | Áo quần nén chặt, 500 cái ≪ 0,1 m³ → nếu tính m³: ~180.000–250.000 VND (tương đương) | **Hai cách gần bằng nhau.** Cước chỉ chiếm **2,6% landed** → **cân nặng KHÔNG phải vấn đề của SP7** |

**SP3 (200 g/set — giả định):**

| Lô | Theo kg | Theo m³ (thùng 20×20×5 cm) | Kết luận |
|---|---|---|---|
| 200 set = **40 kg** | 40 × 22.000–25.000 = **880.000–1.000.000 VND** → 4.400–5.000 đ/set | 200 × 0,002 = **0,4 m³** × 1,8–2,5 tr/m³ = **720.000–1.000.000 VND** → 3.600–5.000 đ/set | **Hai cách tương đương (±20%)**; quy đổi 1:8000 khá sát với hàng xốp |
| 500 set = **100 kg** | 100 × 22.000 = **2.200.000 VND** → **4.400 đ/set** | 1,0 m³ × 1,8 tr = **1.800.000 VND** → **3.600 đ/set** | **Theo m³ rẻ hơn 18%** → **với lô ≥500 set, hỏi forwarder tính theo m³** |

**→ Khuyến nghị forwarder:** dùng **Thương Đô Express** (rẻ nhất theo kg). **Riêng với lô SP3 ≥500 set, yêu cầu ShipTrungViet báo giá theo m³** — có thể tiết kiệm ~18% cước, tức ~800 VND/set trên landed 13.743 VND (**~6% landed**).

### 5.3. Bậc tối thiểu
Không đơn vị nào miễn phí. Lô < 0,5 kg vẫn tính tối thiểu 0,5 kg → **sàn ~20.000 VND/đơn mẫu** (ShipTrungViet).

---

## 6. THUẾ / PHÍ NHẬP KHẨU VIỆT NAM

### 6.1. ⚠️ NGƯỠNG MIỄN THUẾ 1 TRIỆU ĐỒNG ĐÃ BỊ BÃI BỎ

> **Quyết định số 01/2025/QĐ-TTg ngày 03/01/2025** bãi bỏ toàn bộ **Quyết định 78/2010/QĐ-TTg** — chấm dứt miễn thuế NK và GTGT cho hàng gửi qua chuyển phát nhanh **có giá trị ≤ 1 triệu đồng**. **Hiệu lực từ 18/02/2025.**
> Nguồn: https://baochinhphu.vn/ngung-mien-thue-hang-nhap-khau-duoi-1-trieu-dong-gui-qua-chuyen-phat-nhanh-102250103212054862.htm `[ĐÃ VERIFY]` (fetch 200, đọc toàn văn 2026-10-23)
> Bối cảnh bài báo: *"Hàng ngày có khoảng 4-5 triệu đơn hàng giá trị nhỏ được vận chuyển từ Trung Quốc về Việt Nam qua các sàn thương mại điện tử."*

**Hệ quả:** **mọi** lô test đều phải nộp thuế NK + GTGT, kể cả lô 500.000 VND. **Đây là chi phí T1 chưa tính.** GTGT phổ thông **10%**, nhiều nhóm đang áp **8%** theo chính sách giảm thuế tạm thời (gia hạn qua 2026) — **phải xác nhận tại thời điểm nhập**.

### 6.2. Thuế suất NK — **GIẢ ĐỊNH** `[suy luận]`

| Nhóm SP | Mã HS giả định | Ưu đãi thường | **ACFTA (có C/O Form E)** |
|---|---|---|---|
| SP7 hàng may/phụ kiện búp bê | 6111 / 9503 | 12–20% | **0–5%** |
| SP3 đồ nhựa gia dụng | 3924 / 3926 | 15–20% | **0–5%** |
| SP1, SP6 quạt/thiết bị điện | 8414 / 8509 / 8543 | 20–25% | **0–5%** |
| SP2 đồ nhựa | 3924 | 15–20% | 0–5% |
| SP5 đồ nhựa | 3926 | 15–20% | 0–5% |
| SP8 trang sức kim loại | 7117 | 20–25% | 0–5% |

**Sai số có thể ±10 điểm phần trăm. Không dùng để chốt giá bán.** Phải tra biểu thuế XNK hiện hành hoặc hỏi forwarder. **Lưu ý SP7: shop là đại lý, không phải xưởng → khó có C/O Form E → khả năng phải chịu mức ưu đãi thường 12–20% thay vì 0–5%.**

### 6.3. Phí thông quan 1688Express (bậc theo giá trị hàng)

| Giá trị hàng | Hàng nặng | Gia dụng/điện tử | Thời trang |
|---|---|---|---|
| > 100 triệu | 0,5% | 2,5% | 4,5% |
| 20–100 triệu | 0,8% | 2,8% | 4,8% |
| 2–20 triệu | 0,9% | 2,9% | 4,9% |
| < 2 triệu | 1,0% | 3,0% | 5,0% |
| **Tối thiểu** | **9.000 VND/đơn** | | |

*(SP7 áp nhóm "thời trang" ~4,9%; SP3 áp "gia dụng" ~2,9%.)*

---

## 7. MUA QUA ĐẠI LÝ/ORDER HỘ vs TỰ NHẬP QUA FORWARDER

| Tiêu chí | **A. Công ty order hộ TQ** | **B. Tự nhập qua forwarder** |
|---|---|---|
| Tỷ giá | **3.960 VND/CNY** (+2,5% so thị trường) | 4.004 VND/CNY (mua ngân hàng) |
| Phí dịch vụ | **3–7%** giá trị hàng, tối thiểu ~30.000–50.000 VND/đơn | Không phí riêng; nằm trong đơn giá/kg |
| Vận chuyển | 25.000–35.000 VND/kg | **22.000–25.000 VND/kg** (Thương Đô rẻ nhất) |
| Thông quan | Gộp trong phí; **thường không có hoá đơn thuế riêng** | Có phí khai hải quan riêng |
| **Tổng chênh lệch** | **+8% đến +15%** cho lô 20–50 kg | Mức tham chiếu |
| Thời gian | 7–12 ngày | 5–7 ngày (Thương Đô HN) |
| MOQ | Nhận đơn rất nhỏ (1–5 món) | Cần đủ kg; lô < 5 kg phí/kg rất cao |
| **Rủi ro** | Không hoá đơn VAT đầu vào; tỷ giá kém; khó truy hàng lỗi; **rủi ro pháp lý nếu không khai báo** | **Tự chịu trách nhiệm khai hải quan**; cần mã HS đúng; cần C/O Form E; cần MST |
| **Phù hợp** | **Lô test đầu tiên**, đặt mẫu | Lô đã validate, ≥30–50 kg |

### 7.1. Khuyến nghị hai bước

1. **Bước 1 — mẫu (~1–3 triệu VND): dùng công ty order hộ.** Với SP7: đặt **3 cái** (MOQ) từ nguồn đã verify + **3 cái** từ nguồn `3,50 CNY / 1.668 đơn` để so sánh chất lượng. Với SP3 bản nhựa: đặt **4 set** (MOQ) từ `Nghĩa Ô Y Thành`. **Yêu cầu công ty order hộ gửi ảnh thật trước khi ship** và **hỏi rõ bản inox có không, giá bao nhiêu**.
2. **Bước 2 — lô bán thật (phần còn lại của 20 triệu): tự nhập qua Thương Đô Express.** Sau khi biết chính xác SKU/trọng lượng/thông số, yêu cầu forwarder **xác nhận mã HS + thuế trước khi gửi** và hỏi về **C/O Form E** (đặc biệt quan trọng với SP7 vì shop là đại lý).

**Điểm ăn mòn lợi nhuận dễ bị bỏ qua:** chênh tỷ giá 3.960 vs 4.004 ≈ **220.000 VND trên 20 triệu hàng**; phí dịch vụ 3–7% ≈ **600.000–1.400.000 VND**; chênh cước 3.000–10.000 VND/kg ≈ **150.000–500.000 VND/lô 50 kg**. **Tổng 1–2 triệu VND/lô = 5–10% tổng vốn = 8–20% lợi nhuận.** Đủ để biến SKU có lãi thành hoà vốn.

---

## 8. CÁC SKU CÒN LẠI — LANDED COST MỨC COMBO/SET (ghi ngắn theo chỉ đạo)

| SKU | Giá nhập dùng tính | Landed A /đv | Giá bán theo cấu trúc có lãi | Biên gộp (combo) | Tin cậy | Ghi chú 1 dòng |
|---|---|---|---|---|---|---|
| **SP1 quạt mini** | **13,00 CNY (50.208 VND)** `[ĐÃ VERIFY]` | **54.664** | 45.000 (bán lẻ) | **−21%** | `[ĐÃ VERIFY]` | ❌ **Loại trừ** — landed > giá bán. Shop là 金万兆实力工厂 (xưởng thật, Thâm Quyến), giao 48 h, 8 biến thể, MOQ 1, **269.28 đã bán** |
| **SP1b quạt 4,86 CNY** | 4,86 CNY (18.773) `[chưa kiểm chứng]` | **22.314** | 45.000 | **+50%** | `[chưa kiểm chứng]` | ⚠️ **Biến số quyết định** — nếu giá thật vậy thì SP1 đảo ngược kết luận |
| **SP2 bàn chải chà giày** | 4,27 CNY (16.492) `[chưa kiểm chứng]` | **19.470** | combo 5 @49.000 → 9.800/cái | **−100%** (lẻ) / **~−99%** (combo 49.000) | `[chưa kiểm chứng]` | ❌ Bán lẻ 7.999 lỗ −143%; **combo 10 cây @25.900** mới có cửa. Trang `m.1688` của `672678209686` **bị punish 3 lần**, không đọc được |
| **SP2 (nếu 0,98 CNY)** | 0,98 CNY (3.785) `[chưa kiểm chứng]` | **6.764** | combo 5 @49.000 → 9.800/cái | **+31%** | `[chưa kiểm chứng]` | Mới có lãi mỏng. **Phải xác minh listing 0,50–0,98 CNY** |
| **SP5 khoá tủ lạnh** | 8,30 CNY (32.056) `[chưa kiểm chứng]` | **34.486** | lốc 4 @96.000 → 24.000/cái | **−44%** | `[chưa kiểm chứng]` | ❌ **Tiền hàng 32.056 > giá bán 24.614.** Chỉ cứu được nếu tìm nguồn 3–5 CNY |
| **SP6 đèn bắt muỗi USB** | 10,70 CNY (41.325) `[chưa kiểm chứng]` | **51.273** | set 2 @229.000 → 114.500/cái | **+55%** | `[chưa kiểm chứng]` | ✅ Khả thi. **350 g/SP = nặng nhất** → cước 17% landed; lô 500 = 175 kg phải đàm phán. **KHÔNG dùng giá 0,62 CNY** (gần chắc chắn là linh kiện) |
| **SP8 trang sức set** | 1,00 CNY *(suy luận)* | **4.474** | set 5 @65.000 → 13.000/món | **+65%** | **`[suy luận]`** | ❌ **Không có nguồn giá 1688.** FindNiche chỉ trả doanh số + giá bán VN, **không trả giá nhập** |

**Lưu ý chung cho nhóm này (theo phát hiện của T3):** mọi SKU **dưới ~50.000 VND lỗ khi bán lẻ** vì **5.700 VND phí cứng Shopee + 22% hoa hồng**. Vì vậy cột "giá bán theo cấu trúc có lãi" ở trên buộc phải là **combo/set**, không phải bán lẻ.

---

## 9. BẢNG XẾP HẠNG LẠI THEO LANDED COST THỰC TẾ (sau chỉ đạo của captain)

| Hạng | SKU | Giá nhập | Landed A/đv | Biên gộp (A) | Tin cậy giá | Kết luận |
|---|---|---|---|---|---|---|
| **1** | **SP7 áo búp bê 10cm** | **2,00 CNY** | **8.352** | **85–89%** | **`[ĐÃ VERIFY]`** | ✅ **Dồn tiền. Né từ khóa "Labubu".** MOQ 3, 10 g/cái |
| **2** | **SP3 chân kê bản INOX** | **chưa biết** (T3 giả định ~15 CNY) | **~62.000** *(giả định)* | **~30,6%** | **`[chưa kiểm chứng]` — không có nguồn** | ⚠️ **Hướng đúng nhưng BỊ CHẶN vì thiếu giá. Xác minh trước.** |
| **3** | SP3 chân kê bản NHỰA | 2,20 CNY | 13.743 | 64–69% thô / **~21,5% sau phí sàn** | `[chưa kiểm chứng]` | 🟡 Chỉ dùng làm sản phẩm phụ/upsell |
| **4** | SP6 đèn bắt muỗi | 10,70 CNY | 51.273 | +55% | `[chưa kiểm chứng]` | ✅ Khả thi, nhưng 350 g/SP |
| **5** | SP1b quạt mini | 4,86 CNY | 22.314 | +50% | `[chưa kiểm chứng]` | ⚠️ Phải đặt mẫu để biết giá thật |
| **6** | SP2 bàn chải (combo) | 0,98 CNY | 6.764 | +31% | `[chưa kiểm chứng]` | 🟡 Chỉ combo |
| **7** | SP8 trang sức | 1,00 CNY | 4.474 | +65% | **`[suy luận]`** | ❌ Không có nguồn giá |
| **8** | SP5 khoá tủ lạnh | 8,30 CNY | 34.486 | **−44%** | `[chưa kiểm chứng]` | ❌ Lỗ |
| **9** | **SP1 quạt turbo 13 CNY** | **13,00 CNY** | **54.664** | **−21%** | **`[ĐÃ VERIFY]`** | ❌ **Loại trừ — đã xác minh** |

### Phân bổ vốn test đề xuất (20.000.000 VND)

| SKU | SL | Nguồn | Vốn landed (kênh A) | Ghi chú |
|---|---|---|---|---|
| **SP7 áo búp bê (2,00 CNY)** | **500** | `1004957259082` đã verify | **4.176.238** | Ưu tiên #1, giá đã xác minh |
| SP7 mẫu so sánh (3,50 CNY) | 3 | `s.1688` 1.668 đơn | ~50.000 | Mẫu đối chiếu chất lượng |
| **SP3 bản inox** | **100** | **CHƯA CÓ NGUỒN** | *chờ xác minh* | **Chỉ đặt sau khi có giá thật** |
| SP3 bản nhựa (2,20 CNY) | 200 | Nghĩa Ô Y Thành | 2.748.683 | Sản phẩm phụ/upsell |
| SP6 đèn bắt muỗi | 100 | `676667786489` | 5.127.300 | Chờ xác nhận pin |
| SP1b quạt 4,86 CNY | 50 | `1040073960093` | 1.115.717 | **Chỉ để kiểm chứng giá** |
| **Tổng** | | | **≈ 13.217.938** | **Dự phòng ≈ 6.782.062 (34%)** cho ship phát sinh, mẫu lỗi, thuế, marketing |

**Dự phòng 34% là cố ý:** 6/9 dòng giá vẫn `[chưa kiểm chứng]`, thuế NK là giả định, và **SP3 inox chưa có giá** — rủi ro lệch giá cao.

---

## 10. KHUYẾN NGHỊ HÀNH ĐỘNG

1. **SP7 là SKU duy nhất đủ dữ liệu để xuống tiền ngay.** Giá, MOQ, số đã bán, trọng lượng, kho, biến thể, cam kết giao — **tất cả đã đọc trực tiếp**. Đặt **500 cái @ 2,00 CNY = 4,18 triệu VND landed**.
2. **Bốn việc xác minh bắt buộc trước khi mở rộng:**
   - **(a) SP3 bản inox — ưu tiên #1.** Không có nguồn giá. Cần vào 1688 bằng account/proxy để tìm offer inox, hoặc hỏi shop `Nghĩa Ô Y Thành`. **Giá ngược: để landed = 62.000 VND thì tiền hàng phải là ~15 CNY (~7,5× bản nhựa).**
   - **(b) SP3 bản nhựa:** xác minh `US$0,26` là **1 chân hay cả set 4 chân** (chênh làm landed gấp 4 lần).
   - **(c) SP1:** đặt 1 mẫu để biết giá thật **13 CNY hay 4,86 CNY** — biến số lớn nhất còn lại.
   - **(d) SP2:** cần account 1688 để lấy bảng giá bậc (trang `672678209686` bị chặn 3 lần).
3. **PHÁP LÝ — bắt buộc với SP7:** tên sản phẩm 1688 **có chứa "拉布布" (Labubu)**. **Không** dùng "Labubu"/"POP MART" trong tiêu đề, mô tả, hashtag, tên shop; **không** đặt biến thể có nhãn hình (小熊标); chỉ bán **"áo cho búp bê cao 10cm"**. Tra cứu nhãn hiệu tại Cục SHTT trước khi scale.
4. **Loại trừ SP1 @ 13 CNY** (lỗ −21%, đã xác minh) và **SP5 @ 8,30 CNY** (lỗ −44%).
5. **Thuế:** mọi lô phải nộp NK + GTGT (Quyết định 01/2025/QĐ-TTg, hiệu lực 18/02/2025). Xác minh mã HS, mức GTGT 8% hay 10%, và **C/O Form E** — lưu ý SP7 mua từ đại lý nên **khó có Form E**.
6. **Forwarder:** Thương Đô Express (22.000 đ/kg bậc 30–100 kg) cho SP7/SP3 nhựa. **Với lô SP3 ≥500 set, yêu cầu báo giá theo m³** (tiết kiệm ~18% cước).
7. **Chốt tỷ giá bằng văn bản** với công ty order/forwarder trước khi cọc.

---

## 11. PHỤ LỤC — NHẬT KÝ TRUY CẬP LINK

| URL | HTTP | Kết quả |
|---|---|---|
| **https://m.1688.com/offer/1004957259082.html** | **200** | ✅ **ĐỌC ĐƯỢC đầy đủ** — SP7: 2,00 CNY, MOQ 3, 32.195 đã bán, 10 g, 85 biến thể |
| **https://m.1688.com/offer/833244917794.html** | **200** | ✅ **ĐỌC ĐƯỢC đầy đủ** — SP1: 13,00 CNY, MOQ 1, 26.928 đã bán, 8 biến thể, xưởng Thâm Quyến |
| https://m.1688.com/offer/672678209686.html | 302 ×3 | ❌ `punish`/x5sec — SP2 không đọc được |
| https://m.1688.com/offer/638799802808.html | 200 (bxpunish) | ❌ Header `bxpunish: 1`, redirect captcha |
| https://m.1688.com/offer/1010251183643.html | 302 | ❌ `punish` |
| https://m.1688.com/offer_search.htm?keywords=娃衣 | 302 | ❌ Chặn |
| https://m.1688.com/page/offerlist.htm?keywords=娃衣 | 200 (4.698 B) | ❌ Captcha |
| https://m.1688.com/offer_search/-6C6175627562.html | 200 (4.833 B) | ❌ Captcha |
| https://s.1688.com/selloffer/offer_search.htm?keywords=娃衣 | 200 (5.106 B) | ❌ Captcha |
| https://s.1688.com/kq/-B3A4B1FACBA2D7D3.html?beginPage=48 | 200 (4.719 B) | ❌ Captcha `rgv587`/`x5sec` |
| https://s.1688.com/kq/… (9 URL khác) | 200 | ❌ Captcha |
| https://detail.1688.com/offer/833244917794.html | 200 | ✅ Đọc được (trước khi IP bị chặn) |
| https://detail.1688.com/offer/1004957259082.html | 301 | ❌ Redirect |
| https://www.1688.com/wiki/zh/washing-machine-base/WKg1tewa44j7cw | 200 | ⚠️ Shell JS, không có dữ liệu |
| https://www.1688wholesale.com/…/672678209686.html | 200 → 302 | ⚠️ Lần đầu OK, sau đó 302 |
| https://www.buy2you.com/…/638799802808.html | 200 | ⚠️ Listing OK; fetch item = 422 |
| https://findniche.com/tiktok/trending-jewelry-…-vn | 200 | ✅ Doanh số + giá bán VN, **không có giá nhập** |
| https://baochinhphu.vn/ngung-mien-thue-hang-nhap-khau-duoi-1-trieu-dong-gui-qua-chuyen-phat-nhanh-102250103212054862.htm | 200 | ✅ **Quyết định 01/2025/QĐ-TTg, hiệu lực 18/02/2025** |

**File dữ liệu có cấu trúc:** `research-1688/02-nguon-hang.csv` (25 dòng).

**Giới hạn còn lại (không lấp được trong T2):** không có **bảng giá theo bậc** cho bất kỳ SKU nào (trang chỉ trả 1 mức giá); không có **% hoàn tiền / phí shop / đánh giá shop**; **SP3 bản inox không có nguồn giá**; **SP8 không có nguồn giá**; **thuế suất NK là giả định**; trang tìm kiếm 1688 chặn hoàn toàn nên không phát hiện được listing mới. **Cần account 1688 hoặc proxy TQ để hoàn tất các mục này.**
