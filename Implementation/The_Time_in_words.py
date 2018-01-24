h = int(input().strip())
m = int(input().strip())
hours_in_words = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelwe', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'ninteen', 'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine']
hours_in_numeric = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
if m == 0: print(hours_in_words[h]+" o' clock")
elif m == 15: print("quarter past "+hours_in_words[h])
elif m == 45: print("quarter to "+hours_in_words[h+1])
elif m == 30: print("half past "+hours_in_words[h])
elif m == 1: print(hours_in_words[m] + " minute past " + hours_in_words[h])
elif m < 30: print(hours_in_words[m]+" minutes past "+hours_in_words[h])
elif m == 59: print(hours_in_words[(60-m)]+" minute to "+hours_in_words[h+1])
elif m > 30: print(hours_in_words[(60-m)]+" minutes to "+hours_in_words[h+1])