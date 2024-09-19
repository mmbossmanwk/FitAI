# FitAI

## Overview

The **FitAI** is a powerful web application designed to create personalized fitness and diet plans tailored to individual needs. By harnessing the capabilities of Google’s Gemini AI, this tool analyzes user input to generate comprehensive workout and nutrition plans, ensuring users can effectively reach their fitness goals. 

### How It Works

Upon launching the app, users are guided through a series of input fields that gather essential information such as age, height, weight, fitness goals, dietary preferences, and any body sensitivities. Once the user submits their information, the AI processes these inputs using a predefined prompt that simulates the expertise of a professional trainer and dietitian. The result is a customized plan delivered in a structured format that includes diet recommendations, exercise routines, and additional tips.

This approach not only personalizes the experience but also leverages AI to ensure users receive data-driven advice tailored to their unique lifestyles and preferences.

### Why Adopt FitAI?

1. **Personalization**: Tailors plans to individual user needs, enhancing the likelihood of success.
2. **Expert Insights**: Utilizes AI trained on vast datasets to provide professional-grade advice.
3. **User-Friendly Interface**: The Gradio interface makes it easy for anyone to use, regardless of tech proficiency.
4. **Adaptability**: Adjusts plans based on dietary restrictions and fitness levels, accommodating a diverse user base.

### Video DEMO
https://github.com/user-attachments/assets/8c9a19fb-ecb7-4e72-a180-7fd1f1c58da4

### Installation Instructions

To build, install, and run the FitAI, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mmbossmanwk/AI-Fitness-Coach.git
   cd FitAI
   ```

2. **Install Required Libraries**:
   Make sure you have Python installed. Then, install the necessary packages:
   ```bash
   pip install google-generativeai gradio pandas
   ```

3. **Set Up API Key**:
   Replace the API key in the code with your own Google Gemini API key. Locate the line:
   ```python
   genai.configure(api_key="YOUR_API_KEY")
   ```
   and replace `YOUR_API_KEY` with your actual key.

4. **Prepare Data**:
   Ensure you have a `countries.csv` file in the root directory with country names for the dropdown.

5. **Run the Application**:
   Launch the application by running:
   ```bash
   python app.py
   ```
   The app will open in your web browser at `http://localhost:7860`.

### Usage Instructions

1. Fill out the information fields based on your fitness goals, current physical condition, and dietary preferences.
2. Click on the "Submit" button to generate your personalized fitness and diet plan.
3. Review your plan, which will be displayed in a markdown format.

### Conclusion

The FitAI is an innovative tool designed to simplify and enhance the fitness journey for individuals by providing tailored plans that can adapt to their needs. By leveraging cutting-edge AI technology, users can achieve their health and fitness goals with personalized guidance. Join us in revolutionizing the way people approach fitness!
