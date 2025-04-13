from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from datetime import datetime
import pywhatkit as kit

class WhatsAppScheduler(BoxLayout):
    phone_input = ObjectProperty(None)
    message_input = ObjectProperty(None)
    time_input = ObjectProperty(None)
    status_label = ObjectProperty(None)

    def schedule_message(self):
        phone_number = self.phone_input.text
        message = self.message_input.text
        time_str = self.time_input.text

        if not phone_number or not message or not time_str:
            self.status_label.text = "Please fill in all fields"
            return

        try:
            hour, minute = map(int, time_str.split(":"))
            now = datetime.now()

            if hour < 0 or hour > 23 or minute < 0 or minute > 59:
                self.status_label.text = "Invalid time format"
                return

            if hour < now.hour or (hour == now.hour and minute <= now.minute):
                self.status_label.text = "Scheduled time must be in the future"
                return

            # Schedule the message
            Clock.schedule_once(
                lambda dt: self.send_whatsapp(phone_number, message, hour, minute),
                0.1
            )
            self.status_label.text = f"Message scheduled for {hour:02d}:{minute:02d}"

        except ValueError:
            self.status_label.text = "Invalid time format. Use HH:MM"
        except Exception as e:
            self.status_label.text = f"Error: {str(e)}"

    def send_whatsapp(self, phone_number, message, hour, minute):
        try:
            kit.sendwhatmsg(phone_number, message, hour, minute)
            Clock.schedule_once(
                lambda dt: setattr(self.status_label, 'text', "Message sent successfully!"),
                1
            )
        except Exception as e:
            Clock.schedule_once(
                lambda dt: setattr(self.status_label, 'text', f"Error: {str(e)}"),
                1
            )

class WhatsAppSchedulerApp(App):
    def build(self):
        return WhatsAppScheduler()

if __name__ == '__main__':
    WhatsAppSchedulerApp().run()
