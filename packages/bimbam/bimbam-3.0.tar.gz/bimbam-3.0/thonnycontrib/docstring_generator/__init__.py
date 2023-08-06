from .doc_generator import DocGenerator

# Ceci est une implémentation de création d'un singleton pour L1TestRunner
_doc_generator: DocGenerator = None

def get_doc_generator() -> DocGenerator:
    """
    If there's no `DocGenerator` instance creates one and returns it,
    otherwise returns the current `DocGenerator` instance.
    """
    return DocGenerator() if not _doc_generator else _doc_generator