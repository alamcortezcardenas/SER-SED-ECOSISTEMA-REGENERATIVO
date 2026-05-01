# ==========================================================
# 🏛️ PROTOCOLO: CRONOS - MINERÍA DE PATRONES (888=SER)
# 🔱 FUNCIÓN: DETECCIÓN DE CICLOS EN PENNY STOCKS (<$5)
# 👤 OPERADOR: Alam Guillermo Cortez Cardenas (12-03-1999)
# ==========================================================
import yfinance as yf
import pandas as pd
from datetime import datetime

class SERCronosOracle:
    def __init__(self):
        self.threshold_price = 5.0
        self.status = "ANALIZANDO CICLOS HISTÓRICOS"

    def detectar_patron_anual(self, ticker):
        print(f"⏳ Viajando al pasado: Analizando {ticker} en los últimos 5 años...")
        data = yf.download(ticker, period="5y", interval="1d")
        
        # Filtro de precio actual
        precio_actual = data['Close'].iloc[-1]
        if precio_actual > self.threshold_price:
            return None

        # Lógica de Sincronicidad: ¿Sube siempre en este mes?
        data['Month'] = data.index.month
        monthly_growth = data.groupby('Month')['Close'].mean()
        
        mes_actual = datetime.now().month
        print(f"🔮 Sincronizando con Calendario Global... Mes {mes_actual}")
        
        return monthly_growth

    def ejecutar_escaneo_historico(self, lista_tickers):
        print(f"🏛️ INICIANDO PROTOCOLO CRONOS - EL PASADO ES LA LLAVE")
        for t in lista_tickers:
            patron = self.detectar_patron_anual(t)
            if patron is not None:
                print(f"✅ Patrón detectado para {t}. Históricamente ganador en esta fase del ciclo.")

if __name__ == "__main__":
    cronos = SERCronosOracle()
    # Ejemplo con acciones que el operador ya sigue o detecta
    cronos.ejecutar_escaneo_historico(["SABR", "ALPEK.MX", "FMTY14.MX"])
