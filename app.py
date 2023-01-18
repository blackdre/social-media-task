# import get_data
from flask import Flask, jsonify
import concurrent.futures
import requests

app = Flask(__name__)


@app.route("/")
def social_network_activity():
    # TODO: your code here
    """
        GET /social_network_activity from API endpoints
    """
    try:
        # get tweets from twitter endpoint
        def get_tweets():
            twitter = requests.get('https://takehome.io/twitter')
            return twitter

        # get tweets from facebook endpoint
        def get_fb_posts():
            fb = requests.get('https://takehome.io/facebook')
            return fb

        # get tweets from twitter endpoint
        def get_ig_posts():
            ig = requests.get('https://takehome.io/instagram')
            return ig

    except ValueError:
        data = jsonify({"message": "Decoding JSON has failed"})
        return (data)

    def get_api_data():

        with concurrent.futures.ThreadPoolExecutor() as executor:
            f1 = executor.submit(get_tweets)
            f2 = executor.submit(get_fb_posts)
            f3 = executor.submit(get_ig_posts)

        elon = get_tweets().json()
        facebook = get_fb_posts().json()
        instagram = get_ig_posts().json()

        tweets = len(elon)
        fb_posts = len(facebook)
        ig_posts = len(instagram)

        data = {"twitter": tweets,
                "facebook": fb_posts, "instagram": ig_posts}
        return data

    # json_response = {
    #     jsonify(get_api_data())
    # }
    return jsonify(get_api_data())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
