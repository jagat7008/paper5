def credit_card(cc_num):
    marked='*'*(len(cc_num)-4)+cc_num[-4:]
    return marked
cc_num='1234567890126578'
marked_num= credit_card(cc_num)
print(marked_num)