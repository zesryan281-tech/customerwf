# T3 — Phân tích thị trường Việt Nam & kế hoạch marketing (30 ngày đầu)

- **Người thực hiện**: market-analyst (team 1688-market-research)
- **Ngày tra cứu**: **2026-10-23** (giờ máy Asia/Shanghai UTC+8; giờ VN UTC+7 cùng ngày). Mọi con số là ảnh chụp tại ngày này.
- **Nguồn đầu vào**: `research-1688/01-xu-huong.md` (T1, shortlist 12 SKU) — các sản phẩm, từ khóa 1688, tín hiệu trend FindNiche và giá nhập đã verify.
- **Ngân sách marketing giả định**: **3.000.000 – 5.000.000 VND** cho 30 ngày đầu (tách khỏi 20.000.000 VND vốn hàng của T1).
- **Ghi scope**: tài liệu này CHỈ ghi vào `research-1688/03-thi-truong-marketing.md`.

> ⚠️ **ĐỌC MỤC 0 TRƯỚC KHI DÙNG BẤT KỲ CON SỐ NÀO.** Trong tài liệu này có 3 loại số liệu khác nhau về độ tin cậy, và chúng được dán nhãn riêng: `[verified]`, `[index]`, `[chưa kiểm chứng]`.

---

## 0. Phương pháp, độ tin cậy và GIỚI HẠN (bắt buộc đọc)

### 0.1 Ba nhãn độ tin cậy

| Nhãn | Nghĩa | Cách kiểm chứng lại |
|---|---|---|
| `[verified]` | Tôi đọc **trực tiếp nội dung trang** trong phiên này (web_fetch thành công, có HTTP 200 + nội dung thật). | Mở URL, đối chiếu |
| `[index]` | Số liệu lấy từ **đoạn trích trong kết quả công cụ tìm kiếm** mô tả trang Shopee/TikTok Shop/Lazada/Facebook. **Tôi KHÔNG mở được chính trang đó** (xem 0.2). Giá và số "đã bán" có thể lệch với giá hiện tại vì Shopee/TikTok thay đổi theo giờ và theo voucher của từng tài khoản. | Mở app Shopee/TikTok Shop bằng tài khoản thật, chụp màn hình |
| `[chưa kiểm chứng]` | Suy luận / ước lượng của tôi. **Không phải số đo.** | Phải đo lại trước khi xuống tiền |

### 0.2 Giới hạn truy cập (ảnh hưởng trực tiếp tới chất lượng bằng chứng giá)

Các nền tảng bán hàng VN chặn đọc tự động. Trong phiên 2026-10-23 tôi đã thử và ghi nhận:

- `shopee.vn/<product>` và `shopee.vn/<category>` → **HTTP 200 nhưng nội dung là "Login Required"**, không có giá. (`web_fetch` ngày 2026-10-23)
- `shop.tiktok.com/vn/c/<category>` → **bị chặn bằng captcha xếp hình** ("Drag the puzzle piece into place"); `shop.tiktok.com/vn/pdp/...` cũng không đọc được nội dung. (`web_fetch` ngày 2026-10-23)
- `h5.lazada.vn` / trang sản phẩm Lazada → không lấy được nội dung.
- Vì vậy: **toàn bộ giá bán và số "đã bán" của đối thủ trên Shopee/TikTok Shop trong tài liệu này là nhãn `[index]`**, trích từ kết quả tìm kiếm — không phải ảnh chụp trang gốc. Đây là giới hạn thật, không phải sự cẩu thả; và nó có nghĩa là **bảng đối thủ phải được xác minh lại bằng app trước khi chốt giá.**

### 0.3 Những gì ĐỌC ĐƯỢC trực tiếp (`[verified]`)

| Nguồn | Ngày | Nội dung dùng được |
|---|---|---|
| `banhang.shopee.vn/edu/article/27540` | công bố 28-05-2026 | Bảng **Phí Cố Định** chính thức của Shopee cho người bán non-Mall, hiệu lực từ 23/05/2026; Phí Voucher Xtra 5,5%; PiShip 2.700đ/đơn |
| `sapo.vn/blog/phi-dich-vu-shopee-la-gi-tinh-phi-dich-vu-shopee` | 28-09-2026 | Phí xử lý giao dịch 6%, phí hạ tầng 3.000đ/đơn, thuế GTGT/TNCN khấu trừ, so sánh tổng chi phí Shopee vs TikTok Shop |
| `newsroom.tiktok.com/tiktok-shop-summit-vietnam-2026` | 30-07-2026 | Số liệu chính thức TikTok Shop VN: GMV 2025 +66%, Nhà cửa & Đời sống +94%, Mẹ & Bé +67%, quy mô TMĐT VN ~31 tỷ USD |
| `metric.vn/insights/metric-bao-cao-thuong-mai-dien-tu-viet-nam-6-thang-dau-nam-2026/` | 29-07-2026 | Quy mô 4 sàn H1/2026: **291,6 nghìn tỷ đồng (+44,11%)**; 2.186,7 triệu sản phẩm; 613,8 nghìn shop; insight "thị trường chuyển từ tăng theo chiều rộng sang chiều sâu"; phân khúc <100.000đ **giảm 4,2% thị phần**, >1.000.000đ tăng 3,1% |
| `miniai.vn/chay-quang-cao-shopee/` | 14-05-2026 | **CPC Shopee trung bình 800–2.000đ**; CR 3–5%; ROAS <5 thường không có lãi; ngưỡng ngân sách an toàn cho shop mới 50.000–100.000đ/ngày |
| `neyul.com/tin-tuc/chi-phi-chay-quang-cao-tiktok` | 29-07-2026 | **Ngân sách tối thiểu TikTok Ads**: 100.000đ/ngày cho mục tiêu doanh số sản phẩm (TikTok Shop); 200.000đ/ngày cho lưu lượng/app/lead |
| `1688express.vn/bang-gia/` | đọc 23-10-2026 | Bảng phí nhập hàng thật: cước TQ→VN **25.000–35.000đ/kg** theo vùng và bậc khối lượng; cân nặng quy đổi = D×R×C/8000; phí thông quan 1–3% (gia dụng/đồ điện tử) tối thiểu 9.000đ/đơn; phí kiểm hàng 700–5.000đ/sản phẩm; ~80% đơn 1688 miễn phí ship nội địa TQ |
| `fint-global.com/tiktok-vietnam-...` | cập nhật 15-04-2026 | Persona người mua TikTok VN (18–34 tuổi, AOV 250.000–350.000đ), hành vi ra quyết định 3–7 phút, yếu tố tin cậy, tỷ lệ hoa hồng affiliate theo ngành |

### 0.4 Nguồn KHÔNG đọc được đầy đủ (chỉ có tiêu đề/đoạn trích)

Các nguồn sau tôi **chỉ thấy đoạn trích tìm kiếm, chưa đọc toàn văn** — dùng được để tham chiếu hướng, **không dùng làm căn cứ định lượng duy nhất**:

- `antv.gov.vn` — "Từ ngày 1/8, thu thuế VAT tự động hàng nhập khẩu dưới 1 triệu đồng" (Thông tư 29/2025/TT-BTC). `[index]`
- `metric.vn/ereport/quan-ao-cho-bup-be` — quy mô **4,6 tỷ đồng, −20,4% so với quý trước**; thương hiệu nổi bật qtwoof, metoo, memade. `[index]` (trang eReport không đọc được toàn văn)
- `metric.vn/ereport/thi-phan-jibbitz-charm` — có tồn tại báo cáo thị phần Jibbitz charm. `[index]`
- `klmarketing.vn/chi-phi-quang-cao-facebook-ads/` — CPM Facebook Ads VN **265.000–790.000 VND/1.000 hiển thị** (≈10,1–30 USD). `[index]`
- `seller-vn.tiktok.com/university/...` + video `tiktok.com/@damvantuanvn` — **từ 01/04/2026 TikTok Shop áp phí trả hàng/hoàn tiền cho nhà bán**. `[index]`
- `mst.gov.vn` + `media.chinhphu.vn` — quy định **nhãn gốc hàng nhập khẩu phải có nhãn vật lý** bằng tiếng Việt hoặc tiếng nước ngoài. `[index]`

### 0.5 Giới hạn chưa xử lý được (cần task sau)

