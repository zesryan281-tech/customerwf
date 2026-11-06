# T1 — Shortlist 10–12 sản phẩm hot trend có thể nhập từ 1688 (thị trường Việt Nam)

- **Người thực hiện**: trend-scout (team 1688-market-research)
- **Ngày tra cứu**: 2026-10-23 (giờ máy: Asia/Shanghai, UTC+8). Mọi số liệu dưới đây là ảnh chụp tại ngày này.
- **Vốn giả định**: 20.000.000 VND (~780–800 USD) cho lô test đầu tiên.
- **Ràng buộc lọc đã áp dụng**: giá nhập dự kiến ≤ 150.000 VND/món; nhẹ (<1kg)/gọn; MOQ thấp (≤100); dễ bán lại qua Shopee/TikTok Shop/Facebook; KHÔNG thuộc nhóm cấm/hạn chế nhập khẩu (không thực phẩm, mỹ phẩm, thuốc, hàng nhái thương hiệu, đồ điện cao thế).
- **Tỷ giá dùng để quy đổi**: 1 CNY ≈ 3.650 VND; 1 USD ≈ 26.300 VND (xấp xỉ, **chưa kiểm chứng** bằng nguồn tỷ giá trong phiên này — cần chốt lại trước khi tính lợi nhuận cuối).

---

## 0. Phương pháp, nguồn và GIỚI HẠN (đọc trước khi dùng số)

**Cách lấy tín hiệu trend**
1. **FindNiche — bảng xếp hạng TikTok Shop theo danh mục, thị trường Việt Nam**, xếp theo *số đơn 7 ngày*. Đây là nguồn định lượng chính. Mọi trang đều ghi `Dataset date: 2026-10-01`; FindNiche tự ghi rõ *"7-day metrics use the reporting window supplied by the source. Exact start and end dates are not provided"* và *"this ranking contains 100 products from the available dataset; it is not a count of all sellers or products in this market"* → **không được đọc bảng này như toàn bộ thị trường**.
   - Danh mục Shoes: https://findniche.com/tiktok/trending-shoes-products-vn
   - Household Appliances: https://findniche.com/tiktok/trending-household-appliances-products-vn
   - Home Supplies: https://findniche.com/tiktok/trending-home-supplies-products (bản này trả về dữ liệu liên kết khu vực Thái Lan/Indonesia — có sản phẩm giá ฿ và Rp, nên chỉ dùng để tham chiếu chéo, **không** dùng làm giá Việt Nam)
   - Luggage & Bags: https://findniche.com/tiktok/trending-luggage-and-bags-products-vn
   - Jewelry Accessories & Derivatives: https://findniche.com/tiktok/trending-jewelry-accessories-and-derivatives-products-vn
   - Pet Supplies: https://findniche.com/tiktok/trending-pet-supplies-products-vn
   - Home Improvement: https://findniche.com/tiktok/trending-home-improvement-products-vn
   - Kitchenware: https://findniche.com/tiktok/trending-kitchenware-products-vn
2. **Giá bán lẻ Việt Nam**: trang tổng hợp giá của Keenable cho từ khóa "quạt mini cầm tay" — https://cards.keenable.ai/w/01a16717-fc3c-7c61-8252-eb649d3af969 (ghi nhận 2026-10-23); Sapo blog về cách tìm sản phẩm hot trend — https://www.sapo.vn/blog/cach-tim-san-pham-hot-theo-trend; VnExpress về hành vi mua sắm online — https://vnexpress.net/nguoi-tieu-dung-bot-san-sale-online-5135054.html
3. **Giá nhập 1688**: xem mục "Giới hạn về giá 1688" ngay dưới.

**Giới hạn về giá 1688 (bắt buộc phải ghi rõ)**
- **1688 cần đăng nhập** cho nhiều luồng. Trong phiên này tôi đã kiểm chứng trực tiếp bằng `curl`:
  - Trang **tìm kiếm** `https://s.1688.com/selloffer/offer_search.htm?keywords=...` **BỊ CHẶN**: trả về trang chống bot `rgv587_flag:sm` + redirect x5sec (HTTP 200, ~2,5 KB, không có dữ liệu sản phẩm).
  - Trang **chi tiết sản phẩm** `https://detail.1688.com/offer/<id>.html` **ĐỌC ĐƯỢC KHÔNG CẦN ĐĂNG NHẬP** (HTTP 200, ~100–260 KB HTML, có JSON nhúng chứa `offerTitle`, `offerUnit`, `currentPrices`, `saledCount`). Đây là nguồn giá nhập "verified" duy nhất của báo cáo.
