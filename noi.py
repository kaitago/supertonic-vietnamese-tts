# ============================================================
#  SUPERTONIC TTS - File tổng hợp giọng nói
#  Chỉnh sửa 3 phần bên dưới rồi lưu lại và chạy
# ============================================================

from supertonic import TTS
from datetime import datetime
import subprocess, os

# ── 1. VĂN BẢN CẦN ĐỌC ─────────────────────────────────────
# Thay đoạn văn bản bất kỳ vào đây, có thể dài hoặc ngắn tuỳ ý
VAN_BAN = """
Đây là giọng Nữ ép 3 tốc độ đọc là 1 chấm 6. Công cụ sup bơ tô níc Bạn thấy thế nào? Ổn chứ?
"""

# ── 2. GIỌNG NÓI ────────────────────────────────────────────
# Nữ: F1  F2  F3  F4  F5
# Nam: M1  M2  M3  M4  M5
GIONG = "F3"

# ── 3. TỐC ĐỘ ───────────────────────────────────────────────
# Chậm: 0.7 | Bình thường: 1.0 | Nhanh: 1.3 | Rất nhanh: 1.6 | Tối đa: 2.0
TOC_DO = 1.6

# ============================================================
#  KHÔNG CẦN CHỈNH PHÍA DƯỚI
# ============================================================

# Tên file output: tự động gắn thời gian để không bị đè
ten_file = f"Test_{GIONG}_{TOC_DO}x_{datetime.now().strftime('%H%M%S')}.wav"
duong_dan = os.path.join(os.path.expanduser("~"), "Desktop", ten_file)

print(f"\n🎙  Giọng: {GIONG}  |  Tốc độ: {TOC_DO}x  |  File: {ten_file}")
print("⏳ Đang tổng hợp giọng nói...")

tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name=GIONG)
wav, duration = tts.synthesize(
    VAN_BAN.strip(),
    voice_style=style,
    lang="vi",
    speed=TOC_DO,
    max_chunk_length=200,
    silence_duration=0.4
)
tts.save_audio(wav, duong_dan)


print(f"✅ Xong! Thời lượng: {float(duration):.1f} giây")
print(f"📁 Đã lưu: {duong_dan}\n")

# Tự động mở file để nghe ngay
subprocess.run(["open", duong_dan])
