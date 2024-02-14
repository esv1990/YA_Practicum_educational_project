import configuration
import requests

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

response = get_docs()
#print((response.status_code))
#print(response.url)

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count":20})

response = get_logs()
#print(response.status_code)
#print(response.headers)
#print(response.text)

def get_user_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

response = get_user_table()

print(response.status_code)
print(response.request)