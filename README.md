# AI News Email Notifier

This application automatically fetches the latest AI-related news and sends them to a specified email address daily at 10 AM.

## Features
- Fetches latest AI news using NewsAPI
- Sends formatted HTML emails with news summaries
- Runs automatically every day at 10 AM
- Easy configuration using environment variables

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the root directory with the following variables:
```
EMAIL_SENDER="your_email@gmail.com"
EMAIL_PASSWORD="your_app_password"
EMAIL_RECEIVER="recipient_email@example.com"
NEWS_API_KEY="your_newsapi_key"
```

Note: 
- For Gmail, you'll need to use an App Password. You can generate one in your Google Account settings.
- Get your NewsAPI key by signing up at https://newsapi.org

## Usage

Run the application:
```bash
python ai_news_emailer.py
```

The application will:
1. Run immediately to send the first email
2. Schedule itself to run every day at 10 AM
3. Continue running until interrupted with Ctrl+C

## Configuration

You can modify the following in the code:
- News search query in `fetch_ai_news()`
- Number of articles (`pageSize` parameter)
- Email format in `format_email_content()`
- Schedule timing in `main()` 