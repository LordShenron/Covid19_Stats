# COVID-19 Stats

<div align="center">
<img src="http://niepid.nic.in/coronabanner.png"> 
<br>
<p>A simple python script that can fetch covid 19 stats from the virus tracker, Based on <a href="https://github.com/emanuel2718/Covid-19-Scrapper">Emanuel Ramirez's</a> script but a lot simpler and only for India. 
There is another script that can send the stats fetched from the virus tracker to Telegram channels using a @BotFather bot.</p>
<br>
<a>
<img src="https://img.shields.io/badge/license-MIT-success?style=for-the-badge">
</a>
</div>

# Dependencies 
```
pandas==1.0.2
requests==2.23.0
seaborn==0.10.0
matplotlib==3.2.1
PyYAML==5.3.1
```

# How to use
1. Clone the script
```
git clone https://github.com/LordShenron/Covid19_Stats covid-stats && cd covid-stats
```
2. Create a Telegram using @BotFather and add the HTTP_TOKEN to the corona.sh
3. Add the bot you created to any Telegram group or channel.
4. Add the username or userid of the channel or group to the corona.sh
5. Execute the scripts
```
chmod +x corona*
./corona.sh
```

# You can automate the execution of script, I will leave that to you.
