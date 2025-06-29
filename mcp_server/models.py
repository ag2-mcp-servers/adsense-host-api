# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T00:42:58+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field, RootModel


class Account(BaseModel):
    id: Optional[str] = Field(None, description='Unique identifier of this account.')
    kind: Optional[str] = Field(
        'adsensehost#account',
        description='Kind of resource this is, in this case adsensehost#account.',
    )
    name: Optional[str] = Field(None, description='Name of this account.')
    status: Optional[str] = Field(
        None,
        description='Approval status of this account. One of: PENDING, APPROVED, DISABLED.',
    )


class Accounts(BaseModel):
    etag: Optional[str] = Field(
        None, description='ETag of this response for caching purposes.'
    )
    items: Optional[List[Account]] = Field(
        None, description='The accounts returned in this list response.'
    )
    kind: Optional[str] = Field(
        'adsensehost#accounts',
        description='Kind of list this is, in this case adsensehost#accounts.',
    )


class AdClient(BaseModel):
    arcOptIn: Optional[bool] = Field(
        None, description='Whether this ad client is opted in to ARC.'
    )
    id: Optional[str] = Field(None, description='Unique identifier of this ad client.')
    kind: Optional[str] = Field(
        'adsensehost#adClient',
        description='Kind of resource this is, in this case adsensehost#adClient.',
    )
    productCode: Optional[str] = Field(
        None,
        description="This ad client's product code, which corresponds to the PRODUCT_CODE report dimension.",
    )
    supportsReporting: Optional[bool] = Field(
        None, description='Whether this ad client supports being reported on.'
    )


class AdClients(BaseModel):
    etag: Optional[str] = Field(
        None, description='ETag of this response for caching purposes.'
    )
    items: Optional[List[AdClient]] = Field(
        None, description='The ad clients returned in this list response.'
    )
    kind: Optional[str] = Field(
        'adsensehost#adClients',
        description='Kind of list this is, in this case adsensehost#adClients.',
    )
    nextPageToken: Optional[str] = Field(
        None,
        description='Continuation token used to page through ad clients. To retrieve the next page of results, set the next request\'s "pageToken" value to this.',
    )


class AdCode(BaseModel):
    adCode: Optional[str] = Field(None, description='The ad code snippet.')
    kind: Optional[str] = Field(
        'adsensehost#adCode',
        description='Kind this is, in this case adsensehost#adCode.',
    )


class Colors(BaseModel):
    background: Optional[str] = Field(
        None, description='The color of the ad background.'
    )
    border: Optional[str] = Field(None, description='The color of the ad border.')
    text: Optional[str] = Field(None, description='The color of the ad text.')
    title: Optional[str] = Field(None, description='The color of the ad title.')
    url: Optional[str] = Field(None, description='The color of the ad url.')


class Font(BaseModel):
    family: Optional[str] = Field(
        None,
        description='The family of the font. Possible values are: ACCOUNT_DEFAULT_FAMILY, ADSENSE_DEFAULT_FAMILY, ARIAL, TIMES and VERDANA.',
    )
    size: Optional[str] = Field(
        None,
        description='The size of the font. Possible values are: ACCOUNT_DEFAULT_SIZE, ADSENSE_DEFAULT_SIZE, SMALL, MEDIUM and LARGE.',
    )


class AdStyle(BaseModel):
    colors: Optional[Colors] = Field(
        None,
        description='The colors included in the style. These are represented as six hexadecimal characters, similar to HTML color codes, but without the leading hash.',
    )
    corners: Optional[str] = Field(
        None,
        description='The style of the corners in the ad (deprecated: never populated, ignored).',
    )
    font: Optional[Font] = Field(
        None, description='The font which is included in the style.'
    )
    kind: Optional[str] = Field(
        'adsensehost#adStyle',
        description='Kind this is, in this case adsensehost#adStyle.',
    )


class BackupOption(BaseModel):
    color: Optional[str] = Field(
        None,
        description='Color to use when type is set to COLOR. These are represented as six hexadecimal characters, similar to HTML color codes, but without the leading hash.',
    )
    type: Optional[str] = Field(
        None,
        description='Type of the backup option. Possible values are BLANK, COLOR and URL.',
    )
    url: Optional[str] = Field(None, description='URL to use when type is set to URL.')


