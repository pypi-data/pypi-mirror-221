# This file collects routines which are focused on fundamental generation of specific
# matrices and to perform basic matrix operations.
import numpy as np
import mpmath as mp

from njet.common import check_zero
from njet.functions import get_package_name

def printmat(M, tol=1e-14):
    # print a matrix (for e.g. debugging reasons)
    M = mp.matrix(M)
    mp.nprint(mp.chop(M, tol))

def create_J(dim: int, shape=None):
    r'''
    Create a 2*dim-square matrix J, corresponding to the standard 
    symplectic block-matrix
    
             /  0   1  \
        J =  |         |
             \ -1   0  /
             
    Parameters
    ----------
    dim: int
        Dimension/2 of the matrix to be constructed.
        
    shape: tuple, optional
        If given, assume that the 0's and 1's in the above matrix
        have a given shape. Return a multi-dimensional numpy array accordingly.
        
    Returns
    -------
    list
        List of column vectors.
    '''
    dim2 = 2*dim
    J1, J2 = [], []
    if shape is None:
        zeros = 0
        ones = 1
    else:
        zeros = np.zeros(shape, dtype=np.complex128)
        ones = np.ones(shape, dtype=np.complex128)
        
    for k in range(dim):
        J1.append([zeros if i != k + dim else ones for i in range(dim2)])
        J2.append([zeros if i != k else -ones for i in range(dim2)])        
    return np.array(J1 + J2)

