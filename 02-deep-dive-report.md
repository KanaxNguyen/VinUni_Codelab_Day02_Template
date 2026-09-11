# Lab 02 — 02-deep-dive-report (Nhóm)

> **Dự án được chọn:** Phân loại và Điều hướng Khiếu nại / Yêu cầu của Cư dân tự động — **Vinhomes Resident Smart Routing**
> **Mảng kinh doanh:** Vinhomes — Quản lý đô thị thông minh

---

# 🏗️ Phase 3 — DEEP-DIVE

## 3.1. Current-State Workflow Mapping

Sơ đồ quy trình xử lý ticket khiếu nại **thủ công** hiện tại (xem ảnh `04-workflow-diagram.jpg`):

```text
┌─────────────────────┐        ┌─────────────────────┐        ┌─────────────────────┐        ┌─────────────────────┐
│       Bước 1        │        │       Bước 2        │        │       Bước 3        │        │       Bước 4        │
│   Cư dân gửi phản   │        │  Lễ tân/CSKH mở hệ  │        │  Lễ tân gán nhãn &  │        │  Bộ phận chuyên môn │
│   ánh qua App       │──🔄──▶ │  thống, đọc toàn bộ │──🔴──▶ │  forward thủ công   │──🔄──▶ │  tiếp nhận và đi xử │
│   Vinhomes Resident │        │  nội dung ticket     │        │  tới đúng phòng ban │        │  lý hiện trường     │
│                     │        │                     │        │                     │        │                     │
│  Actor: Cư dân      │        │  Actor: Lễ tân/CSKH │        │  Actor: Lễ tân/CSKH │        │  Actor: Kỹ thuật /  │
│  Tool: App Mobile   │        │  ⏱ ~2 phút/ticket   │        │  ⏱ ~1 phút 🔴       │        │  An ninh / Vệ sinh  │
│  In: Văn bản/Ảnh    │        │  In: Text + Ảnh     │        │  In: Kết quả đọc    │        │                     │
│  Out: Ticket mới    │        │  Out: Hiểu bài toán │        │  Out: FW Ticket     │        │                     │
└─────────────────────┘        └─────────────────────┘        └─────────────────────┘        └─────────────────────┘

🔴 = Bottleneck chính          🔄 = Handoff (điểm chuyển giao thông tin)

⏱ Tổng thời gian xử lý thủ công từ lúc gửi ticket đến khi bộ phận chuyên môn nhận được: ~3 phút/ticket
📊 Quy mô: Một khu đô thị lớn như Vinhomes Ocean Park nhận 500–2,000 ticket mỗi ngày.
💸 Tổng lãng phí: ~2,000 ticket × 3 phút = ~100 giờ công/ngày chỉ để "phân luồng".
```

**Ghi chú chi tiết các Bottleneck:**
- 🔴 **Bottleneck 1 (Bước 2):** Nội dung do cư dân gửi thường viết không dấu, tắt chữ, nhiều cảm xúc và mơ hồ (VD: *"lại mất điện nữa rồi bực quá"*, *"thang may hu"*). Lễ tân mất nhiều thời gian đọc, suy luận xem lỗi thuộc hạng mục nào.
- 🔴 **Bottleneck 2 (Bước 3):** Mỗi lễ tân một ca phải xử lý hàng chục ticket cùng lúc. Forwarding sai bộ phận khiến ticket bị "đá qua đá lại" giữa các team, SLA bị vi phạm.

---

