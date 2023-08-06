use pyo3::{prelude::*, types::PyBytes};

#[pyfunction]
fn hash(py: Python, input: &[u8]) -> PyObject {
    let data = x13_rs::x13_hash(input);
    PyBytes::new(py, &data).into()
}

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn x13(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(hash, m)?)?;
    Ok(())
}
