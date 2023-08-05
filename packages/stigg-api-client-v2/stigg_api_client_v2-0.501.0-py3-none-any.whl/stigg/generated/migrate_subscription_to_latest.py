# Generated by ariadne-codegen on 2023-07-23 13:41
# Source: operations.graphql

from pydantic import Field

from .base_model import BaseModel


class MigrateSubscriptionToLatest(BaseModel):
    migrate_subscription_to_latest: "MigrateSubscriptionToLatestMigrateSubscriptionToLatest" = Field(
        alias="migrateSubscriptionToLatest"
    )


class MigrateSubscriptionToLatestMigrateSubscriptionToLatest(BaseModel):
    subscription_id: str = Field(alias="subscriptionId")


MigrateSubscriptionToLatest.update_forward_refs()
MigrateSubscriptionToLatestMigrateSubscriptionToLatest.update_forward_refs()
