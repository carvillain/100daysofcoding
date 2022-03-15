def find_admin(lst, lang): 
    admins_list = []
    
    for item in lst:
        if item['language'] == lang and item['githubAdmin'] == 'yes':
            admins_list.append(item)
    
    return admins_list 