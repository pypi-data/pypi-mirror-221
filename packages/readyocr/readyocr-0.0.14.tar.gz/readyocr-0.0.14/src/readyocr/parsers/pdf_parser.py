import os
import shutil
from uuid import uuid4
from collections.abc import Iterable

import numpy as np
import pdf2image
from pdfminer.high_level import extract_pages
from pdfminer.layout import (
    LTPage,
    LTLine,
    LTRect,
    LTCurve, 
    LTFigure,
    LTImage,
    LTTextLine,
    LTTextBox,
    LTChar,
    LTText
)
from pdfminer.image import ImageWriter
from PIL import Image as PILImage

from readyocr.entities import BoundingBox, Character, Line, Block, Image, Figure, Page, Document


def _parse_bbox(item, page):
    x=float(item.x0/page.width)
    y=float((page.height - item.y1)/page.height)
    width=float(item.width/page.width)
    height=float(item.height/page.height)

    return BoundingBox(
        x=min(1, max(0, x)),
        y=min(1, max(0, y)),
        width=min(1, max(0, width)),
        height=min(1, max(0, height)),
    )


def _parse_page_entity(item, page):
    obj = None
    
    # make temporary directory
    saved_image_dir = str(uuid4())
    os.makedirs(saved_image_dir, exist_ok=True)
    iw = ImageWriter(saved_image_dir)
    
    if isinstance(item, LTLine):
        # print(f"Line: {item}")
        pass
    elif isinstance(item, LTRect):
        # print(f"Rect: {item}")
        pass
    elif isinstance(item, LTCurve):
        # print(f"Curve: {item}")
        pass
    elif isinstance(item, LTFigure):
        obj = Figure(
            id=str(uuid4()),
            bbox=_parse_bbox(item, page),
            confidence=1
        )
    elif isinstance(item, LTImage):
        try:
            name = iw.export_image(item)
            image_path = os.path.join(saved_image_dir, name)
            image = PILImage.open(image_path).convert('RGB')
        except:
            image = None

        obj = Image(
            id=str(uuid4()),
            bbox=_parse_bbox(item, page),
            confidence=1,
            image=image
        )

    elif isinstance(item, LTTextLine):
        obj = Line(
            id=str(uuid4()),
            bbox=_parse_bbox(item, page),
            text=item.get_text(),
            confidence=1
        )
    elif isinstance(item, LTTextBox):
        obj = Block(
            id=str(uuid4()),
            bbox=_parse_bbox(item, page),
            text=item.get_text(),
            confidence=1
        )
    elif isinstance(item, LTChar):
        obj = Character(
            id=str(uuid4()),
            bbox=_parse_bbox(item, page),
            text=item.get_text(),
            confidence=1,
            metadata={
                # 'line-width': item.graphicstate.linewidth,
                # 'line-cap': item.graphicstate.linecap,
                # 'line-join': item.graphicstate.linejoin,
                # 'miter-limit': item.graphicstate.miterlimit,
                # 'dash': item.graphicstate.dash,
                # 'intent': item.graphicstate.intent,
                # 'flatness': item.graphicstate.flatness,
                'color-space': item.ncs.name,
                'ncomponents': item.ncs.ncomponents,
                'font-family': item.fontname,
                'font-size': item.size,
                'text-stroke-color': item.graphicstate.scolor,
                'text-fill-color': item.graphicstate.ncolor,
            }
        )
    elif isinstance(item, LTText):
        pass
    else:
        assert False, str(("Unhandled", item))

    if isinstance(item, Iterable):
        for child in item:
            child_obj = _parse_page_entity(child, page)
            if child_obj is not None:
                obj.children.add(child_obj)

    # remove temporary image dir
    shutil.rmtree(saved_image_dir)
    
    return obj


def _parse_page(ltpage: LTPage, image: PILImage) -> Page:
    page = Page(
        id=str(uuid4()),
        width=ltpage.width,
        height=ltpage.height,
        page_num=ltpage.pageid,
        image=image
    )

    for item in ltpage:
        page_entity = _parse_page_entity(item, page)
        if page_entity is not None:
            page.children.add(page_entity)

    return page


def load(pdf_path: str, last_page: int=None) -> Document:
    if last_page is None:
        images = pdf2image.convert_from_path(pdf_path, fmt='jpeg')
        ltpages = extract_pages(pdf_path)
    else:
        images = pdf2image.convert_from_path(pdf_path, last_page=last_page, fmt='jpeg')
        ltpages = extract_pages(pdf_path, maxpages=last_page)
    
    document = Document()
    
    for idx, (image, ltpage) in enumerate(zip(images, ltpages)):
        page = _parse_page(ltpage=ltpage, image=image.convert('RGB'))
        document.add(page)

    return document