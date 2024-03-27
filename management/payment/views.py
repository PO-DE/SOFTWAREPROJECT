# import stripe
# from django.shortcuts import get_object_or_404, redirect
# from django.urls import reverse
# from django.views import View
#
#
# from management.package.models import Package
# from travel_management import settings
#
# stripe.api_key = settings.STRIPE_SECRET_KEY
#
# class CreateCheckoutSessionView(View):
#     def post(self, request, *args, **kwargs):
#         package_destination = self.kwargs['package_destination']
#         package = get_object_or_404(Package, destination=package_destination)
#         YOUR_DOMAIN = "http://127.0.0.1:8000"  # Change to your domain
#
#         # Create Stripe Checkout Session
#         checkout_session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             line_items=[{
#                 'price_data': {
#                     'currency': 'cad',
#                     'unit_amount': package.price,
#                     'product_data': {
#                         'name': package.destination,
#                     },
#                 },
#                 'quantity': 1,
#             }],
#             mode='payment',
#             success_url=YOUR_DOMAIN + reverse('success_view'),
#             cancel_url=YOUR_DOMAIN + reverse('cancel_view'),
#         )
#         return redirect(checkout_session.url)