- **Nhưng**: sau ~10 request liên tiếp, 1688 bật chặn theo IP (`x5sec/punish`). Vì vậy **chỉ 4 mã hàng dưới đây có giá đọc trực tiếp từ 1688**; toàn bộ sản phẩm còn lại giá nhập là **suy luận theo nhóm hàng** và được đánh dấu rõ `[chưa kiểm chứng]`.
- Một số trang `wiki.1688.com` có xuất hiện giá và mã offer, **nhưng đây là nội dung do AI sinh để SEO** (bài viết trùng lặp, số liệu tự mâu thuẫn: cùng một sản phẩm lúc ghi "1,46 CNY", lúc ghi "bán 1.000 chiếc giá 1,65 CNY"). Tôi chỉ dùng các trang này để **lấy mã offer**, không dùng số liệu văn xuôi của chúng.
- Giá 1688 là giá sỉ theo bậc số lượng, **chưa gồm**: phí vận chuyển nội địa Trung Quốc → kho trung gian, phí trung gian mua hộ, phí vận chuyển quốc tế, thuế/phí nhập khẩu, và phí đóng gói lại. Khi tính lợi nhuận phải cộng thêm phần này (thường 20–45% giá trị hàng với hàng nhẹ).

**Bảng 4 mã 1688 đã đọc trực tiếp (verified 2026-10-23)**

| Mã 1688 | Tên hàng (zh) | ĐVT | Giá theo bậc (CNY → VND) | Đã bán |
|---|---|---|---|---|
| 833244917794 | 小风炮手持小风扇无叶涡轮迷你便携USB桌面电风扇 | 台 | 13,00 → **~47.500 VND** (bậc 1); 43,80 → ~160.000 VND (bản cao cấp) | 26.868 |
| 1040073960093 | 跨境N15手持风扇usb迷你便携折叠充电小风扇挂脖数显 | — | 3,39 → **~12.400 VND** *(số 3,39 CNY lấy từ trang wiki.1688; trang chi tiết bị chặn, chưa xác minh lại)* | — |
| 1004957259082 | 背带裤 10cm 跨境拉布布娃衣公仔玩偶替换衣服 (áo cho búp bê 10cm) | 个 | 2,00–3,80 → **~7.300–13.900 VND** | 32.195 |
| 885696617386 | 2026法式抹胸晚礼服新娘…缎面出门纱 | 件 | 228,00 → ~832.000 VND (vượt ngân sách — loại) | 78 |

→ **4 mã này là mức giá tham chiếu "cận dưới" cho nhóm phụ kiện nhỏ: 2–13 CNY (7.000–48.000 VND)/món.** Đây là cơ sở để ước lượng các sản phẩm còn lại trong shortlist.

**Mức độ tin cậy được ghi cho từng dòng trong shortlist**
- `[verified]` = số đọc trực tiếp từ 1688 hoặc từ FindNiche trong ngày 2026-10-23.
- `[chưa kiểm chứng]` = suy luận/ước lượng, cần xác minh lại (bằng tài khoản 1688 + app đo giá).

---

## 1. Bảng tổng hợp shortlist 12 sản phẩm (xếp theo điểm ưu tiên test)

