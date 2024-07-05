from flask import Flask, request, jsonify
from flask_cors import CORS

import json
import requests
from dotenv import load_dotenv
import os
import nltk
import certifi
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)
cors = CORS(app)

load_dotenv()

@app.route('/analyze', methods=['POST'])

def main():
	# Initialize the VADER sentiment analyzer
	# sia = SentimentIntensityAnalyzer()

	url = "https://twitter154.p.rapidapi.com/search/search/continuation"


	headers = {
		"x-rapidapi-key": "8ca76a5a73msh37efff02acd68c6p1fb499jsn4975698c67cb",
		"x-rapidapi-host": os.getenv("x-rapidapi-host")
	}

	hashtag = request.json.get('text')    
	print("+++",hashtag)
	print("----",type(hashtag))
	querystring = {
		"query":{hashtag},
		"section":"top",
		"min_retweets":"2",
		"limit":"20",
		"continuation_token":"DAACCgACF_Sz76EAJxAKAAMX9LPvoP_Y8AgABAAAAAILAAUAAABQRW1QQzZ3QUFBZlEvZ0dKTjB2R3AvQUFBQUFVWDlJWmx4cHZBZkJmMG5RNUxHdUVQRi9TdTZPSGJzQ0VYOUp6Y3psdUJ3UmYwbFE3Q1dxQWsIAAYAAAAACAAHAAAAAAwACAoAARf0hmXGm8B8AAAA",
		"min_likes":"20",
		"start_date":"2024-01-01",
		"language":"en"
	}
		
	response = requests.get(url, headers=headers, params=querystring)
	print(os.getenv('x-rapidapi-key'))

	# response1 = "I'm not sure how I feel about this."
	if not response:
		return jsonify({'error': 'No response generated'}), 400

	# results = sia.polarity_scores(response1)
	# print(response.json().get('results')[0].get('text'))
	# print(results)
	data = response.json()

	result = {	
		'Positive':0,
		'Negative':0,
		'Mixed':0,
		'Neutral':0,
		'Ambiguous':0
	}

	for i in range(20):
		result[categorize_sentiment(data.get('results')[i].get('text'))] += 1
	
	# return categorize_sentiment(response.json().get('results')[0].get('text'))
	return result

sia = SentimentIntensityAnalyzer()

def categorize_sentiment(text):
    # Get the sentiment scores
    scores = sia.polarity_scores(text)
    pos = scores['pos']
    neg = scores['neg']
    neu = scores['neu']
    comp = scores['compound']

	# print(scores)
    # Categorize based on compound score and other parameters
    if comp >= 0.05:
        return "Positive"
    elif comp <= -0.05:
        return "Negative"
    elif pos > 0 and neg > 0:
        return "Mixed"
    elif comp == 0:
        return "Neutral"
    else:
        return "Ambiguous"

if __name__ == '__main__':
    app.run(debug=True)

# print(response.json())

