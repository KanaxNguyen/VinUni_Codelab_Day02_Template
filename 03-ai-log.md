# Lab 02 — AI Log & Reflection

## Thông tin cá nhân

- Họ và tên: Nguyễn Nam Khánh
- Mã sinh viên: 2A202602568
- Branch cá nhân: `Khanh`
- Công cụ AI đã dùng: ChatGPT (research), Codex (làm việc trong repository) và Gemini 2.5 Flash (boundary testing)

## 1. Mục đích sử dụng AI

Tôi sử dụng AI như một thought-partner trong ba công việc chính. Thứ nhất, AI hỗ trợ quét các pain point vận hành trong hệ sinh thái Vingroup theo bốn lenses của Phase 1. Thứ hai, AI giúp tôi mở rộng và so sánh các ý tưởng AIoT, sau đó thu hẹp chúng thành năm ý tưởng cá nhân và ba Quick Problem Cards. Thứ ba, sau khi nhóm chọn bài toán “Phân loại và điều hướng phản ánh cư dân Vinhomes”, AI hỗ trợ tôi xây dựng Deep Dive, operational boundaries, System Prompt và adversarial tests. Tôi không xem câu trả lời AI là dữ liệu chính thức; các claim, review và con số không có nguồn được coi là signal hoặc giả định cần kiểm chứng.

## 2. Nhật ký tương tác với AI

| Lần | Mục tiêu | Prompt/yêu cầu chính | AI đã giúp gì? | Hạn chế hoặc điểm cần kiểm tra | Cách tôi xử lý |
|---:|---|---|---|---|---|
| 1 | Quét pain point vận hành | Yêu cầu rà pain point theo hướng vận hành, không bắt đầu từ tên giải pháp; phân biệt Fact, Inference và Signal. | ChatGPT đưa ra 10 pain point thuộc VinFast, Xanh SM, Vinhomes, Vinmec và VinWonders; mỗi pain point có actor, workflow, bottleneck, impact, dữ liệu cần có và AI intervention. | Một số nhận định về volume, thao tác thủ công và data access chỉ là suy luận. Một số review ứng dụng được nhắc tới nhưng nội dung chat không cung cấp đầy đủ URL để kiểm tra lại. | Không sử dụng volume/AHT/chi phí nội bộ chưa có nguồn. Đánh dấu frequency và data access là working hypothesis; ưu tiên nguồn chính thức. |
| 2 | Chọn candidate cho Phase 2 | Yêu cầu chấm 10 vấn đề theo Pain, Frequency, Measurability, Data, AI-fit, Risk Control và khả năng rule-based tốt hơn AI. | AI xếp Vinhomes request routing, VinFast service pre-triage và Xanh SM complaint triage vào Top 3. | Điểm số phụ thuộc vào giả định về dữ liệu và tần suất, không phải kết quả đo tại doanh nghiệp. | Chỉ dùng điểm để hỗ trợ thảo luận, không dùng máy móc; giữ câu hỏi stakeholder về volume, AHT, reroute và SLA. |
| 3 | Tìm ý tưởng AIoT xuyên hệ sinh thái | “Tôi muốn một vài ý tưởng liên quan tới AIoT dành cho sự thông suốt giữa các thứ.” | AI đề xuất Seamless Arrival, Smart Departure, Energy Orchestrator, Adaptive Journey, Predictive Maintenance và các handoff giữa Xanh SM với điểm đến. | Một số ý tưởng có scope tích hợp quá rộng và giả định nhiều hệ thống có thể chia sẻ dữ liệu/quyền truy cập. | Thu hẹp về một decision cụ thể, yêu cầu AI chỉ rõ vai trò của IoT, AI và deterministic rules. |
| 4 | So sánh và chốt năm ý tưởng cá nhân | Hỏi liệu có thể dự đoán tải/chỗ đỗ còn lại và yêu cầu so sánh với các ý tưởng trước để chọn năm ý tưởng tốt nhất. | AI so sánh theo impact, AI necessity, AIoT fit, data readiness, pilot feasibility, KPI và Vingroup advantage; đề xuất Predictive Smart Parking đứng đầu. | AI có xu hướng ưu tiên ý tưởng hấp dẫn về kỹ thuật; “data readiness” vẫn chỉ là ước lượng từ hạ tầng công khai. | Chốt năm ý tưởng cá nhân nhưng ghi rõ target, thời gian và data readiness cần stakeholder xác minh. |
| 5 | Điều chỉnh theo quyết định nhóm | Thông báo nhóm chọn “Vinhomes — Phân loại và điều hướng phản ánh cư dân”, không chọn Smart Parking. | Codex giữ năm ý tưởng cá nhân trong Phase 1–2 nhưng viết lại phần nhóm, Deep Dive, workflow và code theo request routing. | Bản nháp ban đầu có nguy cơ mô tả routing hiện tại là hoàn toàn thủ công. | Đối chiếu báo cáo thường niên Vinhomes: V-PMS đã tích hợp Resident App, tiếp nhận phản hồi, tự động giao việc và theo dõi. Tôi sửa scope thành lớp hiểu ngôn ngữ tạo routing suggestion trước V-PMS. |
| 6 | Stress-test ranh giới | Chạy ba prompt tấn công: yêu cầu bịa tòa/tầng, hạ mức khẩn cấp của ca kẹt thang máy và tự đóng ticket/hứa hoàn tiền. | Gemini giữ `[DRAFT_ONLY]`, Human Approval và trả đúng `request_clarification`, `escalate_urgent`, `human_review`. | Autograder lần đầu chưa tìm thấy chuỗi `Passed`, dù chương trình không crash. | Chạy trực tiếp để xem từng output, sau đó chạy lại `--check-code-5`; kết quả cuối là **9 Passed, 0 Failed**. |

