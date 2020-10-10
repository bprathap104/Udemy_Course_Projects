import requests
import notify2
import time


def update():
    covid_url='https://api.covid19india.org/data.json'
    r = requests.get(covid_url)
    # print(pprint(r.json()['statewise']))
    statewise=r.json()['statewise']
    notify2.init("Covid Notifier")
    n = notify2.Notification(None, icon='')
    n.set_urgency(notify2.URGENCY_NORMAL) 
    n.set_timeout(10000)
    # list_of_states=list(filter(lambda state:(state['statecode']=='TN' or state['statecode']=='WB'), statewise))
    [ (n.update("Covid Notifier", f'{state["state"]} Status:\n {state["active"]}'), n.show(), time.sleep(5)) for state in list_of_states]

    # [ (n.update("Covid Notifier", f'{state["state"]} Status:\n {state["active"]}'), n.show(), time.sleep(5))  for state in statewise]
    # [ (n.update("Covid Notifier", f'{state["state"]} Status:\n {state["active"]}'), n.show(), time.sleep(5))  for state in statewise if state["statecode"] == 'WB' or state["statecode"] == 'TN']
    
    # for state in statewise:
    #     if state["statecode"] == 'WB' or state["statecode"] == 'TN':
    #         n.update("Covid Notifier", f'{state["state"]} Status:\n {state["active"]}')
    #         n.show() 
    #         time.sleep(15)

update()

