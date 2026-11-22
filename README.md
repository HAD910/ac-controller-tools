# AC controller tools

Script và ghi chú để chỉnh cấu hình tay cầm (Steam Input, file ini của game) cho Assassin's Creed Brotherhood trên PC, theo mẫu đã dùng cho AC2.

## Nội dung
- `tools/acb_pad.py` — thêm cấu hình Steam Input (appid 48190) vào các configset, cùng mẫu với AC2 (33230). Mặc định chạy thử (dry-run); `--apply` mới ghi.
- `tools/acb_ini.py` — sửa `SelectedInput` và `Button1..4` trong file ini của game. Mặc định chạy thử; `--apply` mới ghi.
- `work/acb_controller_notes.md` — ghi chú quá trình làm: những gì đã kiểm chứng và những gì chưa.

## Lưu ý
- Script chạy trên Windows, cài Steam ở đường dẫn mặc định. Sửa hằng số `CFG`/`TPL` trong `acb_pad.py` nếu khác.
- Trước khi `--apply`: tắt Steam (`steam.exe -shutdown`) với `acb_pad.py`, và thoát game với `acb_ini.py`. Hai script đều từ chối ghi nếu tiến trình tương ứng đang chạy.
- Script ghi backup vào thư mục `backups/` cạnh repo trước khi sửa file.
- Repo không chứa file game nào. Phần chưa kiểm chứng trong game được đánh dấu rõ trong ghi chú.
