import sys; args = sys.argv[1:]
idx = int(args[0])-40

myRegexLst = [
  r"/^[x.o]{64}$/is",
  r"/^[xo]*\.[xo]*$/i",
  r"/^\.|\.$|^[x]{1,}[o]{0,}\.|\.[o]{0,}[x]{1,}$/i",
  r"/^(..)*.$/s",
  r"/^0(01|10|00|11)*$|^1(01|10|00|11)*[01]$/",
  r"/\w*(a[eiou]|e[aiou]|i[aeou]|o[aeiu]|u[aeio])\w*/i",
  r"/^(1?0)*1*$/",
  r"/^[bc]*[abc][bc]*$/",
  r"/^[bc]+$|^([bc]*a[bc]*a[bc]*)+$/",
  r"/^((2|1[20]*1)[2 0]*)+$/"
 ]

if idx < len(myRegexLst):
  print(myRegexLst[idx])

#Kushaan Vardhan 1 2024