import json
import random
import os

class IntentMatcher:
    def __init__(self, intents_file_path):
        self.intents_file_path = intents_file_path
        self.intents = self.train()

    def tokenize(self, input_string):
        processed_string = input_string.lower().strip().replace(r"[^\w\s]|_", "").replace(r"\s+", " ")
        words = processed_string.split(" ")

        return words

    def tokenize_list(self, input_list):
        token_words = []
        for word in input_list:
            token = self.tokenize(word)
            token_words.append(token)

        return token_words

    def train(self):
        with open(self.intents_file_path, "r") as file:
            intents = json.load(file)
        return intents

    def pattern_compare(self, input_string):
        input_string_lower = input_string.lower()
        highest_similarity = 0
        most_similar_pattern = None
        similarity_percentage = 0

        for intent_class in self.intents["intents"]:
            overall_word_list = []
            similarity = 0

            for pattern in intent_class["patterns"]:
                word_list = []
                pattern_lower = pattern.lower()
                word_list = self.tokenize(pattern_lower)
                overall_word_list.append(word_list)
                new_list = []
                new_bag = []

                for word in word_list:
                    word = self.stem(word)
                    new_list.append(word)

                word_list_2 = self.tokenize(input_string_lower)
                for word in word_list_2:
                    word = self.stem(word)
                    new_bag.append(word)

                word_list = new_list
                word_list_2 = new_bag

                for word in word_list_2:
                    if word in word_list:
                        similarity += 1

                if similarity > highest_similarity:
                    similarity_percentage = similarity / (len(overall_word_list) + len(word_list_2))
                    highest_similarity = similarity
                    most_similar_pattern = intent_class

#        print(f"Similarity: {similarity_percentage:.2%}")

        if most_similar_pattern:
            highest_similarity = highest_similarity / 100
            return most_similar_pattern, highest_similarity
        else:
            raise ValueError("No matching intent class found.")

    def response_compare(self, input_string, intent_class):
        input_string_lower = input_string.lower()
        highest_similarity = 0
        similarity_percentage = 0
        distance = 0
        most_similar_response = None

        responses = intent_class["responses"] if intent_class else []

        for response in responses:
            similarity = 0
            Count = 0
            InputCount = 0
            response_lower = response.lower()
            word_list = self.tokenize(response_lower)
            new_list = []
            new_bag = []

            for word in word_list:
                word = self.stem(word)
                new_list.append(word)

            word_list_2 = self.tokenize(input_string_lower)
            for word in word_list_2:
                word = self.stem(word)
                new_bag.append(word)

            word_list = new_list
            word_list_2 = new_bag
            overall_word_list = word_list + word_list_2

            for word in word_list_2:
                if word in word_list:
            # Check if the word begins with a capital letter
                    if word.istitle():
                        similarity += 2  # Add 2 to the similarity for words with capital letters
                    else:
                        similarity += 1

            response_words = self.tokenize(response)
            input_words = self.tokenize(input_string)

            for word in response_words:
                Count += 0.01

            for word in input_words:
                InputCount += 0.01

            distance = Count + InputCount / 2

#            print(distance)

            similarity = similarity - distance

        # Calculate the similarity percentage and the distance
            similarity_percentage = similarity / len(overall_word_list)  # Calculate average similarity

            if similarity > highest_similarity:
                highest_similarity = similarity
                most_similar_response = response

#        print(f"Similarity: {similarity_percentage:.2%}")
#        print(f"Distance: {distance}")

        return most_similar_response

    def stem(self, input_word):
        suffixes = ["ing", "ly", "ed", "es", "'s", "er", "est", "y", "ily", "able", "ful", "ness", "less", "ment", "ive", "ize", "ous"]
        for suffix in suffixes:
            if input_word.endswith(suffix):
                input_word = input_word[:-len(suffix)]
                break
        return input_word

    def stem_sentence(self, input_string):
        word_list = input_string.split(" ")
        stemmed_words = []

        for input_word in word_list:
            word = self.stem(input_word)
            stemmed_word.append(word)

        return stemmed_words

    def stem_list(self, input_list):
        stemmed_words = []
        for word in input_list:
            stemmed_word = self.stem(word)
            stemmed_words.append(stemmed_word)

        return stemmed_words

    # Experimental Development Zone

    def SynonymCompare(self, word):
        newword = None
        thesaurus = self.load_thesaurus()
        for synonym in thesaurus[word]["synonyms"]:
            for associate in thesaurus[word]["related"]:
                if synonym in associate:
                    newword = associate

        if newword is not None:
            return newword
        else:
            random_newword = random.choice(thesaurus[word]["related"])
            return random_newword

    def ResponseGenerator(self, most_similar_response):
        thesaurus = self.load_thesaurus()

        tokens = self.tokenize(most_similar_response)

        for i, token in enumerate(tokens):
            for word in thesaurus:
                if token in thesaurus[word]["synonyms"]:
                    newword = self.SynonymCompare(word)
                    tokens[i] = newword

        generated_response = " ".join(tokens)

        return generated_response

    def load_thesaurus(self):
        file_path = os.path.join(os.path.dirname(__file__), "thesaurus.json")
        with open(file_path, "r") as f:
            thesaurus = json.load(f)
        return thesaurus
