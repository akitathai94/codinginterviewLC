def build_profile(first, last, **user_info):
    user_info['firstname'] = first
    user_info['lastname'] = last
    return user_info

# user_profile = build_profile('Thai', 
#                             'Truong', 
#                             location= 'San Jose',
#                             field='Computer Engineering')

# print(user_profile)