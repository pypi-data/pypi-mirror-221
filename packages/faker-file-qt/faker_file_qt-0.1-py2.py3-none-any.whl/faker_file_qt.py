import ast
import inspect
import logging
import sys
from typing import Any, AnyStr, Dict, List, Tuple, Union, get_args, get_origin

import qdarkstyle
from faker import Faker
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
from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QApplication,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QSizePolicy,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

__title__ = "faker_file_qt"
__version__ = "0.1"
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "FakerFileApp",
    "get_item_key",
    "get_label_text",
    "main",
    "str_to_type",
)

LOGGER = logging.getLogger(__name__)
FAKER = Faker()

KWARGS_DROP = {
    "self",  # Drop as irrelevant
    "storage",  # Drop as non-supported arg
    "return",  # Drop as irrelevant
    "format_func",  # Drop as non-supported arg
    "raw",  # Drop `raw`, because we will be forcing raw=True for streaming
}

OVERRIDES = {
    "DocxFileProvider.docx_file": {
        "annotations": {
            "content": str,
        },
        "model_props": {
            "content": None,
        },
    },
    "Mp3FileProvider.mp3_file": {
        "annotations": {
            "mp3_generator_cls": str,
        },
        "model_props": {
            "mp3_generator_cls": (
                "faker_file.providers.mp3_file.generators"
                ".gtts_generator.GttsMp3Generator"
            ),
        },
    },
    "OdtFileProvider.odt_file": {
        "annotations": {
            "content": str,
        },
        "model_props": {
            "content": None,
        },
    },
    "PdfFileProvider.pdf_file": {
        "annotations": {
            "pdf_generator_cls": str,
        },
        "model_props": {
            "pdf_generator_cls": (
                "faker_file.providers.pdf_file.generators"
                ".pdfkit_generator.PdfkitPdfGenerator"
            ),
        },
    },
}

PROVIDERS = {
    BinFileProvider.bin_file.__name__: BinFileProvider,
    BmpFileProvider.bmp_file.__name__: BmpFileProvider,
    CsvFileProvider.csv_file.__name__: CsvFileProvider,
    DocxFileProvider.docx_file.__name__: DocxFileProvider,
    EmlFileProvider.eml_file.__name__: EmlFileProvider,
    EpubFileProvider.epub_file.__name__: EpubFileProvider,
    GifFileProvider.gif_file.__name__: GifFileProvider,
    GraphicBmpFileProvider.graphic_bmp_file.__name__: GraphicBmpFileProvider,
    GraphicGifFileProvider.graphic_gif_file.__name__: GraphicGifFileProvider,
    GraphicIcoFileProvider.graphic_ico_file.__name__: GraphicIcoFileProvider,
    GraphicJpegFileProvider.graphic_jpeg_file.__name__: (
        GraphicJpegFileProvider
    ),
    GraphicPdfFileProvider.graphic_pdf_file.__name__: GraphicPdfFileProvider,
    GraphicPngFileProvider.graphic_png_file.__name__: GraphicPngFileProvider,
    GraphicTiffFileProvider.graphic_tiff_file.__name__: GraphicTiffFileProvider,
    GraphicWebpFileProvider.graphic_webp_file.__name__: (
        GraphicWebpFileProvider
    ),
    IcoFileProvider.ico_file.__name__: IcoFileProvider,
    JpegFileProvider.jpeg_file.__name__: JpegFileProvider,
    Mp3FileProvider.mp3_file.__name__: Mp3FileProvider,
    OdpFileProvider.odp_file.__name__: OdpFileProvider,
    OdsFileProvider.ods_file.__name__: OdsFileProvider,
    OdtFileProvider.odt_file.__name__: OdtFileProvider,
    PdfFileProvider.pdf_file.__name__: PdfFileProvider,
    PngFileProvider.png_file.__name__: PngFileProvider,
    PptxFileProvider.pptx_file.__name__: PptxFileProvider,
    RtfFileProvider.rtf_file.__name__: RtfFileProvider,
    SvgFileProvider.svg_file.__name__: SvgFileProvider,
    TarFileProvider.tar_file.__name__: TarFileProvider,
    TiffFileProvider.tiff_file.__name__: TiffFileProvider,
    TxtFileProvider.txt_file.__name__: TxtFileProvider,
    WebpFileProvider.webp_file.__name__: WebpFileProvider,
    XlsxFileProvider.xlsx_file.__name__: XlsxFileProvider,
    XmlFileProvider.xml_file.__name__: XmlFileProvider,
    ZipFileProvider.zip_file.__name__: ZipFileProvider,
}

# Names that should show a multi-line text box
MULTI_LINE_INPUTS = [
    "content",
    "data_columns",
    "options",
    "mp3_generator_kwargs",
    "pdf_generator_kwargs",
]


def str_to_type(s: str, t: type) -> Any:
    if t in {int, float}:
        return t(s)
    elif t is bool:
        return bool(s)
    elif t is str:
        return s
    elif t is bytes:
        return s.encode()
    elif t in {AnyStr, Any}:
        return s  # Just return the string
    elif get_origin(t) is Union:
        args = get_args(t)
        if type(None) in args:
            # It's an Optional type
            for arg in args:
                if arg is not type(None):  # Try the other type
                    if s:  # If the string is not empty, try to convert
                        return str_to_type(s, arg)
                    else:  # If the string is empty, return None
                        return None
        elif bytes in args and str in args:  # Special case: Union[bytes, str]
            try:
                return s.encode()  # Try to decode as bytes first
            except UnicodeDecodeError:  # If that fails, return as str
                return s
        else:
            raise NotImplementedError(f"Don't know how to handle {t}")
    else:
        origin = get_origin(t)
        if origin in {list, List}:
            return [str_to_type(x, get_args(t)[0]) for x in ast.literal_eval(s)]
        elif origin in {tuple, Tuple}:
            return tuple(
                str_to_type(x, get_args(t)[0]) for x in ast.literal_eval(s)
            )
        elif origin in {dict, Dict}:
            return {
                k: str_to_type(v, get_args(t)[1])
                for k, v in ast.literal_eval(s).items()
            }
        else:
            raise NotImplementedError(f"Don't know how to handle {t}")


