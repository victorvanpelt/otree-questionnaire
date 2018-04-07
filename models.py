from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import itertools
import json

author = 'Victor van Pelt'

doc = """
Demo of o-Tree Questionnaire
"""


class Constants(BaseConstants):
    name_in_url = 'Questionnaire'
    players_per_group = None
    num_rounds = 1
    StandardChoices=[
        [1, 'Disagree strongly'],
        [2, 'Disagree moderately'],
        [3, 'Disagree a little'],
        [4, 'Neither agree nor disagree'],
        [5, 'Agree a little'],
        [6, 'Agree moderately'],
        [7, 'Agree strongly'],
    ]

    #Survey1
    Survey1Choices=StandardChoices

    #Survey2
    Survey2Choices=StandardChoices

class Subsession(BaseSubsession):
    pass
    #def randomize_page_order(self):
    #def creating_session(self):
    #    pages_names = ['Survey1', 'Survey2']
    #    random.shuffle(pages_names)
    def creating_session(self):
        from .pages import initial_page_sequence
        aaa = [i.__name__.split('_') for i in initial_page_sequence]
        page_blocks = [list(group) for key, group in itertools.groupby(aaa, key=lambda x: x[0])]
        for p in self.get_players():
            pb = page_blocks.copy()
            random.shuffle(pb)
            level1 = list(itertools.chain.from_iterable(pb))
            level2 = ['_'.join(i) for i in level1]
            p.participant.vars['page_sequence'] = json.dumps(level2)

class Group(BaseGroup):
    pass


class Player(BasePlayer):

    #Demographics
    gender = models.IntegerField(
        label="Please select your gender.",
        choices=[
            [1, 'Male'],
            [2, 'Female'],
            [3, 'Other'],
            [4, 'I prefer not to say.'],
        ]
    )

    age = models.IntegerField(label="Please enter your age.", min=14, max=90, blank=True)

    nationality = models.IntegerField(
        label="Please select what best describes your nationality.",
        choices=[
            [1, 'Dutch'],
            [2, 'Other European nationality than Dutch'],
            [3, 'Other nationality than a European nationality'],
            [4, 'I prefer not to say.'],
        ]
    )

    studies = models.IntegerField(
        label="Please estimate how many studies you have participated in since you started studying at this university (excluding this study)",
        choices=[
            [1, 'Less than 5 studies'],
            [2, 'Between 5 and less than 10 studies.'],
            [3, 'between 10 and less than 15 studies.'],
            [4, '15 or more studies.'],
            [5, 'I prefer not to say.']
        ]
    )

    workexperience = models.IntegerField(
        label="Please indicate your work experience. All jobs count, including part-time and volunteer work.",
        choices=[
            [1, 'I do not have work experience.'],
            [2, 'Less than 1 year work experience.'],
            [3, 'Between 1 and less than 2 years of work experience'],
            [4, 'Between 2 and less than 3 years work experience.'],
            [5, 'Between 3 and less than 4 years work experience.'],
            [6, 'Between 4 and less than 5 years work experience.'],
            [7, '5 years or more work experience.'],
            [8, 'I prefer not to say.'],
        ]
    )

    degree = models.IntegerField(
        label="Please indicate which degree you are currently pursuing. If you are currently pursuing more than one degree, please select the highest degree.",
        choices=[
            [1, 'Bachelor degree'],
            [2, 'Master degree'],
            [3, 'PhD degree'],
            [4, 'MBA degree'],
            [5, 'Other'],
            [6, 'I prefer not to say.']
        ]
    )

    english = models.IntegerField(
        label="Please rate your English on a percentage scale between 0 and 100.",
        min=0,
        max=100,
        blank=True,
        initial=None
    )

    #Survey1
    grit1 = models.IntegerField(
        label='I often set a goal but later choose to pursue a different one.',
        choices=Constants.Survey1Choices
    )
    grit2 = models.IntegerField(
        label='I have been obsessed with a certain idea or project for a short time but later lost interest.',
        choices=Constants.Survey1Choices
    )
    grit3 = models.IntegerField(
        label='I have difficulty maintaining my focus on projects that take more than a few months to complete.',
        choices=Constants.Survey1Choices
    )
    grit4 = models.IntegerField(
        label='New ideas and projects sometimes distract me from previous ones.',
        choices=Constants.Survey1Choices
    )
    grit5 = models.IntegerField(
        label='I finish whatever I begin.',
        choices=Constants.Survey1Choices
    )
    grit6 = models.IntegerField(
        label='Setbacks do not discourage me.',
        choices=Constants.Survey1Choices
    )
    grit7 = models.IntegerField(
        label='I am diligent (hardworking).',
        choices=Constants.Survey1Choices
    )
    grit8 = models.IntegerField(
        label='I am a hard worker.',
        choices=Constants.Survey1Choices
    )

    #Survey2
    big1 = models.IntegerField(
        label='I see myself as extraverted, enthusiastic.',
        choices=Constants.Survey2Choices
    )
    big2 = models.IntegerField(
        label='I see myself as critical, quarrelsome.',
        choices=Constants.Survey2Choices
    )
    big3 = models.IntegerField(
        label='I see myself as dependable, self-disciplined.',
        choices=Constants.Survey2Choices
    )
    big4 = models.IntegerField(
        label='I see myself as anxious, easily upset.',
        choices=Constants.Survey2Choices
    )
    big5 = models.IntegerField(
        label='I see myself as open to new experiences, complex.',
        choices=Constants.Survey2Choices
    )
    big6 = models.IntegerField(
        label='I see myself as reserved, quiet.',
        choices=Constants.Survey2Choices
    )
    big7 = models.IntegerField(
        label='I see myself as sympathetic, warm.',
        choices=Constants.Survey2Choices
    )
    big8 = models.IntegerField(
        label='I see myself as disorganized, careless.',
        choices=Constants.Survey2Choices
    )
    big9 = models.IntegerField(
        label='I see myself as calm, emotionally stable.',
        choices=Constants.Survey2Choices
    )
    big10 = models.IntegerField(
        label='I see myself as conventional, uncreative.',
        choices=Constants.Survey2Choices
    )