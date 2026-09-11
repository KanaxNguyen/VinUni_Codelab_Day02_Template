# Lab 02 — Phase 1 & 2: Problem Scan and Quick Assessment

## Thông tin cá nhân

- Họ và tên: Nguyễn Nam Khánh
- Mã sinh viên: 2A202602568
- Branch cá nhân: `Khanh`

> Các target và thời gian vận hành bên dưới là giả định thiết kế cho bài lab, chưa phải số liệu nội bộ của Vinhomes/Vingroup. Nhóm phải xác minh bằng logs hoặc phỏng vấn stakeholder trước khi dùng làm baseline chính thức.

## Phase 1 — SCAN

### Năm cơ hội AIoT được lựa chọn

| # | Công ty thành viên | Lens | Actor | Mô tả bài toán/bottleneck | Business impact | Nguồn hoặc giả định |
|---|---|---|---|---|---|---|
| 1 | Vinhomes | AI-upgrade | Cư dân/khách lái xe và Ban quản lý bãi đỗ | Smart parking hiện có có thể hiển thị chỗ trống hiện tại, nhưng số chỗ có thể thay đổi trong thời gian xe di chuyển. Người lái cần biết xác suất còn chỗ tại thời điểm dự kiến đến, không chỉ trạng thái ở thời điểm truy vấn. | Giảm thời gian chạy vòng tìm chỗ, ùn tắc nội khu và tải hỗ trợ cho nhân viên bãi xe; tăng khả năng sử dụng hiệu quả các zone. | Vinhomes công bố ứng dụng tìm chỗ đỗ, cảm biến và chỉ dẫn; nhu cầu dự báo tại ETA là đề xuất mở rộng, chưa phải mô tả tính năng hiện hành. |
| 2 | Vinhomes × VinFast | Time-consuming | Cư dân sở hữu EV và đơn vị vận hành điện/năng lượng | Nếu nhiều xe cùng sạc vào giờ cao điểm, hệ thống cần quyết định xe nào sạc lúc nào và ở công suất bao nhiêu trong giới hạn hạ tầng, nhu cầu di chuyển và mức pin. Điều phối tĩnh không thích nghi tốt với nhu cầu thay đổi. | Giảm đỉnh phụ tải, tránh quá tải cục bộ, tận dụng giờ thấp điểm và tăng khả năng xe đạt mức pin cần thiết trước giờ khởi hành. | Vinhomes công bố IoT cho quản lý năng lượng; VinFast công bố hệ thống tìm trạm sạc. Logic orchestration và KPI là giả thuyết cần dữ liệu kỹ thuật. |
| 3 | Vinhomes × VinFast | AI-upgrade | Cư dân, khách và hệ thống vận hành tòa nhà | Khi người dùng sắp về hoặc rời nhà, các hệ thống cổng, bãi xe, thang máy, chiếu sáng và sạc hoạt động rời rạc. Khó suy luận đúng ý định và phối hợp đúng thời điểm mà không tạo trải nghiệm xâm phạm riêng tư. | Có thể giảm thao tác chờ và tạo hành trình liền mạch, nhưng sai dự đoán có thể gây phiền, mở sai quyền truy cập hoặc tăng rủi ro riêng tư. | Vinhomes công bố app cư dân, kiểm soát ra vào và hệ sinh thái kết nối; orchestration theo ý định là đề xuất mới. |
| 4 | Vinhomes / Vinpearl / VinWonders | Repetitive | Kỹ thuật viên bảo trì và quản lý vận hành | Thiết bị như thang máy, HVAC, bơm, máy phát hoặc trò chơi cần kiểm tra định kỳ. Lịch bảo trì cố định có thể bỏ sót dấu hiệu bất thường giữa hai kỳ hoặc thay linh kiện khi chưa cần thiết. | Giảm downtime ngoài kế hoạch, ưu tiên đúng work order và sử dụng hiệu quả nhân lực/phụ tùng; rủi ro là cảnh báo giả hoặc bỏ sót lỗi. | Cần kiểm kê thiết bị, lịch sử sự cố và dữ liệu cảm biến thực tế; chưa có dữ liệu nội bộ trong repository. |
| 5 | VinWonders | Stakeholder Pain | Khách tham quan và nhân viên điều phối | Bản đồ tĩnh không phản ánh đầy đủ hàng đợi, thời tiết, lịch biểu diễn, độ tuổi, khả năng tiếp cận và vị trí hiện tại. Khách có thể đi đến điểm quá tải hoặc bỏ lỡ hoạt động phù hợp. | Phân bổ dòng khách tốt hơn, giảm thời gian chờ và tăng mức hài lòng; cần tránh thu thập vị trí quá mức hoặc điều hướng thiếu an toàn. | VinWonders có bản đồ điểm đến trực tuyến; cá nhân hóa hành trình theo trạng thái thời gian thực là đề xuất mới. |

