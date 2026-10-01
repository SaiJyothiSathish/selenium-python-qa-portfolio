# Sample Bug Report

> This is a portfolio example showing bug-report format. Do not report it as a real Sauce Demo defect unless you reproduce and confirm it.

| Field | Details |
|---|---|
| Bug ID | DEMO-001 |
| Title | Checkout accepts a postal code containing only spaces |
| Module | Checkout — Customer Information |
| Severity | Medium |
| Priority | High |
| Environment | Chrome on Windows 11 |
| Status | New |

## Preconditions

- User is logged in.
- At least one product is in the cart.
- User is on the Checkout: Your Information page.

## Steps to Reproduce

1. Enter a valid First Name.
2. Enter a valid Last Name.
3. Enter only spaces in the Postal Code field.
4. Select **Continue**.

## Expected Result

The application should reject blank or whitespace-only postal codes and display a validation message.

## Actual Result

Record the actual observed result after reproducing the issue.

## Attachments

Add a screenshot, video, browser version, date, and console errors when filing a real defect.