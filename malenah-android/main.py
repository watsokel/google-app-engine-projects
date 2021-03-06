import webapp2
import ProviderHandler as P
import ReviewHandler as R
import ReplyHandler as r
import SpecializationHandler as S
import UserHandler as U

config = {
    'M-S': 'malenah-specializations',
    'M-P': 'malenah-providers',
    'M-U': 'malenah-users'
    }

routes = [
    webapp2.Route(r'/<:specialization>/<sid:[0-9]+><:/?>', handler=S.SpecializationHandler, name='specialization'),
    webapp2.Route(r'/<:specialization><:/?>', handler=S.SpecializationHandler, name='specialization-list'),
    webapp2.Route(r'/<:provider>/<pid:[0-9]+>/<:review>/<revid:[0-9]+>/<:reply>/<repid:[0-9]+><:/?>', handler=r.ReplyHandler, name='provider-review-reply'),
    webapp2.Route(r'/<:provider>/<pid:[0-9]+>/<:review>/<revid:[0-9]+>/<:reply><:/?>', handler=r.ReplyHandler, name='provider-review-reply'),
    webapp2.Route(r'/<:provider>/<pid:[0-9]+>/<:review>/<revid:[0-9]+><:/?>', handler=R.ReviewHandler, name='provider-review'),
    webapp2.Route(r'/<:provider>/<pid:[0-9]+>/<:review><:/?>', handler=R.ReviewHandler, name='provider-review-list'),
    webapp2.Route(r'/<:provider>/<pid:[0-9]+><:/?>', handler=P.ProviderHandler, name='provider'),
    webapp2.Route(r'/<:provider><:/?>', handler=P.ProviderHandler, name='provider-list'),
    webapp2.Route(r'/<:review>/<revid:[0-9]+>/<:reply>/<repid:[0-9]+><:/?>', handler=r.ReplyHandler, name='reply'),
    webapp2.Route(r'/<:review>/<revid:[0-9]+>/<:reply><:/?>', handler=r.ReplyHandler, name='reply-list'),
    webapp2.Route(r'/<:review>/<revid:[0-9]+><:/?>', handler=R.ReviewHandler, name='review'),
    webapp2.Route(r'/<:review><:/?>', handler=R.ReviewHandler, name='review-list'),
    webapp2.Route(r'/<:reply>/<repid:[0-9]+><:/?>', handler=r.ReplyHandler, name='reply'),
    webapp2.Route(r'/<:reply><:/?>', handler=r.ReplyHandler, name='reply-list'),
    webapp2.Route(r'/<:user>/<uid:[0-9]+><:/?>', handler=U.UserHandler, name='user'),
    webapp2.Route(r'/<:user><:/?>', handler=U.UserHandler, name='user-list'),
    webapp2.Route(r'/', handler=P.ProviderHandler, name='provider-list'),
]

application = webapp2.WSGIApplication(routes, debug=True, config=config)
