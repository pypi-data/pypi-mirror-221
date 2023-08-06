""" Custom behavior for Indicator

"""
from eea.dexterity.indicators.interfaces import IIndicatorMetadata
from plone.dexterity.interfaces import IDexterityContent
from zope.component import adapter
from zope.interface import implementer


def getAllBlocks(blocks, flat_blocks):
    """Get a flat list from a tree of blocks"""
    for block in blocks.values():
        sub_blocks = block.get(
            "data", {}).get(
            "blocks", {}) or block.get(
            "blocks", {})
        flat_blocks.append(block)
        if sub_blocks:
            getAllBlocks(sub_blocks, flat_blocks)
    return flat_blocks


def find_url(value, key):
    """
    Get a deeply nested url from slate data tree
     >>> from eea.dexterity.indicators.behaviors.indicator import find_url
     >>> value={'children':[{'text' : '', 'url': 'https://www.eea.europa.eu'}]
     ... ,'type': 'p'}
     >>> find_url(value ,'url')
     'https://www.eea.europa.eu'

    """
    stack = [value]
    while stack:
        item = stack.pop()
        if key in item:
            return item[key]
        for v in item.get('children', []):
            if isinstance(v, dict):
                stack.append(v)  # append only nested object to find url
    return None


def remove_api_string(url):
    """
    Remove /api/SITE/ or ++api++ substring from url

    Args:
        url (str): url string
    """
    url = url.replace('/api/SITE/', '/')
    # future use
    # url = url.replace('/++api++/', '/')
    return url


def dedupe_data(data):
    """
    Remove duplication from metadata fields

    >>> from eea.dexterity.indicators.behaviors.indicator import dedupe_data
    >>> value=[{'children':[{'text' : '', 'url': 'https://www.eea.europa.eu'}]
    ... ,'type': 'p'},
    ... {'children':[{'text' : '', 'url': 'https://www.eea.europa.eu'}]
    ... ,'type': 'p'}]
    >>> result = dedupe_data(value)
    >>> len([x for x in result])
    1

    """
    existing = set()
    for value in data:
        url = find_url(value, 'url')
        url = remove_api_string(url)
        if url in existing:
            continue
        existing.add(url)
        yield value


@implementer(IIndicatorMetadata)
@adapter(IDexterityContent)
class Indicator(object):
    """Automatically extract metadata from blocks"""

    def __init__(self, context):
        self.__dict__['context'] = context
        self.__dict__['readOnly'] = [
            'temporal_coverage',
            'geo_coverage',
            'data_provenance',
            'institutional_mandate',
        ]

    def __getattr__(self, name):         # pylint: disable=R1710
        if name not in IIndicatorMetadata:
            raise AttributeError(name)

        if name not in self.__dict__['readOnly']:
            return getattr(
                self.__dict__.get('context'),
                name,
                IIndicatorMetadata[name].missing_value
            )

    def __setattr__(self, name, value):
        if name not in IIndicatorMetadata:
            raise AttributeError(name)

        if name not in self.__dict__['readOnly']:
            setattr(self.context, name, value)

    @property
    def temporal_coverage(self):
        """Get temporal coverage from Data figure blocks"""
        res = {"readOnly": True, "temporal": []}
        temporal = []
        blocks = getattr(self.context, "blocks", None) or {}
        for block in getAllBlocks(blocks, []):
            block_temporal = block.get("temporal", [])
            if not block_temporal:
                continue
            for item in block_temporal:
                if item not in temporal:
                    temporal.append(item)

        res["temporal"] = sorted(temporal, key=lambda x: x.get("label"))
        return res

    @property
    def geo_coverage(self):
        """Get geo coverage from Data figure blocks"""
        res = {"readOnly": True, "geolocation": []}
        geolocation = []
        blocks = getattr(self.context, "blocks", None) or {}
        for block in getAllBlocks(blocks, []):
            block_geolocation = block.get("geolocation", [])
            if not block_geolocation:
                continue
            for item in block_geolocation:
                geo_item = {
                    "label": item.get("label", ""),
                    "value": item.get("value", ""),
                }
                if geo_item not in geolocation:
                    geolocation.append(geo_item)

        res["geolocation"] = sorted(geolocation, key=lambda x: x.get("label"))
        return res

    @property
    def data_provenance(self):
        """Data sources and providers"""
        res = []
        blocks = getattr(self.context, "blocks", None) or {}
        for block in getAllBlocks(blocks, []):
            if block.get("@type", "") != "dataFigure":
                continue

            dataSources = (
                block.get(
                    "metadata", {}).get(
                    "dataSources", {}).get(
                    "value", []) or []
            )
            res.extend(dataSources)
        return [x for x in dedupe_data(res)]

    @property
    def institutional_mandate(self):
        """Institutional mandate"""
        res = []
        blocks = getattr(self.context, "blocks", None) or {}
        for block in getAllBlocks(blocks, []):
            if block.get("@type", "") != "dataFigure":
                continue

            institutionalMandate = (
                block.get(
                    "metadata", {}).get(
                    "institutionalMandate", {}).get(
                    "value", []) or []
            )
            res.extend(institutionalMandate)
        return [x for x in dedupe_data(res)]
