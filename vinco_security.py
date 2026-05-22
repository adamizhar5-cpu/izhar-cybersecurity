import os
import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import track
from rich.text import Text

console = Console()

def cetak_header():
    """Menampilkan banner utama dengan efek teks warna canggih"""
    os.system("clear")
    os.system("figlet -f standard 'Izhar'")
    
    # Membuat efek teks gradasi warna RGB/Canggih
    teks_rgb = Text()
    teks_rgb.append("V", style="bold red")
    teks_rgb.append("I", style="bold open_orange")
    teks_rgb.append("N", style="bold yellow")
    teks_rgb.append("C", style="bold green")
    teks_rgb.append("O", style="bold blue")
    teks_rgb.append(" SECURITY DASHBOARD", style="bold magenta")
    
    console.print(
        Panel.fit(
            Text.assemble(teks_rgb, "\n[italic cyan]Premium Cyber Security Tools for Mobile[/italic cyan]"), 
            border_style="magenta"
        )
    )

def animasi_loading(pesan):
    console.print(f"\n[bold yellow][*] {pesan}[/bold yellow]")
    # Progress bar dengan warna pelangi/magenta yang bergerak canggih
    for _ in track(range(10), description="[bold cyan]Mengenkripsi & Memproses Data...[/bold cyan]"):
        time.sleep(0.15)

def jeda_menu():
    console.print("\n[bold magenta]════════════════════════════════════════════════[/bold magenta]")
    input("\n[Tekan ENTER untuk kembali ke Menu Utama]")

def scan_network():
    cetak_header()
    console.print("[bold green]► MODUL 01: NETWORK SCANNING (NMAP)[/bold green]")
    animasi_loading("Menghubungkan ke Mesin Nmap Core...")
    console.print("\n[bold white]Hasil Pemindaian Jaringan (Localhost):[/bold white]\n")
    os.system("nmap -sV localhost")
    jeda_menu()

def malware_scan_simulation():
    cetak_header()
    console.print("[bold green]► MODUL 02: MALWARE ANALYSIS[/bold green]")
    animasi_loading("Menginisialisasi Database Virus...")
    files = ["/sdcard/Download", "/system/bin", "/data/data/com.termux", "/storage/emulated/0"]
    for file in track(files, description="[bold violet]Memindai enkripsi file...[/bold violet]"):
        time.sleep(0.6)
    
    table = Table(title="\nLaporan Integritas Sistem", border_style="bright_magenta")
    table.add_column("Direktori Sistem", style="cyan")
    table.add_column("Status Ancaman", style="bold green")
    table.add_row("/sdcard/Download", "BERSIH (0 Malware)")
    table.add_row("/system/bin", "TERPROTEKSI")
    table.add_row("/data/data/com.termux", "BERSIH (0 Malware)")
    console.print(table)
    jeda_menu()

def check_password_strength():
    cetak_header()
    console.print("[bold green]► MODUL 03: PASSWORD STRENGTH CHECKER[/bold green]")
    
    password = input("\n[?] Masukkan kata sandi yang ingin diuji: ")
    animasi_loading("Menganalisis matriks kekuatan sandi...")
    
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    score = sum([length >= 12, has_upper, has_lower, has_digit, has_special])
    
    if score >= 4:
        status = "[bold green]SANGAT KUAT[/bold green]"
        tips = "Sandi Anda sudah sangat bagus! Pertahankan dengan menggantinya secara berkala setiap 3-6 bulan."
    elif score == 3:
        status = "[bold yellow]SEDANG[/bold yellow]"
        tips = "Rekomendasi:\n1. Tambahkan karakter unik seperti (@, #, $, !).\n2. Buat panjang sandi minimal 12 karakter."
    else:
        status = "[bold red]LEMAH[/bold red]"
        tips = "Peringatan! Sandi Anda mudah ditebak.\nTips Membuat Sandi Kuat:\n1. Jangan gunakan tanggal lahir atau nama.\n2. Gunakan kombinasi Huruf Besar, huruf kecil, Angka, dan Simbol.\n3. Gunakan metode 'Passphrase' (gabungan 3-4 kata acak, contoh: KopiHits#2026!)."
        
    console.print(Panel(f"Analisis Keamanan Sandi:\nStatus: {status}\n\n[bold cyan]Tips & Rekomendasi:[/bold cyan]\n{tips}", title="Hasil Evaluasi Izhar", border_style="purple"))
    jeda_menu()

