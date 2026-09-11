# 🚀 Phase 0 — worked Example: Xanh SM Intelligent Dispatcher (15 min)

*Giảng viên walk-through ví dụ thực tế từ Vin Smart Future để bạn hiểu rõ cách scoping một bài toán AI.*
Đọc chi tiết worked example tại file [02-deliverable-example.md](02-deliverable-example.md).

---

# 🔍 Phase 1 — SCAN (Cá nhân, 20 min)

Hãy sử dụng **4 Lenses** dưới đây để quét qua hoạt động vận hành của các công ty thành viên Vingroup. Ghi lại **ít nhất 5 bài toán/bottleneck** thực tế.

### 4 Lenses tìm bài toán AI cho Vingroup:
1. **Lặp lại (Repetitive):** Tác vụ lặp đi lặp lại nhiều lần hằng ngày. (Ví dụ: So khớp hóa đơn sạc điện tại VinFast, route lại chuyến taxi tại Xanh SM).
2. **Tốn thời gian (Time-consuming):** Tác vụ ngốn thời gian xử lý thủ công của nhân viên. (Ví dụ: Soạn thảo phản hồi đánh giá 1-star của cư dân Vinhomes).
3. **AI có thể tốt hơn (AI-upgrade):** Dịch vụ khách hàng hiện tại còn chậm hoặc phản hồi rập khuôn. (Ví dụ: Chatbot CSKH Vinpearl hỗ trợ đặt vé vui chơi).
4. **Pain từ người khác (Stakeholder Pain):** Bottleneck khiến khách hàng hoặc nhân viên thực địa phàn nàn. (Ví dụ: Tài xế Xanh SM phàn nàn về việc hệ thống gợi ý điểm đón khách không chính xác).

> [!TIP]
> **🤖 AI Prompts — Partner brainstorm:**
> Hãy sử dụng prompt sau để brainstorm các bài toán thực tế nếu bạn chưa có ý tưởng:
> *"Tôi là AI Engineer tại Vin Smart Future (Vingroup). Tôi đang tìm kiếm các pain point vận hành cụ thể có thể tối ưu bằng AI cho mảng [Chọn một: VinFast / Xanh SM / Vinhomes / Vinmec]. Hãy gợi ý cho tôi 5 quy trình nghiệp vụ thủ công, tốn nhiều thời gian và gây rò rỉ hiệu suất kèm con số thống kê ước tính về tổn thất."*

### 📝 List bài toán của tôi:
| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | Vinhomes | Repetitive | Phát hiện & Xử lý Vi phạm Trật tự - Đỗ xe Sai Quy định Trong Nội khu |
| 2 | VinFast | Time-consuming | Phân loại & Chẩn đoán Mã Lỗi Xe Từ xa qua Nhật ký Telemetry |
| 3 | Vinpearl | AI-upgrade | Xử lý Đổi vé, Hủy vé & Đổi Ngày do Thời tiết Xấu |
| 4 | Vinmec | AI-upgrade | Tối ưu Quy trình Tiếp nhận & Phân loại Yêu cầu Cấp cứu Từ Mạng xã hội |
| 5 | Xanh SM | Stakeholder Pain | Phân loại & Phân công Xử lý Yêu cầu Hỗ trợ Tài xế |

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)

Chọn **top 3 bài toán** từ danh sách trên và hoàn thiện **3 Quick Problem Cards** dưới đây (10 phút/card).

### 📋 Mẫu Thẻ Bài Toán (Template):

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #___                                     │
│                                                             │
│ Bài toán (1 câu): ________________________________________  │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? ______________________________________ │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. ___ ──> 2. ___ ──> 3. ___ ──> 4. ___                   │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? ___ (⏱ ___ phút/lượt)      │
│ AI có thể nhảy vào hỗ trợ ở bước nào? _____________________ │
│                                                             │
│ Đo thành công bằng gì (Metric có số)? ______________________ │
│   VD: "Giảm thời gian soạn phản hồi từ 10 min ──> under 2 min"│
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [ ] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

---

