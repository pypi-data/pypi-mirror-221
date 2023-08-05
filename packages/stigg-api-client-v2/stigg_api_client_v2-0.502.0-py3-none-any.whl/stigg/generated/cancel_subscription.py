# Generated by ariadne-codegen on 2023-07-23 16:26
# Source: operations.graphql

from pydantic import Field

from .base_model import BaseModel
from .fragments import SlimSubscriptionFragment


class CancelSubscription(BaseModel):
    cancel_subscription: "CancelSubscriptionCancelSubscription" = Field(
        alias="cancelSubscription"
    )


class CancelSubscriptionCancelSubscription(SlimSubscriptionFragment):
    pass


CancelSubscription.update_forward_refs()
CancelSubscriptionCancelSubscription.update_forward_refs()
