from typing import Optional, Any
import xmltodict


def parse_xml(xml_string: str) -> Optional[dict[str, Any]]:
    try:
        return xmltodict.parse(xml_string)
    except Exception as e:
        print(f"Error parse xml - {e}")