## 3.2. Problem Statement (6-field) — Vin Smart Future Standard

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Nhân viên Chăm sóc khách hàng (CSKH) và Lễ tân trực tại sảnh các tòa nhà thuộc khu đô thị Vinhomes (VD: Ocean Park, Smart City, Grand Park). |
| **2. Current Workflow** | Khi cư dân gửi ticket qua App Vinhomes Resident, nhân viên CSKH mở hệ thống nội bộ, đọc toàn bộ nội dung (bao gồm cả ảnh đính kèm nếu có), tự đánh giá vấn đề thuộc phòng ban nào (Kỹ Thuật / An Ninh / Vệ Sinh Môi Trường / Hành Chính), gán tag thủ công và click forward. Toàn bộ quá trình này là thủ công 100%, không có bất kỳ hỗ trợ tự động nào. |
| **3. Bottleneck** | Lễ tân phải đọc và phân tích ngữ nghĩa từ văn bản không cấu trúc của cư dân — nhiều khi viết không dấu, viết tắt, sử dụng từ địa phương, hoặc mô tả rất mơ hồ. Đây là tác vụ hiểu ngôn ngữ tự nhiên mà con người phải xử lý lặp đi lặp lại hàng trăm lần mỗi ngày. |
| **4. Business Impact** | Một khu đô thị quy mô lớn nhận 500–2,000 ticket/ngày. Bottleneck phân loại tạo ra lãng phí ~100 giờ công/ngày. Ngoài ra, forward sai bộ phận (ước tính 10–15% ticket) khiến thời gian xử lý thực tế bị tăng gấp đôi, SLA bị vi phạm liên tục, và tỉ lệ hài lòng cư dân (CSAT) sụt giảm. |
| **5. Success Metric** | ① Tỉ lệ phân loại đúng bộ phận tự động đạt **≥ 95%** (benchmark hiện tại thủ công đạt ~88% do nhầm lẫn). <br> ② Thời gian từ lúc cư dân gửi ticket đến khi ticket xuất hiện trên dashboard bộ phận chuyên môn giảm từ **~3 phút → dưới 10 giây**. |
| **6. Operational Boundary** | **✅ AI ĐƯỢC PHÉP:** Đọc nội dung text và phân tích metadata của ticket; Gán nhãn phòng ban phụ trách (Kỹ Thuật / An Ninh / Vệ Sinh / Hành Chính); Tóm tắt nội dung phản ánh thành 1 câu ngắn gọn cho lễ tân và kỹ thuật viên đọc nhanh; Gán mức độ ưu tiên (Khẩn Cấp / Bình Thường). <br><br> **❌ AI TUYỆT ĐỐI KHÔNG ĐƯỢC:** Tự động trả lời trực tiếp với cư dân dưới bất kỳ hình thức nào; Tự động đóng/resolve ticket khi chưa có kỹ thuật viên xác nhận hoàn thành ngoài hiện trường; Chỉnh sửa hoặc xóa nội dung gốc của cư dân; Tiết lộ thông tin cá nhân giữa các cư dân với nhau. |

---

## 3.3. Future-State Flow & AI Fit

* **AI Fit Matrix:** **[x] LLM Feature** — AI đóng vai trò như một **Smart Router** thông minh. Không cần Agent tự trị vì quy trình có cấu trúc đầu ra cố định (phân loại vào 4 nhóm) và cần Human-in-the-loop để duyệt xử lý thực tế.

* **Lý do KHÔNG chọn Rule-based:** Rule-based keyword matching thất bại khi cư dân viết sai chính tả, viết tắt, hoặc dùng từ đồng nghĩa (VD: *"thang may"* vs *"thang máy"* vs *"cái thang bị hỏng"* vs *"lên xuống không được"*). LLM xử lý được tất cả các biến thể này.

* **Quy trình tương lai (Future-State Flow):**

