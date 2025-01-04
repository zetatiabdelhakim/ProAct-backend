import openai
import os
from dotenv import load_dotenv
import json

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_question(context, user_answer):
    try:
        client = openai.OpenAI(api_key=openai.api_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": """
                    You are an entrepreneurial assistant chatbot designed to guide students through business challenges. Your job is to evaluate the student's response based on the entrepreneurial scenario provided. Assess whether the student's decision is correct and provide constructive feedback when necessary.  
                    
                    You should respond only in the following structured format:  
                    
                    If the student's response is correct:  
                    {  
                      "true": true,  
                      "tip": null  
                    }  
                    
                    If the student's response is incorrect or needs improvement:  
                    {  
                      "true": false,  
                      "tip": "Provide a short tip (about 10 words) to guide the student."  
                    }  
                    
                    Important:  
                    - Keep the feedback concise and educational.  
                    - Encourage critical thinking while avoiding giving the full solution directly.  
                    - Focus on entrepreneurial principles, decision-making strategies, and business reasoning.  

                """},
                {"role": "user", "content": f"Challenge : {context} \n User's answer: {user_answer}"}
            ]
        )
        return json.loads(response.choices[0].message.content.strip())
    except Exception as e:
        return f"An error occurred: {str(e)}"

context = """
        Situation:
        You've just officially started your entrepreneurial journey with a bold idea. You’re passionate, but the reality of running a business hits fast. You have to decide where to focus your energy first: should you build a detailed business plan, start networking to find early clients, or jump into product development? Each choice has risks—too much planning could delay action, while rushing into development without validation could backfire.

        Challenge:
        It’s your first day, and you can only focus on one priority. You need to decide how to make the most impact early on while keeping momentum. Should you map out every detail before taking action, or focus on smaller wins to build confidence?

        Text Box for Answer:
        What would you prioritize on your first day as an entrepreneur and why? How do you balance planning with taking action? Explain your strategy and how it would set the foundation for your business success.
         """
user_answer = """
        On the first day, I would prioritize networking to find early clients. Early validation of the idea ensures the product solves real problems, guiding development and avoiding wasted resources. I’d balance planning by outlining key milestones, then taking small, impactful steps to build momentum and adapt quickly.
"""
print(ask_question(context, user_answer))