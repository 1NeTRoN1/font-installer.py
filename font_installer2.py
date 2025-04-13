#!/usr/bin/env python3
import os
import time
import sys
from subprocess import call

class PegasusFontInstaller:
    """
    Archman Linux için gelişmiş font yükleyici
    PeGaSuS tarafından tasarlanmıştır
    """

    COLORS = {
        'red': '\033[91m',
        'green': '\033[92m',
        'blue': '\033[94m',
        'yellow': '\033[93m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'end': '\033[0m',
        'bold': '\033[1m'
    }

    @staticmethod
    def print_banner():
        """Basit ve temiz bir banner gösterir"""
        print(f"{PegasusFontInstaller.COLORS['purple']}")
        print("┌──────────────────────────────────────────────────────┐")
        print("│      ARCHMAN LİNUX GELİŞMİŞ FONT YÜKLEYİCİ          │")
        print(f"└──────────────────────────────────────────────────────┘{PegasusFontInstaller.COLORS['end']}")
        print(f"{PegasusFontInstaller.COLORS['cyan']}✧ Pegasus tarafından özenle hazırlandı ✧{PegasusFontInstaller.COLORS['end']}\n")

    @staticmethod
    def print_colored(text, color, bold=False):
        """Renkli ve kalın yazı yazdırır"""
        style = PegasusFontInstaller.COLORS.get(color, '')
        if bold:
            style += PegasusFontInstaller.COLORS['bold']
        print(f"{style}{text}{PegasusFontInstaller.COLORS['end']}")

    # ... (Diğer fonksiyonlar aynı şekilde kalacak, sadece show_completion güncellendi)

    @staticmethod
    def show_completion():
        """Tamamlandı mesajını gösterir"""
        PegasusFontInstaller.print_colored("\n✔ FONT KURULUMU BAŞARIYLA TAMAMLANDI!", "green", True)
        PegasusFontInstaller.print_colored("ℹ Daha iyi bir görüntü için sistemi yeniden başlatın.", "yellow")
        print(f"\n{PegasusFontInstaller.COLORS['purple']}✧ Pegasus ✧{PegasusFontInstaller.COLORS['end']}")

if __name__ == "__main__":
    PegasusFontInstaller.main()