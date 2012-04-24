__all__ = []

# ApComputation
HbComputation = __import__('HbComputation', globals(), locals(), ['HbComputation']).HbComputation

# loading the different algorithms
HbAlgoEQUI = __import__('HbAlgoEQUI', globals(), locals(), ['HbAlgoEQUI']).HbAlgoEQUI
HbAlgoAPFT = __import__('HbAlgoAPFT', globals(), locals(), ['HbAlgoAPFT']).HbAlgoAPFT
HbAlgoOPT = __import__('HbAlgoOPT', globals(), locals(), ['HbAlgoOPT']).HbAlgoOPT
__all__ = ['HbComputation',
           'HbAlgoEQUI',
           'HbAlgoAPFT',
           'HbAlgoOPT']

__version__ = '0.1'
