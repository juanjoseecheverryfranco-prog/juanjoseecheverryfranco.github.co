import os
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

MODEL_DIR="models"
MODEl_PATH=os.path.join(MODEL_DIR,"model.pkl")
VECTORIZER_PATH=os.path.join(MODEL_DIR,"vectoricer.pkl")
ANSWERS_PATH= os.path.join(MODEL_DIR,"answer.pkl")

def buid_and_train_model(train_pairs):
    questions = [q for q, _ in train_pairs]
    answers = [a for _, a in train_pairs]
    vectorizer = CountVectorizer()
    x=vectorizer.fit_transform(questions)

    unique_answers = sorted(set(answers))
    answer_to_label= {a:i for i,a in enumerate(unique_answers)}
    y = [answer_to_label[a] for a in answers]
    model = MultinomialNB()
    model.fit(x,y)
    # crear parpeta para el modelo si no existe
    os.makedirs(MODEl_PATH, exist_ok=True)
    # Guardar los ojetos entrenados
    with open(MODEL_DIR, "wb") as f:
        pickle.dump(model,f)
    with open(VECTORIZER_PATH, "wb") as f:
        pickle.dump(vectorizer,f) 
    with open(ANSWERS_PATH, "wb") as f:
        pickle.dump(unique_answers,f)
        print("Modelo enrenado y guardado correctamente")
    return model, vectorizer, unique_answers
def load_model():
    if(
    os.path.exists(MODEL_DIR)
    and s.path.exists(VECTORIZER_PATH)
    and s.path.exists(ANSWERS_PATHR)
    )
     with open(MODEL_DIR, "wb") as f:
        pickle.dump(model,f)
    with open(VECTORIZER_PATH, "wb") as f:
        pickle.dump(vectorizer,f) 
    with open(ANSWERS_PATH, "wb") as f:
        pickle.dump(unique_answers,f)
        print("Modelo cargado desde disco")
        return: None,None,None
else:

