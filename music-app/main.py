from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    output_song = None
    if request.method == 'POST':
        input_language = request.form.get('language')
        song_title = request.form.get('song_title')

        # For demonstration purposes, we'll just echo back the input.
        # Replace this with your actual song matching logic.
        output_song = f"Suggested song for '{song_title}' in {input_language} (placeholder)."

    return render_template('index.html', output_song=output_song)


if __name__ == '__main__':
    app.run(debug=True)
