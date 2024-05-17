# Course Recommendation System

## Overview

The Course Recommendation System is a web application designed to help users find the most suitable online courses based on their preferences. By leveraging advanced machine learning techniques and the Gradient AI platform, this system provides personalized course recommendations to enhance the learning experience.

## Introduction

In today's digital age, the availability of online courses is vast, making it challenging for learners to find courses that perfectly match their needs and preferences. This project aims to streamline the course selection process by offering personalized recommendations based on user-defined criteria. Users input their preferences related to course attributes, and the system suggests courses that best fit their requirements.

## Key Details

- **Technologies Used**: Flask, Gradient AI, HTML, Python
- **Main Functionality**: Personalized course recommendations based on user inputs
- **Data Source**: CSV file containing course information
- **Model Fine-Tuning**: Utilizes Gradient AI's model fine-tuning capabilities

## Features

- **User-Friendly Interface**: Simple and intuitive web interface for users to input their course preferences.
- **Personalized Recommendations**: Generates tailored course suggestions based on multiple criteria.
- **Machine Learning Integration**: Uses Gradient AI to fine-tune a recommendation model.
- **Real-Time Results**: Provides instant course recommendations upon form submission.

## Outcomes

By using this application, users will be able to:
- Input specific criteria to filter courses
- Receive personalized course recommendations
- Make informed decisions on which courses to enroll in
- Save time in searching for relevant courses

## Installation Method

### Prerequisites

- Python 3.x
- Flask
- Gradient AI library
- CSV file containing course data

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/samagra44/EduExpert-Intelligent-Learning-Insights.git
   cd EduExpert-Intelligent-Learning-Insights
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables**
   - Ensure you have a Gradient AI account and obtain the `GRADIENT_ACCESS_TOKEN` and `GRADIENT_WORKSPACE_ID`.
   - Set these environment variables in your terminal or `.env` file:
     ```bash
     export GRADIENT_ACCESS_TOKEN="your_access_token"
     export GRADIENT_WORKSPACE_ID="your_workspace_id"
     ```

5. **Prepare the Dataset**
   - Ensure the `Course_data.csv` file is in the root directory of the project.

6. **Run the Application**
   ```bash
   python app.py
   ```
   - The application will be available at `http://localhost:5000`.

## Usage

1. **Home Page**
   - The home page provides an interface for users to input their course preferences.

2. **Input Form**
   - Users can fill out the form with criteria such as whether the course is paid, price range, number of subscribers, reviews, lectures, level, duration, and subject.

3. **Get Recommendations**
   - Upon submitting the form, the application generates a course recommendation based on the input criteria using the fine-tuned Gradient AI model.

4. **View Results**
   - The recommended courses are displayed on the results page, providing users with detailed information about each suggested course.

## Additional Information

- **Model Fine-Tuning**: The model is fine-tuned using course data formatted into a structure that Gradient AI's model understands. The fine-tuning process is chunked to handle large datasets efficiently.
- **User Interface**: Simple and intuitive user interface built with HTML and rendered using Flask.
- **Security**: Environment variables are used to securely manage sensitive information like API tokens and workspace IDs.

## Future Enhancements

- **Advanced Filtering Options**: Add more filtering criteria such as course ratings, language, and instructor experience.
- **User Authentication**: Implement user login and personalized recommendation history.
- **Integration with Course Platforms**: Integrate directly with popular online course platforms for real-time data updates.
- **Feedback System**: Allow users to provide feedback on recommendations to improve model accuracy.

---