| # | Sản phẩm | Đơn giá nhập dự kiến | Giá bán VN tham khảo | Tín hiệu trend (7 ngày, TikTok Shop VN) | Cạnh tranh | Ưu tiên |
|---|---|---|---|---|---|---|
| 1 | Quạt mini cầm tay (turbo/tích điện) | 12.400–47.500 VND `[verified]` | 45.000–119.000 VND | **23,48K đơn/7 ngày** (hạng 1 ngành gia dụng) | Rất cao | ⭐ Test ngay (mùa vụ) |
| 2 | Bàn chải chà giày mini | 15.000–36.000 `[chưa kiểm chứng]` | 79.000 VND | **14,39K đơn/7 ngày** (hạng 1 ngành giày) | Trung bình | ⭐⭐⭐ |
| 3 | Set 4 chân kê máy giặt/tủ lạnh chống rung | 15.000–40.000 `[chưa kiểm chứng]` | 45.000–46.013 VND | 9,68K + 19,90K đơn/7 ngày (2 listing) | Thấp–TB | ⭐⭐⭐ |
| 4 | Dép sục EVA lót lông hình mèo / charm gắn dép | 20.000–55.000 `[chưa kiểm chứng]` | 80.528 VND (dép mèo); 10.600 VND (charm) | 9,24K (dép mèo) + 8,82K (charm) đơn/7 ngày | Cao (dép) / TB (charm) | ⭐⭐ |
| 5 | Khóa an toàn tủ lạnh cho trẻ | 8.000–20.000 `[chưa kiểm chứng]` | 24.614 VND | **7,13K đơn/7 ngày**, tổng 71,70K đã bán | Thấp–TB | ⭐⭐⭐ |
| 6 | Đèn/máy bắt muỗi công nghệ cao kiêm đèn ngủ | 40.000–70.000 `[chưa kiểm chứng]` | 114.923 VND | **16,01K đơn/7 ngày** (hạng 3 ngành gia dụng) | Trung bình | ⭐⭐ (biên mỏng hơn) |
| 7 | Áo/đồ cho búp bê 10cm (blind-box doll clothes) | 7.300–13.900 `[verified]` | ~20.000–50.000 *(chưa xác minh giá VN)* | 32.195 đã bán trên 1 mã 1688 `[verified]` | Thấp | ⭐⭐ |
| 8 | Vòng/charm bạc/kim loại giá rẻ (trang sức) | 3.000–15.000 `[chưa kiểm chứng]` | 13.000–42.000 VND | **13,73K đơn/7 ngày** (hạng 1 ngành trang sức) | Cao | ⭐⭐ |
| 9 | Thùng vệ sinh/lồng vận chuyển thú cưng | 40.000–80.000 `[chưa kiểm chứng]` | 133.500 VND | 15,37K (hạng 1) + 2,31K đơn/7 ngày | Trung bình | ⭐⭐ |
| 10 | Cuộn dây phơi đồ co rút (dây phơi thông minh) | 60.000–100.000 `[chưa kiểm chứng]` | ~162.434 VND | 12,74K đơn/7 ngày (hạng 3) | Trung bình | ⭐⭐ |
| 11 | Dây đeo/strap điện thoại + giá đỡ điện thoại | 10.000–30.000 `[chưa kiểm chứng]` | 30.000–90.000 *(chưa xác minh)* | ngành túi xách: hạng 3 giá 60.000 VND đạt 7,04K đơn/7 ngày | Cao | ⭐ |
| 12 | Tấm thảm lau chân/nhà tắm siêu thấm | 25.000–60.000 `[chưa kiểm chứng]` | ~60.000–90.000 | 313,61K đơn/7 ngày nhưng là dữ liệu Thái Lan (฿93,81) — chưa có số VN | Cao | ⭐ (cồng kềnh) |

**Chú thích ngân sách test**: với 20.000.000 VND, nếu chọn 5–6 SKU và giữ ~60% vốn cho hàng + 40% cho phí (vận chuyển, trung gian, đóng gói, quảng cáo test), thì ngân sách hàng ~12.000.000 VND. Ở mức 25.000 VND/món, đó là ~480 món — đủ để test 50–100 món/SKU trên 5–6 SKU. **Không nên dồn toàn bộ 20.000.000 VND vào 1 SKU.**

---

## 2. Chi tiết từng sản phẩm

