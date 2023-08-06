"""
This module defines a Python client library for the TONB Merchant backend API.

The client library includes a class which has methods for interacting with each API endpoint.
"""

from typing import Dict, Union, Optional
from dataclasses import dataclass
from datetime import datetime
import hmac
import hashlib
import requests
from flask import Request


@dataclass
class Invoice:
    """
    Data class that defines the Invoice object.

    Attributes:
        id: Invoice's ID.
        status: Status of the invoice.
        code: The code of the invoice.
        amount: Amount to be paid.
        domain: The domain related to the invoice.
        order_id: The id of the order.
        transaction: The transaction associated with the invoice.
        created_at: The time at which the invoice was created.
        updated_at: The time at which the invoice was last updated.
        user_from_id: The user ID from which the invoice is generated.
        user_to_id: The user ID to which the invoice is issued.
        wallet_from_id: The wallet ID from which the invoice is generated.
        wallet_to_id: The wallet ID to which the invoice is issued.
        user_from: The user from which the invoice is generated.
        wallet_from: The wallet from which the invoice is generated.
    """

    id: int
    status: str
    code: str
    amount: str
    domain: str
    order_id: int
    transaction: Optional[str]
    created_at: datetime
    updated_at: datetime
    user_from_id: Optional[str]
    user_to_id: str
    wallet_from_id: Optional[int]
    wallet_to_id: int
    user_from: Optional[str]
    wallet_from: Optional[str]

    @staticmethod
    def from_dict(source: dict) -> "Invoice":
        """
        Create an Invoice instance from a dictionary.

        Args:
            source (dict): The dictionary with invoice information.

        Returns:
            Invoice: The created Invoice instance.
        """

        source["created_at"] = datetime.fromisoformat(
            source.pop("createdAt").replace("Z", "+00:00")
        )
        source["updated_at"] = datetime.fromisoformat(
            source.pop("updatedAt").replace("Z", "+00:00")
        )
        return Invoice(**source)


@dataclass
class Webhook:
    """
    Data class that defines the Webhook object.

    Attributes:
        order_id: The order ID related to the webhook.
        amount: Amount related to the webhook.
        code: The code related to the webhook.
        status: The status related to the webhook.
    """

    order_id: int
    amount: int
    code: str
    status: str

    @staticmethod
    def from_dict(source: dict) -> "Webhook":
        """
        Create a WebhookData instance from a dictionary.

        Args:
            source (dict): The dictionary with webhook data information.

        Returns:
            WebhookData: The created WebhookData instance.
        """
        return Webhook(**source)


class TONBApiClient:
    """
    TONB API client to interact with the TONB Merchant backend API.

    Attributes:
        base_url: Base URL for the API.
        timeout: Timeout for the request.
    """

    def __init__(
        self, base_url: str, auth_token: str, merchant_id: str, timeout: int = 10
    ):
        self._auth_token = auth_token
        self.base_url: str = f"{base_url}/m/{merchant_id}"
        self._headers: Dict[str, str] = {
            "Authorization": auth_token,
        }
        self.timeout: int = timeout

    def create_invoice(self, amount: int, order_id: int) -> Invoice:
        """
        Creates a new invoice.

        Args:
            amount (int): Amount of the invoice.
            order_id (int): The order ID for the invoice.

        Returns:
            Invoice: The created invoice.

        Raises:
            ValueError: If there is an error in creating the invoice.
        """

        url: str = self.base_url + "/invoice"
        body: Dict[str, int] = {"amount": amount, "order_id": order_id}
        response = requests.post(
            url, headers=self._headers, json=body, timeout=self.timeout
        ).json()
        if "data" in response and "id" in response["data"]:
            return self.get_invoice(response["data"]["id"])
        raise ValueError(response)

    def get_invoice(self, invoice: Union[Invoice, int]) -> Invoice:
        """
        Retrieves an existing invoice.

        Args:
            invoice (Union[Invoice, int]): The invoice or the invoice ID to retrieve.

        Returns:
            Invoice: The retrieved invoice.

        Raises:
            ValueError: If there is an error in retrieving the invoice.
        """

        invoice_id: int = invoice.id if isinstance(invoice, Invoice) else invoice
        url: str = self.base_url + "/invoice/info"
        params: Dict[str, int] = {"id": invoice_id}
        response = requests.get(
            url, headers=self._headers, params=params, timeout=self.timeout
        ).json()
        if "data" in response:
            return Invoice.from_dict(response["data"])
        raise ValueError(response)

    def get_invoices_stats(self) -> Dict:
        """
        Retrieves statistics about invoices.

        Returns:
            Dict: A dictionary containing invoice statistics.

        Raises:
            ValueError: If there is an error in retrieving the statistics.
        """

        url: str = self.base_url + "/invoice/stats"
        response = requests.get(url, headers=self._headers, timeout=self.timeout).json()
        if "data" in response:
            return response["data"]
        raise ValueError(response)

    def cancel_invoice(self, invoice: Union[Invoice, int]) -> Dict:
        """
        Cancels an existing invoice.

        Args:
            invoice (Union[Invoice, int]): The invoice or the invoice ID to cancel.

        Returns:
            Dict: A dictionary containing the result of the cancellation.

        Raises:
            ValueError: If there is an error in cancelling the invoice.
        """

        invoice_id: int = invoice.id if isinstance(invoice, Invoice) else invoice
        url: str = self.base_url + "/invoice/cancel"
        body: Dict[str, int] = {"invoiceId": invoice_id}
        response = requests.patch(
            url, headers=self._headers, json=body, timeout=self.timeout
        ).json()
        if "data" not in response or response["data"]["status"] != "canceled":
            raise ValueError(response)

    def handle_request(self, request: Request) -> Dict:
        """
        Handles a request.

        Args:
            request (Request): The request to handle.

        Returns:
            Dict: A dictionary containing the result of the handling.

        Raises:
            ValueError: If the webhook data is invalid.
        """

        data = request.get_json()["data"]
        sign = data.pop("sign", None)

        if not self._validate_data(data, sign):
            raise ValueError("Invalid webhook data.")

        return Webhook.from_dict(data)

    def _validate_data(self, data: Dict, sign: str) -> bool:
        response = ";".join(str(value) for key, value in sorted(data.items()))
        hmac_obj = hmac.new(
            self._auth_token.encode(), response.encode(), hashlib.sha256
        )
        computed_sign = hmac_obj.hexdigest()

        return computed_sign == sign
