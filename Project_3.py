import string

with open('stopwords.txt','r',encoding = 'UTF-8') as stops:
    eng_words = [line.rstrip() for line in stops]

def distill_tweet(tweet):
    words = tweet.lower().replace("'",'').translate(tweet.maketrans('‘-','  ','.,!‘?"')).split()
    result = []
    for word in words:
        if word not in eng_words and not word.startswith('http') and not word.isnumeric():
            result.append(word)
    return result

def tweet_lists(filename): 
    result = []
    cur_name = ''
    with open(filename, 'r') as file:
        for line in file:
            line = line.split('\t')
            user = line[1]
            tweet = line[2]
            if user == cur_name:
                cur = open(user + '.txt', 'a')
            else:
            	if cur_name != '': 
            		cur.close() 
            	cur_name = user
            	result += [user]
            	cur = open(user + '.txt', 'w')
            cur.writelines(tweet + '\n')
            cur.close()
    return result 

def tweets_from_file(filename):
    with open(filename, 'r',encoding ='UTF-8') as file:
        tweets = [line.strip() for line in file]
    return tweets

def top_entries(tweets, num_cutoff = 1, hashes = False, mentions = False):
    hashtags = []
    tags = []
    name = []
    for tweet in tweets:
        name.extend(distill_tweet(tweet))
    h_m = {}
        #keys: hashtags, values: number of times hashtag is used
    if hashes == True:
        for word in name:
            if word.startswith('#'):
                hashtags.append(word)
        for word in hashtags:
            if hashtags.count(word) >= num_cutoff:
                if word in h_m:
                    h_m[word] += 1
                else:
                    h_m[word] = 1
        return h_m
    if hashes == False and mentions == True:
        for word in name:
            if word.startswith('@'):
                tags.append(word)
        for word in tags:
            if tags.count(word) >= num_cutoff:
                if word in h_m:
                    h_m[word] += 1
                else:
                     h_m[word] = 1
        return h_m
