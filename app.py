# -*- coding: utf-8 -*-
from flask import Flask, send_from_directory, jsonify, request
import openai

app = Flask(__name__, static_folder='static')

openai.api_key = 'YOUR_API_KEY'

def base_369_framework():
    log = []
    for i in range(1, 370):
        log.append(f"Running iteration {i} of 369")
    return "\n".join(log)

def fibonacci_sequence():
    log = []
    a, b = 0, 1
    for i in range 10):
        a, b = b, a + b
        log.append(f"Fibonacci number {i}: {a}")
    return "\n".join(log)

def golden_ratio():
    phi = (1 + 5 ** 0.5) / 2
    return f"Golden Ratio (φ): {phi}"

def run_framework():
    output = []
    output.append("Framework execution started")
    output.append(base_369_framework())
    output.append(fibonacci_sequence())
    output.append(golden_ratio())
    output.append("Framework execution completed")
    return "\n".join(output)

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/run_framework')
def run_framework_route():
