@echo off
echo Starting AI News Emailer at %date% %time% >> ai_news_log.txt
cd /d "%~dp0"
py ai_news_emailer.py >> ai_news_log.txt 2>&1
echo Finished running at %date% %time% >> ai_news_log.txt
echo. >> ai_news_log.txt 