import random
import pandas as pd
import string
import numpy as np
import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import ne_chunk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import json
import praw
import firebase_admin
from firebase_admin import credentials, firestore
import os

client_id = os.environ.get("client_id")
client_secret = os.environ.get("client_secret")
user_agent = os.environ.get("user_agent")
path = os.environ.get("google_credentials")
cred = credentials.Certificate(path)
firebase_admin.initialize_app(cred)
db = firestore.client()


def authenticate():
    try:
        import google.colab

        IN_COLAB = True
    except ImportError:
        IN_COLAB = False

    if IN_COLAB:
        google.colab.auth.authenticate_user()
        email = google.colab.auth.get_user_email()
        return email
    else:
        print("Not running in Google Colab")


email = authenticate()


def send_results(func_name, email, results):
    if not func_name or not email or not results:
        return json.dumps({"error": "Missing required data"})

    doc_ref = db.collection("students").document(email)
    doc_ref.set({func_name: results})

    return json.dumps({"message": "Data processed successfully!"})


def addition(add_func):
    for _ in range(10):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        expected_result = a + b
        result = add_func(a, b)

        if result == expected_result:
            send_results(
                "addition", email, (f"Addition test passed: {a} + {b} = {result}")
            )
        else:
            send_results(
                "addition",
                email,
                (
                    f"Addition test failed: {a} + {b} = {result}, expected {expected_result}"
                ),
            )


def multiplication(mult_func):
    for _ in range(10):
        a = random.randint(-100, 100)
        b = random.randint(-100, 100)
        expected_result = a * b
        result = mult_func(a, b)

        if result == expected_result:
            send_results(
                "multiplication",
                email,
                (f"Multiplication test passed: {a} * {b} = {result}"),
            )
        else:
            send_results(
                "multiplication",
                email,
                (
                    f"Multiplication test failed: {a} * {b} = {result}, expected {expected_result}"
                ),
            )


def division(div_func):
    for _ in range(10):
        a = random.randint(-100, 100)
        b = random.randint(-100, 100)

        try:
            expected_result = a / b
        except ZeroDivisionError:
            expected_result = "Cannot divide by zero"
        result = div_func(a, b)
        if result == expected_result:
            send_results(
                "multiplication",
                email,
                (f"Division test passed: {a} / {b} = {result}"),
            )
        else:
            send_results(
                "multiplication",
                email,
                (
                    f"Division test failed: {a} / {b} = {result}, expected {expected_result}"
                ),
            )


def get_random_df_for_space_check():
    dataframes = []
    for _ in range(10):
        num_rows = random.randint(1, 10)  # Random number of rows between 1 and 10
        random_text = [
            " ".join(random.choices(string.ascii_letters, k=5)) for _ in range(num_rows)
        ]
        df = pd.DataFrame({"text": random_text})
        dataframes.append(df)
    return dataframes


def dataframe_equality(df1, df2):
    # Check if the DataFrames have the same shape
    if df1.shape != df2.shape:
        return False

    # Check if the column names are the same
    if not np.array_equal(df1.columns, df2.columns):
        return False

    # Check if the values in each cell are the same
    if not df1.equals(df2):
        return False

    # The DataFrames have the same contents
    return True


def replace_spaces(replace_func):
    random_dataframes = get_random_df_for_space_check()
    # Check if the first argument is a DataFrame
    for i, df in enumerate(random_dataframes):
        expected_df = df
        actual_df = replace_func(df)

        if "text" in df.columns:
            expected_df["text"] = expected_df["text"].str.replace(" ", "+")
        else:
            print("Error: 'text' column not found in the DataFrame.")
            return expected_df

        if dataframe_equality(expected_df, actual_df):
            send_results(
                "replace_spaces",
                email,
                (f"Case {i+1} passed"),
            )
        else:
            send_results(
                "replace_spaces",
                email,
                (print(f"Case {i+1} failed")),
            )


def get_random_df_for_the_check():
    dataframes = []
    for _ in range(10):
        num_rows = random.randint(1, 10)  # Random number of rows between 1 and 10
        random_text = []
        for _ in range(num_rows):
            word_length = random.randint(1, 10)  # Random word length between 1 and 10
            random_word = "".join(random.choices(string.ascii_letters, k=word_length))
            position = random.randint(0, word_length)  # Random position within the word
            text = random_word[:position] + " the " + random_word[position:]
            random_text.append(text)
        df = pd.DataFrame({"text": random_text})
        dataframes.append(df)
    return dataframes


def replace_the(replace_func):
    random_dataframes = get_random_df_for_the_check()
    for i, df in enumerate(random_dataframes):
        expected_df = df
        actual_df = replace_func(df)

        if "text" in df.columns:
            expected_df["text"] = expected_df["text"].apply(
                lambda x: re.sub(r"\bthe\b", "a", x)
            )
        else:
            print("Error: 'text' column not found in the DataFrame.")
            return expected_df

        if dataframe_equality(expected_df, actual_df):
            send_results(
                "replace_the",
                email,
                (f"Case {i+1} passed"),
            )

        else:
            send_results(
                "replace_the",
                email,
                (f"Case {i+1} failed"),
            )


