from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField 
from wtforms.validators import DataRequired

# PHQ-9 Form
class PHQ9Form(FlaskForm):
    question1 = RadioField('Little interest or pleasure in doing things?', choices=[('0', 'Not at all'), ('1', 'Several days'), ('2', 'More than half the days'), ('3', 'Nearly every day')])
    question2 = RadioField('Feeling down, depressed, or hopeless?', choices=[('0', 'Not at all'), ('1', 'Several days'), ('2', 'More than half the days'), ('3', 'Nearly every day')])
    question3 = RadioField('Trouble falling or staying asleep, or sleeping too much?', choices=[('0', 'Not at all'), ('1', 'Several days'), ('2', 'More than half the days'), ('3', 'Nearly every day')])
    question4 = RadioField('Feeling tired or having little energy?', choices=[('0', 'Not at all'), ('1', 'Several days'), ('2', 'More than half the days'), ('3', 'Nearly every day')])
    question5 = RadioField('Poor appetite or overeating?', choices=[('0', 'Not at all'), ('1', 'Several days'), ('2', 'More than half the days'), ('3', 'Nearly every day')])
    question6 = RadioField('Feeling bad about yourself - or that you are a failure or have you let yourself or your family down?', choices=[('0', 'Not at all'), ('1', 'Several days'), ('2', 'More than half the days'), ('3', 'Nearly every day')])
    question7 = RadioField('Trouble concentrating on things, such as reading the newspaper or watching television?', choices=[('0', 'Not at all'), ('1', 'Several days'), ('2', 'More than half the days'), ('3', 'Nearly every day')])
    question8 = RadioField('Moving or speaking so slowly that other people could have noticed? Or the opposite - being so fidgety or restless that you have been moving a lot more than usual?', choices=[('0', 'Not at all'), ('1', 'Several days'), ('2', 'More than half the days'), ('3', 'Nearly every day')])
    question9 = RadioField('Thoughts that you would be better off dead, or of hurting yourself in some way?', choices=[('0', 'Not at all'), ('1', 'Several days'), ('2', 'More than half the days'), ('3', 'Nearly every day')])

    def calculate_score(self):
        score = (int(self.question1.data) + int(self.question2.data) + int(self.question3.data) + int(self.question4.data) + 
                 int(self.question5.data) + int(self.question6.data) + int(self.question7.data) + int(self.question8.data) + 
                 int(self.question9.data))
        if score is None:
            score = 0
            return score
        return score

# GAD07 Form
class GAD7Form(FlaskForm):
    question1 = RadioField('Feeling nervous, anxious, or on edge?', choices=[('0', 'Not at all'), ('1', 'Several days'), ('2', 'More than half the days'), ('3', 'Nearly every day')])
    question2 = RadioField('Not being able to stop or control worrying?', choices=[('0', 'Not at all'), ('1', 'Several days'), ('2', 'More than half the days'), ('3', 'Nearly every day')])
    question3 = RadioField('Worrying too much about different things?', choices=[('0', 'Not at all'), ('1', 'Several days'), ('2', 'More than half the days'), ('3', 'Nearly every day')])
    question4 = RadioField('Having trouble relaxing?', choices=[('0', 'Not at all'), ('1', 'Several days'), ('2', 'More than half the days'), ('3', 'Nearly every day')])
    question5 = RadioField('Being so restless that it is hard to sit still?', choices=[('0', 'Not at all'), ('1', 'Several days'), ('2', 'More than half the days'), ('3', 'Nearly every day')])
    question6 = RadioField('Becoming easily annoyed or irritable?', choices=[('0', 'Not at all'), ('1', 'Several days'), ('2', 'More than half the days'), ('3', 'Nearly every day')])
    question7 = RadioField('Feeling afraid as if something awful might happen?', choices=[('0', 'Not at all'), ('1', 'Several days'), ('2', 'More than half the days'), ('3', 'Nearly every day')])
    
    def calculate_score(self):
        score = (int(self.question1.data) + int(self.question2.data) + int(self.question3.data) + int(self.question4.data) + 
                 int(self.question5.data) + int(self.question6.data) + int(self.question7.data))
        if score is None:
            score = 0
            return score
        return score