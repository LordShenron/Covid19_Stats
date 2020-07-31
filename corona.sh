#!/bin/bash
msg=$(mktemp)
python3 corona.py > "${msg}"
function sendTG() {
   curl -s "https://api.telegram.org/botHTTP_TOKEN_OF_YOUR_BOT/sendmessage" --data "text=${*}&chat_id=your_chat_id_here&parse_mode=HTML" > /dev/null
}
MESSAGE=$(cat "${msg}")
sendTG "$MESSAGE"
exit 0