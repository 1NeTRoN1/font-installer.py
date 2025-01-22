import os
import time
import sys

def print_colored(text, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'blue': '\033[94m',
        'yellow': '\033[93m',
        'end': '\033[0m'
    }
    print(f"{colors.get(color, '')}{text}{colors['end']}")

def run_command(command):
    print_colored(f"Çalıştırılıyor: {command}", "blue")
    return os.system(command)

def main():
    if os.geteuid() != 0:
        print_colored("Bu script root yetkisi gerektirir!", "red")
        print_colored("Lütfen 'sudo python font_installer.py' şeklinde çalıştırın.", "yellow")
        sys.exit(1)

    print_colored("\n=== Archman Linux Font Yükleyici ===\n", "green")
    
    # Sistem güncelleme
    print_colored("Sistem güncelleniyor...", "yellow")
    run_command("pacman -Syu --noconfirm")

    # Tüm font paketleri
    font_packages = [
        # Temel fontlar
        "ttf-dejavu",
        "ttf-liberation",
        "noto-fonts",
        "noto-fonts-cjk",
        "noto-fonts-emoji",
        "noto-fonts-extra",
        
        # Ek Latin fontları
        "ttf-caladea",
        "ttf-carlito",
        "ttf-opensans",
        "ttf-roboto",
        "ttf-ubuntu-font-family",
        
        # Asya fontları
        "ttf-baekmuk",
        "wqy-microhei",
        "wqy-zenhei",
        "ttf-hannom",
        "ttf-khmer",
        "ttf-tibetan-machine",
        
        # Matematik ve sembol fontları
        "texlive-fonts-extra",
        "otf-latin-modern",
        "ttf-font-awesome",
        "ttf-joypixels",
        
        # Programlama fontları
        "ttf-fira-code",
        "ttf-jetbrains-mono",
        "ttf-cascadia-code",
        
        # Ekstra fontlar
        "adobe-source-code-pro-fonts",
        "adobe-source-sans-fonts",
        "adobe-source-serif-fonts",
        "cantarell-fonts",
        "gnu-free-fonts",
        "ttf-bitstream-vera",
        "ttf-hack",
        "ttf-inconsolata"
    ]

    # Fontları yükle
    print_colored("\nFontlar yükleniyor...", "yellow")
    for package in font_packages:
        print_colored(f"\nYükleniyor: {package}", "blue")
        run_command(f"pacman -S --noconfirm {package}")
        time.sleep(0.5)

    # Yay kontrolü ve yükleme
    if run_command("which yay > /dev/null") != 0:
        print_colored("\nyay yükleniyor...", "yellow")
        run_command("pacman -S --noconfirm yay")

    # AUR font paketleri
    aur_packages = [
        "ttf-ms-fonts",
        "ttf-google-fonts-git",
        "ttf-monaco",
        "ttf-mac-fonts",
        "ttf-gelasio-ib",
        "ttf-impallari-cantora",
        "ttf-merriweather",
        "ttf-merriweather-sans",
        "ttf-opensans",
        "ttf-signika"
    ]

    # AUR fontlarını yükle
    print_colored("\nAUR fontları yükleniyor...", "yellow")
    for package in aur_packages:
        print_colored(f"\nAUR'dan yükleniyor: {package}", "blue")
        run_command(f"yay -S --noconfirm {package}")
        time.sleep(0.5)

    print_colored("\nFont cache yenileniyor...", "blue")
    run_command("fc-cache -f")

    print_colored("\nFont kurulumu tamamlandı! Sistemi yeniden başlatmanız önerilir.", "green")

if __name__ == "__main__":
    main()