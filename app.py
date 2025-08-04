import streamlit as st
import qrcode
from io import BytesIO
from crypto_core import encrypt_message, decrypt_message, encrypt_file, decrypt_file

st.set_page_config(page_title="Secure Text & File Encryption App", layout="centered")

st.markdown("<h1 style='text-align: center;'>🔐 Secure Text & File Encryption App</h1>", unsafe_allow_html=True)
st.markdown("""
<p style='text-align: center;'>This app securely encrypts and decrypts text and files using secret symmetric encryption. All actions are logged and timestamps for traceability.</p>
""", unsafe_allow_html=True)

# ------------------- Encrypt Text -------------------
st.markdown("## 📄 Encrypt Text")
with st.container():
    msg = st.text_area("Enter message to encrypt")
    pass_encrypt = st.text_input("Enter Password", type="password", key="enc_text_pass")

    if st.button("🔐 Encrypt Text"):
        if msg and pass_encrypt:
            try:
                encrypted = encrypt_message(msg, pass_encrypt)
                st.success("✅ Encryption successful!")
                st.code(encrypted, language="text")

                # QR code
                qr = qrcode.make(encrypted)
                buf = BytesIO()
                qr.save(buf)
                st.image(buf.getvalue(), caption="Encrypted QR Code")
            except Exception as e:
                st.error(f"❌ Encryption failed: {str(e)}")
        else:
            st.warning("⚠️ Please enter both message and password.")

# ------------------- Decrypt Text -------------------
st.markdown("## 🗝️ Decrypt Text")
with st.container():
    encrypted_input = st.text_area("Paste encrypted message")
    pass_decrypt = st.text_input("Enter Password", type="password", key="dec_text_pass")

    if st.button("🔓 Decrypt Text"):
        if encrypted_input and pass_decrypt:
            try:
                decrypted = decrypt_message(encrypted_input, pass_decrypt)
                st.success("✅ Decryption successful!")
                st.code(decrypted, language="text")
            except Exception as e:
                st.error(f"❌ Decryption failed: {str(e)}")
        else:
            st.warning("⚠️ Please enter both encrypted message and password.")

# ------------------- Encrypt File -------------------
st.markdown("## 📁 Encrypt File")
with st.container():
    upload_file = st.file_uploader("Upload a file to encrypt", key="file_enc_uploader")
    file_pass = st.text_input("Enter Password for file encryption", type="password", key="file_enc_pass")

    if st.button("🔐 Encrypt File"):
        if upload_file and file_pass:
            try:
                enc_bytes = encrypt_file(upload_file.read(), file_pass)
                st.success("✅ File encrypted successfully!")

                st.download_button(
                    label="📥 Download Encrypted File",
                    data=enc_bytes,
                    file_name=upload_file.name + ".enc",
                    mime="application/octet-stream"
                )
            except Exception as e:
                st.error(f"❌ File encryption failed: {str(e)}")
        else:
            st.warning("⚠️ Please upload a file and enter a password.")

# ------------------- Decrypt File -------------------
st.markdown("## 📂 Decrypt File")
with st.container():
    encrypted_file = st.file_uploader("Upload an encrypted .enc file", type=["enc"], key="file_dec_uploader")
    file_decrypt_pass = st.text_input("Enter Password for decryption", type="password", key="file_dec_pass")

    if st.button("🔓 Decrypt File"):
        if encrypted_file and file_decrypt_pass:
            try:
                dec_bytes = decrypt_file(encrypted_file.read(), file_decrypt_pass)
                st.success("✅ File decrypted successfully!")

                st.download_button(
                    label="📥 Download Decrypted File",
                    data=dec_bytes,
                    file_name="decrypted_" + encrypted_file.name.replace(".enc", ""),
                    mime="application/octet-stream"
                )
            except Exception as e:
                st.error(f"❌ File decryption failed: {str(e)}")
        else:
            st.warning("⚠️ Please upload a file and enter a password.")

# ------------------- Footer -------------------
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 12px;'>🛡️ Built with Python, Streamlit & Cryptography © 2025 Pooja.M</p>", unsafe_allow_html=True)
