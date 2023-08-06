from beehiiv.email_blasts import EmailBlasts
from beehiiv.posts import Posts
from beehiiv.publications import Publications
from beehiiv.referral_program import ReferralProgram
from beehiiv.segments import Segments
from beehiiv.subscriptions import Subscriptions

class BeeHiiv:

    def __init__(self, api_key, publicationId=None):
        '''init'''
        self.email_blasts = EmailBlasts(api_key, publicationId)
        self.posts = Posts(api_key, publicationId)
        self.publications = Publications(api_key)
        self.referral_program = ReferralProgram(api_key, publicationId)
        self.segments = Segments(api_key, publicationId)
        self.subscriptions = Subscriptions(api_key, publicationId)