```text
┌─────────────────────┐        ┌─────────────────────┐        ┌─────────────────────┐        ┌─────────────────────┐
│       Bước 1        │        │       Bước 2        │        │       Bước 3        │        │       Bước 4        │
│   Cư dân gửi phản   │        │  🔵 AI tự động đọc  │        │  🔵 AI gán nhãn &   │        │  🟢 CSKH/Kỹ thuật  │
│   ánh qua App       │──🔄──▶ │  & tóm tắt nội dung │──────▶ │  route đến đúng     │──🔄──▶ │  review ticket đã   │
│   Vinhomes Resident │        │  ticket             │        │  dashboard team     │        │  được gán nhãn &    │
│                     │        │                     │        │                     │        │  đi xử lý          │
│  Actor: Cư dân      │        │  Actor: Gemini LLM  │        │  Actor: Gemini LLM  │        │  Actor: Kỹ thuật /  │
│  ⏱ -               │        │  ⏱ < 3 giây         │        │  ⏱ < 2 giây         │        │  An ninh / Vệ sinh  │
└─────────────────────┘        └─────────────────────┘        └─────────────────────┘        └─────────────────────┘
                                                                        │
                                                                        ▼
                                                         ↩️ FALLBACK (Khi confidence < 80%):
                                                         AI đánh dấu ticket là [CẦN REVIEW]
                                                         và chuyển vào hàng đợi ưu tiên cho
                                                         CSKH trực đọc và phân loại thủ công.
                                                         
                                                         ↩️ FALLBACK (Khi nội dung khẩn cấp):
                                                         Nếu phát hiện từ ngữ nguy hiểm
                                                         (cháy, ngập, sự cố khẩn), AI tự động
                                                         gán nhãn [URGENT] và gửi thông báo
                                                         tức thời đến Quản lý trực ca.
```

---

# 🏁 Phase 5 — EVALUATE

### AI Readiness Checklist:
1. [x] **Có sẵn dữ liệu mẫu/logs sạch để test?**
   Vinhomes sở hữu kho lịch sử hàng triệu ticket cũ đã được nhân viên gán nhãn đúng thủ công. Đây là nguồn dữ liệu huấn luyện và đánh giá chất lượng cực kỳ giá trị.

2. [x] **Rủi ro khi AI sai có nằm trong tầm kiểm soát?**
   Kiểm soát được thông qua 2 cơ chế:
   - **HITL (Human-in-the-Loop):** Kỹ thuật viên nhận ticket có thể bấm *"Sai phòng ban"* để trả về hàng đợi CSKH duyệt lại trong 1 click.
   - **Fallback tự động:** Mọi ticket có confidence < 80% đều bị giữ lại và đánh dấu để con người duyệt trước khi gửi đi.

3. [x] **Stakeholders sẵn sàng thay đổi quy trình?**
   Nhân viên lễ tân muốn giảm tải việc trực màn hình suốt ca để tập trung đón và hỗ trợ cư dân trực tiếp tại sảnh. Ban Quản lý Vinhomes muốn cải thiện chỉ số CSAT và giảm SLA vi phạm để duy trì đẳng cấp thương hiệu đô thị cao cấp.

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:

**[x] ✅ GO — Bắt đầu xây dựng Prototype tại 1 tòa nhà thử nghiệm**

**Justification (Lý giải dựa trên bằng chứng kỹ thuật và chi phí):**

Dự án này đạt **GO** vì 4 lý do sau:

1. **Bài toán phù hợp với điểm mạnh cốt lõi của LLM:** Phân loại văn bản không cấu trúc, đa dạng từ ngữ, nhiều biến thể chính tả — đây là nơi LLM vượt trội tuyệt đối so với Rule-based. Rule-based keyword matching sẽ thất bại với hàng trăm cách viết khác nhau của cùng một vấn đề.

2. **Dữ liệu huấn luyện sẵn có:** Kho hàng triệu ticket lịch sử đã gán nhãn cho phép đánh giá và fine-tune mô hình ngay lập tức — không cần thu thập dữ liệu mới tốn kém.

3. **Rủi ro vận hành được kiểm soát chặt:** Cơ chế HITL và Fallback đảm bảo không có ticket nào bị mất hoặc xử lý sai mà không có con người kiểm tra. Worst-case scenario: ticket bị chậm vài giây, không phải bị xử lý sai.

4. **ROI rõ ràng và nhanh:** Tiết kiệm ~100 giờ công/ngày × chi phí nhân sự. Với scope triển khai hẹp tại 1 tòa nhà, kết quả đo lường được trong vòng 2 tuần.
