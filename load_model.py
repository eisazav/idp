import pickle
from text_extract import get_raw_content, vectorize_text

loaded_model = pickle.load(open('./app/model/svm_model.sav', 'rb'))

def predict(file):
    raw_text = get_raw_content(file)
    file_vector = vectorize_text(raw_text)
    prediction = loaded_model.predict(X=file_vector)
    return prediction