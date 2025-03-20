# from locust import HttpUser, task
#
# class LibraryCardUser(HttpUser):
#     @task(1)
#     def open_library_card_page(self):
#         """ Open the NYPL Library Card page """
#         self.client.get("/library-card/new")
#
#     @task(1)
#     def fill_personal_information(self):
#         """ Step 1 of 5: Fill in personal information """
#         response = self.client.post(
#             "/library-card/personal?newCard=true",
#             json={
#                 "first_name": "Joe",
#                 "last_name": "Doe",
#                 "date_of_birth": "05/15/2001",
#                 "email": "joedoe_nypl@gmail.com"
#             }
#         )
#         assert response.status_code == 200, f"Failed to submit personal information: {response.status_code}"
#
#     @task(1)
#     def fill_address_information(self):
#         """ Step 2 of 5: Fill in address information """
#         response = self.client.post(
#             "/library-card/location?&newCard=true",
#             json={
#                 "street_address": "123 East 45th Street",
#                 "apartment": "3F",
#                 "city": "New York",
#                 "state": "NY",
#                 "zip": "10017"
#             }
#         )
#         assert response.status_code == 200, f"Failed to submit address information: {response.status_code}"
#
#     @task(1)
#     def address_verification(self):
#         """ Step 3 of 5: Address Verification """
#         response = self.client.post(
#             "/library-card/address-verification?&newCard=true",
#             json={"verify": "true"}
#         )
#         assert response.status_code == 200, f"Failed to verify address: {response.status_code}"
#
#     @task(1)
#     def customize_account(self):
#         """ Step 4 of 5: Customize account details """
#         response = self.client.post(
#             "/library-card/account?&newCard=true",
#             json={
#                 "username": "QaLibUser12345678",
#                 "password": "securepassword",
#                 "verify_password": "securepassword",
#                 "home_library": "Stephen A. Schwarzman Building",
#                 "terms_checkbox": "true"
#             }
#         )
#         assert response.status_code == 200, f"Failed to customize account: {response.status_code}"
#
#     @task(1)
#     def confirm_information(self):
#         """ Step 5 of 5: Confirm the entered information """
#         response = self.client.post(
#             "/library-card/review?&newCard=true",
#             json={"confirm": "true"}
#         )
#         assert response.status_code == 200, f"Failed to confirm information: {response.status_code}"
#
#     @task(1)
#     def view_congrats_page(self):
#         """ View the Congrats page after successful submission """
#         response = self.client.get("/library-card/congrats?&newCard=true")
#         assert response.status_code == 200, f"Failed to access congrats page: {response.status_code}"
