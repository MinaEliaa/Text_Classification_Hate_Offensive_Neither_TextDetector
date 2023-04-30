#Random Forest Model
from flask import Flask, jsonify, request
import pickle
import numpy as np
import ssl

# Load the trained model and TF-IDF vectorizer from disk
model = pickle.load(open('Final_Model_Final.pkl', 'rb'))
vectorizer = pickle.load(open('Final_tfidf_Vectorizer_test_Final.pkl', 'rb'))

# Initialize a Flask app
app = Flask(__name__)

# Define a route for the endpoint that takes in a POST request with a JSON payload containing the tweet text
@app.route('/predict', methods=['POST'])
def predict():
    # Get the tweet text from the JSON payload
    tweet_text = request.json['tweet_text']

    # Transform the tweet text into a TF-IDF feature vector
    tweet_tfidf = vectorizer.transform([tweet_text])

    # Predict the class label of the tweet using the trained Random Forest model
    class_label = model.predict(tweet_tfidf)[0]

    # Get the probability estimates for each class using the predict_proba() method
    class_probs = model.predict_proba(tweet_tfidf)[0]

    # Print the class label and its corresponding percentage probability
    print("Class label: ", class_label)
    print("Percentage probabilities - Hate: {:.2f}%, Offensive: {:.2f}%, Neither: {:.2f}%".format(class_probs[0]*100, class_probs[1]*100, class_probs[2]*100))

    # Return the predicted class label and its corresponding percentage probabilities as a JSON response
    return jsonify({
        'class_label': int(class_label),
        'class_probs': {
            'Hate': '{:.2f}%'.format(class_probs[0] * 100),
            'Offensive': '{:.2f}%'.format(class_probs[1] * 100),
            'Neither': '{:.2f}%'.format(class_probs[2] * 100)
        }
    })

# Run the Flask app
if __name__ == '__main__':
    app.run(host="192.168.1.7", debug=True, port=8080)

#Support Vector Machine Model
# from flask import Flask, jsonify, request
# import pickle
# import numpy as np
# import ssl
# # Load the trained model and TF-IDF vectorizer from disk
# model = pickle.load(open('Final_Model.pkl', 'rb'))
# vectorizer = pickle.load(open('Final_tfidf_Vectorizer_test.pkl', 'rb'))
# # Initialize a Flask app
# app = Flask(__name__)
# # Define a route for the endpoint that takes in a POST request with a JSON payload containing the tweet text
# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get the tweet text from the JSON payload
#     tweet_text = request.json['tweet_text']
#
#     # Transform the tweet text into a TF-IDF feature vector
#     tweet_tfidf = vectorizer.transform([tweet_text])
#
#     # Predict the class label of the tweet using the trained LinearSVC model
#     class_label = model.predict(tweet_tfidf)[0]
#
#     # Get the distance of the tweet feature vector from the decision boundary of each class
#     distances = model.decision_function(tweet_tfidf)[0]
#
#     # Convert the distances into probability estimates using the softmax function
#     class_probs = np.exp(distances) / np.sum(np.exp(distances))
#
#     # Sort the class probabilities from high to low
#     sorted_probs = sorted(zip(class_probs, ['Hate', 'Offensive', 'Neither']), reverse=True)
#
#     # Return the predicted class label and its corresponding percentage probabilities as a JSON response
#     return jsonify({
#         'class_label': int(class_label),
#         'class_probs': {
#             sorted_probs[0][1]: '{:.2f}%'.format(sorted_probs[0][0] * 100),
#             sorted_probs[1][1]: '{:.2f}%'.format(sorted_probs[1][0] * 100),
#             sorted_probs[2][1]: '{:.2f}%'.format(sorted_probs[2][0] * 100)
#         }
#     })
#
# # Run the Flask app
# if __name__ == '__main__':
#     app.run(host="192.168.1.7", debug=True, port=8080)

