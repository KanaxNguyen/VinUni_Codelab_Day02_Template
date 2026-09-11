# 01 — Problem Scan (Cá nhân)

## Phase 1 — SCAN

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|---|---|---|
| 1 | VinFast | Lặp lại | Nhân viên trung tâm bảo hành nhập tay mã lỗi từ máy chẩn đoán OBD vào hệ thống CRM để tạo phiếu sửa chữa, lặp lại ~150 lượt/ngày/trung tâm |
| 2 | Xanh SM | Pain từ người khác | Tài xế phàn nàn hệ thống điều vận gợi ý điểm đón khách sai vị trí thực tế (do dữ liệu bản đồ chưa cập nhật ngõ/hẻm), gây hủy chuyến và mất thời gian tìm khách |
| 3 | Vinhomes | Tốn thời gian | Nhân viên chăm sóc cư dân mất trung bình 12 phút/phản hồi để soạn trả lời cho các đánh giá 1-2 sao trên app cư dân, xử lý ~40 lượt/ngày |
| 4 | Vinmec | AI có thể tốt hơn | Bác sĩ mất 20-30 phút/bệnh nhân để viết tóm tắt hồ sơ xuất viện thủ công từ ghi chú khám bệnh, gây quá tải và chậm trễ xuất viện |
| 5 | Vinpearl/VinWonders | Lặp lại | Nhân viên tổng đài trả lời lặp lại các câu hỏi giống nhau về giá vé, giờ mở cửa, tình trạng phòng trống — ước tính 60% cuộc gọi là câu hỏi lặp lại |

---

## Phase 2 — QUICK-ASSESS (3 Quick Problem Cards)

### Card #1 — VinFast: Tự động hóa nhập liệu chẩn đoán bảo hành

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: Nhân viên trung tâm bảo hành nhập tay mã lỗi từ   │
│ máy chẩn đoán OBD vào hệ thống CRM để tạo phiếu sửa chữa.   │
│ Công ty thành viên: [x] VinFast                             │
│                                                             │
│ Ai đang đau? Nhân viên kỹ thuật bảo hành (KTV tuyến đầu)     │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Cắm máy chẩn đoán OBD, đọc mã lỗi trên màn hình        │
│   → 2. Chụp ảnh/ghi chép tay danh sách mã lỗi               │
│   → 3. Đăng nhập CRM, gõ tay từng mã lỗi + mô tả            │
│   → 4. Gán mức độ ưu tiên sửa chữa thủ công                 │
│                                                             │
│ Bước nào tốn nhất? Bước 3 (⏱ 8 phút/lượt)                   │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3-4              │
│ (Đọc ảnh mã lỗi -> tự động điền CRM -> gợi ý mức ưu tiên)   │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm thời gian tạo phiếu từ 10 phút ──> dưới 2 phút.        │
│                                                             │
│ Quick Architecture: [x] LLM Feature (đọc ảnh + điền form)    │
└─────────────────────────────────────────────────────────────┘
```

### Card #2 — Vinhomes: Trợ lý soạn phản hồi đánh giá tiêu cực

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán: Nhân viên CSKH mất nhiều thời gian soạn phản hồi  │
│ cho đánh giá/phàn nàn tiêu cực (1-2 sao) trên app cư dân.   │
│ Công ty thành viên: [x] Vinhomes                             │
│                                                             │
│ Ai đang đau? Nhân viên chăm sóc cư dân (Resident Care)       │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Đọc đánh giá/phàn nàn trên app                          │
│   → 2. Tra cứu lịch sử căn hộ/cư dân liên quan               │
│   → 3. Soạn thảo phản hồi phù hợp giọng điệu                │
│   → 4. Gửi và theo dõi phản hồi tiếp theo (nếu có)           │
│                                                             │
│ Bước nào tốn nhất? Bước 3 (⏱ 12 phút/lượt)                  │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3                │
│ (Draft phản hồi dựa trên ngữ cảnh + lịch sử cư dân)         │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm thời gian soạn phản hồi từ 12 phút ──> dưới 3 phút.    │
│                                                             │
│ Quick Architecture: [x] LLM Feature (draft, cần duyệt)       │
└─────────────────────────────────────────────────────────────┘
```

### Card #3 — Vinmec: Tóm tắt hồ sơ xuất viện tự động

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán: Bác sĩ mất nhiều thời gian viết tóm tắt hồ sơ     │
│ xuất viện thủ công từ ghi chú khám bệnh trong quá trình     │
│ điều trị.                                                    │
│ Công ty thành viên: [x] Vinmec                               │
│                                                             │
│ Ai đang đau? Bác sĩ điều trị (quá tải giờ hành chính)        │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Tổng hợp ghi chú khám bệnh qua các ngày điều trị        │
│   → 2. Đối chiếu kết quả xét nghiệm/chẩn đoán hình ảnh       │
│   → 3. Viết tóm tắt xuất viện theo chuẩn hồ sơ y tế          │
│   → 4. Bác sĩ trưởng khoa duyệt trước khi phát hành          │
│                                                             │
│ Bước nào tốn nhất? Bước 1 & 3 (⏱ 20 phút/lượt)               │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 1 & 3             │
│ (Tổng hợp dữ liệu -> Draft tóm tắt theo chuẩn y tế)          │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm thời gian viết tóm tắt từ 25 phút ──> dưới 8 phút.     │
│                                                             │
│ Quick Architecture: [x] LLM Feature (bắt buộc bác sĩ duyệt)  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🗳️ Quyết định lựa chọn (nháp — cần cả nhóm thống nhất)

**Bài toán đề xuất để Deep-Dive: Card #1 — VinFast Tự động hóa nhập liệu bảo hành.**

> ⚠️ Ghi chú: đây là bản đề xuất cá nhân. Cần cả nhóm thảo luận và đồng thuận chọn
> trước khi triển khai Phase 3, theo đúng quy trình nộp bài của README.
