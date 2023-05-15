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
        score = int(self.question1.data) + int(self.question2.data) + int(self.question3.data) + int(self.question4.data) + int(self.question5.data) + int(self.question6.data) + int(self.question7.data) + int(self.question8.data) + int(self.question9.data)
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

# Social Anxiety Inventory (SPIN) Form
class SPINForm(FlaskForm):
    question1 = RadioField('I am afraid of people in authority', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Somewhat'), ('3', 'Very much'), ('4', 'Extremely')])
    question2 = RadioField('I am bothered by blushing in front of people', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Somewhat'), ('3', 'Very much'), ('4', 'Extremely')])
    question3 = RadioField('Parties and social events scare me', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Somewhat'), ('3', 'Very much'), ('4', 'Extremely')])
    question4 = RadioField('I avoid talking to people I don\'t know', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Somewhat'), ('3', 'Very much'), ('4', 'Extremely')])
    question5 = RadioField('Being criticized scares me a lot', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Somewhat'), ('3', 'Very much'), ('4', 'Extremely')])
    question6 = RadioField('I avoid doing things or speaking to people for fear of embarassment', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Somewhat'), ('3', 'Very much'), ('4', 'Extremely')])
    question7 = RadioField('Sweating in front of people causes me distress', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Somewhat'), ('3', 'Very much'), ('4', 'Extremely')])
    question8 = RadioField('I avoid going to parties', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Somewhat'), ('3', 'Very much'), ('4', 'Extremely')])
    question9 = RadioField('I avoid activities in which I am the centre of attention', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Somewhat'), ('3', 'Very much'), ('4', 'Extremely')])
    question10 = RadioField('Talking to strangers scares me', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Somewhat'), ('3', 'Very much'), ('4', 'Extremely')])
    question11 = RadioField('I avoid having to give speeches', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Somewhat'), ('3', 'Very much'), ('4', 'Extremely')])
    question12 = RadioField('I would do anything to avoid being critized', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Somewhat'), ('3', 'Very much'), ('4', 'Extremely')])
    question13 = RadioField('Heart palitations bother me when I am around people', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Somewhat'), ('3', 'Very much'), ('4', 'Extremely')])
    question14 = RadioField('I am afraid of doing things when people might be watching', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Somewhat'), ('3', 'Very much'), ('4', 'Extremely')])
    question15 = RadioField('Being embarassed or looking stupid are among my worst fears', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Somewhat'), ('3', 'Very much'), ('4', 'Extremely')])
    question16 = RadioField('I avoid speaking to anyone in authority', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Somewhat'), ('3', 'Very much'), ('4', 'Extremely')])
    question17 = RadioField('Trembling or shaking in front of others is distressing to me', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Somewhat'), ('3', 'Very much'), ('4', 'Extremely')])

# PCL-5 Form (PTSD)
class PCL5Form(FlaskForm):
    question1 = RadioField('Repeated, disturbing, and unwanted memories of the stressful experience?', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Moderately'), ('3', 'Quite a bit'), ('4', 'Extremely')])
    question2 = RadioField('Repeated, disturbing dreams of the stressful experience?', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Moderately'), ('3', 'Quite a bit'), ('4', 'Extremely')])
    question3 = RadioField('Suddenly feeling or acting as if teh stressful experience were actually happenning again (as if you were actually reliving it)?', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Moderately'), ('3', 'Quite a bit'), ('4', 'Extremely')])
    question4 = RadioField('Feeling very upset when something reminded you of the stressful experience?', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Moderately'), ('3', 'Quite a bit'), ('4', 'Extremely')])
    question5 = RadioField('Having strong physical reactions when something reminded you of the stressful experience (for example, heart pounding, trouble breating, sweating)?', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Moderately'), ('3', 'Quite a bit'), ('4', 'Extremely')])
    question6 = RadioField('Avoiding memories, thoughts, or feelings related to the stressful experience?', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Moderately'), ('3', 'Quite a bit'), ('4', 'Extremely')])
    question7 = RadioField('Avoiding external reminders of the stressful experience (for example, people, places, conversations, activities, objects, or situations)?', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Moderately'), ('3', 'Quite a bit'), ('4', 'Extremely')])
    question8 = RadioField('Trouble remembering important parts of the stressful experience?', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Moderately'), ('3', 'Quite a bit'), ('4', 'Extremely')])
    question9 = RadioField('Having strong negative beliefs about yourself, other people, or the world (for example, having thoughts such as: I am bad, there is something seriously wrong with me, no one can be trused, the world is completely dangerous)?', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Moderately'), ('3', 'Quite a bit'), ('4', 'Extremely')])
    question10 = RadioField('Blaming yourself or someone else for the stressful experience or what happened after it?', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Moderately'), ('3', 'Quite a bit'), ('4', 'Extremely')])
    question11 = RadioField('Having strong negative feelings such as fear, horror, anger, guilt, or shame?', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Moderately'), ('3', 'Quite a bit'), ('4', 'Extremely')])
    question12 = RadioField('Loss of interest in activities that you used to enjoy?', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Moderately'), ('3', 'Quite a bit'), ('4', 'Extremely')])
    question13 = RadioField('Feeling distant or cut off from other people?', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Moderately'), ('3', 'Quite a bit'), ('4', 'Extremely')])
    question14 = RadioField('Trouble experiencing positive feelings (for example, being unable to feel happiness or have loving feelings for people close to you)?', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Moderately'), ('3', 'Quite a bit'), ('4', 'Extremely')])
    question15 = RadioField('Irritable behaviour, angry outbursts, or acting aggressively?', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Moderately'), ('3', 'Quite a bit'), ('4', 'Extremely')])
    question16 = RadioField('Taking too many risks or doing things that could cause you harm?', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Moderately'), ('3', 'Quite a bit'), ('4', 'Extremely')])
    question17 = RadioField('Being "superalert" or watchful or on guard?', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Moderately'), ('3', 'Quite a bit'), ('4', 'Extremely')])
    question18 = RadioField('Feeling jumpy or easily startled?', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Moderately'), ('3', 'Quite a bit'), ('4', 'Extremely')])
    question19 = RadioField('Having difficulty concentrating?', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Moderately'), ('3', 'Quite a bit'), ('4', 'Extremely')])
    question20 = RadioField('Trouble falling or staying asleep?', choices=[('0', 'Not at all'), ('1', 'A little bit'), ('2', 'Moderately'), ('3', 'Quite a bit'), ('4', 'Extremely')])