### Chấm điểm để chọn Top 3

Thang điểm 1–5. “Có dữ liệu” được chấm theo mức dữ liệu có khả năng tồn tại trong hệ thống, không khẳng định nhóm đã được cấp quyền truy cập.

| Bài toán | Mức độ ảnh hưởng | Tần suất | Dễ đo kết quả | Có dữ liệu | Phù hợp với AI | Tổng /25 |
|---|---:|---:|---:|---:|---:|---:|
| #1 — Predictive Smart Parking | 5 | 5 | 5 | 4 | 5 | **24** |
| #2 — AI Energy & Charging Orchestrator | 5 | 5 | 5 | 3 | 5 | **23** |
| #3 — Seamless Arrival/Departure | 4 | 5 | 3 | 2 | 4 | **18** |
| #4 — Predictive Maintenance | 5 | 4 | 5 | 4 | 4 | **22** |
| #5 — Adaptive Physical Journey | 4 | 4 | 4 | 3 | 4 | **19** |

### Top 3 được chốt

1. **Predictive Smart Parking — 24/25:** phạm vi cụ thể, đầu ra dự báo rõ, có thể đo offline và pilot, đồng thời tận dụng nền tảng smart parking hiện có.
2. **AI Energy & Charging Orchestrator — 23/25:** tác động năng lượng lớn và decision rõ, nhưng cần dữ liệu pin, lịch khởi hành và giới hạn công suất nhạy cảm.
3. **Predictive Maintenance — 22/25:** giá trị vận hành cao, nhưng cần lịch sử hỏng hóc đủ dài và định nghĩa failure label đáng tin cậy.

Không chọn #3 vì phạm vi tích hợp quá rộng và rủi ro riêng tư/quyền truy cập cao. Không chọn #5 vì trạng thái thời gian thực và mục tiêu hành trình của từng khách khó quan sát chính xác trong giai đoạn đầu.

## Phase 2 — QUICK-ASSESS

### Quick Problem Card 1 — Predictive Smart Parking

- Bài toán trong một câu: Dự báo số chỗ và mức độ còn chỗ ở từng parking zone tại thời điểm xe đến để hỗ trợ người lái chọn zone phù hợp.
- Công ty thành viên: Vinhomes.
- Actor: Cư dân/khách lái xe; Ban quản lý bãi đỗ là operator.
- Workflow hiện tại:
  1. Người dùng kiểm tra chỗ trống hiện tại trên ứng dụng hoặc bảng chỉ dẫn.
  2. Người dùng chọn một zone và di chuyển đến đó.
  3. Trong thời gian di chuyển, xe khác vào/ra làm trạng thái thay đổi.
  4. Nếu zone đầy khi đến, người dùng tìm zone khác hoặc nhờ nhân viên hỗ trợ.