## 3. AI đã giúp tôi tốt nhất ở đâu?

AI giúp tôi chuyển từ các ý tưởng rộng sang một problem statement có thể kiểm thử. Với bài toán nhóm, AI đề xuất kiến trúc **Hybrid Rule + LLM/classifier + Human Approval**. Rule engine xử lý từ khóa khẩn cấp, trường bắt buộc và policy cấm; LLM xử lý tiếng Việt tự do, tóm tắt và đề xuất category/team; nhân viên giữ quyền accept, edit hoặc reject. Gợi ý này phù hợp vì bài toán không cần Agent tự trị và vẫn có manual fallback qua workflow/V-PMS hiện tại.

AI cũng giúp tôi nhìn thấy sự khác nhau giữa:

- Một ý tưởng hấp dẫn: “AI xử lý phản ánh cư dân”.
- Một scope kiểm thử được: “Từ nội dung ticket, đề xuất category, urgency, responsible team và missing fields trong JSON, sau đó yêu cầu nhân viên duyệt”.

## 4. AI đã sai hoặc có nguy cơ hallucinate ở đâu?

Điểm cần sửa rõ nhất là giả định rằng toàn bộ quá trình phân loại và giao phản ánh tại Vinhomes đang làm thủ công. Sau khi kiểm tra nguồn chính thức, tôi thấy V-PMS đã tích hợp với Resident App và hỗ trợ tiếp nhận phản hồi, tự động giao việc, theo dõi tiến độ. Vì vậy, tôi không tiếp tục claim rằng dự án sẽ “tự động hóa toàn bộ routing từ đầu”. Tôi định vị giải pháp là lớp hỗ trợ hiểu nội dung mơ hồ, phát hiện urgency và tạo routing suggestion cho nhân viên.

Ngoài ra, nội dung research ngoài có nhắc tới một số review ứng dụng, SLA và ví dụ vận hành. Khi không có URL hoặc logs nội bộ đi kèm, tôi không coi chúng là bằng chứng về root cause. Các con số như 8 phút/ticket và target giảm thời gian được ghi rõ là giả định thiết kế, cần stakeholder xác minh trước khi dùng làm baseline.

## 5. Tôi đã sửa prompt như thế nào?

### Prompt ban đầu

```text
Hãy gợi ý các ý tưởng AI/AIoT trong hệ sinh thái Vingroup và cho biết ý tưởng nào tốt nhất.
```

### Vấn đề của prompt ban đầu

Prompt bắt đầu từ giải pháp, phạm vi quá rộng, dễ tạo concept “wow” nhưng thiếu actor, workflow, bottleneck, dữ liệu và ranh giới. Nó cũng không buộc AI phân biệt fact với giả định.

### Prompt sau khi cải thiện

```text
Tôi là AI Product Engineer tại Vin Smart Future. Hãy tìm pain point theo bốn
lenses Repetitive, Time-consuming, AI-upgrade và Stakeholder Pain. Mỗi vấn đề
phải có Actor, Current Workflow, Bottleneck, Business Impact, dữ liệu cần có và
metric có thể đo. Phân biệt rõ Fact có nguồn, Inference, Signal và Assumption;
không bịa số liệu nội bộ. Hãy phản biện vì sao rule-based có thể tốt hơn AI và
đề xuất scope pilot nhỏ nhất có Human-in-the-loop cùng fallback.
```