def get_random_df_for_group_check():
    dataframes = []
    np.random.seed(42)  # Set a seed for reproducibility

    for _ in range(10):
        # Generate random DataFrame
        num_rows = np.random.randint(5, 10)
        groups = np.random.randint(1, 4, size=num_rows)
        values = np.random.randint(1, 100, size=num_rows)
        df = pd.DataFrame({"group": groups, "value": values})
        dataframes.append(df)

    return dataframes


def group_check(func):
    random_dataframes = get_random_df_for_group_check()
    for i, df in enumerate(random_dataframes):
        expected_df = df.groupby("group")["value"].agg(["sum", "mean", "median"])
        actual_df = func(df)

        if dataframe_equality(expected_df, actual_df):
            send_results(
                "group_check",
                email,
                (f"Case {i+1} passed"),
            )
        else:
            send_results(
                "group_check",
                email,
                (f"Case {i+1} failed"),
            )


def get_random_df_for_join_check():
    dataframes_list_1 = []
    dataframes_list_2 = []
    np.random.seed(42)  # Set a seed for reproducibility

    for _ in range(10):
        # Generate random DataFrame for list 1
        num_rows = np.random.randint(5, 10)
        ids = [i for i in range(1, num_rows + 1)]
        values = np.random.randint(1, 100, size=num_rows)
        df_1 = pd.DataFrame({"id": ids, "value1": values})
        dataframes_list_1.append(df_1)

        # Generate random DataFrame for list 2
        num_rows = np.random.randint(5, 10)
        ids = [i for i in range(2, num_rows + 2)]
        values = np.random.randint(1, 100, size=num_rows)
        df_2 = pd.DataFrame({"id": ids, "value2": values})
        dataframes_list_2.append(df_2)

    return dataframes_list_1, dataframes_list_2


def join_check(func):
    list1, list2 = get_random_df_for_join_check()
    for i, df_A in enumerate(list1):
        for j, df_B in enumerate(list2):
            expected_df = pd.merge(df_A, df_B, on="id", how="inner")

            # Add 'total' column as the sum of 'value1' and 'value2'
            expected_df["total"] = expected_df["value1"] + expected_df["value2"]
            actual_df = func(df_A, df_B)

            if dataframe_equality(expected_df, actual_df):
                send_results(
                    "join_check",
                    email,
                    (f"Case {i+1} passed"),
                )
            else:
                send_results(
                    "join_check",
                    email,
                    (f"Case {i+1} failed"),
                )


def left_join_check(func):
    list1, list2 = get_random_df_for_join_check()
    for i, df_A in enumerate(list1):
        for j, df_B in enumerate(list2):
            expected_df = pd.merge(df_A, df_B, on="id", how="left", indicator=True)
            expected_df = expected_df[expected_df["_merge"] == "left_only"]

            actual_df = func(df_A, df_B)

            if dataframe_equality(expected_df, actual_df):
                send_results(
                    "left_join_check",
                    email,
                    (f"Case {i+1} passed"),
                )
            else:
                send_results(
                    "left_join_check",
                    email,
                    (f"Case {i+1} failed"),
                )


def get_random_df_for_count_nouns_check():
    dataframes_list = []
    random.seed(42)  # Set a seed for reproducibility

    # Download the NLTK corpora for word validation
    nltk.download("words")
    nltk.download("averaged_perceptron_tagger")

    # Get the list of valid English words from the NLTK corpus
    english_words = set(nltk.corpus.words.words())

    for _ in range(10):
        num_sentences = random.randint(3, 5)
        sentences = []

        for _ in range(num_sentences):
            sentence = []
            num_words = random.randint(5, 10)

            for _ in range(num_words):
                if random.random() < 0.2:  # Probability of adding a noun
                    noun = random.choice(list(english_words))
                    sentence.append(noun)
                elif random.random() < 0.4:  # Probability of adding an adjective
                    adj = random.choice(list(english_words))
                    sentence.append(adj)
                else:  # Probability of adding a verb
                    while True:
                        verb = random.choice(list(english_words))
                        if nltk.pos_tag([verb])[0][1].startswith(
                            "V"
                        ):  # Check if it's a verb
                            break
                    sentence.append(verb)

            sentence = " ".join(sentence)
            sentences.append(sentence)

        df = pd.DataFrame({"text": sentences})
        dataframes_list.append(df)

    return dataframes_list


def count_nouns_check(func):
    nltk.download("punkt")
    nltk.download("averaged_perceptron_tagger")
    random_dataframes = get_random_df_for_count_nouns_check()
    for i, df in enumerate(random_dataframes):
        expected_df = df
        expected_df["num_nouns"] = df["text"].apply(
            lambda x: len(
                [
                    token
                    for token, pos in nltk.pos_tag(nltk.word_tokenize(x))
                    if pos.startswith("NN")
                ]
            )
        )
        actual_df = func(df)

        if dataframe_equality(expected_df, actual_df):
            send_results(
                "count_nouns_check",
                email,
                (f"Case {i+1} passed"),
            )
        else:
            send_results(
                "count_nouns_check",
                email,
                (f"Case {i+1} failed"),
            )


