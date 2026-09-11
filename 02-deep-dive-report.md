# 🏗️ Phase 3 — DEEP-DIVE (Nhóm, 85 min)

> **Dự án:** Vinhomes Resident Incident Triage & Dispatch Copilot  
> **Đơn vị công tác:** Khối AI Vận hành — Vin Smart Future (Phối hợp cùng Ban Quản lý Vinhomes)  
> **Chủ đề lựa chọn:** Phân loại, điều hướng và tự động hóa phản hồi phản ánh của cư dân tại các đại đô thị Vinhomes.

---

## 3.1. Current-State Workflow Mapping (25 min)

Quy trình tiếp nhận và xử lý sự cố/phản ánh thủ công hiện tại của Lễ tân & Trực ban Ban Quản lý (BQL) Vinhomes:

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Tiếp nhận    │     │ Đọc hiểu &   │     │ Tra cứu căn  │     │ Soạn văn bản │
│ phản ánh     │ ──→ │ Phân loại    │ ──→ │ hộ & Phân cấp│ ──→ │ phản hồi     │
│ qua App/Call │     │ sự cố        │     │ xử lý        │     │ gửi cư dân   │
│              │     │              │     │              │     │              │
│ Ai: Lễ tân   │     │ Ai: Trực ban │     │ Ai: Trực ban │     │ Ai: Trực ban │
│ ⏱ 2 phút     │     │ ⏱ 5 phút 🔴  │     │ ⏱ 4 phút 🔴  │     │ ⏱ 5 phút 🔴  │
│ In: Ticket thô│    │ In: Text/Ảnh │     │ In: Sổ tay BQL│   │ In: Dữ liệu  │
│ Out: Log việc│     │ Out: Nhóm lỗi│     │ Out: Team ID │     │ Out: Tin nhắn│
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                                      ▼
                                                               ┌──────────────┐
                                                               │ Bước 5 🔄    │
                                                               │ Điều phối    │
                                                               │ đội thực địa │
                                                               │ (MEP/An ninh)│
                                                               │              │
                                                               │ Ai: Trực ban │
                                                               │ ⏱ 2 phút     │
                                                               └──────────────┘

🔴 = Bottlenecks (Gây trễ SLA, tốn năng lực đọc hiểu & soạn văn bản thủ công)
🔄 = Handoff (Điểm chuyển giao thông tin giữa BQL và Đội Kỹ thuật/An ninh thực địa)
⏱ Tổng thời gian vận hành trung bình: 18 phút / phản ánh.
```

---

## 3.2. Problem Statement (6-field) & Metrics (15 min)

Điền đầy đủ 6 trường thông tin chuẩn của Vin Smart Future:

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Nhân viên Lễ tân tòa nhà, Trực ban Chăm sóc Khách hàng và Điều phối viên Vận hành tại Ban Quản lý (BQL) các Khu đô thị Vinhomes (Ocean Park, Smart City, Grand Park...). |
| **2. Current Workflow** | Cư dân gửi phản ánh (tiếng ồn, thấm dột, mùi rác, vi phạm đỗ xe, hỏng thang máy) qua App *Vinhomes Resident* hoặc hotline. Nhân viên BQL đọc từng nội dung text/ảnh, phân loại mức độ khẩn cấp, mở sổ tay quy trình BQL để tìm đội phụ trách (Kỹ thuật MEP, Ban An ninh, Nhà thầu cây xanh/vệ sinh), gõ tin nhắn phản hồi tiếp nhận hẹn giờ xử lý cho cư dân, và gọi điện/nhắn Zalo giao việc cho đội thực địa. **5 bước thủ công, mất trung bình 18 phút/lượt.** |
| **3. Bottleneck** | **Bước 2, 3 & 4 (chiếm 14/18 phút):**<br>1. *Xử lý ngôn ngữ tự nhiên không cấu trúc:* Cư dân phản ánh bằng câu từ cảm xúc, viết tắt, hoặc đính kèm nhiều ảnh phức tạp.<br>2. *Tra cứu ma trận phân quyền BQL:* Mất thời gian xác định sự cố thuộc trách nhiệm BQL, Chủ đầu tư hay Nhà thầu bảo hành căn hộ.<br>3. *Soạn thảo phản hồi:* Nhân viên phải căn chỉnh câu từ lịch sự, chuẩn mực dịch vụ 5 sao của Vinhomes nhưng không được hứa hẹn sai thẩm quyền. |
| **4. Business Impact** | - Mỗi đại đô thị tiếp nhận **150 – 300 phản ánh/ngày** (lên tới 500+ lượt vào mùa mưa bão hoặc bàn giao phân khu mới).<br>- Tốn **45 – 90 giờ công lao động/ngày** chỉ để phân luồng và trả lời tin nhắn.<br>- Tỉ lệ trễ hạn SLA phản hồi (> 30 phút) lên đến 22%, khiến cư dân bức xúc đăng bài tiêu cực lên các hội nhóm cư dân mạng xã hội (Facebook/TikTok), gây ảnh hưởng nghiêm trọng đến uy tín thương hiệu bất động sản số 1 Việt Nam của Vinhomes. |
| **5. Success Metric** | 1. **Efficiency:** Giảm thời gian từ lúc nhận phản ánh đến khi có bản nháp điều phối từ 18 phút ──> **dưới 2 phút** (giảm gần 90% thời gian).<br>2. **Routing Accuracy:** Tỉ lệ phân loại và điều phối đúng đội chuyên trách ngay từ lần đầu đạt **≥ 95%**.<br>3. **SLA First Response:** 100% cư dân nhận được phản hồi tiếp nhận xác nhận lịch kiểm tra trong vòng **dưới 5 phút**. |
| **6. Operational Boundary** | **AI ĐƯỢC PHÉP:**<br>- Trích xuất tự động: Mã căn hộ, loại sự cố (Ồn ào, Kỹ thuật, Môi trường, An ninh), mức độ khẩn cấp (P1-Khẩn cấp đến P4-Thường).<br>- Tự động tra cứu quy định vận hành BQL và đề xuất đội phụ trách phù hợp.<br>- Tự động tạo bản nháp phản hồi gửi cư dân gắn nhãn `[DRAFT_ONLY]` và lịch hẹn dự kiến.<br><br>⚠️ **AI TUYỆT ĐỐI CẤM (Strict Boundaries):**<br>1. **KHÔNG tự ý cam kết đền bù tài chính/miễn giảm phí dịch vụ** hoặc thừa nhận lỗi pháp lý của BQL khi chưa có kết luận giám định.<br>2. **KHÔNG tự động gửi tin nhắn đến cư dân** khi chưa có Trực ban BQL bấm nút **Duyệt (Approve)** (Bắt buộc Human-In-The-Loop - HITL).<br>3. **Đối với sự cố Đỏ (Cháy nổ, Kẹt thang máy, Tràn nước hầm):** Phải kích hoạt còi báo động khẩn cấp (Red Alert) trên màn hình điều hành trong ≤ 5 giây thay vì xử lý theo luồng ticket thông thường. |

---

## 3.3. Future-State Flow & AI Fit (25 min)

* **Xác định mức AI Fit:** Chọn **LLM Feature kết hợp Rule-based Router (Hybrid Architecture)**.
  * *Lý do:* LLM làm xuất sắc việc đọc hiểu văn bản cảm xúc, trích xuất thực thể và soạn thư phản hồi mềm mỏng, lịch thiệp. Nhưng cần Rule-based để khóa các ranh giới an toàn (không đền bù tiền, lọc từ khóa khẩn cấp cứu hỏa/cứu nạn). Không cần Agentic Loop phức tạp để tránh rủi ro tự hành sai sót.
* **Quy trình tương lai (Future-State Flow):**

```text
┌─────────────────┐     ┌──────────────────────┐     ┌──────────────────────┐     ┌──────────────────────┐
│ Bước 1          │     │ Bước 2 (🔵 AI Step)  │     │ Bước 3 (🔵 AI Step)  │     │ Bước 4 (🟢 HITL)     │
│ Cư dân gửi      │ ──→ │ LLM phân tích text/  │ ──→ │ LLM tạo [DRAFT_ONLY] │ ──→ │ Trực ban BQL         │
│ phản ánh        │     │ ảnh, trích xuất ID,  │     │ câu trả lời cư dân + │     │ kiểm tra 1-click     │
│ qua App Vinhomes│     │ gán Priority & Đội   │     │ lệnh Dispatch việc   │     │ Duyệt & Gửi tin      │
└─────────────────┘     └──────────────────────┘     └──────────────────────┘     └──────────────────────┘
                                                                                                 │
                                                                                                 ▼
                                                                                          ┌──────────────┐
                                                                                          │ ↩️ Fallback   │
                                                                                          │ Nếu AI điểm  │
                                                                                          │ tin cậy thấp │
                                                                                          │ (<80%), cảnh │
                                                                                          │ báo BQL xử lý│
                                                                                          │ thủ công     │
                                                                                          └──────────────┘
