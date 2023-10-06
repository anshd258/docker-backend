import razorpay

class RazorpayPayment:
    def __init__(self, key_id, key_secret):
        self.client = razorpay.Client(auth=(key_id, key_secret))

    def create_order(self, amount, currency):
        data = {
            'amount': amount,
            'currency': currency
        }
        return self.client.order.create(data=data)

    def verify_payment(self, payment_id, amount):
        payment = self.client.payment.fetch(payment_id)
        if payment['status'] == 'captured' and payment['amount'] == amount:
            return True
        return False