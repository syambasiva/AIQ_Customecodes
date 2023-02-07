import pyotp

##secreteid=aiq_1;
##secreteid="KAIKKMKZYPTYJUBYAZZKVPFMGZPMBWEQ"
secreteid='H2RHE6Q2GJL4YYA2ACRO5XTTYRZUAYGJ';
totp = pyotp.TOTP(secreteid)
print(totp.now(),end='')
