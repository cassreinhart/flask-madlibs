from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story, storyList

app = Flask(__name__)
app.config['SECRET_KEY'] ='madlibzarekewl1995'

debug = DebugToolbarExtension(app)

@app.route('/')
def show_form():
    prompts = story.prompts
    return render_template('index.html', prompts= prompts)

@app.route('/story')
def show_story():
    txt = story.generate(request.args)
    return render_template('story.html', txt=txt)

# storyList = [fantasy, camp, weird_news]

@app.route('/madlibs-2')
def show_dropdown():
    print(storyList[0])
    stories = story.getStory(storyList)
    return render_template('menu.html', stories=stories)