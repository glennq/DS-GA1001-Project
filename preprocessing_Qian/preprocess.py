def cleanVehData(fpath):
    df = pd.read_csv(fpath, parse_dates=["PurchDate"]).set_index("RefId")
    # Drop PRIMEUNIT and AUCGUART due to large number of missing values, WheelTypeID due to redundancy with WheelType
    df = df.drop(["PRIMEUNIT", "AUCGUART", "WheelTypeID"], axis = 1)
    # drop records with missing values in reference prices, Color, and Trim, which are hard to fill
    df = df.dropna(axis=0, subset=["MMRAcquisitionAuctionAveragePrice", "MMRAcquisitionAuctionCleanPrice", \
                                   "MMRAcquisitionRetailAveragePrice", "MMRAcquisitonRetailCleanPrice", \
                                   "MMRCurrentAuctionAveragePrice", "MMRCurrentAuctionCleanPrice", \
                                   "MMRCurrentRetailAveragePrice", "MMRCurrentRetailCleanPrice", "Color", "Trim"])
    # Fill WheelType with the largest count value from vehicles with the same Model and Trim
    for i in df[df.WheelType.isnull()].index:
        temp = df.WheelType[(df.Model == df.Model[i]) & (df.Trim == df.Trim[i])].value_counts().index
        if len(temp) > 0:
            df.WheelType[i] = temp[0]
    # Drop records with missing values in WheelType that cannot be filled with abovementioned method
    df = df.dropna(axis=0, subset=["WheelType"])
    # Fill all other missing values with the same method described above
    for k in range(df.shape[1]):
        isna = df.iloc[:,k].isnull()
        if isna.any():
            for i in df[isna].index:
                temp = df.iloc[:,k][(df.Model == df.Model[i]) & (df.Trim == df.Trim[i])].value_counts().index
                if len(temp) > 0:
                    df.iloc[:,k][i] = temp[0]
    return df