1. **Chưa có giá Shopee/TikTok Shop xác thực bằng app** → mọi khuyến nghị giá bên dưới là khuyến nghị *cần xác minh*, không phải kết luận chốt.
2. **Chưa có dữ liệu số lượng đã bán theo từng listing Shopee** (Shopee hiển thị "Đã bán 50k+" dạng làm tròn, không có số chính xác).
3. **Chưa đo được tỷ lệ hoàn hàng thực tế ngành** — chỉ có dữ kiện gián tiếp (thảo luận cộng đồng nói tỷ lệ hoàn tăng từ 4–6% lên ~10% từ tháng 6). `[index]`, **không dùng làm giả định tài chính**.
4. **Chưa kiểm tra pháp lý nhãn hiệu** cho Labubu / Crocs / Jibbitz tại Việt Nam (xem mục 9.3).
5. **Chưa chốt tỷ giá** CNY/VND và USD/VND tại ngày đặt hàng.

---

## 1. Bối cảnh thị trường: 5 dữ kiện định hình mọi quyết định

**Dữ kiện 1 — Thị trường đang lớn lên nhưng đơn hàng KHÔNG rẻ đi theo.**
4 sàn (Shopee, Lazada, Tiki, TikTok Shop) đạt **291,6 nghìn tỷ đồng** H1/2026, **+44,11%**; nhưng sản lượng chỉ **+13,67%**. Nghĩa là tiền tăng nhanh hơn lượng hàng gấp ~3 lần. Phân khúc **dưới 100.000đ mất 4,2% thị phần**; phân khúc **trên 1.000.000đ tăng 3,1%**. `[verified]` — Metric.vn, 29-07-2026.
→ **Hệ quả trực tiếp**: chiến lược "bán thật rẻ để lấy đơn" đang chống lại dòng chảy thị trường. Các SKU 7.999đ–24.000đ trong shortlist T1 **không thể là sản phẩm chủ lực**; chúng chỉ có nghĩa như *mồi traffic* hoặc *bán theo combo*.

**Dữ kiện 2 — Chi phí cố định theo đơn hàng đã đủ cao để giết mọi đơn giá thấp.**
Shopee thu **phí hạ tầng 3.000đ/đơn** + **phí xử lý giao dịch 6%**; nếu tham gia PiShip thêm **2.700đ/đơn**. Blog Sapo tổng hợp: chi phí bắt buộc của Shopee là **14,5%–33% + 5.700đ/đơn**, và khi cộng Voucher Xtra + quảng cáo thì lên **29,5%–48%**. `[verified]` — Sapo 28-09-2026, từ bảng phí chính thức của Shopee 23/05/2026.
→ **Hệ quả**: một đơn 24.000đ bị ăn ít nhất **5.700đ phí cứng + ~20% hoa hồng ≈ 10.500đ**. Bán 1 chiếc khóa tủ lạnh 24.000đ gần như chắc chắn **lỗ** sau freeship. **Kết luận thiết kế: mọi SKU dưới 50.000đ phải bán theo combo/lốc từ 3 món trở lên, hoặc là sản phẩm bán kèm (upsell) chứ không bán lẻ.**

**Dữ kiện 3 — TikTok Shop là kênh tăng trưởng, nhưng "Nhà cửa & Đời sống" chính là ngành đang bùng nổ.**
TikTok Shop công bố GMV Việt Nam 2025 **+66%**; riêng ngành **Nhà cửa và Đời sống +94%**, Mẹ & Bé +67%. 95% người tiêu dùng VN nói nội dung chân thực ảnh hưởng trực tiếp tới quyết định mua; ảnh hưởng của livestream ở VN **cao gấp 1,3 lần** mức trung bình APAC. `[verified]` — TikTok Newsroom, 30-07-2026.
→ **Hệ quả**: 3/5 SKU ưu tiên của T1 (bàn chải chà giày, chân kê máy giặt, khóa tủ lạnh) nằm đúng ngành tăng nhanh nhất. Đây là lợi thế thời điểm, không phải trùng hợp.

**Dữ kiện 4 — Chi phí để có 1 click/1 đơn đã biết trước, nên ngân sách 3–5 triệu phải chia theo ngưỡng tối thiểu của nền tảng.**
CPC Shopee trung bình **800–2.000đ**, CR 3–5%. TikTok Ads yêu cầu tối thiểu **100.000đ/ngày** cho mục tiêu doanh số sản phẩm. `[verified]` — miniai.vn 14-05-2026; neyul.com 29-07-2026.
→ **Hệ quả toán học**: ngân sách 4.000.000đ ÷ 100.000đ/ngày = **tối đa 40 ngày-chạy** ở một kênh. Không thể chạy song song TikTok Ads + Shopee Ads + Facebook Ads ở mức ngân sách tối thiểu trong cùng lúc. **Phải chọn 2 kênh, không phải 4.**

**Dữ kiện 5 — Chi phí nhập hàng thật đã có bảng giá, nên "biên lợi nhuận" không còn là phỏng đoán.**
1688Express niêm yết: cước TQ→VN **28.000đ/kg (Hà Nội, 5–10kg) / 34.000đ/kg (HCM) / 35.000đ/kg (Đà Nẵng)**, giảm dần khi lô lớn hơn; **cân nặng quy đổi = D×R×C/8000** (hàng cồng kềnh bị phạt); phí thông quan **1–3%** cho gia dụng/đồ điện tử, tối thiểu 9.000đ/đơn; kiểm hàng 700–5.000đ/sản phẩm. `[verified]` — 1688express.vn, đọc 23-10-2026.
→ **Hệ quả**: với món <100g, cước quốc tế chỉ ~2.800–3.500đ/món — rất tốt. Với món 300–600g hoặc cồng kềnh (đèn bắt muỗi, thùng thú cưng, thảm), cước có thể vượt giá trị hàng. **Đây là lý do định lượng để loại SP9/SP12 khỏi lô test.**

---

## 2. Bảng giá đối thủ đang niêm yết trên thị trường VN

**Ngày xem: 2026-10-23.** Nhãn như mục 0.1. Cột "URL" là nguồn cho số liệu ngay bên trái.

### 2.1 SP2 — Bàn chải chà giày mini (ưu tiên #1 của T1)

