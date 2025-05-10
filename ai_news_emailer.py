import os
import requests
import yagmail
from datetime import datetime
from dotenv import load_dotenv
from apscheduler.schedulers.blocking import BlockingScheduler

# Load environment variables
load_dotenv()

# Configuration
EMAIL_SENDER = os.getenv('EMAIL_SENDER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
NEWS_API_URL = "https://newsapi.org/v2/everything"

def fetch_ai_news():
    """Fetch the latest AI-related news articles."""
    params = {
        'q': '(artificial intelligence OR AI) AND (technology OR innovation)',
        'sortBy': 'publishedAt',
        'language': 'en',
        'pageSize': 5,
        'apiKey': NEWS_API_KEY
    }
    
    try:
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()
        return response.json()['articles']
    except Exception as e:
        print(f"Error fetching news: {e}")
        return None

def format_email_content(articles):
    """Format the news articles into an HTML email."""
    if not articles:
        return "No AI news articles found today."
    
    html_content = """
    <html>
    <body>
    <h2>Today's Top AI News</h2>
    <p>Here are the latest developments in AI:</p>
    """
    
    for article in articles:
        html_content += f"""
        <div style='margin-bottom: 20px;'>
            <h3><a href='{article['url']}'>{article['title']}</a></h3>
            <p>{article['description']}</p>
            <small>Published: {article['publishedAt'][:10]}</small>
        </div>
        """
    
    html_content += """
    <p>Best regards,<br>Your AI News Bot</p>
    </body>
    </html>
    """
    return html_content

def send_email(content):
    """Send the email using yagmail."""
    try:
        # Initialize yagmail SMTP
        yag = yagmail.SMTP(EMAIL_SENDER, EMAIL_PASSWORD)
        
        # Send email
        subject = f"AI News Update - {datetime.now().strftime('%Y-%m-%d')}"
        yag.send(
            to=EMAIL_RECEIVER,
            subject=subject,
            contents=content
        )
        print(f"Email sent successfully at {datetime.now()}")
    except Exception as e:
        print(f"Error sending email: {e}")

def job():
    """Main job function to fetch news and send email."""
    print(f"Starting job at {datetime.now()}")
    articles = fetch_ai_news()
    if articles:
        email_content = format_email_content(articles)
        send_email(email_content)
    else:
        print("No articles to send")

def main():
    """Main function to schedule and run the job."""
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'cron', hour=10, minute=0)
    
    print("Starting scheduler...")
    print("Press Ctrl+C to exit")
    
    try:
        # Run the job once immediately
        job()
        # Start the scheduler
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("Scheduler stopped")

if __name__ == "__main__":
    main()    