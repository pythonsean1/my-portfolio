from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/quiz', methods=['POST'] ) # Create a quiz route that only handles post requests
def quiz():
    if request.method == 'POST':
        # Get data from form
        question1 = request.form.get('question1') # .get returns None if empty
        if question1 == 'red':
            question1_answer = 'CORRECT! my favourite colour is red'
        else:
            question1_answer = 'INCORRECT my favourite colour is red'

        # question2
        question2 = request.form.get('question2') # .get returns None if empty
        if question2 == 'pizza':
            question2_answer = 'CORRECT! my favourite food is pizza'
        else:
            question2_answer = 'INCORRECT my favourite food is pizza'

        # question3
        question3 = request.form.get('question3') # .get returns None if empty
        if question3 == 'japan':
            question3_answer = 'CORRECT! my dream holiday is Japan'
        else:
            question3_answer = 'INCORRECT my dream holiday is Japan'
        
        # question 4
        question4 = request.form.get('question4') # .get returns None if empty
        if question4 == 'volleyball':
            question4_answer = 'CORRECT! my favourite sport is volleyball'
        else:
            question4_answer = 'INCORRECT my favourite sport is volleyball'
        
        # question 5 
        question5 = request.form.get('question5') # .get returns None if empty
        if question5 == 'injustice':
            question5_answer = 'CORRECT! my favourite game is injustice'
        else:
            question5_answer = 'INCORRECT my favourite game is injustice'
        
        # question 6
        question6 = request.form.get('question6') # .get returns None if empty
        if question6 == 'london':
            question6_answer = 'CORRECT! I live in the city of london'
        else:
            question6_answer = 'INCORRECT I live in the city of london'

        # question 7
        question7 = request.form.get('question7') # .get returns None if empty
        if question7 == 'owl':
            question7_answer = 'CORRECT! My favourite animal is  owl'
        else:
            question7_answer = 'INCORRECT My favourite animal is  owl'
        
        # question 8
        question8 = request.form.get('question8') # .get returns None if empty
        if question8 == 'kendrick':
            question8_answer = 'CORRECT! My favourite rapperl is Kendrick Llamar'
        else:
            question8_answer = 'INCORRECT My favourite rapperl is Kendrick Llamar '
        
        # question 9
        question9 = request.form.get('question9') # .get returns None if empty
        if question9 == 'pokemon':
            question9_answer = 'CORRECT! If I was able to choose to be in a game I would be in Pokemon'
        else:
            question9_answer = 'INCORRECT If I was able to choose to be in a game I would be in Pokemon '
        
        # question 10
        question10 = request.form.get('question10') # .get returns None if empty
        if question10 == 'spiderman btsv':
            question10_answer = 'CORRECT! My favourite movie is Spider-man: Beyond The Spider-Verse'
        else:
            question10_answer = 'INCORRECT My favourite movie is Spider-man: Beyond The Spider-Verse '


        





        



    return render_template('index.html', question1_answer=question1_answer, answer2=question2_answer, answer3=question3_answer, answer4=question4_answer, answer5=question5_answer, answer6=question6_answer, answer7=question7_answer, answer8=question8_answer, answer9=question9_answer, answer10=question10_answer)

if __name__ == '__main__':
    app.run(debug = True)