# 03 — AI Log & Reflection (Cá nhân)

## AI đã giúp tôi những gì?

Trong suốt buổi lab, tôi dùng Claude làm trợ lý đồng hành ở cả hai giai đoạn:
thiết lập môi trường kỹ thuật và tư duy sản phẩm.

- **Thiết lập môi trường:** Tôi gặp hàng loạt lỗi liên tiếp khi setup — lỗi
  `source` không tồn tại trên PowerShell (do lẫn cú pháp bash/Windows), lỗi
  Execution Policy chặn chạy script `.venv\Scripts\Activate.ps1`, lỗi clone
  git vào một thư mục ZIP đã giải nén sẵn (không phải git repo thật) khiến mọi
  lệnh `git` báo "not a git repository". AI giúp tôi chẩn đoán từng lỗi theo
  đúng thông báo lỗi thay vì đoán mò, và giải thích *tại sao* lỗi xảy ra
  (ví dụ: khác biệt giữa tải ZIP và `git clone` thật).
- **Debug code:** Ở bài lab Day 1, tôi nhiều lần gặp lại đúng một lỗi
  `NotImplementedError` dù đã viết code — nguyên nhân thực tế là tôi quên lưu
  file hoặc quên xóa dòng `raise` cũ. AI giúp tôi hình thành thói quen kiểm tra
  "đọc lại file thật trên đĩa" (`cat`/`type`) thay vì chỉ tin vào những gì tôi
  nghĩ mình đã gõ.
- **Tư duy sản phẩm (Scoping):** AI giúp tôi brainstorm nhanh 5 bài toán thuộc
  các công ty thành viên Vingroup theo đúng 4 Lenses, và cấu trúc lại thành
  Quick Problem Card, Problem Statement 6-field theo đúng khung của worksheet.

## AI trả lời sai / hallucination ở đâu?

- Lần đầu tôi hỏi ý tưởng scoping, AI đưa ra danh sách công ty thành viên sai
  (nhắc tới Vinschool, VinUni, Vincom Retail) — không khớp với danh sách chính
  thức trong `01-worksheet.md` (VinFast, Xanh SM, Vinhomes, Vinmec, Vinpearl).
  Đây là hallucination vì AI suy đoán dựa trên hiểu biết chung về Vingroup
  thay vì đọc đúng tài liệu bài lab thật.
- AI cũng từng đưa ra hướng dẫn cấu hình `base_url` cho NVIDIA NIM khá chi
  tiết dựa trên tìm kiếm web, nhưng tôi cần tự kiểm chứng lại số liệu (giá
  credit, giới hạn request/phút) vì các con số này có thể thay đổi theo thời
  gian và không phải lúc nào cũng chính xác 100% so với trang chính thức.

## Tôi đã sửa prompt / ranh giới ra sao?

- Sau khi phát hiện AI dùng sai danh sách công ty, tôi gửi trực tiếp nội dung
  file `01-worksheet.md` thật cho AI đọc, thay vì để AI tự suy đoán từ kiến
  thức chung — kết quả chính xác hơn hẳn.
- Khi debug lỗi `NotImplementedError` lặp lại nhiều lần, tôi học được cách
  luôn gửi kèm *ảnh chụp toàn bộ output lỗi* thay vì mô tả chung chung "vẫn
  lỗi như cũ" — nhờ vậy AI chẩn đoán đúng nguyên nhân (chưa lưu file) thay vì
  đoán sai hướng.
- Đối với phần Quick Problem Card và Problem Statement, tôi không copy nguyên
  bản AI đưa ra mà đọc lại, đối chiếu với dữ liệu thực tế hợp lý hơn (ví dụ
  điều chỉnh lại số liệu tần suất, thời gian xử lý cho sát với quy mô thực tế
  của một trung tâm bảo hành), trước khi đưa vào bản deliverable chính thức.

## Bài học rút ra

AI là công cụ tăng tốc rất hiệu quả cho cả việc debug kỹ thuật lẫn brainstorm
ý tưởng sản phẩm, nhưng độ chính xác phụ thuộc rất nhiều vào việc tôi cung cấp
đúng ngữ cảnh/tài liệu gốc thay vì để AI tự đoán. Việc luôn xác minh lại số
liệu và đối chiếu với tài liệu chính thức của bài lab là bước không thể bỏ qua
trước khi đưa bất kỳ nội dung nào do AI tạo ra vào bản nộp bài chính thức.
