
from prism._utils.exceptions import PrismValueError
from ..._common.const import (
    AggregationType,
    ESGDataComponentType,
    PeriodType,
)
from .._req_builder._list import _list_dataitems_esg
from ..._prismcomponent.datacomponent import (
    _Social,
    _Governance,
    _Summary,
    _Environmental
)
from ..._utils.validate_utils import _validate_args


__all__ = [
    'social',
    'governance',
    'summary',
    'environmental',
    'social_dataitems',
    'environmental_dataitems',
    'governance_dataitems'
]


@_validate_args
def _esg_builder(
    datacomponentclass,
    **kwargs
):
    return datacomponentclass(**kwargs)


def social(dataitemid: int):
    """
    Social Data component

    Parameters
    ----------
        dataitemid : int
            | Unique identifier for the different data item. This identifies the type of the value.

    Returns
    -------
        prism._PrismComponent

    Examples
    --------


    """
    return _esg_builder(_Social, dataitemid=dataitemid)


def governance(dataitemid: int):
    """
    Governance Data component

    Parameters
    ----------
        dataitemid : int
            | Unique identifier for the different data item. This identifies the type of the value.

    Returns
    -------
        prism._PrismComponent

    Examples
    --------


    """
    return _esg_builder(_Governance, dataitemid=dataitemid)


def environmental(dataitemid: int):
    """
    Environmental Data component

    Parameters
    ----------
        dataitemid : int
            | Unique identifier for the different data item. This identifies the type of the value.

    Returns
    -------
        prism._PrismComponent

    Examples
    --------


    """
    return _esg_builder(_Environmental, dataitemid=dataitemid)


def social_dataitems(search: str = None, package: str = None):
    """
    Usable dataitems for social ESG datacomponent.

    Parameters
    ----------
        search : str, default None
            | Search word for dataitems name, the search is case-insensitive.

        package : str, default None
            | Search word for package name, the search is case-insensitive.

    Returns
    -------
        pandas.DataFrame
            Data items that belong to cash flow statement data component.

        Columns:
            - *dataitemid*
            - *dataitemname*
            - *datamodule*
            - *package*
            - *datadescription*

    Examples
    --------
        >>> soc_dataitems = prism.esg.social_dataitems()
        >>> print(soc_dataitems)
            dataitemid                                       dataitemname  datamodule                package  dataitemdescription
        0       700008                            Access to Water - Score       Score  S&P Global ESG Scores  Score of Access to Water\nWater is a pre-requi...
        1       700009                     Addressing Cost Burden - Score       Score  S&P Global ESG Scores  Score of Addressing Cost Burden\nDue to aging ...
        2       700010                   Asset Closure Management - Score       Score  S&P Global ESG Scores  Score of Asset Closure Management\nMining acti...
        3       700011                                  Bioethics - Score       Score  S&P Global ESG Scores  Score of Bioethics\nDetailed and transparent p...
        4       700012  Controversial Issues: Dilemmas in Lending & Fi...       Score  S&P Global ESG Scores  Score of Controversial Issues: Dilemmas in Len...
        ..         ...                                                ...         ...                    ...
        69      700155                        Health & Nutrition - Weight      Weight  S&P Global ESG Scores  Scoring Weight of Health & Nutrition\nPoor die...
        70      700156                        Privacy Protection - Weight      Weight  S&P Global ESG Scores  Scoring Weight of Privacy Protection\nNetworke...
        71      700157          Customer Relationship Management - Weight      Weight  S&P Global ESG Scores  Scoring Weight of Customer Relationship Manage...
        72      700158                       Marketing Practices - Weight      Weight  S&P Global ESG Scores  Scoring Weight of Marketing Practices\nAggress...
        73      700159  Sustainable Marketing & Brand Perception - Weight      Weight  S&P Global ESG Scores  Scoring Weight of Sustainable Marketing & Bran...
    """
    return _list_dataitems_esg(ESGDataComponentType.SOCIAL, search, package)


