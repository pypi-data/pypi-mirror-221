# Generated by ariadne-codegen on 2023-07-23 13:41
# Source: operations.graphql

from pydantic import Field

from .base_model import BaseModel


class CancelSubscriptionUpdates(BaseModel):
    cancel_schedule: str = Field(alias="cancelSchedule")


CancelSubscriptionUpdates.update_forward_refs()
