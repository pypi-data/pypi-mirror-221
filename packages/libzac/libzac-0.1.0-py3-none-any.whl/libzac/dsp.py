import numpy as np
from packaging import version

def rolling_window(array:np.ndarray, window:int, step:int=1):
    """
    return rolling window matrix of input 1d `array` with `step`,
    drop tails that not enough for one window. 
        
    NOTE: THIS FUNCTION RETURN A READ-ONLY "VIEW" OF `array`, THEY SHARE THE SAME MEMORY!
    
    Examples
    --------
    >>> x = np.arange(20)
    >>> rolling_window(x,9,3)
    array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8],
           [ 3,  4,  5,  6,  7,  8,  9, 10, 11],
           [ 6,  7,  8,  9, 10, 11, 12, 13, 14],
           [ 9, 10, 11, 12, 13, 14, 15, 16, 17]])
    >>> # 18/19 is dropped
    
    >>> rolling_window(x,9,-3) 
    array([[11, 12, 13, 14, 15, 16, 17, 18, 19],
           [ 8,  9, 10, 11, 12, 13, 14, 15, 16],
           [ 5,  6,  7,  8,  9, 10, 11, 12, 13],
           [ 2,  3,  4,  5,  6,  7,  8,  9, 10]])
    >>> # 0/1 is dropped

    >>> rolling_window(x,9,-3).flags
      C_CONTIGUOUS : False
      F_CONTIGUOUS : False
      OWNDATA : False
      WRITEABLE : False
      ALIGNED : True
      WRITEBACKIFCOPY : False
    <BLANKLINE>
    """
    if version.parse(np.version.version) < version.parse('1.20.0'):
        # before numpy 1.20.0
        shape = array.shape[:-1] + (array.shape[-1] - window + 1, window)
        strides = array.strides + (array.strides[-1],)
        return np.lib.stride_tricks.as_strided(array, shape=shape, strides=strides)[::step]
    else:
        # sliding_window_view() added after numpy 1.20.0
        return np.lib.stride_tricks.sliding_window_view(array, window)[::step]

def sig2frames(array:np.ndarray, window:int, step:int=0, **pad_kwarg):
    """
    same as `rolling_window()`, but padding zeros to tails to fill up a window.
    Thus return a copy of `array` instead of a view. `**pad_kwarg` is passed to `np.pad()`.
    
    Examples
    --------
    >>> x = np.arange(20)
    >>> sig2frames(x, 9, 3)
    array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8],
           [ 3,  4,  5,  6,  7,  8,  9, 10, 11],
           [ 6,  7,  8,  9, 10, 11, 12, 13, 14],
           [ 9, 10, 11, 12, 13, 14, 15, 16, 17],
           [12, 13, 14, 15, 16, 17, 18, 19,  0]])
    >>> # note the last frame is padded with 0

    >>> sig2frames(x, 9, -3) 
    array([[11, 12, 13, 14, 15, 16, 17, 18, 19],
           [ 8,  9, 10, 11, 12, 13, 14, 15, 16],
           [ 5,  6,  7,  8,  9, 10, 11, 12, 13],
           [ 2,  3,  4,  5,  6,  7,  8,  9, 10],
           [ 0,  0,  1,  2,  3,  4,  5,  6,  7]])
    >>> # when step is negative, pad to head
    """
    n_step = abs(step)
    n_window = (array.size - window)//n_step + 1
    if window+(n_window-1)*n_step < array.size:
        pad_size = window + n_window*n_step - array.size
        array = np.pad(array, (0, pad_size) if step>0 else (pad_size,0), **pad_kwarg)
    return rolling_window(array, window, step)

if __name__ == '__main__':
    import doctest
    doctest.testmod()