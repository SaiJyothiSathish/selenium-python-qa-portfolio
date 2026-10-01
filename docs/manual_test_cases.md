# Manual Test Cases — Sauce Demo

| Test Case ID | Test Scenario | Preconditions | Test Steps | Expected Result |
|---|---|---|---|---|
| MTC-001 | Valid login | User is on the login page | Enter `standard_user`, enter `secret_sauce`, select Login | Products page is displayed. |
| MTC-002 | Invalid login | User is on the login page | Enter invalid username and password, select Login | Error message is displayed. |
| MTC-003 | Add product to cart | User is logged in | Select **Add to cart** for Sauce Labs Backpack | Cart badge displays `1`. |
| MTC-004 | Complete checkout | User is logged in and one product is in the cart | Open cart, select Checkout, enter customer details, select Continue, select Finish | `Thank you for your order!` is displayed. |
| MTC-005 | Required checkout fields | User is on the customer-information page | Leave First Name empty and select Continue | Validation error says First Name is required. |