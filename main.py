from flask import Flask, render_template, request
import webbrowser
from gemini import gen_ai
from rag import retrieve

app = Flask(__name__)


@app.route("/chatbot")
def home():
    return render_template("bot.html")


@app.route("/response", methods=["POST"])
def response():
    input = request.form["n1"]
    answer = retrieve(input)
    print("retrived\n",answer)
    print("Question : ",input)
    prompt = f"""
            You are a hotel assistant chatbot.

            RULES:
            - Use ONLY the provided context
            - If answer is not in context, say: "I don't know. Please contact hotel staff."
            - Do NOT invent information like prices, policies, or links
            - Be short, clear, and helpful

            CONTEXT:
            {answer}

            USER QUESTION:
            {input}

            Answer:

            """
    answer = retrieve(input)
    if "hotel staff" in answer.lower():
        data = "I don't know. Please contact hotel stafff."
    else:
        print("Gemini Response ::")
        data = gen_ai(prompt)

    return render_template("bot.html", data=data)


if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000/chatbot")
    app.run(debug=True,use_reloader= False)