### 📌 QUICK PROBLEM CARD #1 (VinFast)

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán (1 câu): Tự động trích xuất và phân tích log       │
│ telemetry để chẩn đoán mã lỗi xe VinFast từ xa, phân loại   │
│ hướng xử lý (OTA Update vs Kéo xe về Xưởng 3S).             │
│                                                             │
│ Công ty thành viên: [x] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Kỹ sư hỗ trợ kỹ thuật từ xa (Remote    │
│ Technical Support Engineer) & Khách hàng đi xe điện.        │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Nhận ticket báo lỗi đèn taplo từ xe/khách              │
│   ──> 2. Mở công cụ trích xuất thô hàng ngàn dòng log CAN-bus│
│   ──> 3. Tra cứu mã DTC trong tài liệu service manual        │
│   ──> 4. Phân loại & hướng dẫn khách (hoặc gọi cứu hộ)      │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3: Đọc và đối soát │
│ log CAN/BMS thủ công (⏱ 15 - 25 phút/lượt)                  │
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Phân tích tức thì     │
│ log telemetry thô (LLM/Parser), giải mã nguyên nhân gốc rễ   │
│ và soạn sẵn bản nháp hướng xử lý cho kỹ sư duyệt.           │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│   - Giảm thời gian chẩn đoán ban đầu từ 20 min ──> under 2 min│
│   - Giảm 30% tỷ lệ kéo xe không cần thiết về Xưởng dịch vụ  │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

---

### 📌 QUICK PROBLEM CARD #2 (Xanh SM)

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu): Phân loại đa kênh khiếu nại/yêu cầu hỗ trợ│
│ của tài xế Xanh SM, tự động trích xuất ngữ cảnh chuyến đi và│
│ phân công đúng đội phụ trách (Fleet/Bảo hiểm/Tổng đài).     │
│                                                             │
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Tài xế Xanh SM đang chạy trên đường &  │
│ Đội ngũ Trực ban Vận hành / CSKH Đối tác (Driver Support).   │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Nhận yêu cầu hỗ trợ (App/Voice/Zalo từ tài xế)         │
│   ──> 2. Đọc/nghe nội dung & tra cứu ID chuyến/GPS tài xế    │
│   ──> 3. Phân loại mức độ khẩn (va chạm/hết pin/tranh chấp) │
│   ──> 4. Chuyển tiếp ticket thủ công sang đội chuyên môn     │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3: Đọc hiểu ngữ   │
│ cảnh phản ánh và chuyển giao sai phòng ban (⏱ 5-8 phút/ticket)│
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? LLM đọc hiểu giọng nói/│
│ tin nhắn tài xế, trích xuất thực thể (biển số, vị trí, sự cố)│
│ và tự động gán nhãn độ ưu tiên (Priority Tagging) tức thì.   │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│   - Tốc độ phân loại & gán ticket: Dưới 15 giây/ticket       │
│   - Tỷ lệ gán đúng phòng ban ngay lần đầu (First Route): > 90%│
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

---

### 📌 QUICK PROBLEM CARD #3 (Vinpearl)

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán (1 câu): Trợ lý AI tự động đọc hiểu yêu cầu hoàn/   │
│ đổi vé VinWonders do ảnh hưởng thời tiết xấu, đối soát chính│
│ sách và tạo bản nháp phương án bồi hoàn cho CSKH phê duyệt. │
│                                                             │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [x] Khác: Vinpearl/Wonders │
│                                                             │
│ Ai đang đau (Actor)? Đội ngũ CSKH/Ticketing Vinpearl &      │
│ Khách du lịch bị hủy lịch trình do thời tiết dông bão.       │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Tiếp nhận tin nhắn/email khiếu nại dồn dập từ khách     │
│   ──> 2. Tra cứu mã QR vé trên hệ thống (đã quét cổng chưa) │
│   ──> 3. Kiểm tra báo cáo thời tiết trạm khí tượng tại đảo  │
│   ──> 4. Tính toán mức hoàn hủy theo chính sách & gửi khách │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 1 & 4: Đọc hiểu phân  │
│ trần từng ca khách và tính toán bù trừ vé (⏱ 10-15 phút/vé) │
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? LLM trích xuất mã vé, │
│ đối chiếu sự kiện thời tiết bất khả kháng và tự động soạn   │
│ thư phản hồi kèm đề xuất đổi ngày/bù voucher [DRAFT_ONLY].  │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│   - Giảm thời gian phản hồi ca hoàn hủy từ 24h ──> under 5 min│
│   - Tỷ lệ giải quyết khiếu nại thành công trong ngày: > 95%  │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

> [!TIP]
> **🤖 AI Prompts — Stress-Test thẻ bài toán:**
> Hãy dán nội dung thẻ bài toán của bạn vào LLM để nhận phản biện:
> *"Đây là một thẻ bài toán vận hành tôi đề xuất cho Vin Smart Future: [Dán nội dung]. Hãy đóng vai trò là một CFO và Trưởng phòng Vận hành cực kỳ khắt khe, chỉ ra cho tôi 3 điểm yếu về logic, metric, và giải thích vì sao rule-based code thông thường có thể giải quyết bài toán này tốt hơn là dùng AI."*

---
