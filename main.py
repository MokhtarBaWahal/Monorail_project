from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']

    # Implement the signup logic here
    # ...

    class Ticket:
        def __init__(self, title, seatsLeft, startTime, endTime, price ):
            self.title = title
            self.seatsLeft = seatsLeft
            self.startTime = startTime
            self.endTime = endTime
            self.price = price
 


    sched = [Ticket("Elestad - Hesham Barakat", 5, "9:00 am", "9:30 am", 20),
             Ticket("Hesham Barakat - Nori Khatab", 12, "9:30 am", "10:00 am", 10),
             Ticket("Nori Khatab - El Hay ElSabe3", 2, "10:00 am", "10:30 am", 20),
             Ticket("El Hay ElSabe3 - Zaker Hussien", 5, "10:30 am", "11:00 am", 20),
             Ticket("Zaker Hussien - El Manteka El Hora", 5, "11:00 am", "11:30 am", 20),
             Ticket("El Manteka El Hora - El Mosheer Tantawy", 5, "11:30 am", "12:00 pm", 20),
             Ticket("El Mosheer Tantawy - Cairo Festival", 5, "12:00 pm", "12:30 pm", 20),
             Ticket("Cairo Festival - Elshowayfat", 5, "1:00 pm", "1:30 pm", 20),
             Ticket("Elshowayfat - Air Force Hospital", 5, "1:30 pm", "2:00 pm", 20),
             Ticket("Air Force Hospital - Hay El Narges", 5, "2:00 pm", "2:30 pm", 20),
             Ticket("Hay El Narges - Mohamed Nageeb", 5, "2:30 pm", "3:00 pm", 20),
             Ticket("Mohamed Nageeb - AUC", 5, "3:00 pm", "3:30 pm", 20),
             Ticket("AUC - Emaar", 5, "3:30 pm", "4:00 pm", 20),
             ]
    return render_template('trip.html', sched = sched)

@app.route('/signup', methods=['POST'])
def login():
    
    # Implement the login logic here
    # ...
    return render_template('signup.html')

@app.route('/guest', methods=['POST'])
def guest():
    # Implement the guest login logic here
    # ...
    return render_template('trip.html')

if __name__ == '__main__':
    app.run(debug=True)
