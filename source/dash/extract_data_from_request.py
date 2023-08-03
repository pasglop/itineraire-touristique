import requests
import pandas as pd

# ------- Adresse et port de l'API --------------------------------------------------

api_address = 'localhost'
api_port = 8000

# ------- Definition fonction dataframe par itinéraire ------------------------------------

def p_request_response(hotel_poi, days):
    '''return a list of dataframe, one dataframe for each itinary'''
    url = 'http://{address}:{port}/itinary/'.format(address=api_address, port=api_port)
    user_input = {
        "hotel_poi":hotel_poi,
        "days": days
        }
    p_response = requests.post(url, json = user_input)
    dict_response = p_response.json()
    steps = dict_response['itinary']['days']
    iti_list = []
    poi_lists = [{'poi_list' : []} for i in range(user_input['days'])]
    
    # Creating one poi_list for each itinary
    for e in steps:
        iti_list.append(e['steps'])
    for i, iti in enumerate(iti_list):
        for poi in range(len(iti)):
            poi_lists[i]['poi_list'].append(iti[poi]['step_detail'])

    # Creating one dataframe for each itinary
    df_list = ['df_iti_' + str(i+1) for i in range(user_input['days'])]
    for index, i in enumerate(df_list):
        df_list[index] = pd.DataFrame.from_dict(poi_lists[index]['poi_list'])
        
    return df_list
    
    
df_list = p_request_response('226b4112-02fd-bbc4-0a6b-501b9f9d1089', 3)
print(len(df_list))