def get_random_str_for_count_check():
    nltk.download("words")
    english_words = set(nltk.corpus.words.words())
    sentences = []

    for _ in range(10):
        sentence = []
        num_words = random.randint(5, 10)

        for _ in range(num_words):
            word = random.choice(list(english_words))
            sentence.append(word)

        sentence = " ".join(sentence)
        sentences.append(sentence)

    return sentences


def counter_check(func):
    random_words = get_random_str_for_count_check()
    for i, word in enumerate(random_words):
        actual_word_freq = func(word)
        expected_word = word.split()
        expected_word_freq = {}
        for word in expected_word:
            expected_word_freq[word] = expected_word_freq.get(word, 0) + 1

        if expected_word_freq == actual_word_freq:
            send_results(
                "counter_check",
                email,
                (f"Case {i+1} passed"),
            )
        else:
            send_results(
                "counter_check",
                email,
                (f"Case {i+1} failed"),
            )


def count_nouns_check(func):
    random_words = get_random_str_for_count_check()
    for i, word in enumerate(random_words):
        actual_count = func(word)
        tokens = nltk.word_tokenize(word)

        # Perform part-of-speech tagging
        tagged_tokens = nltk.pos_tag(tokens)

        # Count the number of nouns
        expected_count = sum(1 for token, pos in tagged_tokens if pos.startswith("NN"))

        if expected_count == actual_count:
            send_results(
                "count_nouns_check",
                email,
                (f"Case {i+1} passed"),
            )
        else:
            send_results(
                "count_nouns_check",
                email,
                (f"Case {i+1} failed"),
            )


def sentiment_analysis_check(func):
    random_text = get_random_str_for_count_check()
    for i, text in enumerate(random_text):
        nltk.download("vader_lexicon")
        sid = SentimentIntensityAnalyzer()
        sentiment_scores = sid.polarity_scores(text)

        compound_score = sentiment_scores["compound"]

        expected_sentiment = ""
        actual_sentiment = func(text)

        if compound_score >= 0.05:
            expected_sentiment = "Positive"
        elif compound_score <= -0.05:
            expected_sentiment = "Negative"
        else:
            expected_sentiment = "Neutral"

        if expected_sentiment == actual_sentiment:
            send_results(
                "sentiment_analysis_check",
                email,
                (f"Case {i+1} passed"),
            )
        else:
            send_results(
                "sentiment_analysis_check",
                email,
                (f"Case {i+1} failed"),
            )


def named_entity_recognition_check(func):
    random_text = get_random_str_for_count_check()
    for i, text in enumerate(random_text):
        nltk.download("maxent_ne_chunker")  # Download the necessary NLTK data
        nltk.download("words")
        tokens = word_tokenize(text)

        # Perform part-of-speech tagging
        tagged = pos_tag(tokens)

        # Use named entity recognition (NER) to identify entities
        entities = ne_chunk(tagged)

        # Initialize dictionaries to store the entities
        organization_dict = {}
        person_dict = {}
        location_dict = {}

        # Traverse the identified entities and store them in respective dictionaries
        for entity in entities:
            if hasattr(entity, "label") and entity.label() == "ORGANIZATION":
                organization = " ".join([child[0] for child in entity])
                organization_dict.setdefault("ORG", []).append(organization)
            elif hasattr(entity, "label") and entity.label() == "PERSON":
                person = " ".join([child[0] for child in entity])
                person_dict.setdefault("PERSON", []).append(person)
            elif hasattr(entity, "label") and entity.label() == "GPE":
                location = " ".join([child[0] for child in entity])
                location_dict.setdefault("LOC", []).append(location)

        # Create the JSON dictionary
        entities_json = {
            "ORG": organization_dict.get("ORG", []),
            "PERSON": person_dict.get("PERSON", []),
            "LOC": location_dict.get("LOC", []),
        }

        # Convert the JSON dictionary to a JSON string
        expected_entities = json.dumps(entities_json)
        actual_entities = func(text)

        if expected_entities == actual_entities:
            send_results(
                "named_entity_recognition_check",
                email,
                (f"Case {i+1} passed"),
            )
        else:
            send_results(
                "named_entity_recognition_check",
                email,
                (f"Case {i+1} failed"),
            )


def scrape_from_reddit_check(func):
    subreddit_name = "ut_sma"
    actual_content = func(subreddit_name)

    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
    )
    expected_content = []
    subreddit = reddit.subreddit(subreddit_name)

    for submission in subreddit.new(limit=100):
        expected_content.append(submission.title)
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            expected_content.append(comment.body)

    if expected_content == actual_content:
        send_results(
            "named_entity_recognition_check",
            email,
            ("Cases passed"),
        )
    else:
        send_results(
            "named_entity_recognition_check",
            email,
            ("Cases failed"),
        )


# TODO: Upload to the official PyPi repo and try to download in google colab notebook and check if it works
