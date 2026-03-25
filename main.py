from fasthtml.common import *

# Vercel Speed Insights script for FastHTML
# According to Vercel docs, the tracking script is automatically injected 
# at /_vercel/speed-insights/* routes upon deployment
speed_insights_script = Script("""
window.si = window.si || function () { (window.siq = window.siq || []).push(arguments); };
""")

speed_insights_loader = Script(src="/_vercel/speed-insights/script.js", defer=True)

# Create FastHTML app with Speed Insights integration
app, rt = fast_app(
    hdrs=(
        speed_insights_script,
        speed_insights_loader,
    )
)

@rt('/')
def get():
    return Div(
        H1('Welcome to Crossing Hurdles'),
        P('This FastHTML application is configured with Vercel Speed Insights.'),
        hx_get="/about"
    )

@rt('/about')
def get():
    return P('Vercel Speed Insights is now tracking performance metrics for this application.')

serve()
