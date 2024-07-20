from flask import Flask, render_template, redirect, url_for,request
from gradientai import Gradient 
import os
import csv

app = Flask(__name__)

# Define the Dataset Path
course_dataset_path = "course_data.csv"

# Initialize the Gradient
gradient = Gradient(access_token="", workspace_id="")

formatted_data = []
with open(course_dataset_path, encoding='utf-8-sig') as f:
  dataset_data = csv.DictReader(f, delimiter=",")
  for row in dataset_data:
    user_data = f"Is Paid: {row['is_paid']}, Price: {row['price']}, Number of Suscribers: {row['num_subscribers']}, num_reviews: {row['num_reviews']}, num_lectures: {row['num_lectures']}, level: {row['level']}, content_duration: {row['content_duration']}, subject: {row['subject']}"
    course_response = row['course_title']
    formatted_entry = {
        "inputs": f"### User Data:\n{user_data}\n\n### Suggested Course Name:",
        "response": f"{course_response}"
    }
    formatted_data.append(formatted_entry)

base = gradient.get_base_model(base_model_slug="nous-hermes2")
new_model_adapter = base.create_model_adapter(name='ai_course_chat_bot')

print("Fine Tuning the model.......")
chunk_lines = 20
total_chunks = [formatted_data[x:x+chunk_lines] for x in range(0, len(formatted_data), chunk_lines)]
for i, chunk in enumerate(total_chunks):
  try:
    print(f"Fine Tuning chunk {i+1} of {len(total_chunks)}")
    new_model_adapter.fine_tune(samples=chunk)
  except Exception as error:
    print(f"Error occured in fine tuning {i+1}: {error}")

# Home page route
@app.route('/')
def home():
    return render_template('home.html')

# Redirect page route
@app.route('/index',methods=['GET', 'POST'])
def redirect_page():
    if request.method == 'POST':
        paid = request.form['paid']
        price = request.form['price']
        subscriber = request.form['subscriber']
        reviews = request.form['reviews']
        lecture = request.form['lecture']
        level = request.form['level']
        duration = request.form['duration']
        subject = request.form['subject']
        
        user_query = f"Is Paid: {paid}, Price: {price}, Number of Suscribers: {subscriber}, num_reviews: {reviews}, num_lectures: {lecture}, level: {level}, content_duration: {duration}, subject: {subject}"
        formatted_query = f"### User Data:\n{user_query}\n\n### Suggested Course Name:"
        response = new_model_adapter.complete(query=formatted_query, max_generated_token_count=50)
        generated_output = response.generated_output
        return render_template('index.html', user_query=user_query, generated_output=generated_output)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
