import random
import time
import urllib.parse
import os
import hashlib
import webbrowser
import subprocess

# Warna untuk teks
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Banner ASCII
banner = f"""
{RED}╔════════════════════════════════════════════════╗ {RESET}    
{RED}║ {YELLOW}██╗███╗░░░███╗██████╗░███████╗░█████╗░████████╗{RED}║
║{YELLOW} ██║████╗░████║██╔══██╗██╔════╝██╔══██╗╚══██╔══╝{RED}║
║{YELLOW} ██║██╔████╔██║██████╔╝█████╗░░██║░░╚═╝░░░██║░░░║
║ ██║██║╚██╔╝██║██╔═══╝░██╔══╝░░██║░░██╗░░░██║░░░║
║ ██║██║░╚═╝░██║██║░░░░░███████╗╚█████╔╝░░░██║░░░║
║ ╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝░╚════╝░░░░╚═╝░░░║
╠═{GREEN} CREATED BY EXPLOIT INDEPENDENT ft Mr 4REX_503 ║
╠════════════════════════════════════════════════╝
╠═ MASUKAN USERNAME TIK TOK 
╠═ ALAT EXTRAX FEEDBACK DARI IMPECT
╠════════════════════════════════════════════════╝
║
║
║
"""

# Fungsi untuk membuat URL laporan feedback berdasarkan username dan parameter lainnya
def generate_feedback_report_url(username):
    # Menggunakan username untuk menentukan target_id dengan hashing
    target_id = hashlib.md5(username.encode()).hexdigest()
    
    # Menggunakan timestamp yang lebih tepat (misalnya untuk zona waktu Asia/Jakarta)
    current_time = int(time.time())
    
    # Membuat beberapa parameter acak
    device_id = str(random.randint(1000000000000000000, 9999999999999999999))
    odin_id = str(random.randint(1000000000000000000, 9999999999999999999))
    
    # Base URL untuk feedback
    base_url = "https://www.tiktok.com/aweme/v2/aweme/feedback/"
    
    # Parameter lainnya
    params = {
        "WebIdLastTime": str(current_time),  # Menggunakan timestamp yang lebih sesuai
        "aid": "1988",  # Aplikasi ID TikTok
        "app_language": "id-ID",  # Bahasa aplikasi
        "app_name": "tiktok_web",  # Nama aplikasi
        "browser_language": "id-ID",  # Bahasa browser
        "browser_name": "Mozilla",  # Nama browser
        "browser_online": "true",  # Status browser online
        "browser_platform": "Linux armv81",  # Platform browser
        "browser_version": "5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",  # Versi browser
        "channel": "tiktok_web",  # Channel akses
        "cookie_enabled": "true",  # Status cookie
        "current_region": "ID",  # Region
        "data_collection_enabled": "true",  # Pengumpulan data
        "device_id": device_id,  # ID perangkat yang acak
        "device_platform": "web_pc",  # Platform perangkat
        "focus_state": "true",  # Fokus state
        "from_page": "user",  # Halaman pengirim
        "history_len": "11",  # Panjang riwayat
        "is_fullscreen": "false",  # Status fullscreen
        "is_page_visible": "true",  # Status tampilan halaman
        "lang": "id-ID",  # Bahasa aplikasi
        "nickname": username,  # Menggunakan username sebagai nickname
        "object_id": target_id,  # Menggunakan target_id berdasarkan username
        "odinId": odin_id,  # ID Odin
        "os": "linux",  # Sistem operasi
        "owner_id": target_id,  # ID pemilik yang terkait dengan target_id
        "priority_region": "ID",  # Prioritas wilayah
        "reason": "9007",  # Kode alasan untuk laporan
        "referer": "https://www.tiktok.com",  # Referer (halaman sebelumnya)
        "region": "ID",  # Wilayah
        "report_type": "user",  # Jenis laporan
        "screen_height": "942",  # Tinggi layar
        "screen_width": "424",  # Lebar layar
        "secUid": "MS4wLjABAAAA31x94C_gFv9vkfnhamYcz3nKu9ZfVuhlIpkMEM2sG9LvyV4DDbJDS6xGZKqwfMYU",  # Static UID (harus sesuai)
        "target": target_id,  # Target ID
        "tz_name": "Asia/Jakarta",  # Zona waktu
        "user_is_login": "true",  # Status login pengguna
        "webcast_language": "id-ID",  # Bahasa siaran langsung
    }
    
    # URL encode untuk parameter
    query_string = urllib.parse.urlencode(params)
    full_url = f"{base_url}?{query_string}"
    
    return full_url

# Fungsi utama untuk input username dan menghasilkan link laporan
def main():
    # Menyesuaikan clear untuk berbagai sistem operasi
    if os.name == 'nt':  # Untuk Windows
        os.system('cls')
    else:  # Untuk Linux/Mac
        os.system('clear')

    print(banner)
    print("║")
    
    # Meminta input username TikTok
    username = input("╚═㉿localhost ══: ")

    if username:
        # Menghasilkan link laporan feedback
        generated_url = generate_feedback_report_url(username)
        print(f"{CYAN}Generated Feedback Report URL:{RESET} {generated_url}")
        
        # Menunggu pengguna untuk menekan Enter untuk melanjutkan
        input(f"{YELLOW}Copy link di atas dan tekan Enter untuk melanjutkan...{RESET}")
        
        # Membuka URL di browser default
        webbrowser.open(generated_url)
        
        # Menjalankan skrip python lain secara otomatis setelah membuka URL
        try:
            subprocess.run(['python3', 'poison.py'], check=True)  # Sesuaikan dengan nama file skrip Anda
        except subprocess.CalledProcessError as e:
            print(f"{RED}[-] Gagal menjalankan skrip: {e}{RESET}")
    else:
        print(f"{RED}[-] Username tidak boleh kosong!{RESET}")

if __name__ == "__main__":
    main()
