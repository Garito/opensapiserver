from typing import Union, Optional
from enum import Enum
from datetime import datetime

from pydantic import BaseModel, Field, PositiveFloat

class PrescriptionDetail(BaseModel):
  product: str = Field(json_schema_extra = {"primaryKey": True})
  amount: PositiveFloat

  class Config:
    schema_extra = {
      "ui": {
        "product": {
          "singular": "product",
          "plural": "products",
          # "fetch": "http://localhost:8000/products"
          "crypto": [
            { "chain": 80001, "contractAddress": "0xEdbd01E6746c03888aB271468122F20a2AB2cc32" },
            { "chain": 80001, "contractAddress": "0xAC894D824CF3293C51965Fe52C0d2DE33fF53848" },
            { "chain": 80001, "contractAddress": "0xD9Ca36A1Ed1CE974C4dC29450BAfd9237A6B2201" }
          ],
          "optionsArgs": {
            "load": {"name": "collectionName", "json": "null"},
            "value": {
              "fields": ["contractAddress", "tokenId"],
              "write": "{contractAddress}_{tokenId}",
              "read": "(?<contractAddress>[0-9a-zA-Z]{42})_(?<tokenId>[0-9]*)"
            },
            "name": {
              "fields": ["name", "collectionName"],
              "write": "{name} @ {collectionName}"
            }
          }
        }
      }
    }

class Prescription(BaseModel):
  id: str = Field(json_schema_extra = {"primaryKey": True})
  date: datetime
  wallet: str = Field(min_length = 42, max_length = 42, json_schema_extra = {"format": "wallet"}, placeholder = "Wallet's address", description = "You can use Metamask, the CoinBase or any other Walletconnect compatible wallet", alt_description = "This is the alternate description")
  details: list[PrescriptionDetail]
  note: Optional[str] = Field(max_length = 500, format = "html")

  class Config:
    schema_extra = {
      "ui": {
        # "css": "https://cs.lateralthink.club/assets/css/prescriptions.css",
        "css": "http://localhost:9000/assets/css/prescriptions.css",
        "groups": {
          "header": ["id", "date", "wallet"],
          "details": ["details"],
          "note": ["note"]
        }
      }
    }
