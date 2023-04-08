from typing import Optional, Any
import xmltodict


def parse_xml(xml_string: str) -> Optional[dict[str, Any]]:
    try:
        xml_dict = xmltodict.parse(xml_string)
    except Exception as e:
        print(f"Error parse xml - {e}")
        return
    if "root" in xml_dict:
        return xml_dict["root"]
    return xml_dict
