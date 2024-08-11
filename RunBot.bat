@echo off

rem Activate the virtual environment
call .venv/Scripts/activate

rem Move to the bot directory
cd ./BotApplication

rem Run the bot
python Index.py
