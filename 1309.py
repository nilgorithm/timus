
from functools import lru_cache

pre = ( 0, 5392, 1890, 84, 6520, 3149, 2416, 2835, 80, 8614, 742, 7696, 6823, 9492, 7710,
                 9444, 510, 118, 6522, 3213, 4499, 6178, 4565, 763, 1071, 8875, 2688, 9145, 1211,
                 9480, 4056, 1817, 8661, 5467, 3358, 2892, 2205, 8691, 1963, 2386, 8401, 1047, 3691,
                 6824, 825, 7728, 6797, 1720, 8194, 9901, 2823, 1952, 9344, 5022, 1421, 6116, 4511,
                 1289, 2133, 7494, 7298, 5012, 9638, 8753, 5968, 4029, 4804, 9556, 924, 1497, 5886,
                 6078, 2085, 3876, 268, 2910, 8962, 2970, 1015, 3931, 1103, 4872, 4054, 346, 1119,
                 931, 4454, 6530, 1722, 4266, 9888, 7961, 2891, 885, 4461, 7731, 3316, 2155, 93,
                 2871, 9710 );

mod = 9973


@lru_cache(maxsize=None)
def modmin(a, b):
    res = a-b
    return mod + res if res < 0 else res % mod


@lru_cache(maxsize=None)
def modpow(x, n):
    if n == 0:
        return 1
    return (x*modpow(x, n-1))%mod

@lru_cache(maxsize=None)
def A(x):
    x = x % mod
    return modmin(modpow(x, 5), x) + 7

@lru_cache(maxsize=None)
def B(x):
    x = x % mod
    return (modmin(((3*x) + modpow(x,3))%mod, modpow(x, 5))) % mod


def f(n):
    a = 1
    total = 0
    while n >= 0:
        p = A(n)
        if n == 0 or p == 0:
            return total
        if (n-1) % 1000000 == 0:
            return ((total + a*p%mod*pre[(n-1)//1000000])%mod+(a*B((n)))%mod)%mod
        total = (total + a*B(n))%mod
        a = (p*a) % mod
        n -= 1


print(f(int(input())))