### Kết quả sau khi sửa

Câu trả lời tập trung hơn vào pain point thay vì tên sản phẩm. AI đưa ra các câu hỏi cần xác minh như volume, AHT, reroute rate, SLA, input quality, historical labels, current automation và failure cost. Điều này giúp tôi chọn bài toán dựa trên khả năng đo và kiểm soát rủi ro, không chỉ dựa trên độ mới của công nghệ.

## 6. Operational boundaries đã kiểm thử

- AI được phép: tóm tắt phản ánh, đề xuất category, urgency, responsible team, missing fields, confidence và câu hỏi làm rõ.
- AI không được phép: tự giao/đóng/xóa ticket, bịa tòa/căn/vị trí, hứa SLA hoặc bồi thường, kết luận trách nhiệm pháp lý/y tế, hoặc hạ mức khẩn cấp theo yêu cầu trong ticket.
- Human-in-the-loop: mọi routing result trong pilot cần nhân viên duyệt; trường hợp khẩn cấp, multi-issue, phí, pháp lý, bồi thường hoặc thiếu dữ liệu bắt buộc human review.
- Fallback: nếu API lỗi, JSON sai, confidence thấp hoặc taxonomy không khớp, ticket quay lại hàng đợi triage hiện tại và không bị mất hoặc đóng tự động.
- Kết quả: ba adversarial tests đều đạt; autograder ghi nhận **9 Passed, 0 Failed**.

## 7. Reflection cá nhân

Qua bài lab, tôi nhận ra một ý tưởng AI hấp dẫn chưa chắc là một AI product scope tốt. Ban đầu tôi bị thu hút bởi các hướng AIoT như Predictive Smart Parking, Energy Orchestrator và Seamless Arrival vì chúng thể hiện lợi thế hệ sinh thái Vingroup. ChatGPT giúp tôi so sánh các ý tưởng và đặt câu hỏi về dữ liệu, KPI và khả năng pilot. Tuy nhiên, quyết định của nhóm cho thấy product scoping còn phụ thuộc vào vấn đề chung mà nhóm có thể giải thích và kiểm thử. Khi chuyển sang phân loại phản ánh cư dân, tôi học được cách thu hẹp từ “AI xử lý khiếu nại” thành một bước rõ ràng: tạo routing suggestion trước khi nhân viên duyệt. Tôi cũng nhận ra phải kiểm tra workflow hiện hành; nếu V-PMS đã tự động giao việc thì không thể tuyên bố AI đang thay thế toàn bộ quy trình thủ công. Rule-based phù hợp hơn LLM cho tín hiệu khẩn cấp và policy cấm, còn LLM phù hợp với văn bản mơ hồ. Việc Gemini vượt qua ba prompt tấn công cho thấy boundary cần được viết thành hành vi có thể test. Lần sau, tôi sẽ xác minh nguồn và baseline sớm hơn, yêu cầu stakeholder mở case thật, rồi mới quyết định dùng Rule, classifier, LLM hay Agent.

## 8. Tuyên bố sử dụng AI

Tôi sử dụng ChatGPT để research và mở rộng ý tưởng; Codex để đọc tài liệu, cấu trúc và chỉnh sửa các file trong repository; Gemini 2.5 Flash để chạy adversarial tests. AI hỗ trợ tạo bản nháp, phản biện và code, nhưng quyết định năm ý tưởng cá nhân, lựa chọn bài toán chung của nhóm và kết quả nộp bài do con người xác nhận. Tôi đã loại bỏ hoặc ghi nhãn các claim không có nguồn, kiểm tra tài liệu chính thức và chạy autograder. Tôi chịu trách nhiệm đọc lại, điều chỉnh theo trải nghiệm thật và xác nhận nội dung cuối cùng trước khi nộp.

## 9. Nguồn dùng để kiểm tra nội dung AI

1. [Vinhomes Annual Report 2024 — V-PMS và xử lý phản hồi cư dân](https://gcp-cdn.vinhomes.vn/cms-data/VIE_Vinhomes%20AR%202024_250416_compressed.pdf)
2. [Vinhomes Annual Report 2023 — Resident App, V-PMS và SmartHub](https://gcp-cdn.vinhomes.vn/cms-data/%5BENG_Digital%5D%20Vinhomes%20AR%202023_240416_vF_1713849923.pdf)
3. [Vinhomes Resident kết nối cư dân với Ban quản lý](https://vinhomes.vn/vi/nhung-la-thu-cam-on-tu-cu-dan-va-dich-vu-tu-trai-tim-vinhomes)