- Bước tốn thời gian hoặc dễ lỗi nhất: Bước 3–4, vì thông tin hiện tại có thể không còn đúng tại ETA.
- Thời gian hiện tại: Chưa có baseline nội bộ; cần đo median/P90 “gate-in đến park-confirmed” trong ít nhất hai tuần.
- AI có thể hỗ trợ ở bước: dự báo occupancy 5/10/15/30 phút tới theo zone và xếp hạng phương án tại ETA.
- Success metric: trong pilot, MAE dự báo occupancy 15 phút không quá 10 điểm phần trăm; giảm ít nhất 30% median search time so với baseline; không tăng số lượt dẫn tới zone đầy.
- Quick Architecture: Predictive ML/time-series + rule-based recommendation; LLM chỉ giải thích khuyến nghị nếu cần.
- Rủi ro chính: dữ liệu cảm biến sai, concept drift, ETA sai, dự báo bị hiểu nhầm là giữ chỗ.
- Human-in-the-loop: Ban quản lý theo dõi dashboard, xử lý sự cố cảm biến và có quyền tắt khuyến nghị theo zone.

### Quick Problem Card 2 — AI Energy & Charging Orchestrator

- Bài toán trong một câu: Lập lịch sạc EV theo mức pin, giờ rời đi, giới hạn công suất tòa nhà và biểu giá để tránh đỉnh tải nhưng vẫn đáp ứng nhu cầu cư dân.
- Công ty thành viên: Vinhomes × VinFast.
- Actor: Cư dân sở hữu EV; kỹ sư năng lượng và Ban quản lý.
- Workflow hiện tại:
  1. Xe cắm sạc và gửi nhu cầu sạc.
  2. Hệ thống kiểm tra công suất khả dụng.
  3. Các xe sạc theo lịch hoặc giới hạn tĩnh.
  4. Kỹ sư can thiệp khi quá tải hoặc có ưu tiên đặc biệt.
- Bước tốn thời gian hoặc dễ lỗi nhất: phân bổ đồng thời cho nhiều xe khi nhu cầu và phụ tải thay đổi.
- Thời gian hiện tại: chưa có baseline; cần logs công suất theo phút và dữ liệu phiên sạc.
- AI có thể hỗ trợ ở bước: dự báo nhu cầu và đề xuất lịch/công suất; lớp tối ưu hóa có ràng buộc đưa ra quyết định cuối.
- Success metric: giảm peak kW ít nhất 15% trong pilot mà ít nhất 95% phiên đạt mức pin người dùng yêu cầu trước giờ rời đi. Đây là target giả định cần kỹ sư điện phê duyệt.
- Quick Architecture: Forecasting ML + constrained optimization/rules, không dùng LLM để điều khiển công suất trực tiếp.
- Rủi ro chính: sai dự báo làm xe thiếu pin hoặc vượt giới hạn điện.
- Human-in-the-loop: kỹ sư đặt ngưỡng tải, phê duyệt policy và có emergency override.

### Quick Problem Card 3 — Predictive Maintenance

- Bài toán trong một câu: Ước lượng nguy cơ thiết bị hỏng trong một khoảng thời gian để ưu tiên kiểm tra trước khi gây downtime.
- Công ty thành viên: pilot tại Vinhomes trước, sau đó mới cân nhắc Vinpearl/VinWonders.
- Actor: Kỹ thuật viên bảo trì và quản lý vận hành.
- Workflow hiện tại:
  1. Thiết bị gửi telemetry hoặc được kiểm tra định kỳ.
  2. Nhân viên xem cảnh báo/ngưỡng.
  3. Work order được tạo theo lịch hoặc khi đã phát sinh lỗi.
  4. Kỹ thuật viên kiểm tra, sửa chữa và ghi kết quả.
