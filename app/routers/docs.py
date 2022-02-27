
bottom_up_beta_industry = """
NB, debt_to_equity ratio to be used should be for the company you are analysing. **Check the next endpoint that uses firm debt to calculate bottom up beta**. The beta shown here is for industry averages. The professor didn't include the actual beta in the dataset but explained how to calculat it<br>
    For this reason, I have taken the liberty to include bottom_up_leverd_beta calculated according to the professors' lecture, namely:<br><br>
    Levered bottom-up beta = Unlevered beta (1+ (1-t) (Debt/Equity)) <br><br>
    where:<br>
    debt_equity_ratio_firm = sector_total_debt / sector_total_market_cap<br>
    Please, bear in mind this bottom_up_beta was calculated by me. I recommend you go and calculate your own based on this numbers. <br>

    If you are unsure about which industry sector does your company belong to, run reference_item essentials endpoint.
"""