# Importing necessary libraries
import google.generativeai as genai
import gradio as gr
import pandas as pd

# Configure the Gemini API with the user's API key
genai.configure(api_key="GOOGLE_API_KEY")

# Configuration for the AI model's generation settings
generation_config = {
    "temperature": 0.7,        # Controls randomness in responses; higher values mean more randomness
    "top_p": 1,                # Top-p sampling; consider the top p% of probable next tokens
    "top_k": 1,                # Limits the sampling pool to the top k tokens
    "max_output_tokens": 8192, # Maximum number of tokens for the generated response
}

# Safety settings to filter harmful content
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

# Initialize the generative model with specified settings
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    safety_settings=safety_settings
)

def get_countries_name():
    """
    Retrieves a list of country names from a CSV file.

    Returns:
        list: A list of country names.
    """
    countries = pd.read_csv("countries.csv")
    return countries.name.tolist()

# Fetch the list of countries for the dropdown
country_list = get_countries_name()

# Define various options for user input
build_options = ["Thin", "Average", "Broad or Muscular", "Significantly Overweight"]
flexibility_options = ["Very flexible", "Pretty flexible", "Not that good", "I'm not sure"]
diet_preferences = [
    "Vegan", "Vegetarian", "Jain", "Swaminarayan", "Non-Vegetarian",
    "Paleo", "Ketogenic", "Mediterranean", "DASH", "Gluten-Free", "Intermittent Fasting", "Low-FODMAP"
]
water_intake_options = ["Less than 2 glasses", "About 2 glasses", "2 to 6 glasses", "More than 5 glasses"]
sleep_duration_options = ["Less than 5 hours", "5-6 hours", "7-8 hours", "More than 8 hours"]
preferred_workout_duration = ["10-15 minutes", "15-25 minutes", "25+ minutes", "Don't know"]
workout_frequency_options = ["Almost every day", "Several times per week", "Several times per month", "Never"]
work_schedule_options = ["9 to 5", "Night shifts", "My hours are flexible", "Not working/retired"]
daily_activity_choices = ["I spend most of the day sitting", "I take active breaks", "I'm on my feet all day long"]
body_sensitivity_choices = [
    "Sensitive back", "Sensitive knees", "None",
    "Chronic pain", "Recent injury", "Joint issues",
    "Muscle strains", "Limited mobility", "Balance problems"
]
dream_goal_options = ["Build muscle & strength", "Lose weight", "Improve mobility", "Develop flexibility", "Improve overall fitness"]
additional_goals = [
    "Increase endurance", "Improve mental health", "Get fit for an event",
    "Enhance athletic performance", "Improve posture", "Train for a specific sport",
    "Increase flexibility", "Boost energy levels", "Reduce stress", "Achieve a specific weight"
]

def generate_fitness_plan(age, country, height, weight, build, flexibility, diet, water, sleep,
                           workout_time, workout_freq, work_schedule, daily_activity,
                           body_sensitivities, bad_habits, fitness_goal,
                           favorite_foods, disliked_foods, dietary_restrictions,
                           meal_types, macro_goal):
    """
    Generates a personalized fitness and diet plan based on user inputs.

    Parameters:
        age (int): User's age.
        country (str): User's country of residence.
        height (float): User's height in centimeters.
        weight (float): User's weight in kilograms.
        build (str): User's physical build.
        flexibility (str): User's flexibility level.
        diet (str): User's dietary preference.
        water (str): User's daily water intake.
        sleep (str): User's usual sleep duration.
        workout_time (str): Desired workout duration.
        workout_freq (str): User's workout frequency.
        work_schedule (str): User's work schedule.
        daily_activity (str): User's daily activity level.
        body_sensitivities (list): List of body sensitivities.
        bad_habits (str): User's bad habits.
        fitness_goal (str): User's primary fitness goal.
        favorite_foods (str): User's favorite foods.
        disliked_foods (str): Foods to avoid.
        dietary_restrictions (list): List of dietary restrictions.
        meal_types (list): List of preferred meal types.
        macro_goal (str): User's macro goals.

    Returns:
        str: A markdown formatted string containing the diet and exercise plan.
    """
    calculated_bmi = round(weight / ((height / 100) ** 2))
    body_sensitivity = ", ".join(body_sensitivities) if body_sensitivities else "None"
    
    # Create a prompt for the AI model to generate a personalized plan
    prompt = (
        f"You are Chad, an expert body trainer and dietician who has successfully helped numerous celebrities achieve their desired physique. "
        f"A new user has joined your academy, and your job is to guide the user with a proper exercise plan and diet plan to achieve their ideal shape. "
        f"I will provide you with the user information, and you have to strictly output in a markdown table form. "
        f"User Information: "
        f"Age: {age}, "
        f"Country of residence: {country}, "
        f"Height: {height / 100} in meters, "
        f"Weight: {weight} in kilograms, "
        f"BMI: {calculated_bmi}, "
        f"Current physical build: {build}, "
        f"Current body flexibility: {flexibility}, "
        f"Preferred Diet: {diet}, "
        f"Daily water intake: {water}, "
        f"Usual sleep duration: {sleep}, "
        f"How long workouts: {workout_time}, "
        f"Workout frequency: {workout_freq}, "
        f"User work schedule: {work_schedule}, "
        f"Usual daily activity of user: {daily_activity}, "
        f"Body Struggles: {body_sensitivity}, "
        f"Bad Habits: {bad_habits}, "
        f"Dream physique: {fitness_goal}, "
        f"Favorite Foods: {favorite_foods}, "
        f"Foods to Avoid: {disliked_foods}, "
        f"Dietary Restrictions: {', '.join(dietary_restrictions)}, "
        f"Meal Types: {', '.join(meal_types)}, "
        f"Macro Goals: {macro_goal}. "
        f"Carefully design a diet and exercise plan keeping all this information in mind. "
        f"Separate Diet Plan, Exercise Plan, Recommendations by --- at the end."
    )

    # Generate content using the AI model based on the prompt
    response = model.generate_content(prompt)
    return response.text

