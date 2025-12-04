# Dash_dark_contacts_app.py
# Página Dash oscura, estilo futurista, muestra 4 contactos con fechas: hoy, ayer, -2 y -3 días.
# Para ejecutar: pip install dash
# python Dash_dark_contacts_app.py

from datetime import date, timedelta
from dash import Dash, html
import locale

# Intentar formatear en español; si falla, usa formato ISO.
try:
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
except Exception:
    try:
        locale.setlocale(locale.LC_TIME, 'es_AR.UTF-8')
    except Exception:
        # si no se puede establecer locale, seguiremos con strftime en inglés
        pass

app = Dash(__name__)

# Calcular fechas: Contacto 1 = hoy, Contacto 2 = ayer, etc.
ho = date.today()
fechas = [ho - timedelta(days=i) for i in range(0, 4)]  # 0,1,2,3

# Formato de fecha legible (ej: 04 diciembre 2025) — intenta usar locale si está disponible
def formato_fecha(d):
    try:
        return d.strftime('%d de %B de %Y')
    except Exception:
        return d.isoformat()

# Estilos inline (oscuro, futurista, neon)
page_style = {
    'minHeight': '100vh',
    'margin': '0',
    'padding': '40px',
    'background': 'radial-gradient(circle at 10% 10%, #0b1020 0%, #05050a 40%, #030409 100%)',
    'color': '#e6eef8',
    'fontFamily': "'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif",
}

card_style = {
    'background': 'linear-gradient(135deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01))',
    'backdropFilter': 'blur(6px)',
    'borderRadius': '12px',
    'padding': '18px 22px',
    'marginBottom': '18px',
    'boxShadow': '0 6px 30px rgba(2,6,23,0.6), inset 0 1px 0 rgba(255,255,255,0.02)',
    'border': '1px solid rgba(255,255,255,0.03)'
}

title_style = {
    'fontSize': '20px',
    'letterSpacing': '1px',
    'marginBottom': '6px',
}

date_style = {
    'fontSize': '14px',
    'opacity': '0.85'
}

accent = {
    'height': '4px',
    'borderRadius': '6px',
    'marginTop': '10px',
    'background': 'linear-gradient(90deg, #00ffd5, #7b61ff)'
}

header = {
    'display': 'flex',
    'alignItems': 'center',
    'justifyContent': 'space-between',
    'marginBottom': '28px'
}

logo_style = {
    'fontWeight': '700',
    'fontSize': '18px',
    'letterSpacing': '1.5px',
}

from dash import dcc, Output, Input

app.layout = html.Div([
    html.Div([
        html.Div("DASH Futurista — Contactos", style={**logo_style, 'color': '#cfeffa'}),
        html.Div(ho.strftime('%A, %d %B %Y'), style={'opacity': '0.6', 'fontSize': '13px'})
    ], style=header),

    # Contenedores de contactos
    html.Div([
        html.Div([
            html.Div(f"Contacto {i+1}", style=title_style),
            html.Div(formato_fecha(fechas[i]), style=date_style),
            html.Div(style=accent)
        ], style=card_style)
        for i in range(4)
    ], style={'maxWidth': '520px'})
], style={'maxWidth': '520px'}),

    dcc.Interval(id='timer', interval=60*1000, n_intervals=0)
], style=page_style)

# Callback para refrescar las fechas cada minuto
@app.callback(
    Output(component_id=None, component_property=None),
    Input('timer', 'n_intervals')
)
def refresh(_):
    return

if __name__ == '__main__':
    # Modo local; Render no usa esto, usa Gunicorn
    app.run(debug=True)
