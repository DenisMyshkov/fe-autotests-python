import requests


def net_log_creator(sessionID, ae_buyer_id, session_id, name_for_bs):
    try:
        response = requests.get(
            f'https://api.browserstack.com/automate/sessions/{session_id}/networklogs',
            auth=('',''))
        while response.status_code != 200:
            response = requests.get(
                f'https://api.browserstack.com/automate/sessions/{session_id}/networklogs',
                auth=('',''))
        data = response.json()
        log = []
        payment_log = []
        for entre in data['log']['entries']:
            if 'melon' in entre['request']['url'] and entre['response']['status'] in [500,400]:
                log.append(f"URL : {entre['request']['url']}")
                log.append(f"Response status: {entre['response']['status']}")
                log.append(f"{entre['startedDateTime']}")
                for header in entre['request']['headers']:
                    if header['name'] == 'x-aer-session-id':
                        log.append(f"x-aer-session-id: {header['value']}")
                for header in entre['response']['headers']:
                    if header['name'] == 'x-aer-trace-id':
                        log.append(f"x-aer-trace-id: {header['value']}\n")
            if 'payment/query-result' in entre['request']['url'] and entre['request']['method'] == 'POST':
                payment_log.append(f"URL : {entre['request']['url']}")
                payment_log.append(f"Response status: {entre['response']['status']}")
                payment_log.append(f"{entre['startedDateTime']}")
                for header in entre['request']['headers']:
                    if header['name'] == 'x-aer-session-id':
                        payment_log.append(f"x-aer-session-id: {header['value']}")
                for header in entre['response']['headers']:
                    if header['name'] == 'x-aer-trace-id':
                        payment_log.append(f"x-aer-trace-id: {header['value']}\n")
        log_text = "\n".join(log).replace("\n","<br />\n")
        payment_log_text = "\n".join(payment_log).replace("\n","<br />\n")
        finish_log = f"<head></head><body><div>{sessionID}<br /><br />" \
                     f"USER_ID: {ae_buyer_id}<br /><br /></div><div>" \
                     f"{log_text}</div><div>" \
                     f"{payment_log_text}</div><div>" \
                     f"{name_for_bs}</div></body>"
    except:
        finish_log = f"<head></head><body><div>There is an error while catching net log!!!<br /><br />{name_for_bs}</div></body>"
    return finish_log