```

---

# 🏁 Phase 5 — EVALUATE (Nhóm, 20 min)

### AI Readiness Checklist:
1. [x] **Dữ liệu mẫu:** Chúng tôi có sẵn kho dữ liệu lịch sử hàng chục ngàn ticket phản ánh và nhật ký xử lý trên hệ thống ERP/CRM của Vinhomes để fine-tune và làm benchmark test.
2. [x] **Kiểm soát rủi ro:** Cơ chế Human-in-the-loop (BQL duyệt trước khi gửi) và tiền tố `[DRAFT_ONLY]` đảm bảo loại bỏ 100% rủi ro phát ngôn sai chính sách hoặc ảo giác AI.
3. [x] **Sự sẵn sàng của Stakeholders:** Ban Quản lý Vinhomes đang rất cần giảm tải áp lực trực ban ca đêm và giờ cao điểm, cam kết hỗ trợ tích hợp thử nghiệm vào luồng App cư dân.

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:
* [x] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển với scope hẹp (Module phân loại sự cố & Soạn nháp phản hồi CSKH cho Đại đô thị Vinhomes Ocean Park).
* [ ] **NOT YET (Cần tích lũy thêm dữ liệu/xác lập baseline)**
* [ ] **NO-GO (Không khả thi / Rule-based tốt hơn)**

**Justification (Lý giải quyết định dựa trên bằng chứng kỹ thuật và chi phí):**
> 1. **Hiệu quả kinh tế (ROI cao):** Tiết kiệm hơn 70% thời gian trực ban của đội ngũ BQL (ước tính tiết kiệm ~1.200 giờ làm việc/tháng trên mỗi cụm tòa nhà), giúp nhân sự tập trung vào việc đi kiểm tra chất lượng thực địa thay vì ngồi gõ máy tính.
> 2. **Bảo vệ thương hiệu & Giữ vững chuẩn sống 5 sao:** Giải quyết triệt để nút thắt cư dân bức xúc vì phản hồi chậm trễ, nâng tỉ lệ xử lý đúng hạn SLA lên trên 98%.
> 3. **Tính khả thi kỹ thuật vượt trội:** Sử dụng mô hình ngôn ngữ lớn (Gemini 2.5 Flash) xử lý Tiếng Việt rất tự nhiên, chi phí API cực thấp (~0.001 USD/ticket), kiến trúc tích hợp dạng Copilot an toàn tuyệt đối.