def environmental_dataitems(search: str = None, package: str = None):
    """
    Usable dataitems for environmental ESG datacomponent.

    Parameters
    ----------
        search : str, default None
            | Search word for dataitems name, the search is case-insensitive.

        package : str, default None
            | Search word for package name, the search is case-insensitive.

    Returns
    -------
        pandas.DataFrame
            Data items that belong to cash flow statement data component.

        Columns:
            - *dataitemid*
            - *dataitemname*
            - *datamodule*
            - *package*
            - *datadescription*


    Examples
    --------
        >>> env_dataitems = prism.esg.environmental_dataitems()
        >>> print(env_dataitems)
            dataitemid                              dataitemname  datamodule                package                                dataitemdescription
        0       700088                      Biodiversity - Score       Score  S&P Global ESG Scores  Score of Biodiversity\nExtractive industries a...
        1       700089                Building Materials - Score       Score  S&P Global ESG Scores  Score of Building Materials\nA substantial per...
        2       700090  Business Risks and Opportunities - Score       Score  S&P Global ESG Scores  Score of Business Risks and Opportunities\nFin...
        3       700091                  Climate Strategy - Score       Score  S&P Global ESG Scores  Score of Climate Strategy\nMost industries are...  _
        4       700092                     Co-Processing - Score       Score  S&P Global ESG Scores  Score of Co-Processing\nCo-processing involves...
        ..         ...                                       ...         ...                                                                       ...
        65      700233                       Energy Mix - Weight      Weight  S&P Global ESG Scores  Scoring Weight of Energy Mix\nOil & Gas produc...
        66      700234                 Fleet Management - Weight      Weight  S&P Global ESG Scores  Scoring Weight of Fleet Management\nThe airlin...
        67      700235         Sustainable Construction - Weight      Weight  S&P Global ESG Scores  Scoring Weight of Sustainable Construction\nTh...
        68      700236                 Circular Fashion - Weight      Weight  S&P Global ESG Scores  Scoring Weight of Circular Fashion\nThe fashio...
        69      700237         Decarbonization Strategy - Weight      Weight  S&P Global ESG Scores  Scoring Weight of Decarbonization Strategy\nAs...
    """
    return _list_dataitems_esg(ESGDataComponentType.ENVIRONMENTAL, search, package)


def governance_dataitems(search: str = None, package: str = None):
    """
    Usable dataitems for environmental ESG datacomponent.

    Parameters
    ----------
        search : str, default None
            | Search word for dataitems name, the search is case-insensitive.

        package : str, default None
            | Search word for package name, the search is case-insensitive.

    Returns
    -------
        pandas.DataFrame
            Data items that belong to cash flow statement data component.

        Columns:
            - *dataitemid*
            - *dataitemname*
            - *datamodule*
            - *package*
            - *datadescription*


    Examples
    --------
        >>> env_dataitems = prism.esg.environmental_dataitems()
        >>> print(env_dataitems)
            dataitemid                                 dataitemname datamodule  package   dataitemdescription
        0       700045         Anti-crime Policy & Measures - Score      Score  S&P Global ESG Scores  Score of Anti-crime Policy & Measures\nCrimina...
        1       700046                     Antitrust Policy - Score      Score  S&P Global ESG Scores  Score of Antitrust Policy\nAs global competiti...
        2       700047                     Brand Management - Score      Score  S&P Global ESG Scores  Score of Brand Management\nA brand is a living...
        3       700048  Financial Stability & Systemic Risk - Score      Score  S&P Global ESG Scores  Score of Financial Stability & Systemic Risk\n...
        4       700049                      Business Ethics - Score      Score  S&P Global ESG Scores  Score of Business Ethics\nThe criterion evalua...
        ..         ...                                          ...        ...                                                                       ...
        81      700198             Supply Chain Management - Weight     Weight  S&P Global ESG Scores  Scoring Weight of Supply Chain Management\nIn ...
        82      700199            Sustainable Construction - Weight     Weight  S&P Global ESG Scores  Scoring Weight of Sustainable Construction\nTh...
        83      700200                 Sustainable Finance - Weight     Weight  S&P Global ESG Scores  Scoring Weight of Sustainable Finance\nFinanci...
        84      700201                        Tax Strategy - Weight     Weight  S&P Global ESG Scores  Scoring Weight of Tax Strategy\nTax competitio...
        85      700202                    Water Operations - Weight     Weight  S&P Global ESG Scores  Scoring Weight of Water Operations\nWater Oper...
    """
    return _list_dataitems_esg(ESGDataComponentType.GOVERNANCE, search, package)


def summary():
    """
    Summary Data component

    Parameters
    ----------
        dataitemid : int
            | Unique identifier for the different data item. This identifies the type of the value.

    Returns
    -------
        prism._PrismComponent

    Examples
    --------


    """
    return _esg_builder(_Summary, dataitemid=None)

