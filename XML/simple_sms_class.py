import requests


class SMS:
    sms_club_url = 'https://gate.smsclub.mobi/token/'

    def __init__(self, username, token, alpha_name):
        self.username = username
        self.token = token
        self.alpha_name = alpha_name

    def send_sms(self, to_number, text):
        response = requests.get(
            '{}?username={}&token={}&from={}&to={}&text={}'.format(
                self.sms_club_url, self.username, self.token,
                self.alpha_name, to_number, text
            ),
        )
        print('response: ', response.status_code, response.content)
        return response


sms_client = SMS('38269926164', '1K_lMY9V4wVa1ag', 'InetShop')
sms_client.send_sms('38269926164', 'Ok, i will by beer for you')
