import logging
import os
import tempfile
import unittest

import pytest
from faker_file.providers.bin_file import BinFileProvider
from faker_file.providers.bmp_file import (
    BmpFileProvider,
    GraphicBmpFileProvider,
)
from faker_file.providers.csv_file import CsvFileProvider
from faker_file.providers.docx_file import DocxFileProvider
from faker_file.providers.eml_file import EmlFileProvider
from faker_file.providers.epub_file import EpubFileProvider
from faker_file.providers.gif_file import (
    GifFileProvider,
    GraphicGifFileProvider,
)
from faker_file.providers.ico_file import (
    GraphicIcoFileProvider,
    IcoFileProvider,
)
from faker_file.providers.jpeg_file import (
    GraphicJpegFileProvider,
    JpegFileProvider,
)
from faker_file.providers.mp3_file import Mp3FileProvider
from faker_file.providers.odp_file import OdpFileProvider
from faker_file.providers.ods_file import OdsFileProvider
from faker_file.providers.odt_file import OdtFileProvider
from faker_file.providers.pdf_file import (
    GraphicPdfFileProvider,
    PdfFileProvider,
)
from faker_file.providers.png_file import (
    GraphicPngFileProvider,
    PngFileProvider,
)
from faker_file.providers.pptx_file import PptxFileProvider
from faker_file.providers.rtf_file import RtfFileProvider
from faker_file.providers.svg_file import SvgFileProvider
from faker_file.providers.tar_file import TarFileProvider
from faker_file.providers.tiff_file import (
    GraphicTiffFileProvider,
    TiffFileProvider,
)
from faker_file.providers.txt_file import TxtFileProvider
from faker_file.providers.webp_file import (
    GraphicWebpFileProvider,
    WebpFileProvider,
)
from faker_file.providers.xlsx_file import XlsxFileProvider
from faker_file.providers.xml_file import XmlFileProvider
from faker_file.providers.zip_file import ZipFileProvider
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication

from faker_file_qt import FakerFileApp, get_item_key

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("TestFakerFileApp",)

LOGGER = logging.getLogger(__name__)


class TestFakerFileApp(unittest.TestCase):
    __PROVIDERS = (
        BinFileProvider.bin_file.__name__,
        BmpFileProvider.bmp_file.__name__,
        CsvFileProvider.csv_file.__name__,
        DocxFileProvider.docx_file.__name__,
        EmlFileProvider.eml_file.__name__,
        EpubFileProvider.epub_file.__name__,
        GifFileProvider.gif_file.__name__,
        GraphicBmpFileProvider.graphic_bmp_file.__name__,
        GraphicGifFileProvider.graphic_gif_file.__name__,
        GraphicIcoFileProvider.graphic_ico_file.__name__,
        GraphicJpegFileProvider.graphic_jpeg_file.__name__,
        GraphicPdfFileProvider.graphic_pdf_file.__name__,
        GraphicPngFileProvider.graphic_png_file.__name__,
        GraphicTiffFileProvider.graphic_tiff_file.__name__,
        GraphicWebpFileProvider.graphic_webp_file.__name__,
        IcoFileProvider.ico_file.__name__,
        JpegFileProvider.jpeg_file.__name__,
        OdpFileProvider.odp_file.__name__,
        OdsFileProvider.ods_file.__name__,
        OdtFileProvider.odt_file.__name__,
        PdfFileProvider.pdf_file.__name__,
        PngFileProvider.png_file.__name__,
        PptxFileProvider.pptx_file.__name__,
        RtfFileProvider.rtf_file.__name__,
        SvgFileProvider.svg_file.__name__,
        TarFileProvider.tar_file.__name__,
        TiffFileProvider.tiff_file.__name__,
        TxtFileProvider.txt_file.__name__,
        WebpFileProvider.webp_file.__name__,
        XlsxFileProvider.xlsx_file.__name__,
        XmlFileProvider.xml_file.__name__,
        ZipFileProvider.zip_file.__name__,
    )
    __PROVIDERS_INTERNET = (Mp3FileProvider.mp3_file.__name__,)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.app = QApplication([])

    def _test_generate_result(self, providers):
        widget = FakerFileApp()
        # widget.show()

        for i in range(widget.list_widget.count()):  # Iterate over all options
            # Select current item in list
            widget.list_widget.setCurrentRow(i)
            item = widget.list_widget.currentItem()
            item_key = get_item_key(item)
            LOGGER.debug(item)
            LOGGER.debug(item_key)

            # Fill form with test data
            prefix = f"my_file_{item_key}"
            test_data = {
                "prefix": prefix,
                # "length": "1_024",
            }

            if item_key not in providers:
                continue
                # test_data.update({"content": "A", "extension": "txt"})

            for param, input_value in test_data.items():
                widget.param_widgets[param].setText(input_value)

            # Simulate clicking the generate button
            generate_button = widget.form_layout.itemAt(
                widget.form_layout.count() - 1
            ).widget()
            QTest.mouseClick(generate_button, Qt.LeftButton)

            # Check result
            result = widget.result_widget.toPlainText()
            # Assuming the result should contain the text "File generated"
            self.assertTrue(
                result.startswith(
                    os.path.join(tempfile.gettempdir(), "tmp", prefix)
                ),
                f"Unexpected result: {result} for {item_key}",
            )

    def test_generate_results(self):
        self._test_generate_result(
            providers=self.__PROVIDERS,
        )

    @pytest.mark.xfail
    def test_generate_results_allow_failures(self):
        self._test_generate_result(providers=self.__PROVIDERS_INTERNET)


if __name__ == "__main__":
    unittest.main()
