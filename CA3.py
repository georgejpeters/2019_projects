"""
This module (run on Anaconda command prompt) allows a user to monitor and update information on current brewing processes,
see ratios of beer sales between different recipies in the past year, see growth forecasts for the next 10 weeks
based on the previous 12 months worth of data, monitor and update information on brewing equipment.
"""
from datetime import datetime
import pandas as pd
import re
import itertools

bodata = []
cdata = []
fdata = []
hbdata = []

def command():
    """
    This function is the hub of the module, from here you can direct yourself to
    the different functionality within the module.
    """
    comman = input(
        "What functionality would you like to access, sales info (S) or brewery management (B) "
    )
    if comman == "B":
        choose()
    elif comman == "S":
        sales_command = input(
            "Would you like so see ratios between beer sales over the year period (R) or growth analysis and sales reccomendations (G)? "
        )
        if sales_command == "R":
            sales_ratio()
        elif sales_command == "G":
            growth_rate(hbdata, fdata, cdata)
        else:
            print("Invalid input")
            command()
    else:
        print("Invalid Input, please select either S, E or P")


def choose():
    """
    A second function used for traversing the modules functionality
    """
    ch = input(
        "Would you like to, see current brewed inventory (I), fill a machine to hot brew (H), move a brew onto a different stage (M) or use different functionality (F)? "
    )
    if ch == "H":
        fill()
    elif ch == "M":
        move(hbdata, fdata, cdata, bodata)
    elif ch == "I":
        inventory(hbdata, fdata, cdata, bodata)
    elif ch == "F":
        command()
    else:
        print("Incorrect input")
        return choose()
    command()


def sales_ratio():
    """
    This function allows users to specify a ratio of beer sales between two recipies
    the function then calculates the ratio based on the previous years sales records and
    displays it
    """
    requested_growth_rate1 = input(
        "What is the first recipe you would like to compare?: "
    )
    requested_growth_rate2 = input(
        "What is the second recipe you would like to compare?: "
    )
    file = "Barnabys_sales_fabriacted_data.csv"

    x1 = pd.read_csv(file)
    df = pd.DataFrame(x1, columns=["Quantity ordered"])

    rh_sum = df[1:181].sum()
    rh_sum = re.sub("[^0-9]", "", str(rh_sum))

    op_sum = df[182:523].sum()
    op_sum = re.sub("[^0-9]", "", str(op_sum))

    od_sum = df[524:662].sum()
    od_sum = re.sub("[^0-9]", "", str(od_sum))

    all_sum = df.sum()
    all_sum = re.sub("[^0-9]", "", str(all_sum))

    if requested_growth_rate1 == "organic red helles":
        if requested_growth_rate2 == "organic pilsner":
            print(
                "The requested ratio of beer sales is (ORH:OP) " + rh_sum + ":" + op_sum
            )
        elif requested_growth_rate2 == "organic dunkel":
            print(
                "The requested ratio of beer sales is (ORH:OD) " + rh_sum + ":" + od_sum
            )
        else:
            print("Invalid Input, please select organic pilsner or organic dunkel")
    elif requested_growth_rate1 == "organic pilsner":
        if requested_growth_rate2 == "organic dunkel":
            print(
                "The requested ratio of beer sales is (OP:OD) " + op_sum + ":" + od_sum
            )
        elif requested_growth_rate2 == "organic red helles":
            print(
                "The requested ratio of beer sales is (OP:ORH) " + op_sum + ":" + rh_sum
            )
        else:
            print("Invalid Input, please select organic dunkel or organic red helles")
            sales_ratio()
    elif requested_growth_rate1 == "organic dunkel":
        if requested_growth_rate2 == "organic pilsner":
            print(
                "The requested ratio of beer sales is (OD:OP) " + od_sum + ":" + op_sum
            )
        elif requested_growth_rate2 == "organic red helles":
            print(
                "The requested ratio of beer sales is (OD:ORH) " + od_sum + ":" + rh_sum
            )
        else:
            print("Invalid Input, please select organic pilsner or organic red helles")
            sales_ratio()
    command()


