## Basic Questionnaire for oTree

This is a basic questionnaire with page and question randomization that can be executed after or before other applications in [oTree](http://www.otree.org/), an open-source Python framework for experimental and survey research.
It includes five pages which are located under templates/questionnaire/:

- Introduction.html
- Survey1.html
- Survey2.html
- Survey3.html
- Demographics.html

The questionnaire always starts with Introduction.html, and always ends with a Demographics.html.
Between these two pages, the application randomizes other pages included under templates as "Survey*.html" and incorporated in models.py and pages.py.
The order of items and questions on every page are also randomized.  
The questionnaire also includes a progress bar.

The questionnaire was created on oTree version 2.0.29.  
You can test the application [here](https://otree-testserver.herokuapp.com/demo/Questionnaire/).
