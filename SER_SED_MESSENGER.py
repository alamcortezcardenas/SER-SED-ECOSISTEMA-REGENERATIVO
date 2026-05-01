# ==========================================================
# 🏛️ PROTOCOLO: MESSENGER - TELEMETRÍA DE ALERTA (888=SER)
# 🔱 FUNCIÓN: NOTIFICACIÓN DE OPORTUNIDADES ELITE
# 👤 OPERADOR: Alam Guillermo Cortez Cardenas (12-03-1999)
# ==========================================================
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SERMessenger:
    def __init__(self):
        self.sender_email = "tu_bunker_bot@gmail.com" # Un correo secundario para el bot
        self.receiver_email = "alamcortezcardenas@gmail.com"
        # NOTA: Necesitas generar una "App Password" en Google para seguridad
        self.password = "TU_APP_PASSWORD_AQUI" 

    def enviar_alerta(self, ticker, motivo, precio):
        mensaje = MIMEMultipart()
        mensaje["From"] = self.sender_email
        mensaje["To"] = self.receiver_email
        mensaje["Subject"] = f"⚠️ ALERTA 888: {ticker} DETECTADO"

        cuerpo = f"""
        🏛️ INFORME DEL OPERADOR 888
        ----------------------------------
        ACTIVO: {ticker}
        MOTIVO: {motivo}
        PRECIO ACTUAL: < ${precio}
        ESTADO: EL PASADO SE REPITE / VOLUMEN DE ÉLITE DETECTADO.
        
        Sincronización completa al 30 de abril de 2026.
        """
        mensaje.attach(MIMEText(cuerpo, "plain"))

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(self.sender_email, self.password)
                server.sendmail(self.sender_email, self.receiver_email, mensaje.as_string())
            print(f"📧 Alerta enviada a {self.receiver_email}")
        except Exception as e:
            print(f"❌ Error en la transmisión: {e}")

if __name__ == "__main__":
    messenger = SERMessenger()
    # Prueba de enlace
    messenger.enviar_alerta("SABR", "Sincronicidad CRONOS detectada", 5.0)
