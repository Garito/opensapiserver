from typing import Union, Optional
from datetime import datetime

from pydantic import BaseModel, Field

class Fungible(BaseModel):
  img: str = Field(format = "image")
  name: str
  symbol: str
  amount: int

  class Config:
    schema_extra = {
      "id": "fungible",
      "ui": {
        "group": {
          "type": "group", "id": "fungible-container",
          "contents": [
            { "type": "field", "id": "img" },
            {
              "type": "group", "class": "fields",
              "contents": [
                {
                  "type": "group",
                  "contents": [
                    {
                      "type": "group", "id": "identity",
                      "contents": [
                        { "type": "field", "id": "name" },
                        { "type": "field", "id": "symbol" }
                      ]
                    },
                    { "type": "field", "id": "amount" }
                  ]
                },
                { "type": "buttons", "submitText": "Add token", "cancel": True }
              ]
            }
          ]
        },
        "adder": "Fungible",
        "cards": {
          "collectionToken": {
            "front": {
              "type": "group", "class": "lt-card fungible collection-token",
              "contents": [
                {
                  "type": "group", "tag": "figure",
                  "contents": [
                    { "type": "formValue", "field": "img" }
                  ]
                },
                {
                  "type": "group", "class": "contents",
                  "contents": [
                    {
                      "type": "group", "class": "title",
                      "contents": [
                        {
                          "type": "group", "tag": "h2",
                          "contents": [
                            { "type": "formValue", "field": "name" }
                          ]
                        }
                      ]
                    },
                    {
                      "type": "group", "class": "data",
                      "contents": [
                        {
                          "type": "group", "tag": "span", "class": "token-amount",
                          "contents": [
                            { "type": "formValue", "field": "amount" }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          }
        }
      }
    }

class StringProperty(BaseModel):
  name: str
  value: str

  class Config:
    schema_extra = {
      "id": "string",
      "ui": {
        "adder": "string",
        "submitText": "Add string",
        "cancel": True
      }
    }

class NumberProperty(BaseModel):
  name: str
  value: int
  max: int

  class Config:
    schema_extra = {
      "id": "number",
      "ui": {
        "adder": "number"
      }
    }

class RankProperty(BaseModel):
  name: str
  value: int
  max: int

  class Config:
    schema_extra = {
      "id": "rank",
      "ui": {
        "adder": "rank"
      }
    }

class BoostProperty(BaseModel):
  name: str
  value: int
  max: int

  class Config:
    schema_extra = {
      "id": "boost",
      "ui": {
        "adder": "boost"
      }
    }

class BoostPercentProperty(BaseModel):
  name: str
  value: int

  class Config:
    schema_extra = {
      "id": "boostPercent",
      "ui": {
        "adder": "boost %"
      }
    }

class DateProperty(BaseModel):
  name: str
  value: datetime

  class Config:
    schema_extra = {
      "id": "date",
      "ui": {
        "adder": "date"
      }
    }

class NonFungible(BaseModel):
  img: str = Field(title = "Token's image", format = "image")
  name: str
  amount: int
  description: Optional[str] = Field(max_length = 500, format = "html")
  properties: list[Union[StringProperty, NumberProperty, RankProperty, BoostProperty, BoostPercentProperty, DateProperty]] = Field(id = "properties", json_schema_extra = {"format": "table"})

  class Config:
    schema_extra = {
      "id": "non-fungible",
      "ui": {
        "group": {
          "type": "group", "id": "non-fungible-container",
          "contents": [
            {
              "type": "group", "class": "left",
              "contents": [
                { "type": "field", "id": "img" },
                {
                  "type": "group", "class": "main",
                  "contents": [
                    { "type": "field", "id": "name" },
                    { "type": "field", "id": "amount" },
                  ]
                }
              ]
            },
            {
              "type": "group", "class": "right",
              "contents": [
                { "type": "field", "id": "description" },
                { "type": "field", "id": "properties" },
                { "type": "buttons", "submitText": "Add token", "cancel": True }
              ]
            }
          ]
        },
        "adder": "Non fungible",
        "cards": {
          "collectionToken": {
            "front": {
              "type": "group", "class": "lt-card non-fungible collection-token",
              "contents": [
                {
                  "type": "group", "tag": "figure",
                  "contents": [
                    { "type": "formValue", "field": "img" }
                  ]
                },
                {
                  "type": "group", "class": "contents",
                  "contents": [
                    {
                      "type": "group", "class": "title",
                      "contents": [
                        {
                          "type": "group", "tag": "h2",
                          "contents": [
                            { "type": "formValue", "field": "name" }
                          ]
                        },
                        {
                          "type": "clicker",
                          "content": '<i class="fa-solid fa-circle-info"></i>', "message": "toggle",
                          "expression": "return value.description || value.properties.length"
                        }
                      ]
                    },
                    {
                      "type": "group", "class": "data",
                      "contents": [
                        {
                          "type": "group", "tag": "span", "class": "token-amount",
                          "contents": [
                            { "type": "formValue", "field": "amount" }
                          ]
                        }
                      ]
                    }
                  ]
                }
              ]
            },
            "back": {
              "type": "group", "class": "lt-card back non-fungible collection-token",
              "contents": [
                {
                  "type": "group", "class": "contents",
                  "contents": [
                    {
                      "type": "group", "class": "title",
                      "contents": [
                        {
                          "type": "group", "tag": "h2",
                          "contents": [
                            { "type": "formValue", "field": "name" }
                          ]
                        },
                        {
                          "type": "clicker",
                          "content": '<i class="fa-solid fa-circle-xmark"></i>', "message": "toggle"
                        }
                      ]
                    },
                    { "type": "formValue", "field": "description" },
                    { "type": "formValue", "field": "properties" }
                  ]
                }
              ]
            }
          }
        }
      }
    }

class Collection(BaseModel):
  name: str
  tokens: list[Union[Fungible, NonFungible]] = Field(json_schema_extra = {"format": "card", "mode": "collectionToken"})

  class Config:
    schema_extra = {
      "id": "collection",
      "ui": {
        "submitText": "Deploy collection"
      }
    }
