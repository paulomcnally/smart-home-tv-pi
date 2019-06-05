import requests


class Tv:

    @staticmethod
    def command(code):
        url = 'http://192.168.1.20/sony/IRCC'
        payload = ('<?xml version="1.0"?>'
                   '<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">'
                   '<s:Body>'
                   '<u:X_SendIRCC xmlns:u="urn:schemas-sony-com:service:IRCC:1">'
                   '<IRCCCode>%s</IRCCCode>'
                   '</u:X_SendIRCC>'
                   '</s:Body>'
                   '</s:Envelope>') % code
        response = requests.post(
            url,
            data=payload,
            headers={
                'X-Auth-PSK': '2801',
                'SOAPACTION': '"urn:schemas-sony-com:service:IRCC:1#X_SendIRCC"'
            }
        )
        if response.status_code != 200:
            raise RuntimeError(response)
