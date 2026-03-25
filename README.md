# Crossing Hurdles

A FastHTML application with Vercel Web Analytics integration.

## Features

- Built with [FastHTML](https://fastht.ml/) - Modern web applications in pure Python
- Integrated with [Vercel Web Analytics](https://vercel.com/analytics) for privacy-friendly traffic insights

## Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

The application will start on `http://localhost:5001`.

## Deployment

This project is configured for deployment on Vercel:

1. Push your changes to GitHub
2. Import the project in Vercel
3. Enable Web Analytics in your Vercel project dashboard
4. Deploy

### Vercel Configuration

- `runtime.txt` specifies Python 3.10 runtime
- `vercel.json` configures the build command
- Analytics are automatically enabled via the script in `main.py`

## Vercel Web Analytics

This project includes Vercel Web Analytics integration. The analytics script is added to the application headers in `main.py`:

```python
analytics_script = Script(src="/_vercel/insights/script.js", defer=True)
```

To view analytics data:
1. Deploy your application to Vercel
2. Navigate to the Analytics tab in your Vercel project dashboard
3. Enable Web Analytics if not already enabled

Analytics will automatically track page views and provide privacy-friendly traffic insights.

## Project Structure

```
.
├── main.py              # Main FastHTML application with analytics
├── requirements.txt     # Python dependencies
├── runtime.txt          # Python version for Vercel
├── vercel.json          # Vercel configuration
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## License

See [LICENSE](LICENSE) file for details.