# response = {'results': [{'tweet_id': '1808184611002110284', 'creation_date': 'Tue Jul 02 17:03:00 +0000 2024', 'text': 'How to learn python programming in 10 days https://t.co/ESvFlxvEFf\n\n#python https://t.co/l8J1VQK0BY', 'media_url': ['https://pbs.twimg.com/media/GReOWF9aYAAJHCb.png'], 'video_url': None, 'user': {'creation_date': 'Fri Jun 17 12:22:15 +0000 2016', 'user_id': '743780794997547008', 'username': 'Python_Dv', 'name': 'Python Developer', 'follower_count': 85729, 'following_count': 1135, 'favourites_count': 3876, 'is_private': None, 'is_verified': False, 'is_blue_verified': True, 'location': 'United States', 'profile_pic_url': 'https://pbs.twimg.com/profile_images/842358957997883392/59-UQhVS_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/743780794997547008/1489669161', 'description': 'A place for all things related to the #python #programming #coding #webdeveloper #webdevelopment #pythonprogramming #ai #ml #machinelearning #datascience ...', 'external_url': 'https://morioh.com/a/778c1bdf55fa/30-python-projects-for-beginners-to-get-started-coding', 'number_of_tweets': 7516, 'bot': False, 'timestamp': 1466166135, 'has_nft_avatar': False, 'category': None, 'default_profile': False, 'default_profile_image': False, 'listed_count': 751, 'verified_type': None}, 'language': 'en', 'favorite_count': 379, 'retweet_count': 91, 'reply_count': 4, 'quote_count': 3, 'retweet': False, 'views': 22025, 'timestamp': 1719939780, 'video_view_count': None, 'in_reply_to_status_id': None, 'quoted_status_id': None, 'binding_values': None, 'expanded_url': 'https://twitter.com/Python_Dv/status/1808184611002110284/photo/1', 'retweet_tweet_id': None, 'extended_entities': {'media': [{'display_url': 'pic.twitter.com/l8J1VQK0BY', 'expanded_url': 'https://twitter.com/Python_Dv/status/1808184611002110284/photo/1', 'id_str': '1808070285620568064', 'indices': [76, 99], 'media_key': '3_1808070285620568064', 'media_url_https': 'https://pbs.twimg.com/media/GReOWF9aYAAJHCb.png', 'type': 'photo', 'url': 'https://t.co/l8J1VQK0BY', 'ext_media_availability': {'status': 'Available'}, 'features': {'large': {'faces': [{'x': 195, 'y': 710, 'h': 65, 'w': 65}, {'x': 29, 'y': 137, 'h': 222, 'w': 222}]}, 'medium': {'faces': [{'x': 195, 'y': 710, 'h': 65, 'w': 65}, {'x': 29, 'y': 137, 'h': 222, 'w': 222}]}, 'small': {'faces': [{'x': 165, 'y': 603, 'h': 55, 'w': 55}, {'x': 24, 'y': 116, 'h': 188, 'w': 188}]}, 'orig': {'faces': [{'x': 195, 'y': 710, 'h': 65, 'w': 65}, {'x': 29, 'y': 137, 'h': 222, 'w': 222}]}}, 'sizes': {'large': {'h': 801, 'w': 697, 'resize': 'fit'}, 'medium': {'h': 801, 'w': 697, 'resize': 'fit'}, 'small': {'h': 680, 'w': 592, 'resize': 'fit'}, 'thumb': {'h': 150, 'w': 150, 'resize': 'crop'}}, 'original_info': {'height': 801, 'width': 697, 'focus_rects': [{'x': 0, 'y': 0, 'w': 697, 'h': 390}, {'x': 0, 'y': 0, 'w': 697, 'h': 697}, {'x': 0, 'y': 0, 'w': 697, 'h': 795}, {'x': 0, 'y': 0, 'w': 401, 'h': 801}, {'x': 0, 'y': 0, 'w': 697, 'h': 801}]}}]}, 'conversation_id': '1808184611002110284', 'retweet_status': None, 'quoted_status': None, 'bookmark_count': 306, 'source': 'TweetDeck Web App', 'community_note': None}, {'tweet_id': '1800382165156352049', 'creation_date': 'Tue Jun 11 04:18:52 +0000 2024', 'text': 'Data #Analytics with #Python — list of courses: https://t.co/3nIa1QPezf compiled by @tut_ml https://t.co/vh75wWljfL', 'media_url': ['https://pbs.twimg.com/media/GPw-CR_WMAAPHv8.jpg'], 'video_url': None, 'user': {'creation_date': 'Fri Mar 23 16:35:17 +0000 2012', 'user_id': '534563976', 'username': 'KirkDBorne', 'name': 'Kirk Borne', 'follower_count': 450240, 'following_count': 5742, 'favourites_count': 228162, 'is_private': None, 'is_verified': False, 'is_blue_verified': True, 'location': 'Maryland, USA', 'profile_pic_url': 'https://pbs.twimg.com/profile_images/1112733580948635648/s-8d1avb_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/534563976/1706648943', 'description': 'Advisor to startups. Freelancer. Global Speaker. Founder @LeadershipData. Top influencer in #BigData #DataScience #AI #IoT #ML #B2B. PhD Astrophysics @Caltech', 'external_url': 'http://www.linkedin.com/in/kirkdborne', 'number_of_tweets': 181896, 'bot': False, 'timestamp': 1332520517, 'has_nft_avatar': False, 'category': None, 'default_profile': False, 'default_profile_image': False, 'listed_count': 10335, 'verified_type': None}, 'language': 'en', 'favorite_count': 983, 'retweet_count': 247, 'reply_count': 2, 'quote_count': 1, 'retweet': False, 'views': 124124, 'timestamp': 1718079532, 'video_view_count': None, 'in_reply_to_status_id': None, 'quoted_status_id': None, 'binding_values': None, 'expanded_url': 'https://twitter.com/KirkDBorne/status/1800382165156352049/photo/1', 'retweet_tweet_id': None, 'extended_entities': {'media': [{'display_url': 'pic.twitter.com/vh75wWljfL', 'expanded_url': 'https://twitter.com/KirkDBorne/status/1800382165156352049/photo/1', 'id_str': '1800382159951114240', 'indices': [92, 115], 'media_key': '3_1800382159951114240', 'media_url_https': 'https://pbs.twimg.com/media/GPw-CR_WMAAPHv8.jpg', 'type': 'photo', 'url': 'https://t.co/vh75wWljfL', 'ext_media_availability': {'status': 'Available'}, 'features': {'large': {'faces': [{'x': 161, 'y': 411, 'h': 76, 'w': 76}, {'x': 756, 'y': 633, 'h': 222, 'w': 222}]}, 'medium': {'faces': [{'x': 146, 'y': 373, 'h': 68, 'w': 68}, {'x': 686, 'y': 574, 'h': 201, 'w': 201}]}, 'small': {'faces': [{'x': 82, 'y': 211, 'h': 39, 'w': 39}, {'x': 388, 'y': 325, 'h': 114, 'w': 114}]}, 'orig': {'faces': [{'x': 161, 'y': 411, 'h': 76, 'w': 76}, {'x': 756, 'y': 633, 'h': 222, 'w': 222}]}}, 'sizes': {'large': {'h': 1322, 'w': 1116, 'resize': 'fit'}, 'medium': {'h': 1200, 'w': 1013, 'resize': 'fit'}, 'small': {'h': 680, 'w': 574, 'resize': 'fit'}, 'thumb': {'h': 150, 'w': 150, 'resize': 'crop'}}, 'original_info': {'height': 1322, 'width': 1116, 'focus_rects': [{'x': 0, 'y': 0, 'w': 1116, 'h': 625}, {'x': 0, 'y': 0, 'w': 1116, 'h': 1116}, {'x': 0, 'y': 0, 'w': 1116, 'h': 1272}, {'x': 297, 'y': 0, 'w': 661, 'h': 1322}, {'x': 0, 'y': 0, 'w': 1116, 'h': 1322}]}}]}, 'conversation_id': '1800382165156352049', 'retweet_status': None, 'quoted_status': None, 'bookmark_count': 1058, 'source': 'Twitter for iPhone', 'community_note': None}], 'continuation_token': 'DAACCgACF_Sz76EAJxAKAAMX9LPvoP-x4AgABAAAAAILAAUAAABoRW1QQzZ3QUFBZlEvZ0dKTjB2R3AvQUFBQUFjWDlJWmx4cHZBZkJmMG5RNUxHdUVQRi9TdTZPSGJzQ0VYOUp6Y3psdUJ3UmtYOWxMVEc5Rk1HUHcrQ2xZWDBERVg5SlVPd2xxZ0pBPT0IAAYAAAAACAAHAAAAAQwACAoAAhj8PgpWF9AxAAAA'}
# print(response.json().get('results')[0].get('text'))