from tonb import TONBApiClient

client = TONBApiClient(
    "https://merchant-app-api2.tonb.io", "YOUR_API_KEY", "YOUR_MERCHANT_ID"
)

# Create invoice
invoice = client.create_invoice(1000000000, 12345)

# Print data about invoice
print(invoice)

# Cancel invoice
client.cancel_invoice(invoice)

# Get overall stats about invoices
print(client.get_invoices_stats())
