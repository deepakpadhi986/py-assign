import openai
from flask import Flask, render_template, request


app = Flask(__name__)
openai.api_key = "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"


def generate_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text
    except Exception as e:
        return f"Error: {e}"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def result():
    prompt = request.form['message']
    response = generate_response(prompt)
    return render_template('result.html', prompt=prompt, response=response)

if __name__ == '__main__':
    app.run(debug=True)

