# -
def main(command_text: str) -> str:     t = command_text.lower().strip()     if t == "/start":         return "أهلاً بك في بوت النظام الدولي التجريبي!"     if t == "/help":         return "الأوامر: /start, /help"     return "لم أفهم. جرب /help."  if __name__ == "__main__":     # هذا الجزء للاختبار المحلي، لن يتم تشغيله بواسطة تطبيق البوت 