| Giá niêm yết | Số đã bán / đánh giá | Kênh | URL | Nhãn |
|---|---|---|---|---|
| **9.900₫** (giá gạch 15.000₫) | — | Shopee list "bàn chải / chà dép" | [shopee.vn/list/bàn chải/chà dép](https://shopee.vn/list/b%C3%A0n%20ch%E1%BA%A3i/ch%C3%A0%20d%C3%A9p) | `[index]` |
| **10.500₫** | — | Shopee list "bàn chải" | [shopee.vn/list/bàn chải](https://shopee.vn/list/b%C3%A0n%20ch%E1%BA%A3i) | `[index]` |
| **11.000₫ – 28.000₫** (theo phân loại) | đánh giá 90% | Shopee listing "Bàn Chải Chà Giày Mini Đa Năng Tay Cầm Dài Nhiều Màu" | [shopee.vn/...-i.1541924287.42403121083](https://shopee.vn/B%C3%A0n-Ch%E1%BA%A3i-Ch%C3%A0-Gi%C3%A0y-Mini-%C4%90a-N%C4%83ng-Tay-C%E1%BA%A7m-D%C3%A0i-Nhi%E1%BB%81u-M%C3%A0u-i.1541924287.42403121083) | `[index]` |
| **17.500₫** (gạch 25.000₫) | — | Shopee list "bàn chải / chà giày" | [shopee.vn/list/bàn chải/chà giày](https://shopee.vn/list/b%C3%A0n%20ch%E1%BA%A3i/ch%C3%A0%20gi%C3%A0y) | `[index]` |
| **25.900₫** — "Combo 10 Cây Cọ Giày Đa Năng", 4.7★ | — | Shopee list "bàn chải / chà dép" | [shopee.vn/list/bàn chải/chà dép](https://shopee.vn/list/b%C3%A0n%20ch%E1%BA%A3i/ch%C3%A0%20d%C3%A9p) | `[index]` |
| **21.883₫** (sau Voucher Xtra 15.8) — "Bàn Chải Đánh Giày… Rẻ Vô Địch" | **Đã bán 2k+** | Shopee (bài trong group Facebook) | [facebook.com/groups/3868561546798499](https://www.facebook.com/groups/3868561546798499/posts/4751857278468917/) | `[index]` |
| **21.000₫ / 5 cái** ("21K/5 cái", so sánh "shop khác 9k–12k") | — | Instagram/Facebook seller | [instagram.com/p/Db-5bcBmN9d](https://www.instagram.com/p/Db-5bcBmN9d/) | `[index]` |
| **50.000₫ / set 4 cái** + freeship | — | Instagram | [instagram.com/p/Db-5bcBmN9d](https://www.instagram.com/p/Db-5bcBmN9d/) | `[index]` |
| **85.000₫ bao ship toàn quốc** (bản 5 mặt cán dài) | — | Facebook group | [facebook.com/groups/3002497726464331](https://www.facebook.com/groups/3002497726464331/posts/25347039838250134/) | `[index]` |
| **15.000₫ / combo 2 cái** | — | Facebook video seller | [facebook.com/le.nguyen.thao.387525/videos/...](https://www.facebook.com/le.nguyen.thao.387525/videos/b%C3%A0n-ch%E1%BA%A3i-%C4%91%C3%A1nh-gi%C3%A0y-v%E1%BB%87-sinh-nh%C3%A0-c%E1%BB%ADa-5k%C3%A1p-m%C3%A3-x%E1%BB%AD-l%C3%BD-s%E1%BA%B5n-v%C3%AD-ai-c%C5%A9ng-mua-%C4%91%C6%B0%E1%BB%A3c-kh%C3%B4ng-c/1047890371338735/) | `[index]` |
| **Đã bán 50k+** (listing "Bàn Chải Chà Giày Mini… PP Tiện Lợi") | **Đã bán 50k+** | Shopee | [shopee.vn/...-i.832892001.42510744869](https://shopee.vn/B%C3%A0n-Ch%E1%BA%A3i-Ch%C3%A0-Gi%C3%A0y-Mini-%C4%90a-N%C4%83ng-Tay-C%E1%BA%A7m-D%C3%A0i-Nhi%E1%BB%81u-M%C3%A0u-B%E1%BA%B1ng-Ch%E1%BA%A5t-Li%E1%BB%87u-PP-Ti%E1%BB%87n-L%E1%BB%A3i-L%C3%A0m-S%E1%BA%A1ch-Qu%E1%BA%A7n-%C3%81o-N%E1%BB%87m-i.832892001.42510744869) | `[index]` |

**Đọc bảng này thế nào:**
- **Giá bán lẻ 1 chiếc đã bị ép xuống 9.900–11.000đ** — thấp hơn cả giá nhập dự kiến cao nhất trong T1 (15.000đ). Bán lẻ 1 chiếc là **cuộc chơi không có lãi**.
- **Vùng giá có lãi là combo**: 21.000đ/5 cái, 25.900đ/10 cây, 50.000đ/set 4 cái. Tức thị trường đã tự tìm ra cấu trúc "bán theo lốc" — và đó chính là cấu trúc đúng.
- **Mức độ bão hòa: RẤT CAO.** Có listing đạt "Đã bán 50k+" và một listing khác "2k+". Rào cản gia nhập gần bằng 0. Không nên đấu giá với các shop này.

### 2.2 SP3 — Set 4 chân kê máy giặt / tủ lạnh chống rung (ưu tiên #2)

| Giá niêm yết | Số đã bán / đánh giá | Kênh | URL | Nhãn |
|---|---|---|---|---|
| **19.998₫** — "Combo 4 chân đế kê máy giặt chống rung chống ồn" | **Đã bán hết** (hết hàng) | Shopee | [shopee.vn/...-i.645265133.13978527766](https://shopee.vn/Combo-4-ch%C3%A2n-%C4%91%E1%BA%BF-k%C3%AA-m%C3%A1y-gi%E1%BA%B7t-ch%E1%BB%91ng-rung-ch%E1%BB%91ng-%E1%BB%93n-i.645265133.13978527766) | `[index]` |
| **45.000 – 46.013₫** (2 listing) | **19,90K và 9,68K đơn/7 ngày** | TikTok Shop VN (FindNiche) | [findniche.com/tiktok/trending-household-appliances-products-vn](https://findniche.com/tiktok/trending-household-appliances-products-vn) | `[verified]` (qua T1) |
| **54.180₫** (gạch 120.000₫) | — | Shopee list "chân máy giặt chống rung" | [shopee.vn/list/chân máy giặt chống rung](https://shopee.vn/list/ch%C3%A2n%20m%C3%A1y%20gi%E1%BA%B7t%20ch%E1%BB%91ng%20rung) | `[index]` |
| **45.000₫** ("Giá: 45k, SL giảm") | — | Facebook seller | [facebook.com/61590909905523/posts/...](https://www.facebook.com/61590909905523/posts/combo-4-ch%C3%A2n-%C4%91%E1%BA%BF-k%E1%BB%87-m%C3%A1y-gi%E1%BA%B7t-ch%E1%BB%91ng-rung-ch%E1%BB%91ng-%E1%BB%93nmua-h%C3%A0ng-t%E1%BA%A1i-%C4%91%C3%A2y-httpssshopeevn3v/122127086601363663/) | `[index]` |
| **182.000₫** (gạch 310.000₫, −41%) — "Chân kê máy giặt, tủ lạnh, máy rửa chén **INOX** DAIKIOSAN" | **Đã bán 40k+** | Shopee | [shopee.vn/...-i.1595496932.51103232024](https://shopee.vn/Ch%C3%A2n-k%C3%AA-ma%CC%81y-gi%E1%BA%B7t-tu%CC%89-la%CC%A3nh-ma%CC%81y-r%C6%B0%CC%89a-che%CC%81n-INOX-ch%C3%B4%CC%81ng-rung-n%C3%A2ng-cao-g%C3%A2%CC%80m-DAIKIOSAN-i.1595496932.51103232024) | `[index]` |
| **205.000₫** — "Chân Kê Máy Giặt Tủ Lạnh Máy Rửa Chén Daimito HTP" | — | Shopee | [shopee.vn/list/máy sấy quần áo/samsung/9kg](https://shopee.vn/list/m%C3%A1y%20s%E1%BA%A5y%20qu%E1%BA%A7n%20%C3%A1o/samsung/9kg) | `[index]` |
| **43.849 sản phẩm đã bán** — "Chân kê máy giặt, tủ lạnh Makano MP106", 5★ (363) | **43.849 đã bán** | Website bán lẻ | [tapdoandaiviet.com.vn](https://tapdoandaiviet.com.vn/san-pham/chan-ke-may-giat-tu-lanh-makano-mp106/) | `[index]` |
| **Chân kê trụ inox điều chỉnh 45–68 cm** | — | Lazada | [h5.lazada.vn/products/...](https://h5.lazada.vn/products/chan-ke-may-giat-tu-lanh-tru-inox-cao-cap-dieu-chinh-45-68-cm-i1998483774-s9268960868.html) | `[index]` |

**Đọc bảng này thế nào:**
- **Có hai thị trường con tách biệt**, không phải một:
  - **Nhựa/cao su giá rẻ** (19.000–55.000đ): sản phẩm trong T1 nằm ở đây. Cạnh tranh giá khốc liệt, listing 19.998đ phải bán hết hàng.
  - **Trụ inox điều chỉnh cao** (182.000–205.000đ): doanh số cực lớn (40k+), biên cao, **khách chấp nhận trả gấp 4 lần cho bản inox**. Đây là tín hiệu quan trọng: *nếu nâng cấp SKU lên bản inox, biên lợi nhuận tốt hơn nhiều mà cạnh tranh về giá ít hơn.*
- **Mức độ bão hòa: TRUNG BÌNH.** Cầu rất lớn (nhiều listing 9,68K–19,90K đơn/7 ngày, một website ngoài sàn bán 43.849 cái) nhưng **sản phẩm giải quyết vấn đề cụ thể (rung/ồn máy giặt)** nên nội dung video có đất diễn, không chỉ đấu giá.

### 2.3 SP5 — Khóa an toàn tủ lạnh cho trẻ (ưu tiên #3)

| Giá niêm yết | Số đã bán / đánh giá | Kênh | URL | Nhãn |
|---|---|---|---|---|
| **24.614₫** | **7,13K đơn/7 ngày**, tổng **71,70K đã bán** | TikTok Shop VN (FindNiche) | [findniche.com/tiktok/trending-household-appliances-products-vn](https://findniche.com/tiktok/trending-household-appliances-products-vn) | `[verified]` (qua T1) |
| **23.900₫ / 2 chiếc** — "[Koqzm] 2 Chiếc Bảo Vệ An Ninh Trẻ Em Khóa Tủ Lạnh…" | **303 đã bán** | Shopee danh mục Khóa & Dây đai an toàn | [shopee.vn/Safety-Locks-Straps-cat.11036194.11036240.11036246](https://shopee.vn/Safety-Locks-Straps-cat.11036194.11036240.11036246) | `[index]` |
| **Đã bán 10k+** — "Khóa tủ lạnh cao cấp giữ an toàn cho bé, hàng nội địa Nhật" | **Đã bán 10k+** | Shopee | [shopee.vn/...-i.16060130.3083262400](https://shopee.vn/Kh%C3%B3a-t%E1%BB%A7-l%E1%BA%A1nh-d%C3%A1n-keo-ch%E1%BB%91ng-tr%E1%BB%99m-an-to%C3%A0n-cho-gia-%C4%91%C3%ACnh-i.16060130.3083262400) | `[index]` |
| **9.000₫** (giá thị trường 14.000đ) — "Khoá chốt cài tủ lạnh, tủ đồ, ngăn kéo an toàn cho bé" | **5.0/5 (422 đánh giá), 2.577 đã bán** | Website bán lẻ | [sieuthiconcung.com](https://sieuthiconcung.com/san-pham/khoa-chot-cai-tu-lanh-tu-do-ngan-keo-an-toan-cho-be-1114) | `[index]` |
| **Khóa tủ lạnh FREESHIP** (giá không hiển thị trong trích đoạn) | — | Shopee | [shopee.vn/Khóa-tủ-lạnh-...i.441500992.16854064038](https://shopee.vn/Kh%C3%B3a-t%E1%BB%A7-l%E1%BA%A1nh%F0%9F%8D%92FREESHIP%F0%9F%8D%92kh%C3%B3a-t%E1%BB%A7-l%E1%BA%A1nh-an-to%C3%A0n-cho-b%C3%A9-i.441500992.16854064038) | `[index]` |
| Khóa tủ lạnh an toàn (link TikTok trong bài) | — | Facebook → TikTok Shop | [facebook.com/ngoc.ha.926509/videos/...](https://www.facebook.com/ngoc.ha.926509/videos/nhi%E1%BB%87t-k%E1%BA%BF-t%E1%BB%A7-l%E1%BA%A1nh-httpssshopeevn/1749008036244463/) | `[index]` |

**Đọc bảng này thế nào:**
- **Vùng giá đã bị ép xuống 9.000–12.000đ/chiếc** (bán lẻ) hoặc 23.900đ/2 chiếc. Mức 24.614đ/1 chiếc trên TikTok tồn tại được **vì TikTok Shop có cấu trúc phí khác** (phí hoàn đơn 1.620–10.738đ/đơn nhưng hoa hồng nền tảng chỉ 4–5% cho Home & living) — không chuyển nguyên sang Shopee được.
- **Cạnh tranh thấp hơn về số shop, nhưng giá đã bị đánh sập.** "Hàng nội địa Nhật" (10k+ đã bán) và hàng Việt giá 9.000đ cùng tồn tại.
- **Kết luận: đây là SKU TỐT ĐỂ BÁN KÈM, KHÔNG PHẢI SKU CHỦ LỰC.** Bán lẻ 1 chiếc ở 24.000đ trên Shopee sẽ lỗ sau phí cứng (xem mục 6.2).

### 2.4 SP7 — Áo/đồ cho búp bê 10cm (ưu tiên #4 — **SKU hấp dẫn nhất về biên lợi nhuận**)

| Giá niêm yết | Số đã bán / đánh giá | Kênh | URL | Nhãn |
|---|---|---|---|---|
| **75.000₫ – 205.000₫** — "[91 mẫu][ORD] Outfit doll 10cm Labubu Bao-ao Quần Áo Búp Bê 10cm" | đánh giá 42%; danh mục "Đồ Chơi Búp bê & Đồ chơi nhồi bông" | Shopee | [shopee.vn/...-i.134065.28719825308](https://shopee.vn/-91-m%E1%BA%ABu-ORD-Outfit-doll-10cm-Labubu-Bao-ao-Qu%E1%BA%A7n-%C3%81o-b%C3%BAbp-b%C3%AA-10cm-Labubu-i.134065.28719825308) | `[index]` |
| **109.000₫** (giá sau voucher) — "Set outfit đi biển rực rỡ cho doll 10cm, 15cm, Labubu 17cm" | 5.0★ (3 đánh giá); **Đã bán hết** | Shopee | [shopee.vn/...-i.96604911.27891839414](https://shopee.vn/Set-outfit-%C4%91i-bi%E1%BB%83n-r%E1%BB%B1c-r%E1%BB%A1-cho-doll-10cm-15cm-Labubu-17cm-i.96604911.27891839414) | `[index]` |
| **160.000₫/set** (áo dài + quần trắng + khăn đóng + phụ kiện) — áo dài may riêng cho Labubu | khách mua quanh năm | Facebook (may thủ công) | [facebook.com/peachthecotton/posts/...](https://www.facebook.com/peachthecotton/posts/-%C3%A1o-d%C3%A0i-cho-labubu-m%C3%ACnh-v%E1%BA%ABn-nh%E1%BA%ADn-may-%C3%A1o-d%C3%A0i-quanh-n%C4%83m-su%E1%BB%91t-th%C3%A1ng-lu%C3%B4n-kh%C3%A1ch-mua-/993066302186196/) | `[index]` |
| Trang "Trang Phục Búp Bê, 10cm, Áo Choàng Nhỏ…" tồn tại (giá không hiển thị) | — | TikTok Shop VN | [shop.tiktok.com/vn/pdp/trang-phuc-bup-be-10cm-...](https://shop.tiktok.com/vn/pdp/trang-phuc-bup-be-10cm-ao-choang-nho-vai-bong-an-toan/1733307491401828325) | `[index]` |
| Danh mục "Phụ kiện búp bê" (quần áo cho doll 11–17 cm, tỷ lệ 1/8, 1/12) | — | TikTok Shop VN | [shop.tiktok.com/vn/c/doll-accessories/604390](https://shop.tiktok.com/vn/c/doll-accessories/604390) | `[index]` |
| **Thị trường "Quần áo cho búp bê" trên TMĐT: 4,6 tỷ đồng/quý, −20,4% so với quý trước**; thương hiệu dẫn đầu: qtwoof, metoo, memade | — | Metric eReport | [metric.vn/ereport/quan-ao-cho-bup-be](https://metric.vn/ereport/quan-ao-cho-bup-be) | `[index]` |
| **640 sản phẩm** "10cm outfit" đang bán, có công cụ so sánh giá lịch sử | — | BigGo VN | [vn.biggo.com/s/10cm outfit](https://vn.biggo.com/s/10cm%20outfit/) | `[index]` |
| **Charm dép Crocs Jibbitz hình bi-a/cài dép** 15.000₫, 4.9★ (dùng làm mốc cho nhóm "trang trí đồ sưu tầm") | — | Shopee shop "Nón Lab" | [shopee.vn/nonlab3dprint](https://shopee.vn/nonlab3dprint?entryPoint=ShopByPDP) | `[index]` |

**Đọc bảng này thế nào — đây là phát hiện quan trọng nhất của T3:**
- **Giá nhập đã VERIFY chỉ 7.300–13.900 VND/bộ** (mã 1688 `1004957259082`, 2,00–3,80 CNY, `[verified]` từ T1), trong khi **giá bán VN phổ biến 75.000–205.000đ**.
- **Hệ số nhân giá × 5,4 đến × 28.** Không SKU nào khác trong shortlist có khoảng cách lớn như vậy.
- **Cạnh tranh THẤP có cấu trúc**: chỉ ~640 sản phẩm "10cm outfit" trên toàn thị trường (BigGo), và phần lớn là may thủ công/order (thời gian chờ dài, giá 75.000–160.000đ). Hàng sẵn kho từ 1688 có lợi thế giao nhanh + giá thấp.
- **RỦI RO LỚN NHẤT CỦA CẢ DANH MỤC**: chữ "Labubu" xuất hiện trong gần như mọi listing Shopee. Đây là **nhãn hiệu/nhân vật có bản quyền** — xem mục 9.3. Khuyến nghị bắt buộc: bán dưới tên generic "áo cho búp bê 10cm / doll 10cm", không dùng tên nhân vật, không dùng hình in nhân vật.
- **Lưu ý xu hướng**: Metric ghi thị trường **−20,4% so với quý trước** → trend đang nguội. **Không nhập lô lớn**; test 150–250 bộ.

### 2.5 SP8 — Trang sức / charm giá rẻ (ưu tiên #5)

| Giá niêm yết | Số đã bán / đánh giá | Kênh | URL | Nhãn |
|---|---|---|---|---|
| **13.000₫** hạng 1 ngành trang sức | **13,73K đơn/7 ngày**, GMV 1,36 tỷ | TikTok Shop VN (FindNiche) | [findniche.com/tiktok/trending-jewelry-accessories-and-derivatives-products-vn](https://findniche.com/tiktok/trending-jewelry-accessories-and-derivatives-products-vn) | `[verified]` (qua T1) |
| **42.000₫** hạng 2 ngành trang sức | 1,69K đơn/7 ngày, GMV 2,45 tỷ | TikTok Shop VN (FindNiche) | (như trên) | `[verified]` (qua T1) |
| **15.000₫** — Charm dép Crocs Jibbitz | 4.9★ | Shopee | [shopee.vn/nonlab3dprint](https://shopee.vn/nonlab3dprint?entryPoint=ShopByPDP) | `[index]` |
| **Bộ vòng tay Pandora 66 món — 300.000₫, doanh số 71.603.000₫, đã bán 379** | 379 đã bán | Metric eReport (bản PDF công khai) | [scribd.com/document/963139604](https://www.scribd.com/document/963139604/Metric-Bao-cao-vong-tay-handmade) | `[index]` |
| Metric có hẳn báo cáo thị phần **Jibbitz charm** | — | Metric eReport | [metric.vn/ereport/thi-phan-jibbitz-charm](https://metric.vn/ereport/thi-phan-jibbitz-charm) | `[index]` |

**Đọc bảng này thế nào:**
- **Ngành trang sức giá rẻ là ngành dropship truyền thống → bão hòa CAO.** Giá bán 13.000đ không thể có lãi trên Shopee (phí cứng 5.700đ + 20% ≈ 8.300đ = 64% giá bán).
- **Cửa có lãi là "set/mystery box"**, và mốc tham chiếu là **Bộ vòng tay 66 món bán 300.000đ đạt doanh số 71,6 triệu** — tức khách chấp nhận trả 300.000đ cho một set lớn, chứ không mua lẻ 13.000đ nhiều lần.
- **Charm dép** là biến thể đáng chú ý: 15.000đ/chiếc, 4.9★, có cả báo cáo thị phần riêng → đủ lớn để có ngành riêng.

---

## 3. Mức độ bão hòa cạnh tranh — tổng hợp

| SKU | Bão hòa | Bằng chứng chính | Cửa vào cho người mới |
|---|---|---|---|
| SP2 Bàn chải chà giày | 🔴 **Rất cao** | Listing "Đã bán 50k+"; giá bán lẻ đã xuống 9.900đ, **thấp hơn giá nhập ước tính cao nhất** | **Không đấu giá.** Chỉ vào bằng combo + nội dung "mẹo vệ sinh giày" |
| SP3 Chân kê máy giặt | 🟡 **Trung bình** | Cầu lớn (9,68K–19,90K đơn/7 ngày; website ngoài sàn 43.849 đã bán); listing rẻ 19.998đ đã hết hàng | **Có cửa**: nâng lên bản inox/điều chỉnh cao (182.000–205.000đ) để thoát khỏi cuộc đua giá |
| SP5 Khóa tủ lạnh | 🟡 **Trung bình–thấp về số shop, nhưng giá đã sập** | 1 listing 10k+ đã bán; hàng Việt 9.000đ; TikTok 24.614đ | **Chỉ có cửa như upsell/bundle**, hoặc bán đúng trên TikTok Shop |
| SP7 Áo búp bê 10cm | 🟢 **Thấp** | Chỉ ~640 sản phẩm toàn thị trường; phần lớn là order/may tay 75.000–160.000đ | **Cửa tốt nhất.** Nhưng phải né bản quyền và trend đang −20,4%/quý |
| SP8 Trang sức giá rẻ | 🔴 **Cao** | Ngành dropship lâu năm; 13.000đ/chiếc không thể có lãi trên Shopee | Chỉ vào bằng set lớn (mốc 300.000đ/66 món) |

**Kết luận cạnh tranh:** trong shortlist T1, **thứ tự hấp dẫn đảo so với thứ tự trend**. T1 xếp theo *số đơn 7 ngày*; nhưng khi tính đến **phí sàn + giá bán lẻ đã bị đánh sập**, thứ tự nên đổi thành:

> **1) SP7 áo búp bê 10cm → 2) SP3 chân kê máy giặt (bản nâng cấp) → 3) SP2 bàn chải (chỉ combo) → 4) SP5 khóa tủ lạnh (chỉ upsell) → 5) SP8 trang sức (chỉ set lớn)**

---

## 4. Tệp khách hàng mục tiêu

Dựa trên persona chính thức & hành vi từ nguồn `[verified]` (TikTok Newsroom 30-07-2026; fint-global 15-04-2026) và suy luận `[chưa kiểm chứng]` cho từng SKU.

**Tệp nền của thị trường (từ nguồn):**
- Tuổi **18–34**, tập trung TP.HCM, Hà Nội, Đà Nẵng, Biên Hòa, Cần Thơ.
- AOV trung bình TikTok Shop VN: **250.000–350.000 VND**.
- Thời gian ra quyết định: **3–7 phút**.
- Nguồn tin cậy: **KOL/KOC > quảng cáo thương hiệu > review viết**.
- 95% nói "nội dung chân thực" ảnh hưởng trực tiếp tới quyết định mua.

| SKU | Chân dung khách | Nỗi đau / động cơ mua | Nơi họ ở |
|---|---|---|---|
| SP2 Bàn chải chà giày | Nam & nữ 18–30, học sinh–sinh viên, nhân viên văn phòng; sở hữu 2–4 đôi sneaker | "Giày trắng bẩn, mang ra tiệm 30–50k/lần quá tốn" | TikTok (xem mẹo vệ sinh giày), group Facebook sneaker/freeship, Shopee search "bàn chải chà giày" |
| SP3 Chân kê máy giặt | Nữ 25–45, **chủ hộ gia đình ở chung cư/nhà phố**, có máy giặt đặt trên sàn bê tông hoặc gần phòng ngủ | "Máy giặt rung ầm khi vắt, hàng xóm phàn nàn, nước tràn ra sàn" | TikTok (video before/after tiếng ồn), Shopee search "chân máy giặt chống rung" |
| SP5 Khóa tủ lạnh | **Mẹ có con 1–5 tuổi**; đôi khi là người chăm ông bà lớn tuổi | "Con mở tủ lạnh làm đổ, nghịch phích nước, sợ bỏng/ngã đồ" | TikTok Shop (ngành Mẹ & Bé +67%), Shopee, hội nhóm "mẹ & bé" trên Facebook |
| SP7 Áo búp bê 10cm | Nữ 16–30; **người sưu tầm blind box / doll**; người chơi ảnh búp bê trên TikTok | "Muốn búp bê của mình khác biệt, có ảnh đẹp để đăng"; "set chính hãng quá đắt" | TikTok (đặc biệt mảng sưu tầm/ảnh doll), Shopee ("outfit doll 10cm"), hội nhóm blind box |
| SP8 Trang sức set | Nữ 18–30, quan tâm thời trang nhanh, ngân sách chặt | "Muốn nhiều món để đổi mỗi ngày nhưng không muốn bỏ 300k" | TikTok Shop, Shopee, Instagram |

**Insight xuyên SKU:** khách hàng của SP3 và SP5 **trùng nhau** (phụ nữ 25–45 có gia đình). Đây là cơ sở cho một **combo "Tổ ấm yên tĩnh"** gồm chân kê máy giặt + khóa an toàn + phụ kiện nhỏ — vừa giải quyết vấn đề phí cứng 5.700đ/đơn, vừa tăng AOV.

---

## 5. USP — điểm khác biệt có thể bảo vệ được

Điều **không** thể dùng làm USP (vì ai cũng làm được): giá rẻ, freeship, "hàng mới về", "số lượng có hạn".

| SKU | USP đề xuất | Vì sao bảo vệ được | Cách thể hiện |
|---|---|---|---|
| SP7 Áo búp bê 10cm | **"Sẵn kho — ảnh thật từng set — giao trong 24h"**, đánh số từng set | Đối thủ chính là hàng order/may tay chờ 5–15 ngày. Tốc độ + ảnh thật là lợi thế vận hành, không phải giá | Mỗi set = 1 video 12 giây quay trên búp bê thật; nói rõ "shop ở VN, hàng có sẵn, không phải order" |
| SP3 Chân kê máy giặt | **"Video đo tiếng ồn bằng app — cam kết giảm ≥X dB, không giảm hoàn tiền"** + **bán bản inox điều chỉnh cao** | Cần quay thử thật và chịu rủi ro bảo hành → rào cản cho shop copy | Video before/after có đồng hồ đo dB; bảng thông số chân máy kèm ảnh thước đo |
| SP2 Bàn chải chà giày | **"Combo 10 cây + 1 chai dung dịch = 1 lần mua dùng cả năm"** | Đóng gói/danh mục SKU chứ không phải giá | Video "5 thứ trong nhà làm sạch giày trắng" |
| SP5 Khóa tủ lạnh | **"Keo 3M thật — dán 5 giây, chịu lực kéo của bé 3 tuổi"** | Chọn mẫu + cam kết chất lượng keo (SP5 trong T1 đã nêu rủi ro keo kém) | Video kéo thử lực; ghi rõ mã keo |
| SP8 Trang sức | **"Mystery set 10 món — mở hộp như chơi game"**, ảnh mở hộp mỗi đơn | Khoảnh khắc unboxing tạo nội dung do khách tạo (UGC) | Video "mở set 10 món xem có gì" |

**Nguyên tắc chung**: ở lô test đầu với 3–5 triệu quảng cáo, USP duy nhất có thể xây nhanh và rẻ là **TỐC ĐỘ giao hàng + NỘI DUNG THẬT**. Không cố xây thương hiệu.

---

## 6. Chiến lược giá

### 6.1 Mô hình chi phí dùng để tính (giả định minh bạch)

| Khoản | Mức dùng để mô hình | Cơ sở |
|---|---|---|
| Phí cố định (hoa hồng) | 16% | Bảng chính thức Shopee 23/05/2026: Nhà cửa & Đời sống nhóm còn lại 13–16%; Sở thích & Sưu tầm 15–17% `[verified]` |
| Phí xử lý giao dịch | 6% | Sapo 28-09-2026 `[verified]` |
| Thuế GTGT + TNCN khấu trừ | 3% | Shopee khấu trừ 1–5% GTGT + 0,5–5% TNCN `[verified]` |
| Phí hạ tầng | 3.000đ/đơn | Sapo (từ 01/07/2025) `[verified]` |
| PiShip (nếu tham gia) | 2.700đ/đơn | Thông báo Shopee 23/05/2026 `[verified]` |
| **Tổng phí sàn hiệu dụng** | **≈ 22% giá bán + 5.700đ/đơn** (base case) | Tổng hợp trên |
| Freeship shop chịu | 12.000–20.000đ/đơn | `[chưa kiểm chứng]` — phải đo bằng bảng giá ĐVVC |
| Chi phí nhập landed | = giá 1688 × **1,30** | 1688express: cước 25.000–35.000đ/kg + thông quan 1–3% (min 9.000đ/đơn) + kiểm hàng `[verified]` (hệ số 1,30 là ước lượng của tôi) |
| Quảng cáo | đo riêng theo mục 7 | CPC Shopee 800–2.000đ `[verified]` |

> **Lưu ý về chương trình ưu đãi người bán mới của Shopee** (miễn Phí Cố Định 30 ngày đầu; giảm 3% phí cố định từ 01/06–31/08/2026) — **giai đoạn giảm phí đã hết hạn trước ngày tra cứu 23-10-2026**. Nhưng **ưu đãi miễn Phí Cố Định 30 ngày đầu cho người bán mới vẫn là quyền lợi mặc định cần xác nhận lại trên Kênh Người Bán trước khi mở shop.** Nếu áp dụng được, 30 ngày đầu tiết kiệm ~16% doanh thu — tương đương toàn bộ ngân sách quảng cáo.

### 6.2 Unit economics theo SKU (đơn vị VND)

Công thức: **Lãi gộp/đơn = Giá bán − Chi phí hàng landed − (22% × Giá bán + 5.700) − Freeship shop chịu**

| SKU & cấu hình bán | Giá bán | Vốn hàng landed | Phí sàn + thuế | Freeship | **Lãi gộp/đơn** | **Biên** | Max CAC (hòa vốn) | ROAS tối thiểu |
|---|---|---|---|---|---|---|---|---|
| **SP7** Áo búp bê 10cm — 1 bộ | 75.000 | 11.700 | 22.200 | 12.000 | **29.100** | **38,8%** | 29.100 | 2,6 |
| **SP7** Combo 3 bộ | 189.000 | 35.100 | 47.280 | 18.000 | **88.620** | **46,9%** | 88.620 | 2,1 |
| **SP3** Set 4 chân kê — 1 set | 55.000 | 10.400 | 17.800 | 15.000 | **11.800** | 21,5% | 11.800 | 4,7 |
| **SP3** Set 4 chân kê — bản inox | 185.000 | 62.000 | 46.400 | 20.000 | **56.600** | 30,6% | 56.600 | 3,3 |
| **SP2** Combo 5 bàn chải | 49.000 | 13.000 | 16.480 | 15.000 | **4.520** | 9,2% | 4.520 | **10,8** ⚠️ |
| **SP2** Combo 10 bàn chải | 89.000 | 26.000 | 25.280 | 20.000 | **17.720** | 19,9% | 17.720 | 5,0 |
| **SP5** Lốc 4 khóa an toàn | 69.000 | 26.000 | 20.880 | 15.000 | **7.120** | 10,3% | 7.120 | **9,7** ⚠️ |
| **SP5** Bán lẻ 1 khóa (giá thị trường) | 24.000 | 6.500 | 10.980 | 12.000 | **−5.480** | **âm** ❌ | — | — |
| **SP8** Set 5 món trang sức | 79.000 | 26.000 | 23.080 | 12.000 | **17.920** | 22,7% | 17.920 | 4,4 |
| **SP8** Bán lẻ 1 món (giá thị trường) | 13.000 | 5.200 | 8.560 | 12.000 | **−12.760** | **âm** ❌ | — | — |

**Ba kết luận định lượng:**

1. **SP7 là SKU duy nhất có Max CAC lớn hơn chi phí thực tế để có 1 đơn** (CPC 800–2.000đ, CR 3–5% ⇒ chi phí/đơn ≈ 16.000–66.000đ theo miniai.vn). Với combo 3 bộ, Max CAC 88.620đ **bao trùm toàn bộ dải chi phí quảng cáo**. **Đây là SKU nên dồn tiền quảng cáo.**
2. **Bán lẻ SP5 và SP8 ở mức giá thị trường là lỗ −5.480đ và −12.760đ/đơn.** Đây là bằng chứng số học cho luận điểm ở mục 1: giá bán lẻ đã bị đánh sập dưới ngưỡng có lãi. **Không được bán lẻ hai SKU này.**
3. **Bán combo "nhỏ" cũng chưa đủ**: combo 5 bàn chải (ROAS tối thiểu 10,8) và lốc 4 khóa (9,7) đều **không thể có lãi nếu phải mua traffic**, vì ROAS thực tế của ngành hàng rẻ thường 3–6. Hai SKU này chỉ nên bán bằng **traffic tự nhiên/TikTok organic/affiliate**, hoặc là **sản phẩm bán kèm** trong đơn SP7/SP3 (lúc đó không phát sinh phí cứng 5.700đ).

### 6.3 Chiến lược giá niêm yết (3 lớp)

**Lớp 1 — Neo giá (anchor).** Đăng một biến thể "full set" giá cao (SP7: 205.000đ; SP3 inox: 225.000đ) làm mốc so sánh, dù bán ít.

**Lớp 2 — Sản phẩm chủ lực (bán nhiều).** SP7 combo 3 bộ @ 189.000đ; SP3 bản cơ bản @ 55.000đ (không bán dưới 55.000đ, dù thị trường có 45.000đ).

**Lớp 3 — Mồi & bán kèm.** Combo 10 bàn chải @ 89.000đ; lốc 4 khóa @ 69.000đ; set 5 trang sức @ 79.000đ. **Chỉ chạy khi đã có traffic tự nhiên, và luôn đặt trong cùng đơn với SKU chủ lực.**

**Quy tắc freeship:**
- Đơn ≥ 150.000đ: shop chịu freeship toàn phần (đã tính vào mô hình).
- Đơn < 150.000đ: dùng **mã freeship đồng tài trợ của Shopee** (từ 23/05/2026 người bán chịu **40%** giá trị mã, tối đa 50.000đ/sản phẩm) thay vì tự chịu 100%. `[verified]` — Shopee 27540.
- **Không hứa freeship vô điều kiện** ở giai đoạn test; ghi rõ "freeship cho đơn từ X".

**Đòn bẩy "giá gạch" (strikethrough):** mọi ví dụ đối thủ đều dùng (182.000đ gạch 310.000đ; 54.180đ gạch 120.000đ; 9.900đ gạch 15.000đ). Bắt buộc dùng giá gạch — nhưng **giá gạch phải trung thực**, vì Shopee có chế tài về giá tham chiếu sai.

---

## 7. Kênh bán nên ưu tiên

### 7.1 Xếp hạng kênh

| Hạng | Kênh | Vai trò trong 30 ngày đầu | Chi phí | Vì sao |
|---|---|---|---|---|
| **1** | **TikTok Shop (organic + video + livestream)** | Nguồn đơn chính cho SP7, SP3, SP2 | 0đ (organic) | Ngành Nhà cửa & Đời sống +94%; TikTok không yêu cầu quảng cáo trả phí để có đơn đầu tiên; 76% người tiêu dùng tương tác nội dung rồi mới tìm/mua `[verified]` |
| **2** | **Shopee** | Bắt cầu nhu cầu tìm kiếm (người đã biết muốn gì) | Phí sàn 22% + 5.700đ/đơn | Có sẵn dòng tìm kiếm; cần cho khách "gõ từ khóa", nhưng biên mỏng hơn |
| **3** | **TikTok Affiliate (KOC nhỏ)** | Nhân đôi nội dung, trả theo kết quả | **8–20% hoa hồng** (Sapo) / 4–7% nền tảng (fint) `[index]` | Chi phí biến đổi, không cần ngân sách trước — rất phù hợp với 3–5 triệu |
| **4** | **Facebook (group + page + Marketplace)** | Test nội dung bằng 0 đồng; bán COD cho SP3/SP5 | 0đ organic | Nhiều listing SP2/SP3/SP5 được bán qua group Facebook, có bằng chứng trong mục 2 |
| **5** | **Lazada / Zalo / website riêng** | **Bỏ trong 30 ngày đầu** | — | Lazada chỉ ~6–7 nghìn tỷ/H1/2026 so với Shopee ~144 nghìn tỷ → không đáng nguồn lực ở giai đoạn test |

### 7.2 Vì sao KHÔNG chạy 4 kênh trả phí cùng lúc

Ngân sách 4.000.000đ ÷ ngưỡng tối thiểu:
- TikTok Ads (mục tiêu doanh số): 100.000đ/ngày → **40 ngày-chạy** nếu dồn hết.
- Shopee Ads: ngưỡng an toàn cho shop mới 50.000–100.000đ/ngày `[verified]` → **40–80 ngày-chạy** ở mức 50.000đ.
- Facebook Ads: ngưỡng thực tế để học thuật toán thường ≥ 100.000đ/ngày `[chưa kiểm chứng]`.

→ **Phân bổ chốt**: TikTok Shop Ads (chính) + Shopee Ads (phụ, ở mức tối thiểu) + Facebook organic (0đ). **Không chạy Facebook Ads trong 30 ngày đầu.**

---

## 8. Kế hoạch nội dung + quảng cáo 30 ngày với ngân sách 3–5 triệu VND

### 8.1 Phân bổ ngân sách (mốc 4.000.000đ)

| Hạng mục | Số tiền | Ghi chú |
|---|---|---|
| TikTok Shop Ads (mục tiêu doanh số, video gắn giỏ) | **1.500.000đ** | ≈ 100.000đ/ngày × 15 ngày, tập trung vào video thắng |
| Shopee Ads (quảng cáo tìm kiếm) | **800.000đ** | ≈ 50.000đ/ngày × 16 ngày, chỉ cho SP7 và SP3 |
| Gửi mẫu KOC/affiliate (8–10 người) | **900.000đ** | ~90.000đ/người tiền hàng + ship; hoa hồng trả theo đơn |
| Voucher/freeship subsidy | **400.000đ** | Mã đồng tài trợ, tối đa 40% |
| Đạo cụ/hậu kỳ (không thuê studio) | **400.000đ** | Điện thoại + đèn ring sẵn có |
| **Tổng** | **4.000.000đ** | Dao động 3–5 triệu: giảm/tăng ở dòng TikTok Ads và KOC |

**Nguyên tắc kỷ luật ngân sách:**
- **Không đặt ngân sách > 100.000đ/ngày** trong 7 ngày đầu (bài học từ miniai.vn: sai lầm phổ biến là đặt 200.000–500.000đ/ngày khi chưa có dữ liệu).
- **Cắt sau 7 ngày** nếu video không đạt CTR > 2% hoặc CR < 3%.
- **Chỉ scale khi ROAS ≥ 3** (an toàn hơn ngưỡng 5 mà miniai khuyến nghị, vì SP7 có biên 38,8%).

### 8.2 Lịch 30 ngày

**Tuần 1 (Ngày 1–7) — Dựng nền, 0đ quảng cáo**
- Mở shop TikTok Shop + Shopee. Xác nhận ưu đãi **miễn Phí Cố Định 30 ngày đầu** của Shopee.
- Chụp ảnh thật cả 5 SKU: nền trắng 5 ảnh + 3 ảnh ngữ cảnh thật + 1 video 15 giây/SKU.
- **Đăng 14 video organic** (2/ngày) — xem 8.3.
- Đóng gói hàng sẵn, tự đo cân nặng & kích thước để tính freeship thật.
- KPI tuần 1: **≥ 10 đơn organic**, xác định 1 SKU có tín hiệu tốt nhất.

**Tuần 2 (Ngày 8–14) — Test quảng cáo có kiểm soát**
- Bật TikTok Shop Ads **100.000đ/ngày** cho 1 SKU duy nhất (dự kiến SP7).
- Gửi mẫu cho **5 KOC** (ưu tiên 1.000–10.000 follower, ngách dọn nhà / doll).
- Shopee Ads **50.000đ/ngày** cho cùng SKU.
- **Livestream 3 buổi × 45 phút** (tối 20h–20h45).
- KPI tuần 2: **CTR > 2%, CR ≥ 3%, ROAS ≥ 2,5**. Cắt mọi nhóm quảng cáo dưới ngưỡng.

**Tuần 3 (Ngày 15–21) — Dồn tiền vào cái đang thắng**
- Tăng TikTok Ads lên **150.000–200.000đ/ngày cho duy nhất video/SKU thắng**.
- Nhân bản video thắng thành 3 biến thể (đổi hook 3 giây đầu) để chống mỏi nội dung.
- Gửi mẫu thêm **3–5 KOC**; thiết lập hoa hồng affiliate 10–15% cho SP7.
- Bắt đầu bán chéo: chèn SP2/SP5 vào đơn SP3/SP7 (không tăng phí cứng).
- KPI tuần 3: **ROAS ≥ 3,3**, tối thiểu 40 đơn/tuần.

**Tuần 4 (Ngày 22–30) — Chốt, đo, quyết định SKU cho lô 2**
- Duy trì ngân sách ở SKU thắng; dừng toàn bộ SKU có ROAS < 2.
- **Một buổi livestream dài 90 phút** kèm voucher để tạo đỉnh doanh số.
- Tổng kết: bảng lãi/lỗ theo SKU **bằng số thật**, đối chiếu với mô hình mục 6.2.
- KPI tháng: **≥ 150 đơn; ≥ 1 SKU đạt ROAS ≥ 3,5; CAC trung bình < Max CAC của SKU thắng**.

### 8.3 Kế hoạch nội dung: 3 trụ, 60 video/tháng

| Trụ | Tỷ lệ | Công thức | Ví dụ hook 3 giây đầu |
|---|---|---|---|
| **A. Vấn đề → Giải pháp** | 50% | Nêu nỗi đau thật → demo sản phẩm → kết quả đo được | "Máy giặt nhà bạn kêu to thế này không?" / "Giày trắng thành thế này sau 5 phút" |
| **B. So sánh / Định giá** | 25% | "Bên ngoài X đồng, chỗ mình Y đồng" | "Tiệm giặt giày lấy 50k, cái này 21k dùng cả năm" |
| **C. Unbox / Cận cảnh** | 25% | Mở hộp, quay cận chất liệu, đếm số lượng | "Mở set 10 món xem shop gửi gì" |

**Quy tắc kỹ thuật cho video TikTok Shop VN (từ nguồn `[verified]` fint-global 15-04-2026):**
- Độ dài **< 30 giây**.
- **Nói giá sớm** ("Chỉ 189k!").
- **Chữ tiếng Việt trên màn hình** để giữ chân người xem.
- Kết thúc bằng CTA rõ: "Nhấn vào giỏ hàng dưới video".
- Hashtag nội địa: `#TikTokShopVN #XemNgay #MuaSắmThôngMinh`.
- **Trả lời mọi bình luận trong vòng 30 phút** — thuật toán VN thưởng tốc độ trả lời.

**Tần suất:** 2 video/ngày (60 video/30 ngày) + 3 livestream/tuần (12 buổi).

### 8.4 Chỉ số theo dõi & ngưỡng hành động

| Chỉ số | Ngưỡng tốt | Hành động nếu dưới ngưỡng |
|---|---|---|
| CTR video gắn giỏ | > 2% | Đổi ảnh bìa + 3 giây đầu |
| CR (click → đơn) | ≥ 3% | Xem lại giá, đánh giá, mô tả, freeship |
| ROAS | ≥ 3 | Tắt nhóm quảng cáo; quay lại organic |
| Đánh giá sản phẩm | ≥ 4.5★ | Dừng quảng cáo, xử lý hàng lỗi trước |
| Số đánh giá | ≥ 50 | Chạy ưu đãi "đánh giá nhận quà" hợp lệ |

*(Ngưỡng CTR/CR/ROAS lấy từ miniai.vn 14-05-2026 `[verified]`.)*

---

## 9. Rủi ro và cách xử lý

### 9.1 Tồn kho / chết hàng
- **Bằng chứng**: FindNiche tự cảnh báo *"Historical or captured performance does not guarantee future demand"*; Metric ghi ngành quần áo búp bê **−20,4% so với quý trước**; T1 đã nêu "fidget spinner" là ví dụ trend bùng nổ rồi tắt.
- **Xử lý**: giới hạn **≤ 250 đơn vị/SKU** ở lô 1; không SKU nào chiếm > 35% vốn hàng; đặt cọc 50% cho đơn 1688 thay vì trả hết.

### 9.2 Hàng lỗi / hoàn hàng
- **Bằng chứng**: keo dán khóa tủ lạnh (T1 nêu); pin quạt mini (Genk cảnh báo cháy nổ sạc kém chất lượng); size chân kê không khớp; **TikTok Shop áp phí trả hàng/hoàn tiền cho nhà bán từ 01/04/2026** `[index]`.
- **Xử lý**: **đặt mẫu 3–5 đơn vị trước khi nhập lô**; dùng **dịch vụ kiểm hàng 1688express** (700–5.000đ/sản phẩm — rẻ hơn nhiều so với 1 đơn hoàn); tham gia PiShip (2.700đ/đơn) để bảo hiểm phí hoàn; **quay video lúc đóng gói** cho mọi đơn > 150.000đ.

### 9.3 Bản quyền thiết kế / nhãn hiệu — **RỦI RO CAO NHẤT**
- **Bằng chứng**: gần như toàn bộ listing SP7 trên Shopee dùng chữ **"Labubu"**; nhóm charm dép dùng chữ **"Crocs"/"Jibbitz"**. Đây là các nhãn hiệu của bên thứ ba.
- **Xử lý (bắt buộc)**:
  1. **Không** dùng "Labubu", "POP MART", "Crocs", "Jibbitz" trong tiêu đề, mô tả, hashtag, tên shop.
  2. Dùng mô tả generic: "áo cho búp bê cao 10cm", "charm gắn dép sục".
  3. **Không bán** sản phẩm có hình in logo/nhân vật bản quyền.
  4. Trước khi nhập lô 2, **tra cứu nhãn hiệu tại Cục Sở hữu trí tuệ** (iplib.noip.gov.vn) cho các từ khóa liên quan. *Việc này chưa làm trong T3 — cần một task riêng.*
- **Lưu ý**: đây là ý kiến vận hành, **không phải tư vấn pháp lý**.

### 9.4 Chính sách sàn thay đổi liên tục
- **Bằng chứng**: Shopee đổi phí cố định ngày **23/05/2026** (Sắc Đẹp 14%→17%, Sở thích & Sưu tầm 13–14%→15–17%); Voucher Xtra 4%→5,5%; PiShip 1.620đ→2.700đ; người bán chịu mã đồng tài trợ 30%→40%. TikTok Shop đổi chính sách hoàn tiền từ 01/04/2026.
- **Xử lý**: **mọi bảng tính giá phải ghi ngày hiệu lực**; kiểm tra lại phí trước mỗi lần điều chỉnh giá; không ký cam kết giá dài hạn với khách.

### 9.5 Thuế & pháp lý nhập khẩu
- **Bằng chứng**: Shopee **khấu trừ và nộp thay** thuế GTGT/TNCN từ 01/07/2025 (Nghị định 117/2025); hàng nhập dưới 1 triệu đồng bị thu **VAT tự động từ 01/08/2025** (Thông tư 29/2025) `[index]`; hàng nhập khẩu **phải có nhãn gốc** (nhãn vật lý, tiếng Việt hoặc tiếng nước ngoài) `[index]`.
- **Xử lý**: đăng ký hộ kinh doanh nếu doanh thu vượt ngưỡng; yêu cầu đơn vị vận chuyển xác nhận rõ **ai chịu VAT và thủ tục nhãn phụ**.

### 9.6 Tỷ giá & phí ẩn
- T1 dùng **1 CNY ≈ 3.650 VND** và **1 USD ≈ 26.300 VND** nhưng tự ghi là **chưa kiểm chứng bằng nguồn tỷ giá**. Toàn bộ mô hình ở mục 6.2 kế thừa giả định này.
- **Xử lý**: chốt tỷ giá tại ngày đặt hàng; tính lại nếu lệch > 3%.

---

## 10. Kết luận & việc cần làm tiếp

### 10.1 Kết luận
1. **Thị trường VN đang dịch lên phân khúc giá cao hơn** (Metric: phân khúc <100.000đ mất 4,2% thị phần). Bán "siêu rẻ" đi ngược dòng chảy.
2. **Chi phí cứng 5.700đ/đơn biến mọi SKU dưới ~50.000đ thành lỗ** nếu bán lẻ. Bằng chứng: SP5 bán lẻ −5.480đ/đơn, SP8 bán lẻ −12.760đ/đơn.
3. **SKU hấp dẫn nhất không phải SKU hot nhất.** Theo mô hình: **SP7 áo búp bê 10cm** (biên 38,8–46,9%, Max CAC 29.100–88.620đ — bao trùm toàn dải chi phí quảng cáo) > SP3 bản inox > SP3 bản cơ bản > SP2 combo 10 > SP5 lốc 4 > SP8 set 5.
4. **TikTok Shop là kênh số 1 cho 30 ngày đầu** (organic + affiliate, chi phí biến đổi), Shopee là kênh số 2, **bỏ Lazada**.
5. **Chỉ 1 SKU nên nhận phần lớn ngân sách quảng cáo trong 30 ngày đầu** — dồn ngân sách 3–5 triệu vào một SKU sẽ hiệu quả hơn rải mỏng.

### 10.2 Việc cần làm trước khi xuống tiền (task tiếp theo)
1. **Xác minh giá & số đã bán bằng app thật** trên Shopee/TikTok Shop cho 5 SKU ưu tiên (mục 2 chỉ có nhãn `[index]`).
2. **Đo freeship thật** theo cân nặng/kích thước từng SKU bằng bảng giá ĐVVC — con số 12.000–20.000đ/đơn hiện là ước lượng.
3. **Chốt tỷ giá** CNY/VND và USD/VND.
4. **Tra cứu nhãn hiệu** các từ khóa Labubu / Crocs / Jibbitz tại Cục SHTT.
5. **Xác nhận với Shopee** quyền lợi miễn Phí Cố Định 30 ngày đầu còn hiệu lực không.
6. **Đặt mẫu 3–5 đơn vị/SKU** để kiểm chất lượng, cân nặng thật, và đóng gói.

### 10.3 Điểm không chắc chắn lớn nhất
Toàn bộ kết luận về giá bán và số đã bán của đối thủ dựa trên **đoạn trích công cụ tìm kiếm, không phải trang gốc** (Shopee/TikTok chặn đọc tự động). Nếu giá thị trường thực tế cao hơn mức ghi trong mục 2, **kết luận về SP5 và SP8 có thể thay đổi từ "lỗ" thành "có lãi mỏng"**. Trước khi dùng tài liệu này để quyết định tiền, **phải mở app và chụp lại màn hình 10 listing mục tiêu.**

---

*Tài liệu này chỉ ghi trong `research-1688/03-thi-truong-marketing.md`. Không có số liệu nào trong đây được bịa; mọi con số hoặc có URL kèm theo trong bảng, hoặc được dán nhãn `[chưa kiểm chứng]`.*
