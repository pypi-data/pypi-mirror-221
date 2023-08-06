# beehiiv
Python wrapper for BeeHiiv API

#### Install
```
pip3 install beehiiv
```

### Example
```Python
import os
import beehiiv

PUBLICATION_ID = os.environ['BEEHIIV_PUBLICATION_ID']
API_KEY = os.environ['BEEHIIV_API_KEY']

bh = beehiiv.BeeHiiv(api_key=API_KEY, publicationId=PUBLICATION_ID)
subscriptions = bh.subscriptions.index(
  expand=["stats", "custom_fields"],
  limit=5
)
print(subscriptions)
```

## Classes and methods
```
BeeHiiv.email_blast.index - Retrieve all Email Blasts
BeeHiiv.email_blast.show - Retrieve an Email Blast

BeeHiiv.posts.index - Retrieve all posts belonging to a specific publication
BeeHiiv.posts.show - Retreive a single Post belonging to a specific publication
BeeHiiv.posts.destory - Delete or Archive a post.

BeeHiiv.publications.index - Retrieve all publications associated with your API key.
BeeHiiv.publications.show - Retrieve a single publication

BeeHiiv.referral_program.show - Retrieve details about the publication's referral program

BeeHiiv.segments.index - Retrieve information about all segments belonging to a specific publication
BeeHiiv.segments.show - Retrieve a single segment belonging to a specific publication
BeeHiiv.segments.delete - Delete a segment.
BeeHiiv.segments.expand_results - List the Subscriber Ids from the most recent calculation of a specific publication.

BeeHiiv.subscriptions.create - Create new subscriptions for a publication.  
BeeHiiv.subscriptions.index - Retrieve all subscriptions belonging to a specific publication
BeeHiiv.subscriptions.show - Retrieve a single subscription belonging to a specific publication
BeeHiiv.subscriptions.update - Update a subscriber 
BeeHiiv.subscriptions.delete - Delete a subscription.
```
