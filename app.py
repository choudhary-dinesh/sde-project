#Author : Dinesh Kumar(M22AIE227)
#Flsak api for news summerization.
from flask import Flask, render_template, request, jsonify
# Replace below with import of news summarization function
processed_text = """
External Affairs Minister S. Jaishankar’s official visit to London had a surprise twist on Monday, when he met with former U.K. Prime Minister and the country’s newly appointed Foreign Secretary David Cameron. Mr. Jaishankar was scheduled to meet with James Cleverly as Foreign Secretary, but Prime Minister Rishi Sunak had undertaken a major Cabinet reshuffle on Monday morning prior to Mr. Jaishankar’s meeting.

Congratulating him on his appointment, Mr. Jaishankar said he looked forward to working with Mr. Cameron closely, adding that the two Ministers had held a detailed discussion on realising the full potential of the strategic partnership between the two countries.

A pleasure to meet UK Foreign Secretary @David_Cameron this afternoon on his first day in office. Congratulated him on his appointment.

Held a detailed discussion on realizing the full potential of our strategic partnership.

Also exchanged views on the situation in West Asia,… pic.twitter.com/guxyCxLuRM

— Dr. S. Jaishankar (@DrSJaishankar) November 13, 2023
“Also exchanged views on the situation in West Asia, the Ukraine conflict and the Indo-Pacific,” he said.

"""


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_text', methods=['POST'])
def process_text():
    text = request.form.get('input_text')
    # Insert news summarization function call on input text 
    #processed_text = news_summarization_fn(text)
    return jsonify({'processed_text': processed_text})

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = "80", debug=True)