def growth_rate(hbdata, fdata, cdata):
    """
    This function, calcualtes the expected growth rate for the nexr 10 weeks for all beers
    and for each type of beer, to do this it takes the previous 12 months worth of sales data
    splits it up by month and by beer then calcualtes the average over the months. This module 
    also has planning functionality it takes the forecasted growth by beer and the current 
    equipment available and reccomends which beer you should start brewing and reccomends
    equipment that is available.
    """
    start_at = -1
    file = "Barnabys_sales_fabriacted_data.xlsx"
    # opens and reads the file into the module
    x1 = pd.read_excel(file)
    df1 = pd.DataFrame(x1)
    df2 = pd.DataFrame(x1, columns=["Quantity ordered"])
    # initialises 13 empty lists
    nov2018, dec2018, jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov2019 = (
        [] for i in range(13)
    )
    (
        pnov2018,
        pdec2018,
        pjan,
        pfeb,
        pmar,
        papr,
        pmay,
        pjun,
        pjul,
        paug,
        psep,
        poct,
        dnov2018,
        ddec2018,
        djan,
        dfeb,
        dmar,
        dapr,
        dmay,
        djun,
        djul,
        daug,
        dsep,
        doct,
        rnov2018,
        rdec2018,
        rjan,
        rfeb,
        rmar,
        rapr,
        rmay,
        rjun,
        rjul,
        raug,
        rsep,
        roct,
    ) = ([] for i in range(36))
    # loads the column date required into a dataframe
    list = df1["Date Required"].tolist()
    # loads the recipie column into a dataframe
    df3 = df1["Recipe"].tolist()
    df2 = df2.values.tolist()
    lis = []
    for n in list:
        # formats the date required
        n = n.strftime("%d/%m/%Y")
        lis.append(n)

    for n in lis:
        # parses through data looking for dates in 2018
        if n[6:10] == "2018":
            # looks through data for 11 (the month of november)
            if n[3:5] == "11":
                ind = lis.index(n, start_at + 1)
                # adds quantity ordered at this date to the november list for overall beers
                nov2018.append(df2[ind])
                if df3[ind] == "Organic Red Helles":
                    # adds quantity ordered at this date to the november list for Red Helles
                    rnov2018.append(df2[ind])
                elif df3[ind] == "Organic Pilsner":
                    pnov2018.append(df2[ind])
                elif df3[ind] == "Organic Dunkel":
                    dnov2018.append(df2[ind])
                start_at = ind
            elif n[3:5] == "12":
                ind = lis.index(n, start_at + 1)
                dec2018.append(df2[ind])
                if df3[ind] == "Organic Red Helles":
                    rdec2018.append(df2[ind])
                elif df3[ind] == "Organic Pilsner":
                    pdec2018.append(df2[ind])
                elif df3[ind] == "Organic Dunkel":
                    ddec2018.append(df2[ind])
                start_at = ind
        elif n[6:10] == "2019":
            if n[3:5] == "01":
                ind = lis.index(n, start_at + 1)
                jan.append(df2[ind])
                if df3[ind] == "Organic Red Helles":
                    rjan.append(df2[ind])
                elif df3[ind] == "Organic Pilsner":
                    pjan.append(df2[ind])
                elif df3[ind] == "Organic Dunkel":
                    djan.append(df2[ind])
                start_at = ind
            elif n[3:5] == "02":
                ind = lis.index(n, start_at + 1)
                feb.append(df2[ind])
                if df3[ind] == "Organic Red Helles":
                    rfeb.append(df2[ind])
                elif df3[ind] == "Organic Pilsner":
                    pfeb.append(df2[ind])
                elif df3[ind] == "Organic Dunkel":
                    dfeb.append(df2[ind])
                start_at = ind
            elif n[3:5] == "03":
                ind = lis.index(n, start_at + 1)
                mar.append(df2[ind])
                if df3[ind] == "Organic Red Helles":
                    rmar.append(df2[ind])
                elif df3[ind] == "Organic Pilsner":
                    pmar.append(df2[ind])
                elif df3[ind] == "Organic Dunkel":
                    dmar.append(df2[ind])
                start_at = ind
            elif n[3:5] == "04":
                ind = lis.index(n, start_at + 1)
                apr.append(df2[ind])
                if df3[ind] == "Organic Red Helles":
                    rapr.append(df2[ind])
                elif df3[ind] == "Organic Pilsner":
                    papr.append(df2[ind])
                elif df3[ind] == "Organic Dunkel":
                    dapr.append(df2[ind])
                start_at = ind
            elif n[3:5] == "05":
                ind = lis.index(n, start_at + 1)
                may.append(df2[ind])
                if df3[ind] == "Organic Red Helles":
                    rmay.append(df2[ind])
                elif df3[ind] == "Organic Pilsner":
                    pmay.append(df2[ind])
                elif df3[ind] == "Organic Dunkel":
                    dmay.append(df2[ind])
                start_at = ind
            elif n[3:5] == "06":
                ind = lis.index(n, start_at + 1)
                jun.append(df2[ind])
                if df3[ind] == "Organic Red Helles":
                    rjun.append(df2[ind])
                elif df3[ind] == "Organic Pilsner":
                    pjun.append(df2[ind])
                elif df3[ind] == "Organic Dunkel":
                    djun.append(df2[ind])
                start_at = ind
            elif n[3:5] == "07":
                ind = lis.index(n, start_at + 1)
                jul.append(df2[ind])
                if df3[ind] == "Organic Red Helles":
                    rjul.append(df2[ind])
                elif df3[ind] == "Organic Pilsner":
                    pjul.append(df2[ind])
                elif df3[ind] == "Organic Dunkel":
                    djul.append(df2[ind])
                start_at = ind
            elif n[3:5] == "08":
                ind = lis.index(n, start_at + 1)
                aug.append(df2[ind])
                if df3[ind] == "Organic Red Helles":
                    raug.append(df2[ind])
                elif df3[ind] == "Organic Pilsner":
                    paug.append(df2[ind])
                elif df3[ind] == "Organic Dunkel":
                    daug.append(df2[ind])
                start_at = ind
            elif n[3:5] == "09":
                ind = lis.index(n, start_at + 1)
                sep.append(df2[ind])
                if df3[ind] == "Organic Red Helles":
                    rsep.append(df2[ind])
                elif df3[ind] == "Organic Pilsner":
                    psep.append(df2[ind])
                elif df3[ind] == "Organic Dunkel":
                    dsep.append(df2[ind])
                start_at = ind
            elif n[3:5] == "10":
                ind = lis.index(n, start_at + 1)
                oct.append(df2[ind])
                if df3[ind] == "Organic Red Helles":
                    roct.append(df2[ind])
                elif df3[ind] == "Organic Pilsner":
                    poct.append(df2[ind])
                elif df3[ind] == "Organic Dunkel":
                    doct.append(df2[ind])
                start_at = ind
    # sums the red helles january list
    rsum_jan = "".join(map(str, ([sum(i) for i in zip(*rjan)])))
    rsum_feb = "".join(map(str, ([sum(i) for i in zip(*rfeb)])))
    rsum_mar = "".join(map(str, ([sum(i) for i in zip(*rmar)])))
    rsum_apr = "".join(map(str, ([sum(i) for i in zip(*rapr)])))
    rsum_may = "".join(map(str, ([sum(i) for i in zip(*rmay)])))
    rsum_jun = "".join(map(str, ([sum(i) for i in zip(*rjun)])))
    rsum_jul = "".join(map(str, ([sum(i) for i in zip(*rjul)])))
    rsum_aug = "".join(map(str, ([sum(i) for i in zip(*raug)])))
    rsum_sep = "".join(map(str, ([sum(i) for i in zip(*rsep)])))
    rsum_oct = "".join(map(str, ([sum(i) for i in zip(*roct)])))
    rsum_nov2018 = "".join(map(str, ([sum(i) for i in zip(*rnov2018)])))
    rsum_dec2018 = "".join(map(str, ([sum(i) for i in zip(*rdec2018)])))
    psum_jan = "".join(map(str, ([sum(i) for i in zip(*pjan)])))
    psum_feb = "".join(map(str, ([sum(i) for i in zip(*pfeb)])))
    psum_mar = "".join(map(str, ([sum(i) for i in zip(*pmar)])))
    psum_apr = "".join(map(str, ([sum(i) for i in zip(*papr)])))
    psum_may = "".join(map(str, ([sum(i) for i in zip(*pmay)])))
    psum_jun = "".join(map(str, ([sum(i) for i in zip(*pjun)])))
    psum_jul = "".join(map(str, ([sum(i) for i in zip(*pjul)])))
    psum_aug = "".join(map(str, ([sum(i) for i in zip(*paug)])))
    psum_sep = "".join(map(str, ([sum(i) for i in zip(*psep)])))
    psum_oct = "".join(map(str, ([sum(i) for i in zip(*poct)])))
    psum_nov2018 = "".join(map(str, ([sum(i) for i in zip(*pnov2018)])))
    psum_dec2018 = "".join(map(str, ([sum(i) for i in zip(*pdec2018)])))
    dsum_jan = "".join(map(str, ([sum(i) for i in zip(*djan)])))
    dsum_feb = "".join(map(str, ([sum(i) for i in zip(*dfeb)])))
    dsum_mar = "".join(map(str, ([sum(i) for i in zip(*dmar)])))
    dsum_apr = "".join(map(str, ([sum(i) for i in zip(*dapr)])))
    dsum_may = "".join(map(str, ([sum(i) for i in zip(*dmay)])))
    dsum_jun = "".join(map(str, ([sum(i) for i in zip(*djun)])))
    dsum_jul = "".join(map(str, ([sum(i) for i in zip(*djul)])))
    dsum_aug = "".join(map(str, ([sum(i) for i in zip(*daug)])))
    dsum_sep = "".join(map(str, ([sum(i) for i in zip(*dsep)])))
    dsum_oct = "".join(map(str, ([sum(i) for i in zip(*doct)])))
    dsum_nov2018 = "".join(map(str, ([sum(i) for i in zip(*dnov2018)])))
    dsum_dec2018 = "".join(map(str, ([sum(i) for i in zip(*ddec2018)])))
    # averages the first months growth for red helles
    rfma1 = ((int(rsum_dec2018) - int(rsum_nov2018)) / int(rsum_nov2018)) * 100
    rfma2 = ((int(rsum_jan) - int(rsum_dec2018)) / int(rsum_dec2018)) * 100
    rfma3 = ((int(rsum_feb) - int(rsum_jan)) / int(rsum_jan)) * 100
    rfma4 = ((int(rsum_mar) - int(rsum_feb)) / int(rsum_feb)) * 100
    rfma5 = ((int(rsum_apr) - int(rsum_mar)) / int(rsum_mar)) * 100
    rfma6 = ((int(rsum_may) - int(rsum_apr)) / int(rsum_apr)) * 100
    rfma7 = ((int(rsum_jun) - int(rsum_may)) / int(rsum_may)) * 100
    rfma8 = ((int(rsum_jul) - int(rsum_jun)) / int(rsum_jun)) * 100
    rfma9 = ((int(rsum_aug) - int(rsum_jul)) / int(rsum_jul)) * 100
    rfma10 = ((int(rsum_sep) - int(rsum_aug)) / int(rsum_aug)) * 100
    rfma11 = ((int(rsum_oct) - int(rsum_sep)) / int(rsum_sep)) * 100

    dfma1 = ((int(dsum_dec2018) - int(dsum_nov2018)) / int(dsum_nov2018)) * 100
    dfma2 = ((int(dsum_jan) - int(dsum_dec2018)) / int(dsum_dec2018)) * 100
    dfma3 = ((int(dsum_feb) - int(dsum_jan)) / int(dsum_jan)) * 100
    dfma4 = ((int(dsum_mar) - int(dsum_feb)) / int(dsum_feb)) * 100
    dfma5 = ((int(dsum_apr) - int(dsum_mar)) / int(dsum_mar)) * 100
    dfma6 = ((int(dsum_may) - int(dsum_apr)) / int(dsum_apr)) * 100
    dfma7 = ((int(dsum_jun) - int(dsum_may)) / int(dsum_may)) * 100
    dfma8 = ((int(dsum_jul) - int(dsum_jun)) / int(dsum_jun)) * 100
    dfma9 = ((int(dsum_aug) - int(dsum_jul)) / int(dsum_jul)) * 100
    dfma10 = ((int(dsum_sep) - int(dsum_aug)) / int(dsum_aug)) * 100
    dfma11 = ((int(dsum_oct) - int(dsum_sep)) / int(dsum_sep)) * 100

    pfma1 = ((int(psum_dec2018) - int(psum_nov2018)) / int(psum_nov2018)) * 100
    pfma2 = ((int(psum_jan) - int(psum_dec2018)) / int(psum_dec2018)) * 100
    pfma3 = ((int(psum_feb) - int(psum_jan)) / int(psum_jan)) * 100
    pfma4 = ((int(psum_mar) - int(psum_feb)) / int(psum_feb)) * 100
    pfma5 = ((int(psum_apr) - int(psum_mar)) / int(psum_mar)) * 100
    pfma6 = ((int(psum_may) - int(psum_apr)) / int(psum_apr)) * 100
    pfma7 = ((int(psum_jun) - int(psum_may)) / int(psum_may)) * 100
    pfma8 = ((int(psum_jul) - int(psum_jun)) / int(psum_jun)) * 100
    pfma9 = ((int(psum_aug) - int(psum_jul)) / int(psum_jul)) * 100
    pfma10 = ((int(psum_sep) - int(psum_aug)) / int(psum_aug)) * 100
    pfma11 = ((int(psum_oct) - int(psum_sep)) / int(psum_sep)) * 100

    sum_jan = "".join(map(str, ([sum(i) for i in zip(*jan)])))
    sum_feb = "".join(map(str, ([sum(i) for i in zip(*feb)])))
    sum_mar = "".join(map(str, ([sum(i) for i in zip(*mar)])))
    sum_apr = "".join(map(str, ([sum(i) for i in zip(*apr)])))
    sum_may = "".join(map(str, ([sum(i) for i in zip(*may)])))
    sum_jun = "".join(map(str, ([sum(i) for i in zip(*jun)])))
    sum_jul = "".join(map(str, ([sum(i) for i in zip(*jul)])))
    sum_aug = "".join(map(str, ([sum(i) for i in zip(*aug)])))
    sum_sep = "".join(map(str, ([sum(i) for i in zip(*sep)])))
    sum_oct = "".join(map(str, ([sum(i) for i in zip(*oct)])))
    sum_nov2019 = "".join(map(str, ([sum(i) for i in zip(*nov2019)])))
    sum_nov2018 = "".join(map(str, ([sum(i) for i in zip(*nov2018)])))
    sum_dec2018 = "".join(map(str, ([sum(i) for i in zip(*dec2018)])))

    fma1 = ((int(sum_dec2018) - int(sum_nov2018)) / int(sum_nov2018)) * 100
    fma2 = ((int(sum_jan) - int(sum_dec2018)) / int(sum_dec2018)) * 100
    fma3 = ((int(sum_feb) - int(sum_jan)) / int(sum_jan)) * 100
    fma4 = ((int(sum_mar) - int(sum_feb)) / int(sum_feb)) * 100
    fma5 = ((int(sum_apr) - int(sum_mar)) / int(sum_mar)) * 100
    fma6 = ((int(sum_may) - int(sum_apr)) / int(sum_apr)) * 100
    fma7 = ((int(sum_jun) - int(sum_may)) / int(sum_may)) * 100
    fma8 = ((int(sum_jul) - int(sum_jun)) / int(sum_jun)) * 100
    fma9 = ((int(sum_aug) - int(sum_jul)) / int(sum_jul)) * 100
    fma10 = ((int(sum_sep) - int(sum_aug)) / int(sum_aug)) * 100
    fma11 = ((int(sum_oct) - int(sum_sep)) / int(sum_sep)) * 100
    # calculates the average monthly growth for red helles
    ramg = (
        rfma1
        + rfma2
        + rfma3
        + rfma4
        + rfma5
        + rfma6
        + rfma7
        + rfma8
        + rfma9
        + rfma10
        + rfma11
    ) / 11
    # calcualtes the average growth every 10 weeks for red helles
    rweeks_10 = ramg * 2.3
    damg = (
        dfma1
        + dfma2
        + dfma3
        + dfma4
        + dfma5
        + dfma6
        + dfma7
        + dfma8
        + dfma9
        + dfma10
        + dfma11
    ) / 11
    dweeks_10 = damg * 2.3
    pamg = (
        pfma1
        + pfma2
        + pfma3
        + pfma4
        + pfma5
        + pfma6
        + pfma7
        + pfma8
        + pfma9
        + pfma10
        + pfma11
    ) / 11
    pweeks_10 = pamg * 2.3

    amg = (
        fma1 + fma2 + fma3 + fma4 + fma5 + fma6 + fma7 + fma8 + fma9 + fma10 + fma11
    ) / 11
    weeks_10 = amg * 2.3

    inpu = input(
        "Would you like to see overall beer growth (O) growth by recipie (R) or the reccomended brewing plan (P)? "
    )
    if inpu == "R":
        i = input(
            "Would you like to see the 10 week growth estimate for Red Helles (R), Dunkel (D) or Pilsner(P) "
        )
        if i == "R":
            print(
                "The predicted percentage growth in beers sales over the next 10 weeks for Red Helles, based on the previous 12 month period is: "
                + str(round(rweeks_10, 2))
                + "%"
            )
        elif i == "D":
            print(
                "The predicted percentage growth in beers sales over the next 10 weeks for Dunkel, based on the previous 12 month period is: "
                + str(round(dweeks_10, 2))
                + "%"
            )
        elif i == "P":
            print(
                "The predicted percentage growth in beers sales over the next 10 weeks for Pilsner, based on the previous 12 month period is: "
                + str(round(pweeks_10, 2))
                + "%"
            )
        else:
            print("Invalid Input, please select either R, D or P")
    elif inpu == "O":
        gq = input(
            "Would you like to see the predicted growth for next month (M), or the predicted growth for the next 10 weeks (10)? "
        )
        if gq == "M":
            print(
                "The predicted percentage growth in beers sales over the next month based on the previous 12 month period is: "
                + str(round(amg, 2))
                + "%"
            )
        elif gq == "10":
            print(
                "The predicted percentage growth in beers sales over the next 10 weeks based on the previous 12 month period is: "
                + str(round(weeks_10, 2))
                + "%"
            )
        else:
            print("Invalid Input, please select either O or M")
    elif inpu == "P":
        available_v1000 = []
        available_v800 = []
        available_v680 = []
        v1000 = ("Albert", "Camilla", "Emily")
        v800 = ("Brigadier", "Dylon", "Florence", "R2D2")
        v680 = ("Gertrude", "Harry")
        for n in v1000:
            # looks through list of 1000L machines in use marks available in not in use
            if n not in hbdata:
                available_v1000.append(n)
            elif n not in cdata:
                available_v1000.append(n)
            elif n not in fdata:
                available_v1000.append(n)
        for n in v800:
            if n not in hbdata:
                available_v800.append(n)
            elif n not in cdata:
                available_v800.append(n)
            elif n not in fdata:
                available_v800.append(n)
        for n in v680:
            if n not in hbdata:
                available_v680.append(n)
            elif n not in cdata:
                available_v680.append(n)
            elif n not in fdata:
                available_v680.append(n)

        if rweeks_10 > pweeks_10:
            if rweeks_10 > dweeks_10:
                print(
                    "As the 10 week growth prediction for Red Helles is highest Red Helles production should be prioritised, the following list is that of available machines that could be used to brew Red Helles in order of highest to lowest volume "
                    + str(available_v1000)
                    + str(available_v800)
                    + str(available_v680)
                )
                command()
            elif rweeks_10 < dweeks_10:
                print(
                    "As the 10 week growth prediction for Dunkel is highest Dunkel production should be prioritised, the following list is that of available machines that could be used to brew Dunkel in order of highest to lowest volume "
                    + str(available_v1000)
                    + str(available_v800)
                    + str(available_v680)
                )
                command()
        elif pweeks_10 > rweeks_10:
            if pweeks_10 > dweeks_10:
                print(
                    "As the 10 week growth prediction for Pilsner is highest Pilsner production should be prioritised, the following list is that of available machines that could be used to brew Pilsner in order of highest to lowest volume "
                    + str(available_v1000)
                    + str(available_v800)
                    + str(available_v680)
                )
                command()
            elif pweeks_10 < dweeks_10:
                print(
                    "As the 10 week growth prediction for Dunkel is highest Dunkel production should be prioritised, the following list is that of available machines that could be used to brew Dunkel in order of highest to lowest volume "
                    + str(available_v1000)
                    + str(available_v800)
                    + str(available_v680)
                )
                command()
        else:
            print("Error has occured")
            command()
    else:
        print("Invalid Input, please select either O or R")
        command()
    command()