class ContentAdsSettings(BaseModel):
    backupOption: Optional[BackupOption] = Field(
        None,
        description='The backup option to be used in instances where no ad is available.',
    )
    size: Optional[str] = Field(
        None,
        description='Size of this ad unit. Size values are in the form SIZE_{width}_{height}.',
    )
    type: Optional[str] = Field(
        None,
        description='Type of this ad unit. Possible values are TEXT, TEXT_IMAGE, IMAGE and LINK.',
    )


class MobileContentAdsSettings(BaseModel):
    markupLanguage: Optional[str] = Field(
        None, description='The markup language to use for this ad unit.'
    )
    scriptingLanguage: Optional[str] = Field(
        None, description='The scripting language to use for this ad unit.'
    )
    size: Optional[str] = Field(None, description='Size of this ad unit.')
    type: Optional[str] = Field(None, description='Type of this ad unit.')


class AdUnit(BaseModel):
    code: Optional[str] = Field(
        None,
        description='Identity code of this ad unit, not necessarily unique across ad clients.',
    )
    contentAdsSettings: Optional[ContentAdsSettings] = Field(
        None,
        description='Settings specific to content ads (AFC) and highend mobile content ads (AFMC - deprecated).',
    )
    customStyle: Optional[AdStyle] = Field(
        None, description='Custom style information specific to this ad unit.'
    )
    id: Optional[str] = Field(
        None,
        description='Unique identifier of this ad unit. This should be considered an opaque identifier; it is not safe to rely on it being in any particular format.',
    )
    kind: Optional[str] = Field(
        'adsensehost#adUnit',
        description='Kind of resource this is, in this case adsensehost#adUnit.',
    )
    mobileContentAdsSettings: Optional[MobileContentAdsSettings] = Field(
        None,
        description='Settings specific to WAP mobile content ads (AFMC - deprecated).',
    )
    name: Optional[str] = Field(None, description='Name of this ad unit.')
    status: Optional[str] = Field(
        None,
        description='Status of this ad unit. Possible values are:\nNEW: Indicates that the ad unit was created within the last seven days and does not yet have any activity associated with it.\n\nACTIVE: Indicates that there has been activity on this ad unit in the last seven days.\n\nINACTIVE: Indicates that there has been no activity on this ad unit in the last seven days.',
    )


class AdUnits(BaseModel):
    etag: Optional[str] = Field(
        None, description='ETag of this response for caching purposes.'
    )
    items: Optional[List[AdUnit]] = Field(
        None, description='The ad units returned in this list response.'
    )
    kind: Optional[str] = Field(
        'adsensehost#adUnits',
        description='Kind of list this is, in this case adsensehost#adUnits.',
    )
    nextPageToken: Optional[str] = Field(
        None,
        description='Continuation token used to page through ad units. To retrieve the next page of results, set the next request\'s "pageToken" value to this.',
    )


class AssociationSession(BaseModel):
    accountId: Optional[str] = Field(
        None,
        description='Hosted account id of the associated publisher after association. Present if status is ACCEPTED.',
    )
    id: Optional[str] = Field(
        None, description='Unique identifier of this association session.'
    )
    kind: Optional[str] = Field(
        'adsensehost#associationSession',
        description='Kind of resource this is, in this case adsensehost#associationSession.',
    )
    productCodes: Optional[List[str]] = Field(
        None,
        description='The products to associate with the user. Options: AFC, AFG, AFV, AFS (deprecated), AFMC (deprecated)',
    )
    redirectUrl: Optional[str] = Field(
        None,
        description='Redirect URL of this association session. Used to redirect users into the AdSense association flow.',
    )
    status: Optional[str] = Field(
        None,
        description='Status of the completed association, available once the association callback token has been verified. One of ACCEPTED, REJECTED, or ERROR.',
    )
    userLocale: Optional[str] = Field(
        None,
        description='The preferred locale of the user themselves when going through the AdSense association flow.',
    )
    websiteLocale: Optional[str] = Field(
        None, description="The locale of the user's hosted website."
    )
    websiteUrl: Optional[str] = Field(
        None, description="The URL of the user's hosted website."
    )


class CustomChannel(BaseModel):
    code: Optional[str] = Field(
        None,
        description='Code of this custom channel, not necessarily unique across ad clients.',
    )
    id: Optional[str] = Field(
        None,
        description='Unique identifier of this custom channel. This should be considered an opaque identifier; it is not safe to rely on it being in any particular format.',
    )
    kind: Optional[str] = Field(
        'adsensehost#customChannel',
        description='Kind of resource this is, in this case adsensehost#customChannel.',
    )
    name: Optional[str] = Field(None, description='Name of this custom channel.')


