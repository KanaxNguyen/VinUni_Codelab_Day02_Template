## 🏛️ Bối cảnh: Tôi là ai?

Tôi là **Đăng**, AI Engineer tại **Vin Smart Future**. Nhóm chúng tôi được giao nhiệm vụ phối hợp với Khối Vận Hành của **Vinhomes (VHN)** để tìm kiếm các cơ hội tối ưu hóa bằng trí tuệ nhân tạo.

Thông qua khảo sát thực địa tại Trung tâm Điều vận Xanh SM Hà Nội, tôi nhận thấy các điều phối viên (Dispatchers) đang gặp một áp lực cực kỳ lớn vào giờ cao điểm, dẫn đến việc rò rỉ hiệu suất điều xe và tăng tỉ lệ khách hàng hủy chuyến. Bài toán tôi mang vào buổi Lab hôm nay đến từ chính quan sát thực tế này.

# 🔍 Phase 1 — SCAN: Tìm kiếm cơ hội (Cá nhân)

Dùng **4 Lenses** quét qua vận hành của các công ty thành viên Vingroup.


| # | Subsidiary | Lens                             | Mô tả ngắn bài toán                                                                                                    |
| - | ---------- | -------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| 1 | Vinhomes   | Tốn thời gian (Time-consuming) | Phân loại & Điều hướng phản ánh/khiếu nại của cư dân đến đúng ban quản lý (BQL) khu vực                 |
| 2 | VinFast    | Lặp lại (Repetitive)           | So khớp tự động hóa đơn sạc điện từ các trạm sạc đối tác với dữ liệu phiên sạc hệ thống             |
| 3 | Xanh SM    | Stakeholder Pain                 | Tối ưu hóa việc phân bổ xe và điều hướng tài xế đón khách tại các điểm nóng (Hotspots) giờ cao điểm |
| 4 | Vinmec     | AI-upgrade                       | Tự động trích xuất thông tin bệnh án và mã hóa chuẩn ICD-10 phục vụ quyết toán bảo hiểm                   |
| 5 | Vinpearl   | AI-upgrade                       | Trợ lý virtual CSKH tự động lên lịch trình cá nhân hóa và xử lý đặt vé vui chơi theo thời gian thực     |

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards (Cá nhân)

Chọn top 3 từ danh sách SCAN: **#2 (Xanh SM Sự cố sạc), #4 (Vinhomes CSKH), #6 (Xanh SM Hủy chuyến).**

## Thẻ bài toán tiêu biểu: Card #1 — Phân loại tự động, trích xuất thực thể (phòng, loại sự cố) và điều hướng phản ánh cư dân về đúng BQL tòa nhà/kỹ thuật.

**Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)**

**QUICK PROBLEM CARD #01**

* **Bài toán:** Phân loại tự động, trích xuất thực thể (phòng, loại sự cố) và điều hướng phản ánh cư dân về đúng BQL tòa nhà/kỹ thuật.
* **Công ty thành viên:** [X] Vinhomes
* **Ai đang đau (Actor)?** Nhân viên CSKH/Ban quản lý Vinhomes & Cư dân (chờ lâu/chuyển nhầm)
* **Workflow thủ công hiện tại (3-5 bước):**

1. Cư dân gửi phản ánh (App/Hotline)
2. CSKH đọc & gán nhãn thủ công (Tòa, Loại lỗi)
3. Chuyển phiếu cho Đội Kỹ thuật/BQL tương ứng
4. Xử lý & Phản hồi cư dân

* **Bước nào tốn thời gian/lỗi nhất?** Bước 2: CSKH gán nhãn & điều hướng (⏱ 12 phút/lượt)
* **AI có thể nhảy vào hỗ trợ ở bước nào?** Bước 2 & gợi ý mẫu phản hồi cho Bước 4
* **Đo thành công bằng gì (Metric có số)?**
* Giảm thời gian phân loại & điều hướng phản ánh từ 12 phút ──> dưới 30 giây/lượt
* Tỷ lệ điều hướng đúng Ban Quản lý/Đội kỹ thuật đạt ≥ 95%
* **Quick Architecture:** [X] Agent

**QUICK PROBLEM CARD #02**

* **Bài toán:** Tự động trích xuất dữ liệu hồ sơ bệnh án và gợi ý mã hóa ICD-10 phục vụ thanh toán bảo hiểm y tế.
* **Công ty thành viên:** [X] Vinmec
* **Ai đang đau (Actor)?** Nhân viên phòng bảo hiểm y tế & Bác sĩ Vinmec
* **Workflow thủ công hiện tại (3-5 bước):**

1. Bác sĩ kê bệnh án văn bản/hình ảnh
2. NV Bảo hiểm đọc thủ công toàn bộ hồ sơ
3. Tra cứu & nhập mã ICD-10 tương ứng
4. Gửi yêu cầu chi trả sang phía Bảo hiểm

* **Bước nào tốn thời gian/lỗi nhất?** Bước 2 & 3: Đọc hồ sơ & Tra cứu mã ICD (⏱ 15 phút/lượt)
* **AI có thể nhảy vào hỗ trợ ở bước nào?** Bước 2 & 3 (AI đọc file, trích xuất & gợi ý mã)
* **Đo thành công bằng gì (Metric có số)?**
* Giảm thời gian xử lý hồ sơ bảo hiểm từ 15 phút ──> dưới 2 phút/hồ sơ
* Giảm tỷ lệ hồ sơ bị cơ quan BH từ chối do sai mã ICD-10 từ 6% ──> dưới 1%
* **Quick Architecture:** [X] LLM

**QUICK PROBLEM CARD #03**

* **Bài toán:** Phân tích nhu cầu chuyến đi và điều hướng tài xế Xanh SM đón khách tại các vị trí chốt điểm nóng (Hotspots) theo thời gian thực.
* **Công ty thành viên:** [X] Xanh SM
* **Ai đang đau (Actor)?** Tài xế Xanh SM & Điều hành viên trung tâm dispatch
* **Workflow thủ công hiện tại (3-5 bước):**

1. Điều hành viên theo dõi biểu đồ cầu thủ công
2. Phát thông báo hotspot chung
3. Tài xế tự di chuyển theo kinh nghiệm
4. Nhận chuyến nếu có khách

* **Bước nào tốn thời gian/lỗi nhất?** Bước 1 & 3: Dự báo & Di chuyển rỗng (⏱ 20 phút chạy rỗng)
* **AI có thể nhảy vào hỗ trợ ở bước nào?** Bước 1 (Dự báo nhu cầu) & Bước 2 (Điều hướng xe)
* **Đo thành công bằng gì (Metric có số)?**
* Giảm tỷ lệ quãng đường di chuyển không tải (deadhead) từ 22% ──> dưới 12%
* Giảm thời gian chờ xe trung bình của khách hàng (ETA) từ 7 phút ──> dưới 3 phút
* **Quick Architecture:** [X] Agent
