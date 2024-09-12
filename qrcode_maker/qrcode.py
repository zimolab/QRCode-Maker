import segno
from pyguiadapter.exceptions import ParameterError


def make_qrcode(
        text: str,
        save_path: str,
        dot_size: int,
        foreground: str,
        background: str,
        error_correction: str,
        border: int,
        encoding: str
):
    # Before we do the actual work, it is highly recommended to check the parameters first.
    if not text:
        raise ParameterError("text", "Text cannot be empty!")

    if not save_path or save_path.strip() == "":
        raise ParameterError("save_path", "Save path cannot be empty!")

    if dot_size < 1:
        raise ParameterError("dot_size", f"Invalid dot size: {dot_size}")

    if not foreground or foreground.strip() == "":
        raise ParameterError("foreground", "Foreground color cannot be empty!")

    if not background or background.strip() == "":
        raise ParameterError("background", "Background color cannot be empty!")

    if error_correction not in ["L", "M", "Q", "H"]:
        raise ParameterError("error_correction", f"Invalid error correction level: {error_correction}")

    if border < 0:
        raise ParameterError("border", f"Invalid border size: {border}")

    # OK, here we think all the parameters are valid, let encode the text into a QR code
    qr = segno.make_qr(
        content=text,
        error=error_correction,
    )
    qr.save(
        out=save_path,
        scale=dot_size,
        border=border,
        dark=foreground,
        light=background,
    )