# Gradio Interface setup
with gr.Blocks() as demo:
    gr.Markdown("## AI Fitness Coach 🤖")
    gr.HTML("<h4>Let's start! Fill out the information below to help me understand your goals and needs.</h4>")

    # Input fields for user data
    age_input = gr.Number(label="What is your age?", value=18, minimum=16)
    selected_country = gr.Dropdown(label="Select Your Country:", choices=country_list)
    height_input = gr.Number(label="What is your height (in centimeters)?", value=168, minimum=100)
    weight_input = gr.Number(label="What is your weight (in kilograms)?", value=60, minimum=20)

    selected_build = gr.Dropdown(label="How would you describe your physical build?", choices=build_options)
    selected_flexibility = gr.Dropdown(label="How flexible are you?", choices=flexibility_options)
    selected_diet = gr.Dropdown(label="What type of diet do you prefer?", choices=diet_preferences)
    selected_water_intake = gr.Dropdown(label="What's your daily water intake?", choices=water_intake_options)
    selected_sleep_duration = gr.Dropdown(label="How much sleep do you usually get?", choices=sleep_duration_options)
    selected_workout_time = gr.Dropdown(label="How long do you want your workouts to be?", choices=preferred_workout_duration)
    selected_workout_frequency = gr.Dropdown(label="How often do you work out?", choices=workout_frequency_options)
    selected_work_schedule = gr.Dropdown(label="What is your work schedule like?", choices=work_schedule_options)
    selected_daily_activity = gr.Dropdown(label="How would you describe your typical day?", choices=daily_activity_choices)
    selected_body_sensitivity = gr.CheckboxGroup(label="Do you struggle with any of the following? (Select multiple if needed)", choices=body_sensitivity_choices)
    bad_habits_input = gr.Textbox(label="Any bad habits? Please specify:", placeholder="E.g., Watching TV while eating, Smoking")
    selected_fitness_goal = gr.Dropdown(label="What Is Your Main Goal?", choices=dream_goal_options)
    selected_additional_goals = gr.CheckboxGroup(label="Do you have any additional fitness goals?", choices=additional_goals)
    favorite_foods_input = gr.Textbox(label="Favorite Foods (comma-separated):", placeholder="E.g., Chicken, Broccoli, Rice")
    disliked_foods_input = gr.Textbox(label="Foods to Avoid (comma-separated):", placeholder="E.g., Nuts, Dairy")
    dietary_restrictions = gr.CheckboxGroup(label="Do you have any dietary restrictions?", choices=["Gluten-Free", "Nut-Free", "Dairy-Free", "Vegetarian", "Vegan"])
    meal_types = gr.CheckboxGroup(label="What types of meals do you want plans for?", choices=["Breakfast", "Lunch", "Dinner", "Snacks"])
    macro_goal_input = gr.Textbox(label="Set your macro goals (carbs/protein/fat in grams):", placeholder="E.g., 200/150/70")

    submit_button = gr.Button("Submit")
    output_box = gr.Markdown("")  # Placeholder for the output

    def handle_submit(age, country, height, weight, build, flexibility, diet, water, sleep,
                      workout_time, workout_freq, work_schedule, daily_activity,
                      body_sensitivities, bad_habits, fitness_goal,
                      favorite_foods, disliked_foods, dietary_restrictions,
                      meal_types, macro_goal):
        """
        Handles the submission of user data, generates a fitness plan, and returns the result.

        Parameters:
            (same as above)
        
        Returns:
            str: Output message or error if applicable.
        """
        if not body_sensitivities:
            return "Please select at least one option from Body Sensitivity to continue."
        
        # Call the fitness plan generation function with the collected parameters
        return generate_fitness_plan(age, country, height, weight, build, flexibility, diet,
                                      water, sleep, workout_time, workout_freq, work_schedule,
                                      daily_activity, body_sensitivities, bad_habits, fitness_goal,
                                      favorite_foods, disliked_foods, dietary_restrictions,
                                      meal_types, macro_goal)

    # Connect the submit button to the handle_submit function
    submit_button.click(
        handle_submit,
        inputs=[
            age_input, selected_country, height_input, weight_input,
            selected_build, selected_flexibility, selected_diet,
            selected_water_intake, selected_sleep_duration,
            selected_workout_time, selected_workout_frequency,
            selected_work_schedule, selected_daily_activity,
            selected_body_sensitivity, bad_habits_input,
            selected_fitness_goal, favorite_foods_input,
            disliked_foods_input, dietary_restrictions,
            meal_types, macro_goal_input
        ],
        outputs=output_box
    )

# Launch the Gradio app
demo.launch()
