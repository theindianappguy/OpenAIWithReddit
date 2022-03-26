from ResponseGiver import response
import praw
import creds

reddit = praw.Reddit(client_id=creds.CLIENT_ID, client_secret=creds.CLIENT_SECRET,
                     username=creds.USERNAME, password=creds.PASSWORD, user_agent="realhardik18isgod")
c = 0
for comment in reddit.submission(id='tojzt0').comments:
    print(
        f'comment:- {comment.body}||by:- {comment.author} at:-{comment.created_utc}||comment_id:-{comment.id}')
    c += 1
print(f'total comments-{c}')
#print(response('what are you doingg'))