def fill():
    """
    This function starts off the brewing process by allowing users to choose which machine to 
    start hot brewing their beer in, it then tracks the request and keeps note of all current
    brewing processes input
    """
    beers = "organic dunkel, organic pilsner, organic red helles"
    machine_list = (
        "Albert",
        "Brigadier",
        "Camilla",
        "Dylon",
        "Emily",
        "Florence",
        "Gertrude",
        "Harry",
        "R2D2",
    )
    v1000 = ("Albert", "Camilla", "Emily")
    v800 = ("Brigadier", "Dylon", "Florence", "R2D2")
    v680 = ("Gertrude", "Harry")
    fermenters = (
        "Albert",
        "Brigadier",
        "Camilla",
        "Dylon",
        "Emily",
        "Florence",
        "R2D2",
    )
    conditioners = (
        "Albert",
        "Brigadier",
        "Camilla",
        "Dylon",
        "Emily",
        "Florence",
        "Gertrude",
        "Harry",
    )

    beer = input("What beer would you like to brew: ")
    if beer in beers:
        machine = input("What machine would you like to use for this process: ")
        if machine in v1000:
            # adds the machine in use, the quanity being brewed, the time of brewing and the recipie to a list of hot brew processes
            hbdata.extend((machine, "1000L", datetime.now(), beer))
            print(
                machine
                + " now has 1000L in and started the hotbrew stage at "
                + str(datetime.now())
            )

        elif machine in v800:
            hbdata.extend((machine, "800L", datetime.now(), beer))
            print(
                machine
                + " now has 800L in and started the hotbrew stage at "
                + str(datetime.now())
            )

        elif machine in v680:
            hbdata.extend((machine, "680L", datetime.now(), beer))
            print(
                machine
                + " now has 680L in and started the hotbrew stage at "
                + str(datetime.now())
            )

        else:
            print("Machine not found")
            return fill()
    else:
        print("Beer not found, choose between " + beers)
        return fill()
    choi = input("Would you like to fill another machine (Y/N)? ")
    if choi == "Y":
        return fill()
    elif choi == "N":
        return choose()
    else:
        print("Invalid  Input")
        return choose()
    command()


