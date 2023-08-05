# Generated by ariadne-codegen on 2023-07-23 13:41
# Source: operations.graphql

from pydantic import Field

from .base_model import BaseModel
from .fragments import SlimSubscriptionFragment


class UpdateSubscription(BaseModel):
    update_subscription: "UpdateSubscriptionUpdateSubscription" = Field(
        alias="updateSubscription"
    )


class UpdateSubscriptionUpdateSubscription(SlimSubscriptionFragment):
    pass


UpdateSubscription.update_forward_refs()
UpdateSubscriptionUpdateSubscription.update_forward_refs()
