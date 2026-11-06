from pathlib import Path
from faq_bot import faqs
from flask import Flask, jsonify, request, send_from_directory
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ============================================================
# FLASK SETUP
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

app = Flask(
    __name__,
    static_folder=BASE_DIR,
    static_url_path="/static"
)


# ============================================================
# PREPARE QUESTIONS
# ============================================================

questions = []

question_to_faq = []


for faq_index, faq in enumerate(faqs):

    for question in faq["questions"]:

        questions.append(question)

        # Store which FAQ this question belongs to
        question_to_faq.append(faq_index)


# ============================================================
# CREATE TF-IDF VECTORIZER
# ============================================================

vectorizer = TfidfVectorizer(stop_words="english")


# Convert all FAQ questions into TF-IDF vectors
question_vectors = vectorizer.fit_transform(questions)


# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def home():

    return send_from_directory(
        BASE_DIR,
        "index.html"
    )


# ============================================================
# ASK ROUTE
# ============================================================

@app.route("/ask", methods=["POST"])
def ask():

    # Get JSON data sent by the frontend
    data = request.get_json(silent=True)


    # Check whether the received data is valid
    if not isinstance(data, dict):

        return jsonify({
            "answer": "Please send a question as JSON."
        }), 400


    # Get the user's question
    user_question = data.get("question", "").strip()


    # Check if the user entered nothing
    if not user_question:

        return jsonify({
            "answer": "Please enter a question."
        })


    # Check for exit message
    if user_question.lower() == "bye":

        return jsonify({
            "answer": "Goodbye! 👋"
        })


    # ========================================================
    # CONVERT USER QUESTION INTO TF-IDF VECTOR
    # ========================================================

    user_vector = vectorizer.transform([
        user_question
    ])


    # ========================================================
    # CALCULATE COSINE SIMILARITY
    # ========================================================

    similarities = cosine_similarity(
        user_vector,
        question_vectors
    )


    # ========================================================
    # FIND BEST MATCH
    # ========================================================

    best_match = similarities.argmax()


    # Get similarity score of the best match
    best_score = similarities[0][best_match]
    print("User question:", user_question)
    print("Best match:", questions[best_match])
    print("Similarity score:", best_score)


    # ========================================================
    # SIMILARITY THRESHOLD
    # ========================================================

    if best_score >= 0.3:

        # Find the FAQ that the matching question belongs to
        faq_index = question_to_faq[best_match]


        # Get the answer from that FAQ
        answer = faqs[faq_index]["answer"]

    else:

        # If no sufficiently similar question was found
        answer = "I'm sorry, I don't understand the question. Please try asking it in a different way."


    # ========================================================
    # SEND ANSWER BACK TO FRONTEND
    # ========================================================

    return jsonify({
        "answer": answer
    })


# ============================================================
# RUN FLASK APPLICATION
# ============================================================

if __name__ == "__main__":

    app.run(debug=True)