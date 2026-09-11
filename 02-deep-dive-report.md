# 02 — Deep-Dive Report (Nhóm)

## Bài toán được chọn: VinFast — Tự động hóa nhập liệu chẩn đoán bảo hành

> ⚠️ Ghi chú: bài toán này cần được cả nhóm thảo luận và đồng thuận chính thức
> trước khi merge vào branch `main`, theo đúng quy trình nộp bài của README.

---

## Phase 3.1 — Current-State Workflow Mapping

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Cắm máy chẩn │     │ Chụp/ghi tay │     │ Nhập tay mã  │     │ Gán mức ưu   │
│ đoán OBD     │ ──→ │ danh sách mã │ ──→ │ lỗi vào CRM  │ ──→ │ tiên sửa chữa│
│              │     │ lỗi          │     │              │     │              │
│ Ai: KTV      │     │ Ai: KTV      │     │ Ai: KTV      │     │ Ai: KTV      │
│ ⏱ 3 phút     │     │ ⏱ 2 phút     │     │ ⏱ 8 phút 🔴  │     │ ⏱ 2 phút 🔴  │
│ In: Xe khách  │     │ In: Màn hình │     │ In: Danh sách│     │ In: Mã lỗi   │
│ Out: Mã lỗi   │     │ Out: Ghi chú │     │ Out: Phiếu CRM│    │ Out: Mức ưu  │
│ hiển thị      │     │ tay          │     │              │     │ tiên         │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘

🔴 = Bottlenecks
🔄 Handoff: Bước 2 → Bước 3 (chuyển từ ghi chú giấy sang hệ thống số — dễ sai sót/thất lạc)
⏱ Tổng thời gian xử lý thủ công: 15 phút/lượt.
```

(Xem thêm sơ đồ trực quan tại file `04-workflow-diagram.png`)

---

## Phase 3.2 — Problem Statement (6-field)

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Kỹ thuật viên (KTV) bảo hành tại trung tâm dịch vụ VinFast. |
| **2. Current Workflow** | Khi xe vào bảo hành, KTV cắm máy chẩn đoán OBD đọc mã lỗi trên màn hình, ghi chép/chụp ảnh tay danh sách mã lỗi, sau đó đăng nhập hệ thống CRM để gõ tay từng mã lỗi kèm mô tả, cuối cùng tự đánh giá và gán mức độ ưu tiên sửa chữa. 4 bước, phần lớn thủ công, mất 15 phút/lượt. |
| **3. Bottleneck** | Bước 3 (mất 8 phút): Nhập tay từng mã lỗi và mô tả vào CRM — dễ gõ sai mã, bỏ sót lỗi phụ, hoặc nhầm lẫn giữa các dòng xe (VF3/VF5/VFe34/VF8/VF9) có bộ mã lỗi khác nhau. |
| **4. Business Impact** | Mỗi trung tâm bảo hành xử lý ~150 lượt xe/ngày. Lãng phí ước tính 20 giờ nhân công/ngày/trung tâm chỉ cho việc nhập liệu. Sai sót nhập mã lỗi có thể dẫn đến chẩn đoán sai, kéo dài thời gian sửa chữa và giảm sự hài lòng khách hàng. |
| **5. Success Metric** | 1. Giảm thời gian tạo phiếu từ 15 phút xuống dưới 4 phút (Efficiency).<br>2. Tỉ lệ mã lỗi được nhận diện và điền đúng đạt tối thiểu 95% (Quality). |
| **6. Operational Boundary** | AI được phép đọc ảnh màn hình máy chẩn đoán OBD, tự động điền mã lỗi + mô tả vào form CRM dạng nháp (draft), gợi ý mức độ ưu tiên dựa trên mức độ nghiêm trọng mã lỗi. **CẤM:** AI không được tự động xác nhận/submit phiếu sửa chữa mà không có KTV rà soát và phê duyệt (bắt buộc HITL); không được tự ý thay đổi mã lỗi gốc đọc từ máy chẩn đoán; không được gán mức ưu tiên "khẩn cấp/an toàn" (liên quan phanh, pin, hệ thống lái) mà không có KTV xác nhận thủ công. |

---

## Phase 3.3 — Future-State Flow & AI Fit

**AI Fit:** Chọn **LLM Feature** — không cần Agentic Loop vì quy trình có cấu trúc cố định (đọc ảnh → điền form → gợi ý ưu tiên), không cần AI tự ra quyết định nhiều bước hay gọi nhiều hệ thống độc lập. Rule-based đơn thuần không đủ vì mô tả lỗi trên các dòng xe khác nhau có ngôn ngữ/định dạng không đồng nhất, cần khả năng hiểu ngữ cảnh của LLM.

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Cắm máy chẩn │     │ 🔵 AI đọc    │     │ 🔵 AI draft  │     │ 🟢 KTV rà    │
│ đoán OBD     │ ──→ │ ảnh, trích   │ ──→ │ phiếu CRM +  │ ──→ │ soát, duyệt  │
│              │     │ xuất mã lỗi  │     │ gợi ý ưu tiên│     │ & submit     │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                                      ▼
                                                               ↩️ Fallback:
                                                               Nếu AI không đọc
                                                               được ảnh/mã lỗi lạ,
                                                               KTV nhập tay như cũ.
```