class CustomChannels(BaseModel):
    etag: Optional[str] = Field(
        None, description='ETag of this response for caching purposes.'
    )
    items: Optional[List[CustomChannel]] = Field(
        None, description='The custom channels returned in this list response.'
    )
    kind: Optional[str] = Field(
        'adsensehost#customChannels',
        description='Kind of list this is, in this case adsensehost#customChannels.',
    )
    nextPageToken: Optional[str] = Field(
        None,
        description='Continuation token used to page through custom channels. To retrieve the next page of results, set the next request\'s "pageToken" value to this.',
    )


class Header(BaseModel):
    currency: Optional[str] = Field(
        None,
        description='The currency of this column. Only present if the header type is METRIC_CURRENCY.',
    )
    name: Optional[str] = Field(None, description='The name of the header.')
    type: Optional[str] = Field(
        None,
        description='The type of the header; one of DIMENSION, METRIC_TALLY, METRIC_RATIO, or METRIC_CURRENCY.',
    )


class Report(BaseModel):
    averages: Optional[List[str]] = Field(
        None,
        description='The averages of the report. This is the same length as any other row in the report; cells corresponding to dimension columns are empty.',
    )
    headers: Optional[List[Header]] = Field(
        None,
        description='The header information of the columns requested in the report. This is a list of headers; one for each dimension in the request, followed by one for each metric in the request.',
    )
    kind: Optional[str] = Field(
        'adsensehost#report',
        description='Kind this is, in this case adsensehost#report.',
    )
    rows: Optional[List[List[str]]] = Field(
        None,
        description='The output rows of the report. Each row is a list of cells; one for each dimension in the request, followed by one for each metric in the request. The dimension cells contain strings, and the metric cells contain numbers.',
    )
    totalMatchedRows: Optional[str] = Field(
        None,
        description='The total number of rows matched by the report request. Fewer rows may be returned in the response due to being limited by the row count requested or the report row limit.',
    )
    totals: Optional[List[str]] = Field(
        None,
        description='The totals of the report. This is the same length as any other row in the report; cells corresponding to dimension columns are empty.',
    )
    warnings: Optional[List[str]] = Field(
        None, description='Any warnings associated with generation of the report.'
    )


class UrlChannel(BaseModel):
    id: Optional[str] = Field(
        None,
        description='Unique identifier of this URL channel. This should be considered an opaque identifier; it is not safe to rely on it being in any particular format.',
    )
    kind: Optional[str] = Field(
        'adsensehost#urlChannel',
        description='Kind of resource this is, in this case adsensehost#urlChannel.',
    )
    urlPattern: Optional[str] = Field(
        None,
        description='URL Pattern of this URL channel. Does not include "http://" or "https://". Example: www.example.com/home',
    )


class UrlChannels(BaseModel):
    etag: Optional[str] = Field(
        None, description='ETag of this response for caching purposes.'
    )
    items: Optional[List[UrlChannel]] = Field(
        None, description='The URL channels returned in this list response.'
    )
    kind: Optional[str] = Field(
        'adsensehost#urlChannels',
        description='Kind of list this is, in this case adsensehost#urlChannels.',
    )
    nextPageToken: Optional[str] = Field(
        None,
        description='Continuation token used to page through URL channels. To retrieve the next page of results, set the next request\'s "pageToken" value to this.',
    )


class Alt(Enum):
    csv = 'csv'
    json = 'json'


class FilterAdClientId(RootModel[List[str]]):
    root: List[str]


class HostCustomChannelId(RootModel[List[str]]):
    root: List[str]


class Dimension(RootModel[List[str]]):
    root: List[str]


class Filter(RootModel[List[str]]):
    root: List[str]


class Metric(RootModel[List[str]]):
    root: List[str]


class Sort(RootModel[List[str]]):
    root: List[str]


class ProductCodeEnum(Enum):
    AFC = 'AFC'
    AFG = 'AFG'
    AFMC = 'AFMC'
    AFS = 'AFS'
    AFV = 'AFV'


class ProductCode(RootModel[List[ProductCodeEnum]]):
    root: List[ProductCodeEnum]