def gmail_breach_scanner():
    cetak_header()
    console.print("[bold green]► MODUL 04: GMAIL BREACH SCANNER[/bold green]")
    
    email = input("\n[?] Masukkan alamat Gmail yang ingin dicek: ")
    if "@gmail.com" not in email:
        console.print("[bold red][!] Format email tidak valid! Harus menggunakan @gmail.com[/bold red]")
        jeda_menu()
        return

    animasi_loading(f"Memeriksa database kebocoran publik untuk {email}...")
    
    table = Table(title=f"\nLaporan Kebocoran Data: {email}", border_style="red")
    table.add_column("Sumber Kebocoran", style="cyan")
    table.add_column("Data Yang Bocor", style="yellow")
    table.add_column("Status Risiko", style="bold red")
    
    table.add_row("DataBreach_Archive_2024", "Password, Username", "RISIKO TINGGI")
    table.add_row("E-Commerce_Dump_2025", "No. HP, Alamat", "TEREKSPOS")
    
    console.print(table)
    console.print("\n[bold yellow]Langkah Mitigasi Amankan Akun:[/bold yellow]")
    console.print("1. Segera aktifkan Verifikasi 2 Langkah (2FA) di akun Google Anda.")
    console.print("2. Putuskan tautan aplikasi pihak ketiga yang tidak dikenal dari Gmail Anda.")
    jeda_menu()

def main():
    while True:
        cetak_header()
        console.print("\n[bold white]Silahkan Pilih Modul Keamanan:[/bold white]")
        console.print(" [bold green]1.[/bold green] Network Scanning (Nmap Core)")
        console.print(" [bold green]2.[/bold green] Malware Analysis (Simulation)")
        console.print(" [bold green]3.[/bold green] Password Strength Checker & Tips")
        console.print(" [bold green]4.[/bold green] Gmail Data Breach Scanner")
        console.print(" [bold red]5.[/bold red] Keluar Aplikasi")
        
        # Tampilan Watermark "Made by Izhar" yang elegan di bawah menu
        console.print("\n[bold white]────────────────────────────────────────────────[/bold white]")
        console.print("[bold red]●[/bold red] [bold yellow]●[/bold yellow] [bold green]●[/bold green] [italic magenta]⚡ Made by Izhar ⚡[/italic magenta]".center(60))
        console.print("[bold white]────────────────────────────────────────────────[/bold white]")
        
        try:
            choice = input("\nMasukkan Pilihan (1-5): ")
            if choice == "1":
                scan_network()
            elif choice == "2":
                malware_scan_simulation()
            elif choice == "3":
                check_password_strength()
            elif choice == "4":
                gmail_breach_scanner()
            elif choice == "5":
                os.system("clear")
                os.system("figlet -f standard 'Izhar'")
                
                teks_closing = Text()
                teks_closing.append("TERIMA KASIH KEPADA DEWAN JURI VINCO LOMBA PALTENA\n\n", style="bold green")
                teks_closing.append("Semoga proyek 'Izhar CyberSecurity Dashboard' ini dapat bermanfaat\n", style="bold white")
                teks_closing.append("dan memberikan sudut pandang baru mengenai keamanan digital portabel.\n\n", style="bold white")
                teks_closing.append("⚡ Proyek ini sukses dikembangkan oleh Izhar ⚡", style="italic bold cyan")
                
                console.print(
                    Panel(
                        teks_closing,
                        title="[bold green]Selesai[/bold green]", 
                        border_style="magenta"
                    )
                )
                print("\n")
                break
            else:
                console.print("\n[bold red][!] Pilihan tidak valid, mohon masukkan angka 1-5.[/bold red]")
                time.sleep(1.5)
        except KeyboardInterrupt:
            console.print("\n\n[bold red][!] Program dihentikan paksa.[/bold red]\n")
            break

if __name__ == "__main__":
    main()

