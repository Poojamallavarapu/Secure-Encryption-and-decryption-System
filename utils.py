import qrcode
import datetime
import os

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

def create_log_entry(action, data_type, status):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"[{timestamp}] | Action: {action} | Data Type: {data_type} | Status: {status}"

def save_log(entry, logfile="logs/activity.log"):
    with open(logfile, "a") as f:
        f.write(entry + "\n")

def generate_qr(data, filename="qrcode.png"):
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")
        img.save(filename)
    except Exception as e:
        print(f"QR code generation failed: {str(e)}")