def expandingSum(pairs):
    '''Compute a transformation matrix T, to transform a given
    (2n)x(2n) matrix M, represented in (q1, p1, q2, p2, ..., qn, pn)-coordinates, into
    a (q1, q2, ..., qn, p1, p2, ..., pn)-representation via
    M' = T^(-1)@M@T. T will be orthogonal (and unitary), i.e. T^(-1) = T.transpose().
    
    See also Refs. [1, 2] or (alternatively) in Ref. [3], p. 292. In particular, M
    is given in terms of 2x2 block matrices, then M' is called the 'expanding Sum' of M.
    
    Parameters
    ----------
        
    pairs: int or list
        If an integer is given, then it is assumed that this integer denotes
        the dimension of the current problem. A respective square matrix T
        (array-like) will be constructed, as described above.
        
        If a list is given, then it is assumed that this list consists of
        tuples by which one can tweak the order of the original coordinates:
        In this case the list must unambigously identify each pair (q_i, p_j) by a specific tuple
        (i, j) in the list. The outcome will be an orthogonal (and unitary) matrix T
        which transformations the coordinates (q_i, ..., p_j, ...) into 
        (q_i, ..., q_n, p_j, ..., p_n). Herby the k'th element in the list will be cast to
        positions k, k + dim.
        
    Returns
    -------
    np.matrix
        Numpy matrix T defining the aforementioned transformation.
        
    Reference(s):
    [1]: M. Titze: "Space Charge Modeling at the Integer Resonances for the CERN PS and SPS", PhD Thesis (2019)
    [2]: M. Titze: "On emittance and optics calculation from the tracking data in periodic lattices", arXiv.org (2019)
    [3]: R. J. de la Cruz and H. Faßbender: "On the diagonalizability of a matrix by a symplectic equivalence, similarity or congruence transformation (2016).
    '''
    if type(pairs) == int:
        dim = pairs
        # the 'default' ordering is used, transforming (q1, p1, q2, p2, ...) into (q1, q2, ..., p1, p2, ...)
        indices_1 = [(j, j//2) if j%2 == 0 else (j, dim + (j - 1)//2) for j in range(2*dim)]
    else:
        dim = len(pairs)
        indices_1 = [(pairs[k][0], k) for k in range(dim)] + [(pairs[k][1], k + dim) for k in range(dim)]
        
    T = np.zeros([dim*2, dim*2])
    # define the columns of T:
    for i, j in indices_1:
        T[i, j] = 1
    return T

def matrix_from_dict(M, symmetry: int=0, **kwargs):
    '''
    Create matrix from (sparse) dict.
    
    Parameters
    ----------
    M: dict
        The dictionary defining the entries M_ij of the matrix in the form:
        M[(i, j)] = M_ij
        
    n_rows: int, optional
        The number of rows.

    n_cols: int, optional
        The number of columns.
    
    symmetry: int, optional
        If 0, no symmetry is assumed (default). 
        If 1, matrix is assumed to be symmetric. Requires n_rows == n_cols.
        If -1, matrix is assumed to be anti-symmetric. Requires n_rows == n_cols.
        
    Returns
    -------
    A: ndarray
        A numpy ndarray representing the requested matrix.
    '''
    assert symmetry in [-1, 0, 1]

    dict_shape = max(M.keys(), default=(0, 0))
    n_rows = kwargs.get('n_rows', dict_shape[0] + 1)
    n_cols = kwargs.get('n_cols', dict_shape[1] + 1)
    
    # determine shape of entries in case of multi-dimensional input
    key0 = next(iter(M))
    val0 = M[key0]
    if hasattr(val0, 'shape'):
        zero = np.zeros(val0.shape)
    else:
        zero = 0
    
    # create a column-matrix
    if symmetry == 0:
        mat = [[0]*n_rows for k in range(n_cols)]
        for i in range(n_rows):
            for j in range(n_cols):
                mat[i][j] = M.get((i, j), zero)
    else:
        dim = max([n_rows, n_cols])
        mat = [[0]*dim for k in range(dim)]
        for i in range(dim):
            for j in range(i + 1):
                hij = M.get((i, j), zero)
                hji = M.get((j, i), zero)
                
                hij_c0 = check_zero(hij)
                hji_c0 = check_zero(hji)
                
                if not hij_c0 and not hji_c0 and symmetry != 0:
                    check = hij == symmetry*hji
                    try:
                        assert check
                    except:
                        assert check.all()

                if hij_c0 and not hji_c0:
                    hij = symmetry*hji
                    
                # (hij != 0 and hji == 0) or (hij == 0 and hji == 0). 
                mat[i][j] = hij
                mat[j][i] = symmetry*hij
    return np.array(mat)
    
def vecmat(mat):
    '''
    Map a given NxN-matrix to a vector, by concatenating its rows.
    '''
    return np.concatenate([mat[k, :] for k in range(mat.shape[0])])

def matvec(vec):
    '''
    Map a given vector of length N**2 to an NxN matrix. This map is the
    inverse of the vecmat routine.
    '''
    n = len(vec)
    assert np.sqrt(n)%1 == 0, 'Vector does not appear to originate from square matrix.'
    m = int(np.sqrt(n))
    return np.array([[vec[j + k*m] for j in range(m)] for k in range(m)])

def adjoint(mat):
    '''
    Map a given NxN-matrix to its adjoint representation with respect to the vecmat and matvec routines.
    '''
    assert mat.shape[0] == mat.shape[1], 'Matrix not square.'
    n = mat.shape[0]
    delta = lambda *z: 1 if z[0] == z[1] else 0
    result = np.zeros([n**2, n**2], dtype=np.complex128)
    for u in range(n**2):
        alpha, beta = divmod(u, n)
        for v in range(n**2):
            i, j = divmod(v, n)
            result[v, u] = mat[i, alpha]*delta(beta, j) - delta(alpha, i)*mat[beta, j]      
    return result

def create_pq2xieta(dim, code, **kwargs):
    '''
    Create a unitary matrix, mapping (p, q)-coordinates to (xi, eta)-coordinates via
    xi = (q + 1j*p)/sqrt(2)
    eta = (q - 1j*p)/sqrt(2)
    '''
    assert dim%2 == 0
    
    if code == 'numpy':
        sqrt2 = np.sqrt(2)
    if code == 'mpmath':
        if 'dps' in kwargs.keys():
            mp.mp.dps = kwargs['dps'] 
        sqrt2 = mp.sqrt(2)
        
    U1, U2 = [], []
    dim_half = dim//2
    for k in range(dim_half):
        k2 = k + dim_half
        U1.append([0 if i != k and i != k2 else 1/sqrt2 for i in range(dim)])
        U2.append([0 if i != k and i != k2 else 1j/sqrt2 if i == k else -1j/sqrt2 if i == k2 else 0 for i in range(dim)])
        
    out = np.array(U1 + U2).transpose()
    if code == 'mpmath':
        out = mp.matrix(out)
    return out


class emat:
    '''
    emat: extended matrix
    
    Class to maintain the same behavior as the ordinary mpmath or numpy arrays
    concerning matrix multiplication, but when it comes to matrix multiplication
    and transposition, only modify the first two axes.
    '''
    def __init__(self, matrix, code=None):
        self.__array_priority__ = 1000 # prevent numpy __mul__ and force self.__rmul__ instead if multiplication from left with a numpy object
        
        if code is None:
            self.code = get_package_name(matrix)
        else:
            self.code = code
        self.matrix = matrix
        if hasattr(matrix, 'shape'):
            self.shape = self.matrix.shape
    
    def __add__(self, other):
        assert self.code == other.code
        return self.__class__(self.matrix + other.matrix, code=self.code)
    
    def __radd__(self, other):
        return self + other
    
    def __neg__(self):
        return self.__class__(-self.matrix, code=self.code)
    
    def __sub__(self, other):
        return self + -other
    
    def __rsub__(self, other):
        return other - self
    
    def __mul__(self, other):
        return self.__class__(self.matrix*other, code=self.code)
    
    def __rmul__(self, other):
        return self*other
    
    def __matmul__(self, other):
        if self.code == 'numpy':
            if get_package_name(other) == 'numpy':
                B = other
            elif hasattr(other, 'matrix'):
                # assume other is of class emat
                B = other.matrix
            else:
                raise NotImplementedError(f'Matrix multiplication between {self.__class__} and {other.__class__} not implemented.')
                
            A = self.matrix
            shape1 = A.shape
            shape2 = B.shape
            assert shape1[1] == shape2[0]
            if len(shape1[2:]) == 0 and len(shape2[2:]) == 0:
                # both are ordinary matrices
                AB = A@B
            elif len(shape1[2:]) > 0 and len(shape2[2:]) == 0:
                # B is an ordinary matrix
                AB1 = np.tensordot(A, B, axes=(1, 0)) # axes not in proper order yet
                # the last axes of AB1 corresponds to the second axis of the ordinary matrix B, so it needs to be moved to the 2nd position of the result
                for k in range(len(shape2[1:])):
                    AB2 = np.moveaxis(AB1, -1, 0)
                    AB1 = np.swapaxes(AB2, 0, 1)
                AB = AB1
            elif len(shape1[2:]) == 0 and len(shape2[2:]) > 0:
                # A is an ordinary matrix
                AB = np.tensordot(A, B, axes=(1, 0))
            else:
                assert shape1[2:] == shape2[2:]
                # component-wise multiplication of the remaining terms
                AB_shape = [shape1[0]] + [shape2[1]] + list(shape1[2:])
                AB = np.empty(AB_shape, dtype=np.complex128)
                for i in range(shape2[1]):
                    AB[i, ...] = sum([A[i, k, ...]*B[k, ...] for k in range(shape1[1])])

            return self.__class__(AB, code=self.code)
        else:
            if not hasattr(other, 'matrix'): # other might be a numpy or mpmath array
                return self.__class__(self.matrix@other, code=self.code)
            else:
                return self.__class__(self.matrix@other.matrix, code=self.code)
            
        def __rmatmul__(self, other):
            return self.__class__(other, code=self.code)@self
        
    def transpose(self):
        if self.code == 'numpy':
            return self.__class__(np.swapaxes(self.matrix, 0, 1), code=self.code)
        else:
            return self.__class__(self.matrix.transpose(), code=self.code)
        
    def conjugate(self):
        return self.__class__(self.matrix.conjugate(), code=self.code)
    
    def __len__(self):
        return len(self.matrix)
    