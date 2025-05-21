from datetime import datetime


class Invoice:
    """Represents an invoice for a collection of services rendered to a recipient"""

    def __init__(self,
                 sender_name,
                 recipient_name,
                 sender_address,
                 recipient_address,
                 sender_email,
                 recipient_email):
        # externally determined variables
        self.sender_name = sender_name
        self.recipient_name = recipient_name
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.sender_email = sender_email
        self.recipient_email = recipient_email

        # internally determined variables
        self.date = datetime.now()
        self.cost = 0
        self.items = []
        self.comments: list[str] = []

    def add_item(self, name, price, tax):
        # python makes working with trivial data-objects quite easy
        item = {
            "name": name,
            "price": price,
            "tax": tax
        }

        # hold on to the unmodified item for later, we'll do tax/discount calculations on an as-needed basis
        self.items.append(item)

    def calculate_total(self, discount):
        discounted_subtotal = 0
        total_tax = 0

        for item in self.items:
            price = item["price"]
            tax_rate = item["tax"]

            discounted_price = price * (1 - discount / 100)
            item_tax = discounted_price * tax_rate

            discounted_subtotal += discounted_price
            total_tax += item_tax

        return discounted_subtotal + total_tax
    
    def comment(self, comment: str):
        """Add a comment to the invoice"""
        return self.comments.append(comment)
    
    def get_comments(self):
        """Get a string representation of the comments"""
        return "\n".join(self.comments)




if __name__ == '__main__':
    invoice = Invoice(
        "Larry Jinkles",
        "Tod Hooper",
        "34 Windsor Ln.",
        "14 Manslow road",
        "lejank@billing.com",
        "discreetclorinator@hotmail.com"
    )

    invoice.add_item("34 floor building", 3400, .1)
    invoice.add_item("Equipment Rental", 1000, .1)
    invoice.add_item("Fear Tax", 340, 0.0)
    invoice_total = invoice.calculate_total(20)
    print(invoice_total)
    invoice.comment("Please pay in cash")
    invoice.comment("No refunds")
    print(invoice.get_comments())
    