def get_label_text(name: str) -> str:
    return name.replace("_", " ")


def get_item_key(item) -> str:
    return item.data(QtCore.Qt.UserRole)


class FakerFileApp(QWidget):
    def __init__(self):
        super().__init__()

        self.param_widgets = {}
        self.param_annotations = (
            {}
        )  # Add this line to initialize the dictionary

        self.initUI()

    def initUI(self):
        # Set window size
        self.setGeometry(200, 200, 960, 600)

        # Create a QHBoxLayout
        layout = QHBoxLayout()

        self.list_widget = QListWidget()
        self.list_widget.itemClicked.connect(self.show_form)

        self.form_widget = QWidget()
        self.form_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.form_layout = QFormLayout(self.form_widget)
        self.form_layout.setContentsMargins(
            10, 10, 10, 10
        )  # set some margins for spacing

        form_wrapper = QWidget()
        form_wrapper_layout = QVBoxLayout()
        form_wrapper_layout.addWidget(self.form_widget)
        form_wrapper_layout.addStretch(1)
        form_wrapper.setLayout(form_wrapper_layout)

        self.result_widget = QTextEdit()

        for file_type in PROVIDERS.keys():
            list_item = QListWidgetItem(get_label_text(file_type))
            # Store the original string in the UserRole data role
            list_item.setData(QtCore.Qt.UserRole, file_type)
            self.list_widget.addItem(list_item)
            # self.list_widget.addItem(file_type)

        self.list_widget.setCurrentRow(0)
        self.list_widget.itemClicked.emit(self.list_widget.currentItem())

        layout.addWidget(self.list_widget, -1)
        # layout.addWidget(self.form_widget, 1)
        layout.addWidget(form_wrapper, 3)
        layout.addWidget(self.result_widget, 3)
        self.setLayout(layout)

    def show_form(self, item):
        file_type = get_item_key(item)
        # file_type = item.text()
        provider = PROVIDERS[file_type]

        method = getattr(provider(FAKER), file_type)
        method_specs = inspect.getfullargspec(method)

        # Clear the form
        for i in reversed(range(self.form_layout.count())):
            self.form_layout.itemAt(i).widget().deleteLater()

        self.param_widgets = {}  # Clear this dictionary here
        self.param_annotations = {}  # And this one

        # Build the form
        for arg in method_specs.args[1:]:  # Omit 'self'
            if arg not in KWARGS_DROP:
                label = QLabel(get_label_text(arg))
                line_edit = (
                    QTextEdit() if arg in MULTI_LINE_INPUTS else QLineEdit()
                )
                line_edit.setSizePolicy(
                    QSizePolicy.Expanding, QSizePolicy.Fixed
                )
                line_edit.setFixedWidth(300)

                self.form_layout.addWidget(label)
                self.form_layout.addWidget(line_edit)
                # self.form_layout.addRow(label, line_edit)

                self.param_widgets[
                    arg
                ] = line_edit  # Store a reference to the widget
                self.param_annotations[arg] = method_specs.annotations.get(
                    arg, str
                )  # Store the type annotation

        generate_button = QPushButton("Generate")
        generate_button.clicked.connect(self.generate_result)
        self.form_layout.addWidget(generate_button)

    def generate_result(self):
        kwargs = {}

        # Extract the values from the QLineEdit widgets and convert them to
        # their appropriate types.
        for param, widget in self.param_widgets.items():
            # input_value = widget.text().strip()
            if isinstance(widget, QTextEdit):
                input_value = widget.toPlainText().strip()
            elif isinstance(widget, QLineEdit):
                input_value = widget.text().strip()

            type_annotation = self.param_annotations[param]

            # If the input value is not empty, convert it to its appropriate
            # type.
            if input_value:
                converted_value = str_to_type(input_value, type_annotation)
            else:  # If the input value is empty, use None
                converted_value = None
            if input_value:
                # kwargs[param] = input_value
                kwargs[param] = converted_value

        # Add the overrides here if necessary
        for key, value in OVERRIDES.items():
            provider_key, method_name = key.split(".")
            if get_item_key(self.list_widget.currentItem()) == method_name:
                if "model_props" in value and value["model_props"]:
                    kwargs.update(value["model_props"])

        file_type = get_item_key(self.list_widget.currentItem())
        provider = PROVIDERS[file_type]
        method = getattr(provider(FAKER), file_type)

        try:
            result = method(**kwargs)  # Get your result here
            result_text = result.data["filename"]
        except Exception as err:
            LOGGER.debug(kwargs)
            LOGGER.exception(err)
            result = None
            result_text = ""
        self.result_widget.setText(str(result_text))  # Display the result


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    # app.setStyleSheet(
    #     qdarkstyle._load_stylesheet(
    #         qt_api='pyqt5',
    #         palette=qdarkstyle.light.palette.LightPalette,
    #     )
    # )
    ex = FakerFileApp()
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
