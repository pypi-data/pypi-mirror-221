# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_utils.ipynb.

# %% auto 0
__all__ = ['let_only_digits', 'format_cnpj', 'format_cpf', 'fill_zeros']

# %% ../nbs/02_utils.ipynb 2
def let_only_digits(doc: str) -> str:
    """Remove all non-digit characters from a string"""
    return ''.join(filter(str.isdigit, doc))

# %% ../nbs/02_utils.ipynb 6
def format_cnpj(cnpj: str) -> str:
    """Format a CNPJ string"""
    return cnpj[:2] + '.' + cnpj[2:5] + '.' + cnpj[5:8] + '/' + cnpj[8:12] + '-' + cnpj[12:]

# %% ../nbs/02_utils.ipynb 8
def format_cpf(cpf: str) -> str:
    """Format a CPF string"""
    return cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]

# %% ../nbs/02_utils.ipynb 10
def fill_zeros(doc: str, n: int) -> str:
    """Fill a string with zeros to the left with n characters"""
    return doc.zfill(n)
