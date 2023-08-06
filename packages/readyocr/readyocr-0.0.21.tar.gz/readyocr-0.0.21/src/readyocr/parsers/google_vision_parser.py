from typing import Dict
from readyocr.entities import BoundingBox, Word, Line, Paragraph, Block, Table, Cell, MergedCell, Key, Value, Page, Document
from readyocr.entities.entity_list import EntityList


def _create_object(entity_json):
    """_summary_

    :param entity_json: entity information json format
    :type entity_json: json
    """
    # TODO: code to return Page Entity
    pass


def load(response: Dict) -> Document:
    """
    Convert GoogleVision OCR json to ReadyOCR document

    :param response: json response from Google Vision OCR
    :type response: Dict
    :return: ReadyOCR document
    :rtype: Document
    """
    document = Document()
    # TODO: Read JSON response from Google Vision OCR and return ReadyOCR Document

    return document