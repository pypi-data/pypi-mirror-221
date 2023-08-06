from datetime import datetime
import unittest.mock as mock
import pytest
import requests_mock
from tonb import TONBApiClient, Invoice, Webhook


@pytest.fixture
def api_client():
    return TONBApiClient(
        base_url="http://test.com",
        auth_token="12b79d58-35c7-49a4-8877-d59e47651f75",
        merchant_id="19",
    )


@pytest.fixture
def invoice():
    return Invoice(
        id=241,
        status="created",
        code="cd693f40427b4e486a9908b7eec5",
        amount="1231321",
        domain="https://74e1-5-161-206-160.ngrok-free.app",
        order_id="123",
        transaction=None,
        created_at=datetime.fromisoformat(
            "2023-07-25T08:13:19.996Z".replace("Z", "+00:00")
        ),
        updated_at=datetime.fromisoformat(
            "2023-07-25T08:13:19.996Z".replace("Z", "+00:00")
        ),
        user_from_id=None,
        user_to_id="1749027454",
        wallet_from_id=None,
        wallet_to_id=88,
        user_from=None,
        wallet_from=None,
    )


def test_create_invoice(api_client, invoice):
    with requests_mock.Mocker() as m:
        m.post("http://test.com/m/19/invoice", json={"data": {"id": 1}})
        m.get(
            "http://test.com/m/19/invoice/info",
            json={
                "data": {
                    "id": 241,
                    "status": "created",
                    "code": "cd693f40427b4e486a9908b7eec5",
                    "amount": "1231321",
                    "domain": "https://74e1-5-161-206-160.ngrok-free.app",
                    "order_id": "123",
                    "transaction": None,
                    "createdAt": "2023-07-25T08:13:19.996Z",
                    "updatedAt": "2023-07-25T08:13:19.996Z",
                    "user_from_id": None,
                    "user_to_id": "1749027454",
                    "wallet_from_id": None,
                    "wallet_to_id": 88,
                    "user_from": None,
                    "wallet_from": None,
                }
            },
        )

        result = api_client.create_invoice(amount=100, order_id=1)
        assert result == invoice


def test_get_invoice(api_client, invoice):
    with requests_mock.Mocker() as m:
        m.get(
            "http://test.com/m/19/invoice/info",
            json={
                "data": {
                    "id": 241,
                    "status": "created",
                    "code": "cd693f40427b4e486a9908b7eec5",
                    "amount": "1231321",
                    "domain": "https://74e1-5-161-206-160.ngrok-free.app",
                    "order_id": "123",
                    "transaction": None,
                    "createdAt": "2023-07-25T08:13:19.996Z",
                    "updatedAt": "2023-07-25T08:13:19.996Z",
                    "user_from_id": None,
                    "user_to_id": "1749027454",
                    "wallet_from_id": None,
                    "wallet_to_id": 88,
                    "user_from": None,
                    "wallet_from": None,
                }
            },
        )

        result = api_client.get_invoice(invoice=1)
        assert result == invoice


def test_get_invoices_stats(api_client):
    with requests_mock.Mocker() as m:
        m.get(
            "http://test.com/m/19/invoice/stats",
            json={"data": {"invoice_sum": "0", "count": 44}},
        )

        result = api_client.get_invoices_stats()
        assert result == {"count": 44, "invoice_sum": "0"}


def test_cancel_invoice(api_client):
    with requests_mock.Mocker() as m:
        m.patch(
            "http://test.com/m/19/invoice/cancel",
            json={
                "data": {
                    "id": 241,
                    "code": "cd693f40427b4e486a9908b7eec5",
                    "order_id": "123",
                    "status": "canceled",
                }
            },
        )

        api_client.cancel_invoice(invoice=1)


def test_handle_request(api_client):
    request_data = {
        "status": "canceled",
        "data": {
            "order_id": "12345",
            "amount": "1000000000",
            "code": "d484781287e359ae7f863fca6c76",
            "status": "canceled",
            "sign": "bbf31457703fa6e853f6dc8b62c734b85db8ebc9f481b7dd7c16ce157ef8e1b5",
        },
    }
    request = mock.Mock()
    request.get_json = mock.Mock(return_value=request_data)

    result = api_client.handle_request(request)
    assert isinstance(result, Webhook)


def test_get_invoice_not_found(api_client):
    with requests_mock.Mocker() as m:
        m.get(
            "http://test.com/m/19/invoice/info",
            status_code=404,
            json={"message": "Invoice not found"},
        )

        with pytest.raises(Exception) as excinfo:
            api_client.get_invoice(invoice=999)
        assert "Invoice not found" in str(excinfo.value)


def test_invalid_cancel_invoice(api_client):
    with requests_mock.Mocker() as m:
        m.patch(
            "http://test.com/m/19/invoice/cancel",
            status_code=400,
            json={
                "err": "the invoice 2555 cannot cancel",
                "slug": "invoice_cannot_canceled",
            },
        )

        with pytest.raises(Exception) as excinfo:
            api_client.cancel_invoice(invoice=999)
        assert "invoice_cannot_canceled" in str(excinfo.value)


def test_handle_request_invalid_signature(api_client):
    request_data = {
        "status": "canceled",
        "data": {
            "order_id": "12345",
            "amount": "1000000000",
            "code": "d484781287e359ae7f863fca6c76",
            "status": "canceled",
            "sign": "invalid_signature",
        },
    }
    request = mock.Mock()
    request.get_json = mock.Mock(return_value=request_data)

    with pytest.raises(Exception) as excinfo:
        api_client.handle_request(request)
    assert "Invalid webhook data" in str(excinfo.value)
