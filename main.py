from fasthtml.common import *

# Configure Vercel Web Analytics by adding the analytics script to headers
analytics_script = Script(src="/_vercel/insights/script.js", defer=True)

# Initialize FastHTML app with Pico CSS and Vercel Analytics
app, rt = fast_app(
    hdrs=(
        analytics_script,
    )
)

@rt("/")
def get():
    return Titled(
        "Crossing Hurdles",
        Main(
            H1("Welcome to Crossing Hurdles"),
            P("A FastHTML application with Vercel Web Analytics enabled."),
            cls="container"
        )
    )

if __name__ == "__main__":
    serve()
