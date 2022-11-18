import json
def json_file_to_dict(file_path: str) -> dict:
    '''convert json to dict
    
    Args:
        file_path (str): file path.
        
    Returns:
        dict: dict data
    '''
    data=open(file_path).read()
    data_json=json.loads(data)
    return data_json


def get_number_of_users(data: dict) -> int:
    '''all users' data.
    
    Args:
        data (dict): users data
    
    Returns:
        int: number of all users.
    '''

    return len(data['users'])
d=json_file_to_dict('data.json')
#print(get_number_of_users(d))


    


def get_all_countries(data: str) -> list:
    '''all users' data.
    
    Args:
        data (dict): users data
    
    Returns:
        list: list of counrties
    '''
    r=[]
    
    for i in range(len(data['users'])):
        r.append((data['users'][i]['country']))
        
        
   
    return r
print(get_all_countries(d))
#print(d['users'])



def get_all_users_fullname(data: str) -> list:
    '''all users' data.
    
    Args:
        data (dict): users data
    
    Returns:
        list: list of all users' full name
    '''
    r=[]
    
    for i in range(len(data['users'])):
        r.append((data['users'][i]['first_name'])+' '+(data['users'][i]['last_name']))
        
        
   
    return r
print(get_all_users_fullname(d))


def get_user_by_id(a,id: int) -> dict:
    '''get user by id
    
    Args:
        id (int): user id.
        
    Returns:
        dict: user data
    ''' 
    for i in a['users']:
        if i['id'] == str(id):
            return i
        
        
    
print(get_user_by_id(d,8))


def get_user_by_firstname(a,first_name: str) -> dict:
    '''get user by first name
    
    Args:
        first_name (str): user's first name.
        
    Returns:
        dict: user data
    '''
    for i in a['users']:
        if i['first_name'] == first_name:
            return i
    


def get_user_by_lastname(a,last_name: str) -> dict:
    '''get user by last name
    
    Args:
        first_name (str): user's last name.
        
    Returns:
        dict: user data
    '''
    for i in a['users']:
        if i['last_name'] == last_name:
            return i
    
   

def get_user_by_country(a,country: str) -> dict:

    '''get user by country
    
    Args:
        country (str): name of user's country.
        
    Returns:
        dict: user data
    '''
    for i in a['users']:
        if i['country'] == country:
            return i

    

