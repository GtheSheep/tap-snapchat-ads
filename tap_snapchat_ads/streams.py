"""Stream type classes for tap-snapchat-ads."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_snapchat_ads.client import SnapchatAdsStream


class OrganizationsStream(SnapchatAdsStream):
    name = "organizations"
    path = "/me/organizations"
    records_jsonpath = "$.organizations[*].organization"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("created_at", th.DateTimeType),
        th.Property("name", th.StringType),
        th.Property("country", th.StringType),
        th.Property("postal_code", th.StringType),
        th.Property("locality", th.StringType),
        th.Property("contact_name", th.StringType),
        th.Property("contact_email", th.StringType),
        th.Property("contact_phone", th.StringType),
        th.Property("address_line_1", th.StringType),
        th.Property("administrative_district_level_1", th.StringType),
        th.Property("accepted_term_version", th.StringType),
        th.Property("contact_phone_optin", th.BooleanType),
        th.Property("configuration_settings", th.ObjectType(
            th.Property("notifications_enabled", th.BooleanType)
        )),
        th.Property("type", th.StringType),
        th.Property("state", th.StringType),
        th.Property("roles", th.ArrayType(th.StringType)),
        th.Property("my_display_name", th.StringType),
        th.Property("my_invited_email", th.StringType),
        th.Property("my_member_id", th.StringType),
    ).to_dict()

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        return {
            'organization_id': record["id"]
        }


class AdAccountsStream(SnapchatAdsStream):
    name = "ad_accounts"
    path = "/organizations/{organization_id}/adaccounts"
    parent_stream_type = OrganizationsStream
    ignore_parent_replication_key = True
    records_jsonpath = "$.adaccounts[*].adaccount"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("created_at", th.DateTimeType),
        th.Property("name", th.StringType),
        th.Property("type", th.StringType),
        th.Property("status", th.StringType),
        th.Property("organization_id", th.StringType),
        th.Property("funding_source_ids", th.ArrayType(th.StringType)),
        th.Property("currency", th.StringType),
        th.Property("lifetime_spend_cap_micro", th.IntegerType),
        th.Property("timezone", th.StringType),
        th.Property("advertiser", th.StringType),
        th.Property("advertiser_organization_id", th.StringType),
        th.Property("agency_representing_client", th.BooleanType),
        th.Property("client_based_in_country", th.StringType),
        th.Property("client_paying_invoices", th.BooleanType),
        th.Property("agency_client_metadata", th.ObjectType(
            th.Property("name", th.StringType),
            th.Property("email", th.StringType),
            th.Property("address_line_1", th.StringType),
            th.Property("city", th.StringType),
            th.Property("administrative_district_level_1", th.StringType),
            th.Property("country", th.StringType),
            th.Property("zipcode", th.StringType),
            th.Property("tax_id", th.StringType),
        )),
        th.Property("paying_advertiser_name", th.StringType),
        th.Property("billing_type", th.StringType),
        th.Property("regulations", th.ObjectType(
            th.Property("restricted_delivery_signals", th.BooleanType)
        )),
    ).to_dict()

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        return {
            'ad_account_id': record["id"]
        }


class CampaignsStream(SnapchatAdsStream):
    name = "campaigns"
    path = "/adaccounts/{ad_account_id}/campaigns"
    parent_stream_type = AdAccountsStream
    ignore_parent_replication_key = True
    records_jsonpath = "$.campaigns[*].campaigns"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("created_at", th.DateTimeType),
        th.Property("name", th.StringType),
        th.Property("ad_account_id", th.StringType),
        th.Property("daily_budget_micro", th.IntegerType),
        th.Property("status", th.StringType),
        th.Property("objective", th.StringType),
        th.Property("start_time", th.DateTimeType),
        th.Property("end_time", th.DateTimeType),
        th.Property("lifetime_spend_cap_micro", th.IntegerType),
        th.Property("buy_model", th.StringType),
        th.Property("measurement_spec", th.ObjectType()),
        th.Property("regulations", th.ObjectType()),
    ).to_dict()

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        return {
            'ad_account_id': record["id"]
        }