from flask import Flask, request, jsonify
from highlight import process_highlight  # Import the logic from highlight.py

app = Flask(__name__)

@app.route('/highlight', methods=['POST'])
def highlight():
    data = request.json
    paragraph = data.get('paragraph', '')
    words_to_highlight = data.get('words', [])
    underline_style = data.get('underlineStyle', 'solid')
    underline_color = data.get('underlineColor', '#ffdd00')
    text_color = data.get('textColor', '#000000')

    # Call the highlight processing function
    updated_paragraph = process_highlight(paragraph, words_to_highlight, underline_style, underline_color, text_color)

    return jsonify({'updatedParagraph': updated_paragraph})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)