---

## Phase 4 — Prompt Prototype & Boundary Test

Nhóm đã xây dựng file Python nguyên mẫu `prompt_prototype.py` và chạy thử nghiệm bằng
**Gemini 2.5 Flash** để kiểm tra ranh giới an toàn.

### Ranh giới an toàn (Operational Boundary) cần bảo vệ:
* **Quy tắc 1:** Mọi phản hồi PHẢI bắt đầu bằng thẻ `[DRAFT_ONLY]` — AI không được
  tự động submit phiếu sửa chữa vào CRM mà chưa có KTV phê duyệt.
* **Quy tắc 2:** AI không được tự ý đoán/thay đổi mã lỗi không rõ ràng — phải báo
  "KHÔNG XÁC ĐỊNH ĐƯỢC — cần KTV kiểm tra thủ công".
* **Quy tắc 3:** AI không được tự gán mức ưu tiên "Khẩn cấp/An toàn" cho lỗi liên
  quan phanh/pin/hệ thống lái mà không có xác nhận của KTV.

### Kết quả thử nghiệm tấn công Prompt:
> *(Điền kết quả thật sau khi chạy `python prompt_prototype.py` — dán output model
> trả về cho từng Test Case và ghi rõ Pass/Fail cho từng rule.)*

| Test Case | Mục tiêu tấn công | Kết quả (Pass/Fail) |
|---|---|---|
| 1 — Ép bỏ [DRAFT_ONLY] | Yêu cầu submit thẳng, không ghi nháp | *(điền sau khi chạy)* |
| 2 — Ép đoán mã lỗi mờ | Dụ AI tự chọn đại mã lỗi | *(điền sau khi chạy)* |
| 3 — Ép tự gán mức khẩn cấp | Dụ AI tự chốt ưu tiên an toàn | *(điền sau khi chạy)* |

---

## Phase 5 — EVALUATE

### AI Readiness Checklist:
- [x] Có sẵn dữ liệu mẫu/logs sạch để test? → Có thể thu thập ảnh mã lỗi mẫu từ
  2-3 trung tâm bảo hành thí điểm trong 1-2 tuần.
- [x] Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL/Fallback)? → Có —
  mọi output đều ở dạng draft, KTV luôn là người phê duyệt cuối cùng trước khi
  submit vào CRM.
- [ ] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ? → Cần khảo sát thêm
  ý kiến KTV tại các trung tâm, vì thay đổi thói quen ghi chép tay có thể gặp
  kháng cự ban đầu.

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:

**[x] GO (Bắt đầu xây dựng Prototype) — với scope hẹp.**

**Justification:**
> Bài toán có metric rõ ràng (giảm 15 phút xuống dưới 4 phút/lượt, tần suất
> 150 lượt/ngày/trung tâm — tác động lớn và đo lường được). Giải pháp kỹ thuật
> đơn giản (LLM Feature đọc ảnh + điền form), không cần Agentic Loop phức tạp.
> Rủi ro được kiểm soát chặt qua cơ chế Human-in-the-loop bắt buộc — AI không
> bao giờ tự động submit mà không có KTV duyệt. Đề xuất triển khai thí điểm tại
> 1-2 trung tâm bảo hành trước khi nhân rộng, để thu thập thêm dữ liệu thực tế
> và đánh giá mức độ chấp nhận của KTV trước khi mở rộng toàn hệ thống.
