# Satsang App UI Designs

This directory contains the UI designs for the Satsang App, created using Streamlit. The designs cover all major sections of the application as specified in the SRS Scope Document.

## Sections Covered

1. Home Page
2. User Management
3. Content Management
4. Event Management
5. Analytics Dashboard

## Setup Instructions

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Install wkhtmltopdf (required for PDF generation):
- For macOS:
```bash
brew install wkhtmltopdf
```
- For Ubuntu/Debian:
```bash
sudo apt-get install wkhtmltopdf
```
- For Windows: Download and install from https://wkhtmltopdf.org/downloads.html

## Running the UI Designs

To run the UI designs:

```bash
streamlit run app.py
```

This will open a web browser with the interactive UI designs. You can navigate between different sections using the sidebar menu.

## Features

- Interactive UI components
- Responsive design
- Navigation between different sections
- Export to PDF functionality (coming soon) 