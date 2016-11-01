from __future__ import absolute_import
from django_alexa.api import intent, ResponseBuilder

@intent(app="topopps")
def LaunchRequest(session):
    """
    ---
    launch
    """
    message = "Welcome to TopOPPS!"
    reprompt = "What can I help you with today?"
    return ResponseBuilder.create_response(message=message, reprompt=reprompt, end_session=False, launched=True)

@intent(app="topopps")
def DetailOpportunity(session, oppname):
    """
    Get details for the specified opp name
    ---
    details on {oppname}
    details for {oppname}
    more info for {oppname}
    more information for {oppname}
    """
    print "***DetailOpportunity session", dict(session), oppname
    #oppname = "Putin's poutine"
    kwargs = {}
    kwargs['launched'] = launched = session.get('launched')
    kwargs['oppname'] = oppname = oppname or session.get('oppname')
    if launched:
        kwargs['reprompt'] = "What opportunity would you like details for?"
        kwargs['end_session'] = False
    kwargs['message'] = str(oppname)+"'s next meeting is on December 12, 2012, and the next steps are call Jim and get the deal signed."
    kwargs.pop("oppname")
    return ResponseBuilder.create_response(**kwargs)

@intent(app="topopps")
def UpdateOpportunityCloseDate(session, closedate, oppname):
    """
    update close date for a specified opportunity
    ---
    update close date to {closedate} for {oppname}
    set close date to {closedate} for {oppname}
    for {oppname} update close date to {closedate}
    for {oppname} set close date to {closedate}
    """
    print "***DetailOpportunity", dict(session), closedate, oppname
    #closedate = "2016-11-02"
    #oppname = "this week"
    kwargs = {}
    kwargs['launched'] = launched = session.get('launched')
    kwargs['oppname'] = oppname = oppname or session.get('oppname')
    kwargs['closedate'] = oppname = oppname or session.get('closedate')
    if launched:
        kwargs['reprompt'] = "What opportunity would you like to update?"
        kwargs['end_session'] = False
    kwargs['message'] = str(oppname)+"'s close date has been updated to "+str(closedate)
    kwargs.pop("oppname")
    kwargs.pop("closedate")
    return ResponseBuilder.create_response(**kwargs)

@intent(app="topopps")
def BestOpportunities(session):
    """
    The 3 best opportunities
    ---
    What are my top opportunities
    """
    message = "Your top 3 opportunities are as follows."
    message += " 1. United Oil Workers. Currently in Pending and marked as Commit, expected to close on December 12, 2012."
    message += " 2. United Oil Workers. Currently in Pending and marked as Commit, expected to close on December 12, 2012."
    message += " 3. United Oil Workers. Currently in Pending and marked as Commit, expected to close on December 12, 2012."
    return ResponseBuilder.create_response(message=message)

