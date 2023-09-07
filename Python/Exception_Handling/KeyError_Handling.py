facebook_posts = [
    {'Likes':21, 'Comments':2},
    {'Likes':13, 'Comments':2, 'Shear':1},
    {'Likes':33, 'Comments':8, 'Shear':3},
    {'Comments':2, 'Shear':2},
    {'Comments':2, 'Shear':1},
    {'Likes':19, 'Comments':3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass

print(total_likes)