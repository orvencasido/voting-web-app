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

@app.route('/github-webhook', methods=['POST'])
def github_webhook():
    # Just return a simple 200 OK for now to let GitHub know it's working
    return 'Webhook received!', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

