import pyautogui as pg  # استيراد مكتبة pyautogui للتحكم بالماوس ولوحة المفاتيح
import time             # استيراد مكتبة الوقت للتعامل مع تأخيرات الوقت

def type_message(message, num_times, interval_seconds, tim):
    """
    تحاكي كتابة رسالة بشكل متكرر.

    Args:
        message (string): الرسالة التي سيتم كتابتها.
        num_times (int): عدد مرات كتابة الرسالة.
        interval_seconds (float): الفاصل الزمني (بالثواني) بين كل رسالة وأخرى.
        tim (float): مدة الانتظار (بالثواني) قبل بدء الكتابة.
    """
    
    # طباعة معلومات عن العملية التي سيتم تنفيذها
    print(f"Typing '{message}' {num_times} times with an interval of {interval_seconds} seconds after waiting {tim} seconds:")
    
    # الانتظار لمدة 'tim' ثوانٍ قبل بدء الكتابة
    time.sleep(tim)
    
    # حلقة لكتابة الرسالة بشكل متكرر
    for _ in range(num_times):
        pg.write(message)  # كتابة الرسالة
        pg.press("Enter")  # الضغط على مفتاح Enter بعد كل رسالة
        time.sleep(interval_seconds)  # الانتظار للفاصل الزمني المحدد قبل كتابة الرسالة التالية
    
    # طباعة رسالة تشير إلى اكتمال عملية الكتابة
    print("Message typing complete")

# طلب الرسالة من المستخدم
message = input("Please enter the message to type: ")
# طلب عدد مرات إرسال الرسالة من المستخدم
num_times = int(input("Please enter the number of messages you want to send: "))
# طلب الفاصل الزمني بين كل رسالة وأخرى من المستخدم
interval_seconds = float(input("Please enter the time interval between each message (e.g., 0.1): "))
# طلب مدة الانتظار قبل بدء الكتابة من المستخدم
tim = float(input("Please enter the duration to wait before you start typing (in seconds): "))
# استدعاء الدالة لكتابة الرسالة المدخلة من المستخدم بالفاصل الزمني المحدد
type_message(message, num_times, interval_seconds, tim)
