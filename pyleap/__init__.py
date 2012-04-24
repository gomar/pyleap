__all__ = []

# ApComputation
ApComputation = __import__('ApComputation', globals(), locals(), ['ApComputation']).ApComputation

# loading the different algorithms
ApAlgoEQUI = __import__('ApAlgoEQUI', globals(), locals(), ['ApAlgoEQUI']).ApAlgoEQUI
ApAlgoAPFT = __import__('ApAlgoAPFT', globals(), locals(), ['ApAlgoAPFT']).ApAlgoAPFT
ApAlgoOPT = __import__('ApAlgoOPT', globals(), locals(), ['ApAlgoOPT']).ApAlgoOPT
__all__ = ['ApComputation',
           'ApAlgoEQUI',
           'ApAlgoAPFT',
           'ApAlgoOPT']
