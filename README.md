# 📡 InternetSpeedComplaintBot

A Python bot that tests your internet speed using [Speedtest.net](https://www.speedtest.net/) and automatically tweets a complaint to your internet provider if the speed is slower than what you pay for.

---

## ⚙️ Features

- Automatically opens Speedtest.net and checks internet speed using Selenium
- Compares the result with your promised download/upload speed
- Logs in to Twitter and tweets a message if the speed is below the threshold
- Fully automated and customizable

---

## 🧰 Technologies Used

- Python 🐍
- Selenium WebDriver
- Speedtest.net
- Twitter (Web Automation)

---


## 🚀 How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/RohitKumarChaudhari/InternetSpeedComplaintBot.git
cd InternetSpeedComplaintBot
```

### 3. Configure Settings
- Promised download/upload speeds
- Twitter login credentials

Example:  
```
PROMISED_DOWN = 100  # Mbps
PROMISED_UP = 20     # Mbps
TWITTER_EMAIL = "your_email"
TWITTER_PASSWORD = "your_password"
```

## ▶️ Run the Script
```bash
python main.py
```
If your current speed is less than promised, the bot will tweet:  
```
Hey ISP, why is my internet speed 45 Mbps down/6 Mbps up when I pay for 100 Mbps down/20 Mbps up? #InternetSpeedTest
```
## 🛑 Warning  

- This script uses Twitter's web interface, which may break if Twitter updates its layout.  
- Make sure to use a separate account for testing to avoid rate limits or lockouts.

## Built By  

🧠 Built with Selenium and Python by Rohit to keep ISPs honest. 🛰️

## 📬 Contact  
Have ideas or found bugs? Open an issue
