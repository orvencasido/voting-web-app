from flask import Flask, render_template, request
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        vote = request.form['vote']
        r.incr(vote)
    votes = {animal: r.get(animal) or 0 for animal in ['Cat', 'Dog', 'Mouse']}
    return render_template('index.html', votes=votes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