- Bước tốn thời gian hoặc dễ lỗi nhất: phân biệt tín hiệu bất thường có ý nghĩa với nhiễu và ưu tiên đúng thiết bị.
- Thời gian hiện tại: cần CMMS/work-order logs và lịch sử telemetry; chưa có baseline.
- AI có thể hỗ trợ ở bước: anomaly detection/risk scoring và xếp hạng danh sách cần kiểm tra.
- Success metric: phát hiện ít nhất 70% sự cố thuộc danh mục pilot trước 24 giờ với precision tối thiểu 60%, đồng thời giảm 20% downtime ngoài kế hoạch. Target cần stakeholder xác minh.
- Quick Architecture: ML anomaly detection/survival model + rule thresholds; không cho AI tự dừng thiết bị.
- Rủi ro chính: failure labels hiếm, cảnh báo giả và bỏ sót sự cố an toàn.
- Human-in-the-loop: kỹ sư quyết định kiểm tra, dừng hoặc sửa thiết bị.

## Quyết định của nhóm cho Deep Dive

Năm ý tưởng và Top 3 ở trên là kết quả **cá nhân**. Sau khi thảo luận, nhóm không chọn một trong Top 3 cá nhân này mà thống nhất chọn bài toán chung sau:

- Bài toán nhóm chọn: **Vinhomes — Phân loại và điều hướng phản ánh cư dân**.
- Actor: nhân viên CSKH/Ban quản lý tiếp nhận phản ánh và các đội Kỹ thuật, An ninh, Vệ sinh, Cảnh quan chịu trách nhiệm xử lý.
- Vấn đề: phản ánh dạng văn bản tự do có thể mơ hồ, chứa nhiều vấn đề hoặc thiếu thông tin. Việc xác định đúng loại yêu cầu, mức khẩn cấp, tòa/zone và đội phụ trách có thể cần con người đọc, hỏi lại hoặc chuyển tuyến.
- Cơ hội AI: đề xuất category, urgency, responsible team và dữ liệu còn thiếu; kết quả luôn là bản nháp để nhân viên duyệt.
- Scope pilot: chỉ xử lý nhóm yêu cầu vận hành phổ biến, rủi ro thấp tại một khu đô thị; không tự xử lý khiếu nại pháp lý, phí, bồi thường hoặc tình huống khẩn cấp.
- Lý do nhóm chọn: khối lượng tác vụ lặp lại, đầu vào ngôn ngữ tự nhiên phù hợp với LLM/classifier, kết quả phân loại có thể đo, và có thể fallback về quy trình V-PMS/manual hiện tại.
- Giả định cần xác minh: tỷ lệ phân loại/chuyển tuyến thủ công hiện tại, taxonomy đang dùng, reroute rate, thời gian triage, dữ liệu ticket có nhãn và quy định xử lý dữ liệu cá nhân.

## Nguồn tham khảo

1. [Vinhomes Smart City — ứng dụng tìm chỗ đỗ và thanh toán tự động](https://smartcity.vinhomes.vn/bai-viet/vingroup-tien-phong-ung-dung-cong-nghe-thong-minh-nang-tam-cuoc-song-cu-dan-dai-do-thi-vinhomes-smart-city/)
2. [Vinhomes Annual Report 2023 — nâng cấp quản lý đỗ xe thông minh, app cư dân và IoT](https://gcp-cdn.vinhomes.vn/cms-data/Vinhomes-2023-AR-vF_1712109407.pdf)
3. [Vinhomes Annual Report 2024 — Resident app và giải pháp IoT cho năng lượng/vận hành](https://gcp-cdn.vinhomes.vn/cms-data/ENG%20Vinhomes%20AR%202024_250411_compressed.pdf)
4. [VinWonders — bản đồ điểm đến và tiện ích](https://vinwonders.com/en/map/?lang=en)
5. [A review of smart parking systems — Transportation Research Procedia, 2023](https://www.sciencedirect.com/science/article/pii/S235214652301219X)
6. [Smart parking occupancy prediction theo ETA — IET Intelligent Transport Systems](https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/iet-its.2017.0406)
7. [Vinhomes Annual Report 2024 — V-PMS tiếp nhận phản hồi, tự động giao việc và theo dõi tiến độ](https://gcp-cdn.vinhomes.vn/cms-data/VIE_Vinhomes%20AR%202024_250416_compressed.pdf)
