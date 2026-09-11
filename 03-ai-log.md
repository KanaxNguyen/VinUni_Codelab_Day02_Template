# Lab 02 — 03-ai-log (AI Interaction Log & Reflection)

> **Cá nhân:** Trần Chí Vĩ
> **Ngày thực hiện:** 11/09/2026
> **Bài toán được chọn:** Phân loại & Điều hướng Khiếu nại Cư dân tự động — Vinhomes

---

# 📝 Phase 6 — REFLECTION: Nhật ký tương tác AI trong buổi Lab

## 1. AI đã giúp tôi điều gì?

Trong buổi Lab hôm nay, tôi đã sử dụng **Google Gemini** như một người đồng hành tư duy (thought-partner) xuyên suốt toàn bộ quá trình scoping bài toán AI.

**Cụ thể, AI đã hỗ trợ tôi trong các khâu sau:**

- **Brainstorm Phase 1 (SCAN):** Khi tôi chưa nghĩ ra đủ 5 bài toán, tôi dán vào AI prompt: *"Tôi là AI Engineer tại Vin Smart Future. Hãy gợi ý 5 pain point vận hành thực tế tại Vinhomes mà AI có thể giải quyết, kèm ước tính tổn thất."* AI trả về 8 bài toán chi tiết với con số ước tính, tôi chọn lọc và chỉnh lại thành 5 bài toán phù hợp nhất.

- **Stress-test Quick Problem Card (Phase 2):** Tôi dán nội dung Card #2 (Vinhomes phân loại khiếu nại) vào Gemini với prompt: *"Đóng vai CFO cực kỳ khắt khe, chỉ ra 3 điểm yếu về logic và vì sao Rule-based có thể tốt hơn AI."* AI chỉ ra rằng Rule-based với từ khóa cố định sẽ **nhanh hơn và rẻ hơn** nếu danh mục phân loại không quá phức tạp. Điều này buộc tôi phải bổ sung thêm lập luận về khả năng xử lý văn bản không dấu và viết tắt — điểm mà Rule-based không làm được.

- **Hỗ trợ viết Problem Statement 6-field (Phase 3):** Tôi đưa ra thông tin thô về bài toán và nhờ Gemini giúp diễn đạt lại trường **Business Impact** bằng ngôn ngữ định lượng hơn (con số giờ công lãng phí, tỉ lệ SLA vi phạm).

- **Thiết kế Operational Boundary:** Tôi nhờ AI đóng vai **Luật sư rủi ro** và hỏi: *"Ranh giới nào của AI Vinhomes có thể gây ra khiếu kiện pháp lý?"* Từ đó tôi phát hiện ra cần thêm điều khoản cấm AI tiết lộ thông tin cá nhân giữa các cư dân.

---

## 2. AI đã nói sai / Hallucinate ở đâu?

**Lần 1 — Số liệu thiếu căn cứ:**
Khi tôi hỏi Gemini *"Vinhomes Ocean Park có bao nhiêu ticket khiếu nại mỗi ngày?"*, AI trả lời rằng **"Vinhomes Ocean Park nhận khoảng 3,000–5,000 ticket mỗi ngày"** với vẻ rất tự tin. Đây là **hallucination** vì đây là số liệu nội bộ mà không AI nào có thể biết chính xác. Tôi đã tự điều chỉnh con số xuống còn **"500–2,000 ticket/ngày"** (ước tính thận trọng hơn) và ghi rõ đây là ước tính, không phải số liệu chính thức.

**Lần 2 — Đề xuất kiến trúc phức tạp hơn cần thiết:**
Gemini ban đầu đề xuất xây dựng **Multi-Agent System** với 3 agent (Intent Classifier, Department Router, Priority Scorer) cho bài toán này. Tôi nhận ra đây là over-engineering — một **LLM Feature đơn lẻ** với một structured JSON output là đủ để giải quyết bài toán mà không cần thêm độ phức tạp và chi phí. Nguyên tắc "Problem First, AI Second" giúp tôi nhận ra điều này.

**Lần 3 — Thiếu ràng buộc về data privacy:**
Khi Gemini giúp tôi viết Operational Boundary, AI không tự động đề cập đến rủi ro về bảo mật dữ liệu cư dân (PDPA). Tôi phải chủ động hỏi thêm về khía cạnh pháp lý mới có được câu trả lời đầy đủ hơn.

---

## 3. Tôi đã sửa prompt và ranh giới như thế nào?

| Vấn đề phát hiện | Cách sửa prompt / ranh giới |
|---|---|
| AI hallucinate số liệu ticket/ngày | Thêm vào prompt: *"Chỉ đưa ra ước tính thận trọng, không bịa số liệu nội bộ. Nếu không có dữ liệu, hãy nói rõ là ước tính."* |
| AI đề xuất kiến trúc phức tạp hơn cần | Thêm constraint: *"Ưu tiên giải pháp đơn giản nhất có thể giải quyết được bài toán. Giải thích tại sao LLM Feature là đủ trước khi đề xuất Agent."* |
| AI bỏ sót rủi ro privacy | Thêm role vào prompt: *"Hãy đóng thêm vai Data Privacy Officer và kiểm tra lại ranh giới vận hành."* |

---

## 4. Bài học rút ra

1. **AI là công cụ khuếch đại tư duy, không phải người ra quyết định.** Tất cả các số liệu, quyết định kiến trúc, và ranh giới vận hành cuối cùng đều phải được tôi tự kiểm chứng và chịu trách nhiệm.

2. **Cần chỉ định role cụ thể để AI có góc nhìn phản biện đa chiều.** Prompt *"Đóng vai CFO khắt khe"* hoặc *"Đóng vai Luật sư rủi ro"* hiệu quả hơn nhiều so với prompt chung *"Hãy phân tích bài toán này cho tôi."*

3. **Hallucination xuất hiện nhiều nhất khi hỏi về số liệu nội bộ.** Cần luôn yêu cầu AI ghi rõ nguồn gốc hoặc nói thẳng rằng đó là ước tính.
