# Crossing Hurdles

A FastHTML web application with Vercel Speed Insights integration.

## Features

- Built with [FastHTML](https://fastht.ml/) - A modern Python web framework
- Integrated with [Vercel Speed Insights](https://vercel.com/docs/speed-insights) for performance monitoring
- Ready for deployment on Vercel

## Prerequisites

- Python 3.11 or higher
- pip package manager

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Locally

Start the development server:
```bash
python main.py
```

The application will be available at `http://localhost:5001`

## Deployment

This application is configured for deployment on Vercel:

1. Install Vercel CLI:
```bash
npm i -g vercel
```

2. Deploy:
```bash
vercel deploy
```

3. Enable Speed Insights in your Vercel dashboard to start tracking performance metrics

## Vercel Speed Insights

Speed Insights is automatically configured and will start tracking Core Web Vitals once deployed to Vercel. The integration uses the HTML/JavaScript approach suitable for FastHTML applications.

To view metrics:
1. Deploy your application to Vercel
2. Navigate to your project dashboard
3. Access the Speed Insights section
4. Performance data will appear after users visit your site

## Project Structure

- `main.py` - Main application file with FastHTML routes and Speed Insights integration
- `requirements.txt` - Python dependencies
- `vercel.json` - Vercel deployment configuration
- `.python-version` - Python version specification
- `runtime.txt` - Runtime configuration for Vercel

## License

See LICENSE file for details.
