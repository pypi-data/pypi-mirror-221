# Generated by ariadne-codegen on 2023-07-23 13:41
# Source: operations.graphql

from pydantic import Field

from .base_model import BaseModel
from .fragments import UsageHistoryFragment


class UsageHistory(BaseModel):
    usage_history: "UsageHistoryUsageHistory" = Field(alias="usageHistory")


class UsageHistoryUsageHistory(UsageHistoryFragment):
    pass


UsageHistory.update_forward_refs()
UsageHistoryUsageHistory.update_forward_refs()
