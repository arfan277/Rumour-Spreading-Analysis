import os
import json

# file path to the dataset
dataset = 'prince-toronto'
path_file = '/Users/benzpreuengineer/Desktop/pheme-rumour-scheme-dataset/threads/en/' + dataset

# Access the tweet (original tweet structure, folder)
def Tweet(data, file):
    os.chdir(path_file + '/' + file + '/source-tweets')
    user = open(file + '.json')
    user_data = json.load(user)

    tweet = {
        "id": file,
        "text": user_data["text"],
        "user": user_data["user"]["name"],
        "user_id": user_data["user"]["id_str"],
        "replies": []
    }
    # if there is nested object
    if data[file] != []:
        Hierarchical(data[file], file, file, tweet['replies'])

    return tweet

# Access nested object (object of previous tweet, reply to whom, folder that contains data, array to store replies)
def Hierarchical(origin, pretweet, file, reply_list):

    replies = list(origin.keys())
    for reply in replies:

        os.chdir(path_file + '/' + file + '/reactions')
        user = open(reply + '.json')
        user_data = json.load(user)
        post = {
            "id": reply,
            "text": user_data["text"],
            "user": user_data["user"]["name"],
            "user_id": user_data["user"]["id_str"],
            "replied": pretweet
        }
        reply_list.append(post)

        if origin[reply] != []:
            Hierarchical(origin[reply], reply, file, reply_list)

# convert the object to json (object, iteration)
def convert_json(new_data, index):
    filename = 'reactions' + str(index) + '.json'
    
    os.chdir(path_file + '/reactions')
    with open(filename, 'w') as r:
        json.dump(new_data, r, indent=4)

# change directory to prince toronto
os.chdir(path_file)

num = 0
# access to each tweet
for folder in os.listdir():
    if folder == '.DS_Store' or folder == 'reactions':
        continue

    os.chdir(path_file + '/' + folder)
    structure = open('structure.json')
    s = json.load(structure)

    convert_json(Tweet(s, folder), num)
    print("reaction file No.{} has been successfully created!".format(num))
    num += 1
