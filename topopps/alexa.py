from __future__ import absolute_import
from random import randint
from collections import OrderedDict
from rest_framework.serializers import CharField
from django_alexa.api import fields, intent, ResponseBuilder


HOUSES = ("gryffindor", "hufflepuff", "ravenclaw", "slytherin")
# Ordered
CURSES = OrderedDict()
CURSES["The Cruciatus Curse"] = "Crucio"
CURSES["The Imperius Curse"] =  "Imperio"
CURSES["The Killing Curse"] = "Avada Kedavra"


@intent(app="topopps")
def LaunchRequest(session):
    """
    ---
    launch
    """
    message = "Welcome to Hog warts school of witchcraft and wizardry!"
    reprompt = "What house would you like to give points to?"
    return ResponseBuilder.create_response(message=message,
                                           reprompt=reprompt,
                                           end_session=False,
                                           launched=True)


class PointsForHouseSlots(fields.AmazonSlots):
    points = fields.AmazonNumber()
    house = fields.AmazonCustom(label="HOUSE_LIST", choices=HOUSES)


@intent(app="topopps", slots=PointsForHouseSlots)
def PointsForHouse(session, points, house):
    """
    Direct response to add points to a house
    ---
    {house}
    {points}
    {points} {house}
    {points} points {house}
    add {points} points to {house}
    give {points} points to {house}
    """
    kwargs = {}
    kwargs['launched'] = launched = session.get('launched')
    kwargs['marauder'] = marauder = session.get('marauder')
    kwargs['points'] = points = points or session.get('points')
    kwargs['house'] = house = house or session.get('house')
    if points is None:
        kwargs['message'] = "How many points?".format(house)
        kwargs["end_session"] = False
        return ResponseBuilder.create_response(**kwargs)
    if house is None:
        kwargs['message'] = "Which house?".format(points)
        kwargs["end_session"] = False
        return ResponseBuilder.create_response(**kwargs)
    if marauder:
        kwargs['message'] = "messers can not give points to houses, we lose them in the name of mischief!"
        kwargs['message'] += " {0} points removed from house {1}.".format(randint(1,10), house or HOUSES[randint(0, 3)])
        kwargs['reprompt'] = "What mischief brings you here?"
        kwargs['end_session'] = False
    else:
        if launched:
            kwargs['reprompt'] = "What house would you like to give points to?"
            kwargs['end_session'] = False
        kwargs['message'] = "{0} points added to house {1}.".format(points, house)
        kwargs.pop("house")
        kwargs.pop("points")
    return ResponseBuilder.create_response(**kwargs)


@intent(app="topopps")
def UnforgivableCurses(session):
    """
    The 3 unforgivable curses
    ---
    What are the unforgivable curses
    """
    message = "Your top 3 opportunities are as follows."
    message += "1. United Oil Workers. Currently in Pending and marked as Commit, expected to close on 12/12/12."
    message += "2. United Oil Workers. Currently in Pending and marked as Commit, expected to close on 12/12/12."
    message += "3. United Oil Workers. Currently in Pending and marked as Commit, expected to close on 12/12/12."
    return ResponseBuilder.create_response(message=message)


@intent(app="topopps")
def MaraudersLaunchRequest(session):
    """
    ---
    i solemnly swear i am up to no good
    """
    message = "Messers Moony, Wormtail, Padfoot and Prongs are proud to present the Marauders Map!"
    reprompt = "What mischief brings you here?"
    return ResponseBuilder.create_response(message=message,
                                           reprompt=reprompt,
                                           end_session=False,
                                           marauder=True)


@intent(app="topopps")
def MaraudersSessionEndedRequest(session):
    """
    Default End Session Intent
    ---
    mischief managed
    """
    return ResponseBuilder.create_response()