import aiohttp
import json
from flask import current_app

async def send_message(data):
    headers = {
         "Content-type"  :"application/json",
         "Authorization" : f"Bearer{'EAAJZAehx8ONYBAHJtPBy6141oFiOv9DDXZAEWElOC4aZCCNiSRqbdVzZBYvyjIM2r2YC0KkZCHit3hgUWw6clzvHfmMK2n65AHWDuB76jmOVYxZBZAXixd7IZCAs2IS7WIeCcRZAJltwCmU8SsKLkaTTmd08lrglREPmy4fIojmrmbgMOHjZAWMjHolDF9awoevMOyy2iEZBsHvkndB93OgvzYfq0GFSZBT0sLieWDgEUlwj7gZDZD'}",
         }

    async with aiohttp.ClientSession() as session:
        url='https://graph.facebook.com' + f"/{'v13.0'}/{'+5581991581431'}/messages"
        try:
            async with session.post(url, data=data, headers=headers) as response:
                if response.status == 200:
                    print('OK!!!')
                    print("Status:",response.status)
                    print ( "Content-type:",response.headers['content-type'])

                    html = await response.text()
                    print ("Body:", html)
                else:
                    print('NÃO!!!')
                    print(response.status)
                    print (response)
        except aiohttp.ClientConnectorError as e:
            print('Connection Error', str(e))

def get_text_message_input(recipient, text):
    print(recipient)
    return json.dumps({
        "messaging_product" : "whatsapp",
        "preview_url": False,
        "recipient_type" : "individual",
        "to" : recipient,
        "type" : "text",
        "text" : {
            "body" : text
            }
        })