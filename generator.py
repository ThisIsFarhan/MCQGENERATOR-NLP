import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

nlp = spacy.load("en_core_web_sm")

def preprocess(text):
  filtered = []
  for token in nlp(text):
    if token.is_stop or token.is_punct:
      continue
    filtered.append(token.lemma_)
  return " ".join(filtered)

class mcqQuestion:
  def __init__(self, ques, choices, correct_answer):
    self.ques = ques
    self.choices = choices
    self.correct_answer = correct_answer

def generateMCQS(text, numofQuestions):
    fil_index = 0

    text = text.lower()

    # nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    sentences  = []
    for sent in doc.sents:
        # print(sent.text)
        sentences.append(sent.text)

    filtered_sentences = [preprocess(sent) for sent in sentences]

    v = TfidfVectorizer()
    vectorized_sentences = v.fit_transform(filtered_sentences)

    feat_names = v.get_feature_names_out()

    scores = []
    for word in feat_names:
        index_v = v.vocabulary_.get(word)
        scores.append(v.idf_[index_v])

    n = len(feat_names)
    for i in range(n):
        for j in range(0, n-i-1):
            if scores[j] < scores[j+1]:
                scores[j], scores[j+1] = scores[j+1], scores[j]
                feat_names[j], feat_names[j+1] = feat_names[j+1], feat_names[j]

    # numofQuestions = 5
    mcqs = feat_names[:numofQuestions]

    Questions = []
    for mcq in mcqs:
        for doc in filtered_sentences:
            if mcq in doc:
            #   print(mcq, "|" ,doc, filtered_sentences.index(doc))
                fil_index = filtered_sentences.index(doc) # index of the doc containing that word

            for token in nlp(sentences[fil_index]):
                if token.is_stop or token.is_punct:
                    continue
                if token.lemma_ == mcq:
                    correctAns = token.text
                    ques = sentences[fil_index].replace(token.text, "____", 1)
                    choices = np.array([])
                    while len(choices) < 3:
                        option = np.random.choice(feat_names, 1, replace=False)
                        if option not in choices and not np.equal(option, correctAns):
                            choices = np.append(choices, option)

                    choices = np.append(choices, correctAns)
                    np.random.shuffle(choices)
            
                    objectQues = mcqQuestion(ques, choices, correctAns)

                    for q in Questions:
                        if q.ques == objectQues.ques:
                        #   print("Duplicate")
                            break
                    else:
                        Questions.append(objectQues)

    return Questions



# multiple = generateMCQS("Modern operating systems, such as Windows, macOS, and Linux, offer a wide range of features and functionalities to cater to different user needs. Windows, developed by Microsoft, is known for its user-friendly interface and extensive software compatibility. It is widely used in personal computers and enterprise environments. macOS, created by Apple, is renowned for its sleek design, robust security features, and seamless integration with other Apple products. It is the preferred choice for creative professionals and those who value a polished user experience.")

# for ques in multiple:
#   print(ques.ques)
#   print(ques.choices)
#   print(ques.correct_answer)
#   print("\n")