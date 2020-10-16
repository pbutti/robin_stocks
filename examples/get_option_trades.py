import robin_stocks as r

'''
'''

#!!! Fill out username and password
username = ''
password = ''
#!!!

login = r.login(username,password)

profileData = r.load_portfolio_profile()
optionOrders = r.get_all_option_orders()

debug = False
TotalCredit = 0.
TotalDebit  = 0.
dump = False
if dump:
    r.export_completed_option_orders("../", "options")


for kv in optionOrders:
    info = ""
    openOption = True
    #filter out the cancelled options
    if float(kv["canceled_quantity"]) > 0. :
        continue
    else:
        if kv['chain_symbol']:
            #It's a closing option
            if not kv['opening_strategy']:
                openOption=False

            if debug:
                print (kv)
            if kv['direction']=='credit':
                TotalCredit+=float(kv['processed_premium'])
            else:
                TotalDebit+=float(kv['processed_premium'])
                
            if (openOption):
                info+="Equity: "  +kv['chain_symbol']+ " "
                info+="Opening Strategy: "+kv['opening_strategy'] +" "
                info+="Price: "   +'%.3f' % float(kv['price']) + " "
                info+="Processed Premium: "   +'%.3f' % float(kv['processed_premium']) + " "
                print (info)
            else:
                info+="Equity: "  +kv['chain_symbol']+ " "
                info+="Closing Strategy: "+kv['closing_strategy'] +" "
                info+="Price: "   +'%.3f' % float(kv['price']) + " "
                info+="Processed Premium: "   +'%.3f' % float(kv['processed_premium']) + " "
                print (info)


print("Total Credit = %.3f" % TotalCredit)
print("Total Debit  = %.3f" % TotalDebit)
print("Gross Gains  = %.3f" % (TotalCredit-TotalDebit))
NetGain =  (TotalCredit-TotalDebit)*0.8
print("Net Gains    = %.3f" % NetGain)

