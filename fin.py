import praw
import os
from dotenv import load_dotenv
load_dotenv()

def get_reddit_ai_news(subreddit: str, limit: int = 5) -> dict[str, list[str]]:
    """
    Fetches top post titles from a specified subreddit using the Reddit API.

    Args:
        subreddit: The name of the subreddit to fetch news from (e.g., 'AINewsAndTrends').
        limit: The maximum number of top posts to fetch.

    Returns:
        A dictionary with the subreddit name as key and a list of
        post titles as value. Returns an error message if credentials are
        missing, the subreddit is invalid, or an API error occurs.
    """

    print(f"--- Tool called: Fetching from r/{subreddit} via Reddit API ---")
    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    user_agent = os.getenv("REDDIT_USER_AGENT")
    # Check if all required credentials are present
    print("client_id: ",client_id)
    print("client_secret: ",client_secret)
    print("user_agent: ",user_agent)

    if not all([client_id, client_secret, user_agent]):
        print("--- Tool error: Reddit API credentials missing in .env file. ---")
        return {subreddit: ["Error: Reddit API credentials not configured."]}

    try:
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )

        # Check if the subreddit exists
        reddit.subreddits.search_by_name(subreddit, exact=True)
        sub = reddit.subreddit(subreddit)
        top_posts = list(sub.hot(limit=limit)) # Fetch hot posts
        titles = [post.title for post in top_posts]
        if not titles:
             return {subreddit: [f"No recent hot posts found in r/{subreddit}."]}
        
        return {subreddit: titles}
    
    except praw.exceptions.PRAWException as e:
        print(f"--- Tool error: {e} ---")
        return {subreddit: [f"Error fetching from r/{subreddit}: {str(e)}"]}
    
    except Exception as e:
        print(f"--- Tool error: {e} ---")
        return {subreddit: [f"An unexpected error occurred: {str(e)}"]}
    

print(get_reddit_ai_news("AINewsAndTrends", 5))














































# from datetime import datetime


# class Invoice:
#     """Represents an invoice for a collection of services rendered to a recipient"""

#     def __init__(self,
#                  sender_name,
#                  recipient_name,
#                  sender_address,
#                  recipient_address,
#                  sender_email,
#                  recipient_email):
#         # externally determined variables
#         self.sender_name = sender_name
#         self.recipient_name = recipient_name
#         self.sender_address = sender_address
#         self.recipient_address = recipient_address
#         self.sender_email = sender_email
#         self.recipient_email = recipient_email

#         # internally determined variables
#         self.date = datetime.now()
#         self.cost = 0
#         self.items = []
#         self.comments: list[str] = []

#     def add_item(self, name, price, tax):
#         # python makes working with trivial data-objects quite easy
#         item = {
#             "name": name,
#             "price": price,
#             "tax": tax
#         }

#         # hold on to the unmodified item for later, we'll do tax/discount calculations on an as-needed basis
#         self.items.append(item)

#     def calculate_total(self, discount):
#         discounted_subtotal = 0
#         total_tax = 0

#         for item in self.items:
#             price = item["price"]
#             tax_rate = item["tax"]

#             discounted_price = price * (1 - discount / 100)
#             item_tax = discounted_price * tax_rate

#             discounted_subtotal += discounted_price
#             total_tax += item_tax

#         return discounted_subtotal + total_tax
    
#     def comment(self, comment: str):
#         """Add a comment to the invoice"""
#         return self.comments.append(comment)
    
#     def get_comments(self):
#         """Get a string representation of the comments"""
#         return "\n".join(self.comments)




# if __name__ == '__main__':
#     invoice = Invoice(
#         "Larry Jinkles",
#         "Tod Hooper",
#         "34 Windsor Ln.",
#         "14 Manslow road",
#         "lejank@billing.com",
#         "discreetclorinator@hotmail.com"
#     )

#     invoice.add_item("34 floor building", 3400, .1)
#     invoice.add_item("Equipment Rental", 1000, .1)
#     invoice.add_item("Fear Tax", 340, 0.0)
#     invoice_total = invoice.calculate_total(20)
#     print(invoice_total)
#     invoice.comment("Please pay in cash")
#     invoice.comment("No refunds")
#     print(invoice.get_comments())
    