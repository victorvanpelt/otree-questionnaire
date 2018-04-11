## Basic Questionnaire for oTree

This is a basic questionnaire that can be executed after or before other applications in [oTree](http://www.otree.org/), an open-source Python framework for experimental and survey research.
It includes four pages which are located under templates:

- Introduction.html
- Survey1.html
- Survey2.html
- Demographics.html

The questionnaire always starts with Introduction.html, and always ends with a Demographics.html.
Between these two pages, the application randomizes other pages included under templates as "Survey*.html" and incorporated in models.py and pages.py.
The order of items and questions on every page are also randomized.  
  
The questionnaire was created on oTree version 2.0.29.  
You can test the application [here](https://otree-questionnaire.herokuapp.com) by choosing "Questionnaire".

## Adding a page
Below are basic instructions to include another page (i.e., Survey3.html).

### templates/questionnaire/
Copy/paste "Survey2.html" and rename it to "Survey3.html" under /templates/questionnaire/.

### models.py
In models.py, add your questions and items to the Player class. Make sure to specify a label and choice information.

### pages.py
In pages.py, copy/paste the Survey2 class and rename this new class to Survey3.  
Also, add Survey3 to "initial_page_sequence":  
```python
initial_page_sequence = [
    Survey1,
    Survey2,
    Survey3,
]
```
