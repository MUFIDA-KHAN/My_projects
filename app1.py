# import streamlit as st
# import pickle
# import pandas as pd
# import docx2txt
# import re
# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.model_selection import train_test_split
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.svm import SVC
# from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# # Load the trained SVM classifier
# loaded_clf = pickle.load(open('clf1.pkl', 'rb'))

# # Load the pre-trained CountVectorizer from the pickle file
# with open('cv1.pkl', 'rb') as file:
#     loaded_cv = pickle.load(file)
# cv = pickle.load(open('cv.pkl', 'rb'))  
# # Function to preprocess the input resume text
# def preprocess_resume(text):
#     # Perform the same preprocessing steps as in the training code
#      # Convert text to lowercase
#     text = text.lower()

#     # Remove any non-alphabetic characters except spaces
#     text = re.sub('[^a-zA-Z ]', '', text)

#     # Tokenize the text
#     words = nltk.word_tokenize(text)

#     # Lemmatize words to their base form
#     lemmatizer = WordNetLemmatizer()
#     words = [lemmatizer.lemmatize(word) for word in words]

#     # Remove stop words
#     stop_words = set(stopwords.words('english'))
#     words = [word for word in words if word not in stop_words]

#     # Reconstruct the text from processed words
#     processed_text = ' '.join(words)

#     return processed_text

# # # Function to make predictions using the loaded classifier
# # def make_prediction(resume_text):
# #     preprocessed_text = preprocess_resume(resume_text)
# #     input_df = pd.DataFrame([preprocessed_text], columns=['Raw'])
# #     prediction = loaded_clf.predict(input_df)[0]
# #     category_map = {0: 'React', 1: 'SQL', 2: 'PeopleSoft', 3: 'workday r'}
# #     predicted_category = category_map[prediction]
# #     return predicted_category

# def make_prediction(resume_text):
#     # Preprocess the extracted text
#     preprocessed_text = preprocess_resume(resume_text)

#     # Convert the preprocessed text into a DataFrame
#     input_df = pd.DataFrame([preprocessed_text], columns=['Raw'])

#     # Use the pre-trained CountVectorizer to transform the input text
#     input_transformed = loaded_cv.transform(input_df['Raw'])

#     # Use the loaded SVM classifier to make predictions
#     prediction = loaded_clf.predict(input_transformed)

#     return prediction[0]

# def main():
#     st.title('Resume Classification App')
#     st.write("Upload your DOCX file below and click the 'Predict' button to get the category.")

#     # User input for uploading the DOCX file
#     uploaded_file = st.file_uploader("Upload your DOCX file", type=['docx'])

#     if st.button('Predict'):
#         if uploaded_file is not None:
#             # Extract text from the uploaded DOCX file
#             resume_text = docx2txt.process(uploaded_file)

#             # Preprocess the extracted text
#             preprocessed_text = preprocess_resume(resume_text)

#             # Convert the preprocessed text into a DataFrame
#             input_df = pd.DataFrame([preprocessed_text], columns=['Raw'])

#             # Use the loaded classifier and CountVectorizer to make predictions
#             input_transformed = cv.transform(input_df['Raw'])  # Transform input using CountVectorizer
#             prediction = loaded_clf.predict(input_transformed)[0]

#             # Map numerical label back to category name
#             category_map = {0: 'React', 1: 'SQL', 2: 'PeopleSoft', 3: 'workday r'}
#             predicted_category = category_map[prediction]

#             # Display the predicted category
#             st.success(f"Predicted Category: {predicted_category}")

# if __name__ == "__main__":
#     main()

import streamlit as st
import pickle
import pandas as pd
import docx2txt
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
# Load the trained SVM classifier
loaded_clf = pickle.load(open('clf.pkl', 'rb'))

# Load the pre-trained CountVectorizer from the pickle file
with open('cv.pkl', 'rb') as file:
    loaded_cv = pickle.load(file)
    
# Function to preprocess the input resume text
def preprocess_resume(text):
    # Perform the same preprocessing steps as in the training code
     # Convert text to lowercase
    text = text.lower()

    # Remove any non-alphabetic characters except spaces
    text = re.sub('[^a-zA-Z ]', '', text)

    # Tokenize the text
    words = nltk.word_tokenize(text)

    # Lemmatize words to their base form
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    # Reconstruct the text from processed words
    processed_text = ' '.join(words)

    return processed_text

# # Function to make predictions using the loaded classifier
# def make_prediction(resume_text):
#     preprocessed_text = preprocess_resume(resume_text)
#     input_df = pd.DataFrame([preprocessed_text], columns=['Raw'])
#     prediction = loaded_clf.predict(input_df)[0]
#     category_map = {0: 'React', 1: 'SQL', 2: 'PeopleSoft', 3: 'workday r'}
#     predicted_category = category_map[prediction]
#     return predicted_category

def make_prediction(resume_text):
    # Preprocess the extracted text
    preprocessed_text = preprocess_resume(resume_text)

    # Convert the preprocessed text into a DataFrame
    input_df = pd.DataFrame([preprocessed_text], columns=['Raw'])

    # Use the pre-trained CountVectorizer to transform the input text
    input_transformed = loaded_cv.transform(input_df['Raw'])

    # Use the loaded SVM classifier to make predictions
    input_transformed_dense = input_transformed.toarray()
    prediction = loaded_clf.predict(input_transformed_dense )

    return prediction[0]

# Define a function to extract skills from the resume text
def extract_skills(text):
    # For demonstration purposes, let's use a fixed list of skills
    skills = ["React", "SQL", "Python", "Data Analysis", "Machine Learning"]
    return skills

def main():
    st.title('Resume Classification App')
    st.write("Upload your DOCX file below and click the 'Predict' button to get the category.")

    # User input for uploading the DOCX file
    uploaded_file = st.file_uploader("Upload your DOCX file", type=['docx','txt','pdf'])

    if st.button('Predict'):
        if uploaded_file is not None:
            # Extract text from the uploaded DOCX file
            resume_text = docx2txt.process(uploaded_file)

            # Make predictions using the loaded classifier
            predicted_category = make_prediction(resume_text)


            # Display the predicted category
            st.success(f"Predicted Category: {predicted_category}")
            img_path = 'skills.png.jpeg'
            st.image(img_path, caption='Your Image Caption', use_column_width=True)

        else:
            st.warning("Please upload a DOCX file to proceed with prediction.")

if __name__ == "__main__":
    main()
