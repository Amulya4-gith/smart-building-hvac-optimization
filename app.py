from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = "change-this-secret-key"

# Demo data only. Replace with real IoT/BMS sensor integrations for production.
state = {
    "temperature": 24.5,
    "humidity": 48,
    "air_quality": 42,
    "occupancy": 18,
    "energy_kwh": 126.4,
    "hvac_mode": "Auto",
    "setpoint": 24,
    "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
}

def refresh_demo_readings():
    state["temperature"] = round(random.uniform(22.0, 28.0), 1)
    state["humidity"] = random.randint(35, 65)
    state["air_quality"] = random.randint(20, 110)  # illustrative index
    state["occupancy"] = random.randint(0, 45)
    state["energy_kwh"] = round(state["energy_kwh"] + random.uniform(0.1, 1.8), 1)
    state["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_alerts():
    alerts = []
    if state["temperature"] > 27:
        alerts.append("Temperature is high. Check cooling performance.")
    if state["humidity"] > 60:
        alerts.append("Humidity is high. Review ventilation and dehumidification.")
    if state["air_quality"] > 100:
        alerts.append("Air-quality index is elevated. Inspect ventilation filters.")
    if state["occupancy"] == 0 and state["hvac_mode"] != "Off":
        alerts.append("No occupants detected. Consider reducing HVAC operation.")
    if not alerts:
        alerts.append("No abnormal conditions detected.")
    return alerts

@app.route("/")
def dashboard():
    refresh_demo_readings()
    return render_template(
        "index.html",
        state=state,
        alerts=get_alerts(),
        energy_status="Within demo range" if state["energy_kwh"] < 150 else "Review energy usage"
    )

@app.post("/control")
def control():
    mode = request.form.get("hvac_mode", "Auto")
    setpoint = request.form.get("setpoint", "24")
    if mode not in {"Auto", "On", "Off"}:
        flash("Invalid HVAC mode.", "error")
        return redirect(url_for("dashboard"))
    try:
        setpoint_value = float(setpoint)
        if not 16 <= setpoint_value <= 30:
            raise ValueError
    except ValueError:
        flash("Setpoint must be between 16°C and 30°C.", "error")
        return redirect(url_for("dashboard"))
    state["hvac_mode"] = mode
    state["setpoint"] = setpoint_value
    flash(f"HVAC mode set to {mode}; target temperature is {setpoint_value:g}°C.", "success")
    return redirect(url_for("dashboard"))

@app.route("/health")
def health():
    return {"status": "ok", "service": "smart-building-hvac"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
