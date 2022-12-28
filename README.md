# Python-With-Rust

Writeup of work from https://maxwellrules.com/programming/rusty-python.html .

## Installation 

- Install rust (and cargo) from: https://www.rust-lang.org/tools/install
- Install pyenv: https://github.com/pyenv/pyenv#installation
- Optionally install `pyenv-virtualenv`: https://github.com/pyenv/pyenv-virtualenv + `pyenv install 3.8.5`
    - If you have problems with `pyenv install 3.x.x` on MacOS, a solution I found was found here: https://github.com/asdf-community/asdf-python/issues/124 i.e `brew uninstall binutils`.
    -  On my platform `3.8.5` could not build the wheel: `ERROR: Rumpy-0.1.0-cp38-cp38-macosx_10_7_x86_64.whl is not a supported wheel on this platform.`. Therefore re-ran with `pyenv install 3.10.9`. 

## Running

- Edit `Rumpy/Cargo.toml` with the provided code.
- Edit `Rumpy/src/lib.rs` with the provided code.
- Run `maturin develop --release` in the `Rumpy/` directory.