'''
This module is all about pot interface functions
'''

import db

db_name = "pot.sqlite"
tbl_name = "pot"

def Register(project_name, suffix_query, notif_method, template, counter_atk, will_expire_in):
    '''
    Add the given information into the Pot DB:
        - Generate url suffixes as Primary Keys from suffix_query
        - counter_atk is a list of all counter attack ids
        - will_expire_in is an integer minutes that this pot will be deleted in,
            needs to use _Calculate_timestamp to calculate the target timestamp.
    @Return:
        A tuple: (# suffixes needed to register, # registered suffixes)
    '''
    num_of_registered_url_suffixes = 0
    url_suffix_list = _Suffix_query_parse(suffix_query)
    for each_url_suffix in url_suffix_list:
        # Check if each url_suffix exists, if not, then add into the db
        if db.Exist("url_suffix", each_url_suffix, db_name, tbl_name):
            # Do nothing and goto the next url_suffix
            continue
        # Calculate valid_til timestamp
        valid_til = _Calculate_timestamp(int(will_expire_in))
        # Construct and Add the new record into pot database
        data = {
            "project_name"  :   project_name,
            "url_suffix"    :   each_url_suffix,
            "suffix_query"  :   suffix_query,
            "notif_method"  :   notif_method,
            "template"      :   template,
            "counter_atk"   :   counter_atk,
            "valid_til"     :   valid_til
        }
        db.Add(data, db_name, tbl_name)
        num_of_registered_url_suffixes += 1
    return (len(url_suffix_list), num_of_registered_url_suffixes)

def Delete(suffix_query):
    '''
    Remove certain pots given the suffix_query
    @Return: None
    '''
    for each_url_suffix in _Suffix_query_parse(suffix_query):
        # Skip deletion if the url_suffix does not exist in db.
        if not db.Exist("suffix_query", each_url_suffix, db_name, tbl_name):
            continue
        # Remove the record from database's table
        db.Remove("suffix_query", each_url_suffix, db_name, tbl_name)

def _Calculate_timestamp(num_of_minutes):
    '''
    @Return: expire_timestamp = current_timestamp + num_of_minutes
    '''
    import datetime
    current_timestamp = int(datetime.datetime.now().timestamp())
    expire_timestamp = current_timestamp + num_of_minutes * 60
    return expire_timestamp

def _Suffix_query_parse(suffix_syntax):
    '''
    Parses the suffix syntax query into a distinct list of url suffixes
    @Return: A list of all suffixes generated by the given suffix query
    '''
    # Temporarily make url_suffix the same as the suffix query,
    #   need to change later on
    return [suffix_syntax]

def Get_all_pots():
    '''
    @Return: A JSON dict of all pots information.
    '''
    pass


# for i in range(1000):
#     Register(
#         "project_name",
#         str(i) + "suffix_query",
#         "notif_method",
#         "html",
#         "counter_atk",
#         str(i)
#     )
#     print(db.Size(db_name, tbl_name))
# print("End!")
# import time
# time.sleep(5)
for i in range(1000):
    Delete(str(i) + "suffix_query")
    print(db.Size(db_name, tbl_name))
