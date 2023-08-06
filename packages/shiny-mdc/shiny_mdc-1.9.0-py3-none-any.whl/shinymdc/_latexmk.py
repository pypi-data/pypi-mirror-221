import subprocess
import sys
from pathlib import Path
from typing import Literal


def run_latexmk(
    input_path: Path,
    build_dir: Path,
    pdf_engine: Literal["pdflatex", "lualatex", "xelatex"],
    clean: bool = False,
    verbose: bool = False,
    force: bool = False,
    strict: bool = False,
) -> Path:
    """Compile a LaTeX file using `latexmk`.

    Args:
        input_path: Path to input file.
        build_dir: Path to build directory.
        pdf_engine: PDF engine to use.
        clean: Whether to do a clean build by passing `-gg` to `latexmk`.
        verbose: Whether to enable verbose output.
        force: Whether to pass `-f` to `latexmk`.
        strict: Whether to pass `-Werror` to `latexmk`.

    Returns:
        Path to output file.

    Raises:
        subprocess.CalledProcessError: If `latexmk` subprocess fails.
    """
    cmd = ["latexmk", "-interaction=nonstopmode"]

    if pdf_engine == "pdflatex":
        cmd.append("-pdf")
    elif pdf_engine in ("lualatex", "xelatex"):
        cmd.append(f"-{pdf_engine}")
    else:
        raise ValueError(
            f"invalid pdf engine (expected 'pdflatex/lualatex/xelatex'): "
            f"{pdf_engine}"
        )

    if clean:
        cmd.append("-gg")
    if not verbose:
        cmd.append("-silent")
    if force:
        cmd.append("-f")
    if strict:
        cmd.append("-Werror")

    cmd.append(f"-output-directory={build_dir}")
    cmd.append(str(input_path))

    print("+", *cmd, file=sys.stderr)
    subprocess.run(
        cmd,
        check=True,
        stdout=sys.stdout if verbose else subprocess.DEVNULL,
        stderr=sys.stderr,
    )
    return build_dir / input_path.with_suffix(".pdf").name