def move(cdata, fdata, hbdata, bodata):
    """
    This function tracks current stage at which a batch is being brewed
    and allows a user to move batches onto the next stage eg fermentation to
    conditioning and then tracks that move, it also keeps inventory of all 
    completed and bottled batches in a list with all the relevant information
    called bodata.
    """
    v1000 = ("Albert", "Camilla", "Emily")
    v800 = ("Brigadier", "Dylon", "Florence", "R2D2")
    v680 = ("Gertrude", "Harry")
    proc = input("At what stage of brewing is your brew currently at (HB, F, C) ")
    mach = input(
        "Which machine contains the brew you would like to move on to the next stage? "
    )
    nm = input(
        "Which machine would you like to move your brew to, or would you like to begin bottling (B)? "
    )
    if proc == "HB":
        if hbdata != []:
            if mach in hbdata:
                for n in hbdata:
                    if n == mach:
                        ind = hbdata.index(n)
                        time_in_hb = datetime.now() - hbdata[ind + 2]
                        time_in_hb = str(time_in_hb)
                        print(
                            mach
                            + " has been emptied, this batch began hot brewing at "
                            + str(datetime.now())
                        )
                        print("It was hot brewing for " + time_in_hb)
                        if hbdata[ind + 1] == "1000L":
                            if nm in v1000:
                                # adds the machine name to the fermentation data list
                                fdata.append(nm)
                                # adds the quanity being brewed to the fermentation data list
                                fdata.append("1000L")
                                # adds the time fermentation started to the fermentation data list
                                fdata.append(datetime.now())
                                # adds recipie of the batch to the fermentation data list
                                fdata.append(hbdata[ind + 3])
                                print(
                                    "This 1000L batch of "
                                    + hbdata[ind + 3]
                                    + " is now fermenting in "
                                    + nm
                                )
                                # removes all irrelevant data from previous processes list
                                hbdata.pop(ind)
                                hbdata.pop(ind)
                                hbdata.pop(ind)
                                hbdata.pop(ind)

                            else:
                                print(
                                    "The machine you selected has a different volume to the previous machine, to avoid waste please select one of the following machines"
                                    + v1000
                                )
                                return move(cdata.fdata, hbdata, bodata)
                        elif hbdata[ind + 1] == "800L":
                            if nm in v800:
                                fdata.append(nm)
                                fdata.append("800L")
                                fdata.append(datetime.now())
                                fdata.append(hbdata[ind + 3])
                                print(
                                    "This 800L batch of "
                                    + hbdata[ind + 3]
                                    + " is now fermenting in "
                                    + nm
                                )
                                hbdata.pop(ind)
                                hbdata.pop(ind)
                                hbdata.pop(ind)
                                hbdata.pop(ind)

                            else:
                                print(
                                    "The machine you selected has a different volume to the previous machine, to avoid waste please select one of the following machines"
                                    + v800
                                )
                                return move(cdata.fdata, hbdata, bodata)
                        elif hbdata[ind + 1] == "680L":
                            if nm in v680:
                                fdata.append(nm)
                                fdata.append("680L")
                                fdata.append(datetime.now())
                                fdata.append(hbdata[ind + 3])
                                print(
                                    "This 680L batch of "
                                    + hbdata[ind + 3]
                                    + " is now fermenting in "
                                    + nm
                                )
                                hbdata.pop(ind)
                                hbdata.pop(ind)
                                hbdata.pop(ind)
                                hbdata.pop(ind)
                            else:
                                print(
                                    "The machine you selected has a different volume to the previous machine, to avoid waste please select one of the following machines"
                                    + v680
                                )
                                return move(cdata.fdata, hbdata, bodata)
    elif proc == "F":
        if fdata != []:
            if mach in fdata:
                for n in fdata:
                    if n == mach:
                        ind = fdata.index(n)
                        time_in_f = datetime.now() - fdata[ind + 2]
                        time_in_f = str(time_in_f)
                        print(
                            mach
                            + " has been emptied, this batch was put in this conditioner at "
                            + str(datetime.now())
                        )
                        print("It was in the fermenter for " + time_in_f)
                        if fdata[ind + 1] == "1000L":
                            if nm in v1000:
                                cdata.append(nm)
                                cdata.append("1000L")
                                cdata.append(datetime.now())
                                cdata.append(hbdata[ind + 3])
                                print(
                                    "This 1000L batch of "
                                    + fdata[ind + 3]
                                    + " is now conditioning in "
                                    + nm
                                )
                                fdata.pop(ind)
                                fdata.pop(ind)
                                fdata.pop(ind)
                                fdata.pop(ind)

                            else:
                                print(
                                    "The machine you selected has a different volume to the previous machine, to avoid waste please select one of the following machines"
                                    + v1000
                                )
                                return move(cdata.fdata, hbdata, bodata)
                        elif fdata[ind + 1] == "800L":
                            if nm in v800:
                                cdata.append(nm)
                                cdata.append("800L")
                                cdata.append(datetime.now())
                                cdata.append(hbdata[ind + 3])
                                print(
                                    "This 800L batch of "
                                    + fdata[ind + 3]
                                    + " is now conditioning in "
                                    + nm
                                )
                                fdata.pop(ind)
                                fdata.pop(ind)
                                fdata.pop(ind)
                                fdata.pop(ind)

                            else:
                                print(
                                    "The machine you selected has a different volume to the previous machine, to avoid waste please select one of the following machines"
                                    + v800
                                )
                                return move(cdata.fdata, hbdata, bodata)
                        elif fdata[ind + 1] == "680L":
                            if nm in v680:
                                cdata.append(nm)
                                cdata.append("680L")
                                cdata.append(datetime.now())
                                cdata.append(hbdata[ind + 3])
                                print(
                                    "This 680L batch of "
                                    + fdata[ind + 3]
                                    + " is now fermenting in "
                                    + nm
                                )
                                fdata.pop(ind)
                                fdata.pop(ind)
                                fdata.pop(ind)
                                fdata.pop(ind)
                            else:
                                print(
                                    "The machine you selected has a different volume to the previous machine, to avoid waste please select one of the following machines"
                                    + v680
                                )
                                return move(cdata.fdata, hbdata, bodata)
    elif proc == "C":
        if cdata != []:
            if mach in cdata:
                for n in cdata:
                    if n == mach:
                        ind = cdata.index(n)
                        time_in_c = datetime.now() - cdata[ind + 2]
                        time_in_c = str(time_in_c)
                        print(
                            mach
                            + " has been emptied, this batch began bottling at "
                            + str(datetime.now())
                        )
                        print("It was in the conditioner for " + time_in_c)
                        if cdata[ind + 1] == "1000L":
                            if nm == "B":
                                bodata.append("1000L")
                                bodata.append(datetime.now())
                                bodata.append(hbdata[ind + 3])
                                print(
                                    "This 1000L batch of "
                                    + cdata[ind + 3]
                                    + " is now being bottled"
                                )
                                cdata.pop(ind)
                                cdata.pop(ind)
                                cdata.pop(ind)
                                cdata.pop(ind)

                            else:
                                print(
                                    "You have selected an invalid input, select B if you would like to begin bottling a batch"
                                )
                                return move(cdata.fdata, hbdata, bodata)
                        elif cdata[ind + 1] == "800L":
                            if nm == "B":
                                bodata.append("800L")
                                bodata.append(datetime.now())
                                bodata.append(hbdata[ind + 3])
                                print(
                                    "This 800L batch of "
                                    + cdata[ind + 3]
                                    + " is now being bottled"
                                )
                                cdata.pop(ind)
                                cdata.pop(ind)
                                cdata.pop(ind)
                                cdata.pop(ind)

                            else:
                                print(
                                    "You have selected an invalid input, select B if you would like to begin bottling a batch"
                                )
                                return move(cdata.fdata, hbdata, bodata)
                        elif cdata[ind + 1] == "680L":
                            if nm == "B":
                                bodata.append("680L")
                                bodata.append(datetime.now())
                                bodata.append(hbdata[ind + 3])
                                print(
                                    "This 680L batch of "
                                    + cdata[ind + 3]
                                    + " is now being bottled"
                                )
                                cdata.pop(ind)
                                cdata.pop(ind)
                                cdata.pop(ind)
                                cdata.pop(ind)
                            else:
                                print(
                                    "You have selected an invalid input, select B if you would like to begin bottling a batch"
                                )
                                return move(cdata.fdata, hbdata, bodata)
        else:
            print("This machine could not be found try a different one")
            return move(hbdata, fdata, cdata, bodata)

    else:
        print("You have selected an invalid process please either input HB, C or F")
        return choose()
    return choose()


def inventory(hbdata, fdata, cdata, bodata):
    """
    This module allows the user to view all current processes in the brewery, and the amount, type of beer and time of completion
    of bottled beers
    """
    ic = input(
        "Would you like to view the beer currently being brewed (E), or the beer that has been bottled (B)?"
    )
    if ic == "E":
        print(
            "The beer currently being hot brewed (formatted [machine, amount, time put in the machine, recipie]) is: "
            + str(hbdata)
        )
        print(
            "The beer currently in the fermenter (formatted [machine, amount, time put in the machine, recipie]) is: "
            + str(fdata)
        )
        print(
            "The beer currently in the conditioner (formatted [machine, amount, time put in the machine, recipie]) is: "
            + str(cdata)
        )
    if ic == "B":
        print(
            "The beer that is undergoing or has undergone the bottling process (formatted [amount, time bottling process began, recipie]) is: "
            + str(bodata)
        )
    ii = input("Would you like to see any other data (Y/N)? ")
    if ii == "Y":
        return inventory(hbdata, fdata, cdata, bodata)
    elif ii == "N":
        return command()
    else:
        print("Invalid Input")
        return command()
    choose()


command()