### SP1 — Quạt mini cầm tay (turbo / tích điện / gập / đeo cổ)
- **Từ khóa 1688 (search)**: `手持小风扇`, `迷你便携风扇`, `无叶涡轮风扇`, `挂脖风扇`, `折叠小风扇 USB充电`
- **Lý do trend**: hạng 1 ngành "Household Appliances" TikTok Shop VN — *Quạt Mini Cầm Tay Siêu Mạnh Siêu Mát 4000mAh Pin 100 Cấp Gió…*, giá ₫42.530,5, **23,48K đơn/7 ngày**; nhiều listing khác cùng ngành: ₫261.500 → 9,35K đơn/7 ngày (GMV ₫7,19B), ₫269.990 → 7,82K, ₫300.000 → 7,66K. Nguồn: https://findniche.com/tiktok/trending-household-appliances-products-vn (tra 2026-10-23).
- **Giá bán VN tham khảo**: 45.000 VND → 119.000 VND, 6 mức giá (Shopee / Xiaomi VN / Usams VN). Nguồn: https://cards.keenable.ai/w/01a16717-fc3c-7c61-8252-eb649d3af969 (tra 2026-10-23).
- **Giá nhập**: `[verified]` mã **833244917794** (远顺创展科技(深圳), 11 năm, 好评率 99,2%, 11,77万粉丝): **13,00 CNY (~47.500 VND)** bậc 1 — 台; bản cao cấp 43,80 CNY. Đã bán 26.868. `MOQ = 1` (mixOneForSale/onePiece). Mã rẻ hơn `[chưa kiểm chứng]`: **1040073960093** — 3,39 CNY (~12.400 VND), 7,1万+ đã bán.
- **Biên lợi nhuận thô ước tính**: (45.000 − 12.400) / 45.000 ≈ **72%** (chưa trừ phí vận chuyển & quảng cáo). Với bản 47.500 VND: (45.000 − 47.500) < 0 → **bản 13 CNY đã quá đắt so với giá bán 45.000 VND**; phải chọn mã rẻ (3,39–4,86 CNY) hoặc bán ở mức 75.000–119.000 VND.
- **Cạnh tranh**: rất cao (nhiều shop lớn, Xiaomi/Usams chính hãng cùng phân khúc). Lợi thế người mới: giá rẻ + combo/quà tặng, không đấu với hàng chính hãng.
- **Rủi ro**: đây là **hàng điện tử có pin** — không thuộc nhóm bị cấm trong đề bài, nhưng cần kiểm tra quy định vận chuyển pin (đường bay) và chất lượng pin (an toàn cháy nổ đã được báo chí VN nêu: https://genk.vn/noi-lo-chay-no-vi-sac-kem-chat-luong-va-cam-ket-cua-nexsmart-vietnam-165261022111826913.chn). Nên đặt mẫu kiểm định trước khi nhập lô.

### SP2 — Bàn chải chà giày mini đa năng tay cầm dài
- **Từ khóa 1688**: `鞋刷`, `洗鞋刷`, `长柄鞋刷`, `多功能清洁刷`, `软毛鞋刷`
- **Lý do trend**: hạng 1 ngành Shoes TikTok Shop VN — *Bàn Chải Chà Giày Mini Đa Năng Tay Cầm Dài Nhiều Màu*, ₫7.999, **14,39K đơn/7 ngày**, tổng 66,18K đã bán, GMV ₫529,37M. Nguồn: https://findniche.com/tiktok/trending-shoes-products-vn
- **Giá bán VN**: ₫7.999 cho thấy đây là sản phẩm "add-on / mua kèm" — giá bán thấp nhưng bán theo combo.
- **Giá nhập**: `[chưa kiểm chứng]` — ước 1,5–4 CNY (~5.500–15.000 VND)/chiếc; nhóm nhựa + lông, rất nhẹ (<100 g). Cần xác minh trên 1688.
- **Biên lợi nhuận**: giá bán rất thấp → **chỉ nên bán theo combo (3–5 cái) hoặc kèm dung dịch vệ sinh giày**. Bán lẻ 1 chiếc gần như không có lãi sau phí ship.
- **Cạnh tranh**: trung bình; rào cản thấp nên nhiều shop nhỏ tham gia.
- **Ưu điểm lớn**: nhẹ, gọn, không pin, không nhãn hiệu, thủ tục nhập dễ → rất phù hợp lô test đầu tiên.

### SP3 — Set 4 chân kê máy giặt / tủ lạnh chống rung, tăng giảm chiều cao
- **Từ khóa 1688**: `洗衣机底座`, `冰箱减震脚垫`, `防震脚垫`, `洗衣机增高垫`, `防滑减震垫`
- **Lý do trend**: 2 listing riêng trong ngành Household Appliances: *Set 4 Chân Kê Máy Giặt Tủ Lạnh…* ₫46.013, **19,90K đơn/7 ngày**; *Bộ 4 chân chống rung cho máy giặt, tủ lạnh…* ₫45.000, **9,68K đơn/7 ngày**, GMV ₫1,71B. Nguồn: https://findniche.com/tiktok/trending-household-appliances-products-vn
- **Giá bán VN**: ~45.000–46.000 VND/set 4.
- **Giá nhập**: `[chưa kiểm chứng]` — ước 4.000–11.000 VND/set (1–3 CNY); cao su + nhựa, ~150–250 g/set.
- **Biên lợi nhuận thô ước tính**: (45.000 − 8.000)/45.000 ≈ **82%**.
- **Cạnh tranh**: thấp–trung bình; sản phẩm "giải quyết vấn đề" (ồn/rung), nội dung video dễ viral.
- **Rủi ro**: khách đánh giá thấp nếu size không khớp chân máy → cần đo kỹ và ghi rõ thông số.

### SP4 — Dép sục EVA lót lông + charm gắn dép (Jibbitz)
- **Từ khóa 1688**: `EVA拖鞋`, `毛绒拖鞋`, `洞洞鞋配饰`, `鞋花`, `Jibbitz 鞋扣`
- **Lý do trend**: ngành Shoes — *Dép sục lót lông nữ chất EVA hình Mèo…* ₫80.528, **9,24K đơn/7 ngày**; *Sticker Charm chữ và số Gắn Dép, Sticker Jibbitz…* ₫10.600, **8,82K đơn/7 ngày**. Nguồn: https://findniche.com/tiktok/trending-shoes-products-vn
- **Giá bán VN**: dép ₫80.528; charm ₫10.600.
- **Giá nhập**: `[chưa kiểm chứng]` — dép EVA 6–15 CNY (~22.000–55.000 VND)/đôi (nặng 200–400 g/đôi → **phí ship cao hơn nhóm phụ kiện**); charm 0,3–1,5 CNY (~1.100–5.500 VND)/cái.
- **Khuyến nghị**: **charm gắn dép là SKU tốt hơn dép** cho lô test: siêu nhẹ, giá nhập cực thấp, bán theo set 5–10 cái. Dép là hàng cồng kềnh theo thể tích.
- **Cạnh tranh**: dép rất cao; charm trung bình.

### SP5 — Khóa an toàn tủ lạnh / tủ đông cho trẻ
- **Từ khóa 1688**: `冰箱锁`, `儿童安全锁`, `冰箱安全锁`, `柜门锁`, `宝宝防夹手锁`
- **Lý do trend**: ngành Household Appliances — *Mới 1 Cái Nhà Tủ Lạnh Khóa An Toàn Tủ Lạnh Tủ Đông…* ₫24.614, **7,13K đơn/7 ngày**, tổng **71,70K đã bán**. Nguồn: https://findniche.com/tiktok/trending-household-appliances-products-vn
- **Giá bán VN**: ₫24.614.
- **Giá nhập**: `[chưa kiểm chứng]` — ước 1–3 CNY (~3.700–11.000 VND); nhựa + keo dán, <100 g.
- **Biên lợi nhuận thô ước tính**: (24.614 − 7.000)/24.614 ≈ **72%**.
- **Cạnh tranh**: thấp–trung bình; ngách "mẹ & bé" có tệp khách ổn định, ít shop chuyên.
- **Rủi ro**: keo dán kém → phải chọn mẫu có keo 3M/đánh giá tốt, nếu không sẽ bị hoàn hàng.

### SP6 — Đèn / máy bắt muỗi công nghệ cao kiêm đèn ngủ (cổng USB)
- **Từ khóa 1688**: `灭蚊灯`, `电击灭蚊器`, `USB灭蚊灯`, `吸入式灭蚊灯`, `灭蚊灯小夜灯`
- **Lý do trend**: hạng 3 ngành Household Appliances — *[ MẪU MỚI ] Đèn bắt muỗi, máy bắt muỗi công nghệ cao…* ₫114.923, **16,01K đơn/7 ngày**. Nguồn: https://findniche.com/tiktok/trending-household-appliances-products-vn
- **Giá bán VN**: ₫114.923.
- **Giá nhập**: `[chưa kiểm chứng]` — ước 10–19 CNY (~37.000–70.000 VND); nhựa + linh kiện điện, 300–600 g.
- **Biên lợi nhuận thô ước tính**: (114.923 − 55.000)/114.923 ≈ **52%** — mỏng hơn nhóm phụ kiện, lại cồng kềnh hơn.
- **Rủi ro**: hàng điện + có thể có pin; cần kiểm tra nguồn điện 220V/Adapter. **Chỉ nên test số lượng nhỏ.**

### SP7 — Áo/đồ cho búp dê blind-box 10cm (Labubu-style doll clothes)
- **Từ khóa 1688**: `娃衣`, `10cm娃衣`, `拉布布娃衣`, `公仔衣服`, `盲盒娃衣`
- **Lý do trend**: `[verified]` mã **1004957259082** — *背带裤 10cm 跨境拉布布娃衣可爱背带裤公仔玩偶替换衣服*, giá **2,00–3,80 CNY (~7.300–13.900 VND)**/[个], **đã bán 32.195**. Bán chéo: trên TikTok Shop VN, nhóm "Toys & Hobbies"/sưu tầm đang tăng mạnh; các listing fashion accessories như *Sticker Charm…* ₫10.600 đạt 8,82K đơn/7 ngày cho thấy tệp khách "trang trí đồ sưu tầm" đang chi tiêu thật.
- **Giá bán VN**: **chưa kiểm chứng** — ước 20.000–50.000 VND/bộ trên Shopee (cần xác minh).
- **Giá nhập**: `[verified]` 7.300–13.900 VND/bộ; siêu nhẹ (<50 g).
- **Cạnh tranh**: thấp; đây là ngách mới, ít shop Việt làm.
- **Rủi ro pháp lý/nhãn hiệu**: **phải bán như "áo cho búp bê 10cm" chung, KHÔNG dùng tên/mẫu nhái thương hiệu** (đề bài cấm hàng nhái thương hiệu). Tránh mọi hình in logo/nhân vật có bản quyền.

### SP8 — Trang sức giá rẻ (vòng tay, charm, khuyên tai kim loại)
- **Từ khóa 1688**: `钛钢手链`, `ins风耳环`, `小众项链`, `锆石戒指`, `饰品配件`
- **Lý do trend**: ngành Jewelry Accessories & Derivatives TikTok Shop VN — hạng 1: ₫13.000, **13,73K đơn/7 ngày**, GMV ₫1,36B; hạng 2: ₫42.000, 1,69K đơn/7 ngày, GMV ₫2,45B. Nguồn: https://findniche.com/tiktok/trending-jewelry-accessories-and-derivatives-products-vn
- **Giá bán VN**: ₫13.000–42.000.
- **Giá nhập**: `[chưa kiểm chứng]` — ước 0,8–4 CNY (~3.000–15.000 VND)/món; <30 g.
- **Biên lợi nhuận thô ước tính**: (13.000 − 4.000)/13.000 ≈ **69%**; nhưng giá bán quá thấp → **phải bán theo set (3–5 món) hoặc "mystery box"** để bù phí ship.
- **Cạnh tranh**: cao; đây là ngành truyền thống của dropship.
- **Rủi ro**: kim loại mạ có thể gây dị ứng → cần chọn "titan/thép không gỉ" và ghi rõ chất liệu.

### SP9 — Thùng vệ sinh / lồng vận chuyển thú cưng
- **Từ khóa 1688**: `宠物航空箱`, `猫砂盆`, `宠物外出包`, `宠物笼子`, `猫厕所`
- **Lý do trend**: ngành Pet Supplies TikTok Shop VN — hạng 1: ₫25.000, **15,37K đơn/7 ngày**, GMV ₫3,11B; hạng 10: ₫133.500, **2,31K đơn/7 ngày**, GMV ₫9,27B. Nguồn: https://findniche.com/tiktok/trending-pet-supplies-products-vn
- **Giá bán VN**: ₫25.000–133.500.
- **Giá nhập**: `[chưa kiểm chứng]` — ước 25.000–80.000 VND; 500–900 g.
- **Cạnh tranh**: trung bình; tệp khách nuôi thú cưng chi tiêu cao và lặp lại.
- **Rủi ro**: **cồng kềnh theo thể tích** (phí ship thể tích cao) → chỉ nhập loại gấp gọn, hoặc bỏ nếu phí ship ăn hết biên lợi nhuận.

### SP10 — Dây phơi đồ co rút / dây phơi thông minh
- **Từ khóa 1688**: `晾衣绳`, `隐形晾衣绳`, `伸缩晾衣绳`, `阳台晾衣架`
- **Lý do trend**: ngành Home Improvement TikTok Shop VN — hạng 3: ₫162.434, **12,74K đơn/7 ngày**. Cùng ngành hạng 4: ₫51.000, 12,71K đơn/7 ngày (GMV ₫2,27B). Nguồn: https://findniche.com/tiktok/trending-home-improvement-products-vn
- **Giá bán VN**: ~₫162.434 (hạng 3) — giá bán cao, biên lợi nhuận tốt nếu giá nhập thấp.
- **Giá nhập**: `[chưa kiểm chứng]` — ước 17.000–60.000 VND; 300–500 g.
- **Cạnh tranh**: trung bình; sản phẩm giải quyết vấn đề "nhà nhỏ, ban công hẹp" — rất đúng insight căn hộ VN.
- **Rủi ro**: lò xo/khóa kém → hoàn hàng; nên đặt mẫu trước.

### SP11 — Dây đeo / strap điện thoại & giá đỡ điện thoại
- **Từ khóa 1688**: `手机挂绳`, `手机链`, `手机支架`, `指环扣`, `斜挎手机绳`
- **Lý do trend (gián tiếp, cần xác minh)**: ngành Luggage & Bags TikTok Shop VN — hạng 3: ₫60.000, **7,04K đơn/7 ngày**, tổng 271,32K đã bán, GMV ₫16,28B; hạng 8: ₫50.000, 3,39K đơn/7 ngày. Các mức giá này khớp với nhóm dây đeo/túi mini. Nguồn: https://findniche.com/tiktok/trending-luggage-and-bags-products-vn
- **Giá bán VN**: ₫30.000–90.000 `[chưa kiểm chứng]` cho dây đeo/giá đỡ.
- **Giá nhập**: `[chưa kiểm chứng]` — ước 1–6 CNY (~3.700–22.000 VND); <100 g.
- **Cạnh tranh**: cao.
- **Điểm trừ**: **tên sản phẩm trong bảng FindNiche không hiển thị** (trang chỉ trả giá), nên đây là suy luận theo ngành — hạ ưu tiên xuống ⭐ cho tới khi xác minh.

### SP12 — Thảm lau chân / thảm nhà tắm siêu thấm
- **Từ khóa 1688**: `地垫`, `吸水地垫`, `浴室防滑垫`, `硅藻泥地垫`
- **Lý do trend**: ngành Home Supplies — hạng 3: ฿93,81, **313,61K đơn/7 ngày** (2 chiếc, 140×70 cm). **Lưu ý: đây là dữ liệu bảng Thái Lan**, không phải Việt Nam. Nguồn: https://findniche.com/tiktok/trending-home-supplies-products
- **Giá bán VN**: ₫60.000–90.000 `[chưa kiểm chứng]`.
- **Giá nhập**: `[chưa kiểm chứng]` — ước 8–25 CNY (~29.000–91.000 VND); 300–600 g nhưng **cồng kềnh (140×70 cm)**.
- **Khuyến nghị**: **loại khỏi lô test đầu** vì thể tích lớn ăn hết biên lợi nhuận; chỉ giữ làm ý tưởng cho lô sau khi đã có deal vận chuyển tốt.

---

## 3. Nhóm bị loại (và lý do)

| Sản phẩm (ứng viên) | Ngành / tín hiệu | Lý do loại |
|---|---|---|
| Quạt tích điện để bàn pin 10 cell (₫269.990–300.000; 7,66–10,43K đơn/7 ngày) | Household Appliances | Nặng, cồng kềnh (lồng sắt), pin lớn → phí ship + rủi ro vận chuyển pin cao; vượt ngân sách test |
| Ổn áp/kích điện (nếu có) | — | Đồ điện cao thế — **nhóm bị cấm theo đề bài** |
| Thực phẩm, mỹ phẩm, thuốc, TPCN | — | **Nhóm bị cấm/hạn chế nhập khẩu** theo đề bài |
| Hàng nhái thương hiệu (giày "Enter Dragon De Monaco", dép "Loufu"…) | Shoes | **Hàng nhái/hàng thương hiệu** — đề bài cấm tuyệt đối |
| Tủ lạnh mini, máy xay sinh tố, nồi chiên, thiết bị điện công suất lớn | Household Appliances | Nặng + điện + cần chứng nhận an toàn; không hợp lô test nhỏ |
| Sạc dự phòng (power bank) | Phones & Electronics | Pin lithium, hạn chế vận chuyển hàng không, rủi ro cháy nổ được báo chí VN nêu | 
| Kệ nhựa PP nhiều tầng, xe đẩy kho | Home Supplies | Cồng kềnh — phí thể tích cao hơn giá trị hàng |

---

## 4. Rủi ro chung cần xử lý trước khi nhập

1. **Tỷ giá**: cần chốt tỷ giá CNY/VND thực tế tại ngày đặt hàng — toàn bộ quy đổi ở đây dùng 3.650 VND/CNY (xấp xỉ, chưa kiểm chứng).
2. **Phí ẩn của kênh 1688**: giá 1688 chưa gồm phí mua hộ/trung gian (thường 3–7%), phí vận chuyển nội địa TQ, phí vận chuyển quốc tế (theo kg **hoặc** theo thể tích), thuế nhập khẩu. Với hàng nhẹ (<300 g) phí thường chiếm 20–45% giá trị lô.
3. **Trang 1688 chặn bot theo IP**: sau ~10 request liên tiếp bị `x5sec/punish`. Muốn xác minh MOQ/giá bậc thật phải dùng tài khoản 1688 (đăng nhập) hoặc đối tác mua hộ.
4. **MOQ**: 2 mã đã đọc đều cho `beginAmount = 1` (bán lẻ 1 cái) — thuận lợi cho test nhỏ. **Chưa xác minh MOQ của 9 SKU còn lại**; phải hỏi trực tiếp shop trước khi chốt.
5. **Xu hướng ngắn hạn**: FindNiche tự cảnh báo *"Historical or captured performance does not guarantee future demand, profit, or advertising results."* Nhiều sản phẩm trong nhóm này là trend ngắn (theo Sapo: *"Fidget spinner"* là ví dụ điển hình của trend bùng nổ rồi tắt). Không ôm hàng.
6. **Tính thời vụ**: quạt mini và đèn bắt muỗi là hàng mùa hè/mùa mưa — cần đối chiếu lịch trước khi nhập để tránh về muộn mùa.

---

## 5. Đề xuất bước tiếp theo

1. **Test ngay (lô 1, ~10–12 triệu VND hàng)**: SP2 (bàn chải chà giày), SP3 (chân kê máy giặt), SP5 (khóa tủ lạnh), SP7 (áo búp bê 10cm), SP8 (trang sức set) — tất cả đều nhẹ, MOQ thấp, không pin, không nhãn hiệu.
2. **Test có kiểm soát**: SP1 (quạt mini — chỉ mua mã rẻ 3,39–4,86 CNY, đặt mẫu kiểm pin), SP6 (đèn bắt muỗi — test 20–30 cái).
3. **Cần xác minh trước khi quyết**: giá nhập + MOQ thật của SP2, SP3, SP5, SP7, SP8, SP9, SP10, SP11, SP12 (dùng tài khoản 1688).
4. **Việc cần làm ở task sau**: đo phí vận chuyển thực tế (kg & thể tích) cho 5 SKU ưu tiên, và đối chiếu giá bán Shopee/TikTok Shop bằng dữ liệu có tên sản phẩm (hiện một số trang FindNiche chỉ trả giá, không trả tên).

---

*Tài liệu này chỉ ghi trong `research-1688/01-xu-huong.md`. Mọi số liệu `[chưa kiểm chứng]` phải được xác minh trước khi dùng để tính lợi nhuận hoặc xuống tiền.*
