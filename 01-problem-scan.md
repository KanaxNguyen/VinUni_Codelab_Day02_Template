# Lab 02 — 01-problem-scan (Cá nhân: Trần Chí Vĩ)

---

# 🔍 Phase 1 — SCAN (5 Bài toán thực tế tại Vingroup)

Sử dụng 4 Lenses: Lặp lại (Repetitive), Tốn thời gian (Time-consuming), AI-upgrade, Stakeholder Pain.

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | **Vinmec** | Tốn thời gian | **Soạn thảo tóm tắt hồ sơ xuất viện (Discharge Summary):** Bác sĩ mất quá nhiều thời gian (20-30 phút/bệnh nhân) để đọc lại bệnh án điện tử, xét nghiệm và ghi chú tay để viết bản tóm tắt xuất viện cho bệnh nhân. |
| 2 | **VinFast** | AI có thể tốt hơn | **Chẩn đoán lỗi kỹ thuật ban đầu qua mô tả tiếng Việt:** Khách hàng mô tả lỗi xe bằng văn nói (ví dụ: "xe kêu lạch cạch ở gầm"), hệ thống cần tự động phân loại mã lỗi kỹ thuật sơ bộ để điều phối đúng kỹ thuật viên. |
| 3 | **Vinhomes** | Lặp lại | **Phân loại & Điều hướng khiếu nại cư dân:** Cư dân gửi hàng trăm phản ánh qua App (mất nước, ồn ào, thẻ từ hỏng). Hiện tại Ban quản lý phải đọc thủ công từng cái để chuyển cho các bộ phận (Kỹ thuật, An ninh, CSKH). |
| 4 | **Xanh SM** | Pain từ người khác | **Xử lý sự cố hết pin thực địa của tài xế:** Tài xế cạn pin gọi lên tổng đài, điều phối viên phải tra cứu thủ công vị trí xe và trạm sạc trống gần nhất (mất 15 phút), khiến tài xế chờ đợi lâu và mất doanh thu cuốc xe. |
| 5 | **Vinpearl** | Tốn thời gian | **Tổng hợp và phân loại Review khẩn cấp:** Đọc thủ công hàng trăm review từ Booking.com, Agoda mỗi ngày để tìm ra các phàn nàn khẩn cấp (như phòng có mùi, nhân viên thái độ) nhằm xử lý ngay lập tức. |

---

# 🃏 Phase 2 — QUICK-ASSESS (3 Quick Problem Cards)

Dưới đây là 3 thẻ bài toán tiềm năng nhất được lọc ra để phân tích nhanh.

## Card 1: Vinmec — Tóm tắt hồ sơ xuất viện
```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: Tự động trích xuất thông tin bệnh án để soạn thảo │
│ bản tóm tắt xuất viện bằng ngôn ngữ dễ hiểu cho bệnh nhân.  │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [x] Vinmec   [ ] Khác                   │
│                                                             │
│ Ai đang đau (Actor)? Bác sĩ điều trị (quá tải hành chính)   │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Đọc lại bệnh án điện tử (EMR) ──> 2. Xem kết quả xét   │
│   nghiệm ──> 3. Đọc ghi chú hằng ngày ──> 4. Gõ tay bản tóm │
│   tắt xuất viện.                                            │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 4 (⏱ 25 phút/lượt)    │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 1 đến 4          │
│ (AI tự động đọc EMR, xét nghiệm và draft sẵn bản tóm tắt)   │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│   Giảm thời gian soạn tóm tắt từ 25 phút ──> dưới 5 phút    │
│   (Bác sĩ chỉ cần đọc lại và ký duyệt).                     │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

## Card 2: Vinhomes — Phân loại khiếu nại tự động
```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán: Tự động phân loại và điều phối các khiếu nại/yêu  │
│ cầu của cư dân gửi qua App Vinhomes Resident tới đúng team. │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác                   │
│                                                             │
│ Ai đang đau (Actor)? Nhân viên Lễ tân / CSKH tòa nhà        │
│                                                             │
│ Workflow thủ công hiện tại (3 bước):                        │
│   1. Đọc ticket trên hệ thống ──> 2. Đánh giá nội dung      │
│   ──> 3. Forward thủ công cho team Kỹ Thuật/An Ninh/VSinh   │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ 3 phút/ticket)│
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 1, 2 và 3        │
│ (AI đọc chữ/hình ảnh và tự gán tag, forward tự động)        │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│   100% ticket được phân loại và forward dưới 10 giây với độ │
│   chính xác > 95%.                                          │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

## Card 3: VinFast — Chẩn đoán lỗi sơ bộ qua văn nói
```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán: Dịch các mô tả lỗi xe bằng văn nói của khách hàng │
│ thành mã lỗi kỹ thuật ban đầu để điều phối trạm dịch vụ.    │
│ Công ty thành viên: [x] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác                   │
│                                                             │
│ Ai đang đau (Actor)? Tổng đài viên CSKH VinFast             │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Nghe khách mô tả lỗi ──> 2. Ghi chú lại theo ý hiểu    │
│   ──> 3. Tra cứu cẩm nang kỹ thuật ──> 4. Gán mã lỗi sơ bộ  │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 (⏱ 8 phút/cuộc gọi) │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3 & 4            │
│ (AI mapping trực tiếp mô tả dân dã với cơ sở dữ liệu lỗi)   │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│   Giảm thời gian xử lý cuộc gọi báo lỗi từ 10 phút ──> 3 phút.│
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```
