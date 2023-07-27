from flask import Flask, render_template, request, jsonify
import bardapi

app = Flask(__name__)

token = ''


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form.get('question')

        # Send an API request and get a response.
        response = bardapi.core.Bard(token).get_answer(question)

        # Get the content from the response.
        content = response['content']

        return jsonify({'content': content})

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
