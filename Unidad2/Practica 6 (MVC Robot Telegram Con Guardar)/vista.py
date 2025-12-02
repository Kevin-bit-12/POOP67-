def mensaje(texto):
    return f"📢 {texto}"

def info_dht(temp, hum):
    return f"🌡 Temp: {temp:.1f}°C\n💧 Humedad: {hum:.1f}%"

def estado_boton(pressed):
    return "🔘 Botón PRESIONADO" if pressed else "⚪ Botón suelto"
