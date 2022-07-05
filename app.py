
from stories import stories,story_dict
import random
from flask import Flask, request, render_template

app =Flask(__name__)


@app.route('/')
def home_page():
    return render_template('homePage.html')




@app.route('/allStories')
def stories_page():
    return render_template('allStories.html',lst =stories)


@app.route('/storyForm')
def Form_page():
    story =None
    if request.args.get("story"):
        story = request.args.get("story")
    else:
        story =random.choice(stories)
    lst =story.prompts
    return render_template('storyForm.html',lst =lst, story_id =story.id)


@app.route('/Stories')
def get_story():
    story_id =request.args["story_id"]
    current_story = story_dict.get(story_id)
    text = current_story.generate(request.args)
    return render_template('Madlibs.html',text=text)
