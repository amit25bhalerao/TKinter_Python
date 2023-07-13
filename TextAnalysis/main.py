from flask import Flask, render_template, request, jsonify
import tkinter as tk
from tkinter import messagebox
import re

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/count_characters', methods=['POST'])
def count_characters():
    input_text = request.form['input_text']
    character_count = len(input_text) if input_text else 0
    return jsonify({'character_count': character_count})


@app.route('/count_words', methods=['POST'])
def count_words():
    input_text = request.form['input_text']
    words = re.findall(r'\w+', input_text)
    word_count = len(words)
    return jsonify({'word_count': word_count})


@app.route('/count_spaces', methods=['POST'])
def count_spaces():
    input_text = request.form['input_text']
    space_count = input_text.count(" ")
    return jsonify({'space_count': space_count})


if __name__ == '__main__':
    app.run(debug=True)
