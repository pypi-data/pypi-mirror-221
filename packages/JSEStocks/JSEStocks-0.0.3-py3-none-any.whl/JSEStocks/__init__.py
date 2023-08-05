import yfinance as yf

def ReturnListStocks():
    stocks = '''
        StockCode,CompanyNames
        PRX,Prosus N.V. 
        ANH,Anheuser-Busch Inbev 
        BTI,British American Tobacco 
        GLN,Glencore plc 
        CFR,Compagnie Fin Richemont 
        BHP,BHP Group plc 
        NPN,Naspers Limited - N 
        AGL,Anglo American plc 
        AMS,Anglo American Platinum Ltd 
        FSR,Firstrand Limited 
        MTN,MTN Group Limited 
        VOD,Vodacom Group Limited 
        SBK,Standard Bank Group 
        CPI,Capitec Bank Holdings 
        SOL,Sasol Limited 
        S32,South32 Limited 
        IMP,Impala Platinum Holdings Limited 
        MNP,Mondi plc 
        KIO,Kumba Iron Ore 
        SSW,Sibanye Stillwater Limited 
        ABG,Absa Group Limited 
        GFI,Gold Fields Limited 
        SLM,Sanlam Limited 
        SHP,Shoprite Holdings Limited 
        ANG,Anglogold Ashanti 
        BID,Bid Corporation Limited 
        DSY,Discovery Limited 
        NED,Nedbank Group Limited 
        APN,Aspen Pharmacare Holdings Limited 
        PPH,Pepkor Holdings Limited 
        NHM,Northam Platinum Limited 
        RMI,Rand Merchant Investment Holdings 
        CLS,Clicks Group Limited 
        REM,Remgro Limited 
        OMU,Old Mutual Limited 
        NRP,Nepi Rockcastle plc 
        BVT,Bidvest Group 
        INP,Investec plc 
        EXX,Exxaro Resources Limited 
        RNI,Reinet Investments S.C.A. 
        WHL,Woolworths Holdings Limited 
        MCG,MultiChoice Group 
        MRP,Mr Price Group 
        GRT,Growthpoint Properties Limited 
        ARI,African Rainbow Minerals 
        MEI,Mediclinic International plc 
        QLT,Quilter plc 
        RBP,Royal Bafokeng Platinum Limited 
        TFG,The Foschini Group 
        DGH,Distell Group Holdings 
        VVO,Vivo Energy plc 
        HMN,Hammerson plc 
        TBS,Tiger Brands Limited 
        N91,Ninety One plc 
        LHC,Life Healthcare Group 
        TXT,Textainer Group Holdings 
        HAR,Harmony Gold Mining Company 
        SPP,Spar Group Limited 
        TCP,Transaction Capital Ltd 
        SRE,Sirius Real Estate 
        SNT,Santam Limited 
        CCO,Capital & Counties Properties plc 
        DCP,Dis-Chem Pharmacies Limited 
        MSP,MAS Real Estate Inc 
        MTM,Momentum Metropolitan Holdings 
        LBH,Liberty Holdings Limited 
        INL,Investec Limited 
        APH,Alphamin Resources Corporation 
        BAW,Barloworld Limited 
        PIK,Pick n Pay Stores Limited 
        AVI,AVI Limited 
        TKG,Telkom SA Limited 
        RDF,Redefine Properties Limited 
        RES,Resilient REIT Limited 
        SAP,Sappi Limited 
        TRU,Truworths International Limited 
        BYI,Bytes Technology Group 
        MTH,Motus Holdings Limited 
        SNH,Steinhoff International Holdings NV 
        NTC,Netcare Limited 
        ITE,Italtile Limited 
        KST,PSG Konsult Limited 
        PSG,PSG Group Limited 
        CML,Coronation Fund Managers 
        KRO,Karooooo Ltd 
        NY1,Ninety One Limited 
        EQU,Equites Property Fund Limited 
        FFA,Fortress REIT Limited - A 
        LTE,Lighthouse Capital Limited 
        RCL,RCL Foods Limited 
        IPL,Imperial Logistics Limited 
        MSM,Massmart Holdings Limited 
        AFE,AECI Limited 
        HYP,Hyprop Investments Limited 
        SPG,Super Group Limited 
        TGA,Thungela Resources Limited 
        IAP,Irongate Group 
        TSG,Tsogo Sun Gaming 
        ACL,ArcelorMittal South Africa Limited 
        VKE,Vukile Property Fund Limited 
        KAP,Kap Industrial Holdings Limited 
        STP,Stenprop Limited 
        DRD,DRDGOLD Limited 
        JSE,JSE Limited 
        IPF,Investec Property Fund Limited 
        OMN,Omnia Holdings Limited 
        EPP,EPP N.V. 
        GTC,Globe Trade Centre S.A. 
        AIP,Adcock Ingram Holdings 
        AIL,African Rainbow Capital Investments 
        RLO,Reunert Limited 
        ADH,ADvTECH Limited 
        AFT,Afrimat Limited 
        PAN,Pan African Resources plc 
        COH,Curro Holdings Limited 
        DTC,Datatec Limited 
        JBL,Jubilee Metals Group Plc 
        OCE,Oceana Group Limited 
        THA,Tharisa plc 
        PPC,PPC Limited 
        ARL,Astral Foods Limited 
        CSB,Cashbuild Limited 
        FBR,Famous Brands Limited 
        SSS,Stor-Age Property REIT 
        SUI,Sun International Limited 
        WBO,Wilson Bayly Holmes-Ovcon Limited 
        RBX,Raubex Group Limited 
        HCI,Hosken Consolidated Investments Limited 
        MUR,Murray & Roberts Holdings Limited 
        SAC,SA Corporate Real Estate Fund Limited 
        BAT,Brait SE 
        ATT,Attacq Limited 
        MTA,Metair Investments Limited 
        AFH,Alexander Forbes Group Holdings Limited 
        RAV,Raven Property Group Limited 
        EMI,Emira Property Fund Limited 
        MPT,Mpact Limited 
        ZED,Zeder Investments Limited 
        GSH,Grindrod Shipping Holdings 
        TGO,Tsogo Sun Hotels 
        MED,Middle East Diamond Resources Limited 
        SHG,Sea Harvest Group Limited 
        BLU,Blue Label Telecoms 
        L2D,Liberty Two Degrees Limited 
        REN,Renergen Limited 
        MIX,Mix Telematics Limited 
        HDC,Hudaco Industries Limited 
        LBR,Libstar Holdings Limited 
        GML,Gemfields Group Limited 
        L4L,Long4Life Limited 
        KAL,Kaap Agri Limited 
        NT1,Net 1 UEPS Technologies Inc 
        FFB,Fortress REIT Limited - B 
        MTNZF,MTN Zakhele Futhi 
        PPE,Purple Group Limited 
        CLI,Clientele Limited 
        AHB,Arrowhead Properties Limited B 
        RFG,RFG Holdings Limited 
        AEG,Aveng Group Limited 
        MRF,Merafe Resources Limited 
        GND,Grindrod Limited 
        AEL,Allied Electronics Corporation 
        CAT,Caxton & CTP Publishers & Printers Limited 
        EXP,Exemplar Reitail Limited 
        CLH,City Lodge Hotels Limited 
        IVT,Invicta Holdings Limited 
        SCD,Schroder European Real Estate Investment Trust 
        LEW,Lewis Group Limited 
        ACT,Afrocentric Investment Corp 
        SDO,STADIO Holdings Limited 
        HET,Heriot REIT Limited 
        HIL,Homechoice International plc 
        TDH,Tradehold Limited 
        WEZ,Wesizwe Platinum Limited 
        OAO,Oando PLC 
        NPK,Nampak Limited 
        CTA,Capital Appreciation Limited 
        SYG,Sygnia Limited 
        YYLBEE,YeboYethu (RF) Limited 
        DIA,Dipula Income Fund Limited A 
        SBP,Sabvest Capital Limited 
        OCT,Octodec Investments Limited 
        RMH,RMB Holdings Limited 
        FVT,Fairvest Property Holdings 
        CRP,Capital & Regional plc 
        AVV,Alviva Holdings Limited 
        SUR,Spur Corporation Limited 
        DRA,DRA Global Limited 
        CMH,Combined Motor Holdings Limited 
        TTO,Trustco Group Holdings Limited 
        SEA,Spear Reit Limited 
        MDI,Master Drilling Group Limited 
        ARH,ARB Holdings Limited 
        BWN,Balwin Properties Limited 
        ACS,Acsion Limited 
        BRN,Brimstone Investment Corporation - N Shares 
        SAR,Safari Investments RSA Limited 
        ENX,enX Group Limited 
        EMN,E Media Holdings Limited - N Shares 
        HLM,Hulamin Limited 
        MFL,Metrofile Holdings Limited 
        EPE,EPE Capital Partners Limited 
        OAS,Oasis Crescent Property Fund 
        ORN,Orion Minerals Limited 
        UPL,Universal Partners Limited 
        TEX,Texton Property Fund Limited 
        GPL,Grand Parade Investments Limited 
        BEL,Bell Equipment Limited 
        AYO,AYO Tech Solutions 
        YRK,York Timber Holdings Limited 
        ILU,Indluplace Properties Limited 
        DIB,Dipula Income Fund Limited B 
        HPR,Hosken Passenger Logistics and Rail Limited 
        APF,Accelerate Property Fund Ltd 
        QFH,Quantum Foods Holdings 
        SOLBE1,Sasol Limited - BEE 
        CHP,Choppies Enterprises Limited 
        AHA,Arrowhead Properties Limited A 
        PBG,PBT Group Limited 
        SFN,Sasfin Holdings Limited 
        EOH,EOH Holdings 
        TRE,Trencor Limited 
        TPF,Transcend Residential Property Fund Limited 
        BCF,Bowler Metcalf Limited 
        MST,Mustek Limited 
        FGL,Finbond Group Limited 
        DNB,Deneb Investments Limited 
        SNV,Santova Limited 
        NVS,Novus Holdings Limited 
        MMP,Marshall Monteagle PLC 
        WSL,Wescoal Holdings Limited 
        OLG,Onelogix Group Limited 
        TMT,Trematon Capital Investments Limited 
        ART,Argent Industrial Limited 
        DKR,Deutsche Konsum REIT-AG 
        NWL,Nu-World Holdings Limited 
        KP2,Kore Potash Plc 
        ADR,Adcorp Holdings Limited 
        TON,Tongaat Hulett Limited 
        EPS,Eastern Platinum Limited 
        HUG,Huge Group Limited 
        CND,Conduit Capital Limited 
        CKS,Crookes Brothers Limited 
        TPC,Transpaco Limited 
        CGR,Calgro M3 Holdings Limited 
        ALH,Alaris Holdings Limited 
        VUN,Vunani Limited 
        SEP,Sephaku Holdings Limited 
        NVE,Nvest Financial Holdings Limited 
        AEE,African Equity Empowerment Investments 
        DLT,Delta Property Fund Limited 
        ISB,Insimbi Industrial Holdings Ltd 
        ASC,Ascendis Health Limited 
        RSG,Resource Generation Limited 
        NRL,Newpark REIT Limited 
        RHB,RH Bophelo Limited 
        SOH,South Ocean Holdings 
        WKF,Workforce Holdings Limited 
        BUC,Buffalo Coal Corporation 
        BIK,Brikor Limited 
        TRL,Trellidor Holdings Limited 
        SEB,Sebata Holdings Limited 
        BAU,Bauba Resources Limited 
        AME,African Media Entertainment 
        EMH,E Media Holdings Limited 
        AVL,Advanced Health Limited 
        BRT,Brimstone Investment Corporation 
        ARA,Astoria Investments Limited 
        ETO,Etion Limited 
        ELI,Ellies Holdings Limited 
        LNF,London Finance & Investment Group Plc 
        HUL,Hulisani Limited 
        FSE,Firestone Energy Limited 
        KBO,Kibo Energy PLC 
        PFB,Premier Fishing and Brands 
        REA,Rebosis Property Fund - A Shares 
        RTN,Rex Trueform Group - N Shares 
        CVW,Castleview Property Fund Limited 
        REB,Rebosis Property Fund 
        CMO,Chrometco Limited 
        MCZ,MC Mining Limited 
        CSG,CSG Holdings Limited 
        ISA,ISA Holdings Limited 
        4SI,4Sight Holdings Limited 
        CGN,Cognition Holdings Limited 
        PPR,Putprop Limited 
        EEL,Efora Energy Limited 
        LAB,Labat Africa Limited 
        PMV,Primeserv Group Limited 
        SSK,Stefanutti Stocks Holdings Limited 
        EUZ,Europa Metals Limited 
        RNG,Randgold And Exploration Company 
        JSC,Jasco Electronics Holdings 
        AON,African and Overseas Enterprises - N Shares 
        TLM,TeleMasters Holdings Limited 
        UAT,Union Atlantic Minerals Limited 
        BSR,Basil Read Holdings Limited 
        AHL,AH-Vest Limited 
        HWA,Hwange Colliery Company Limited 
        RTO,Rex Trueform Group 
        SVB,SilverBridge Holdings Limited 
        NCS,Nictus Limited 
        PEM,Pembury Lifestyle Group 
        CAC,CAFCA Limited 
        PSV,PSV Holdings Limited 
        ILE,Imbalie Beauty Limited 
        MRI,Mine Restoration Investments Limited 
        TAS,Taste Holdings Limited 
        AOO,African and Overseas Enterprises Limited 
        VIS,Visual International Holdings Limited 
        ADW,African Dawn Capital 
        ECS,Ecsponent Limited 
        GLI,Go Life International Ltd 
        WEA,WG Wearne Limited 
        NFP,New Frontier Properties Limited 
        NUT,Nutritional Holdings Limited 
        ACZ,Arden Capital Limited 
        PHM,Phumelela Gaming And Leisure Limited 
        RPL,RDI REIT PLC 
        ACE,Accentuate Limited 
        RDI,Rockwell Diamonds Incorporated 
        AFX,African Oxygen Limited 
        ACG,Anchor Group Limited 
        ALP,Atlantic Leaf Properties Limited 
        TBG,Tiso Blackstar Group SE 
        CTK,Cartrack Holdings 
        UCP,Unicorn Capital Partners Limited 
        VLE,Value Group Limited 
        COM,Comair Limited 
        CIL,Consolidated Infrastructure Group 
        EFG,Efficient Group Limited 
        ELR,ELB Group Limited 
        ESR,Esor Limited 
        FDP,Freedom Property Fund Limited 
        GAI,Gaia Infrastructure Capital Limited 
        GRF,Group Five Limited 
        HPB,Hospitality Property Fund - B 
        IDQ,Indequity Group Limited 
        KDV,Kaydav Group Limited 
        MZR,Mazor Group Limited 
        MLE,Mettle Investments Limited 
        MNK,Montauk Holdings Limited 
        '''
    print(stocks)


def ReturnSouthAfricanETFs():
    companyNames = [
        "1nvest Top 40 ETF",
        "1nvest SWIX 40 ETF",
        "FNB Top 40 ETF",
        "Satrix 40 ETF",
        "Satrix SWIX Top 40 ETF",
        "Sygnia Itrix SWIX 40 ETF",
        "Sygnia Itrix Top 40 ETF",
        "CoreShares Next 40",
        "CoreShares Wealth Top 20",
        "CoreShares Top 50 ETF",
        "CoreShares DivTrax ETF",
        "FNB Mid Cap ETF",
        "Satrix S&P GIVI SA Top 50 ETF",
        "Satrix Volatility Managed Defensive Equity ETF",
        "Satrix Volatility Managed High Growth Equity ETF",
        "Satrix Volatility Managed Moderate Equity ETF",
        "Satrix Equity Momentum  ETF",
        "Satrix Value Equity ETF",
        "Satrix Low Volatility Equity ETF",
        "Satrix Shari'ah Top 40 ETF",
        "CoreShares Scientific Beta Mult-Factor ETF",
        "Satrix Capped All Share ETF",
        "Satrix DIVI ETF",
        "Satrix FINI ETF",
        "Satrix Inclusion & Diversity ETF",
        "Satrix INDI ETF",
        "Satrix Momentum ETF",
        "Satrix  Quality South Africa ETF",
        "Satrix RAFI 40 ETF",
        "Satrix RESI ETF",
        "CoreShares S&P 500 ETF",
        "1nvest S&P 500 Index Feeder ETF",
        "1nvest S&P 500 Info Tech Index Feeder ETF",
        "1nvest MSCI EM Asia Index Feeder ETF",
        "1nvest MSCI Wordld Socially Responsible Investment Index Feeder ETF",
        "1nvest MSCI World Index Feeder ETF",
        "FNB Global 1200 Equity Fund of Funds ETF",
        "CoreShares Total World Stock Feeder ETF",
        "CoreShares S&P Global Dividend Aristocrats ETF",
        "Satrix S&P 500 ETF",
        "Satrix MSCI China ETF",
        "Satrix Smart City Infrastructure Feeder ETF",
        "Satrix MSCI EM ESG Enhanced ETF",
        "Satrix MSCI Emerging Markets ETF",
        "Satrix MSCI World ESG Enhanced ETF",
        "Satrix Healthcare Innovation Feeder ETF",
        "Satrix Global Infrastucture ETF",
        "Satrix MSCI India ETF",
        "Satrix Nasdaq 100 ETF",
        "Satrix MSCI World ETF",
        "Sygnia Itrix 4th Industrial Revolution Global Equity ETF",
        "Sygnia Itrix S&P 500",
        "Sygnia Itrix New China Sectors ETF",
        "Sygnia Itrix MSCI Emerging Markets 50 ETF",
        "Sygnia Itrix S&P Global 1200 ESG ETF",
        "Sygnia DJ EuroStoxx 50 ETF",
        "Sygnia Itrix Solactive Healthcare 150 ETF",
        "Sygnia Itrix MSCI Japan ETF",
        "Sygnia Itrix Sustainable Economy ETF",
        "Sygnia Itrix FTSE 100 ETF",
        "Sygnia Itrix MSCI USA ETF",
        "Sygnia Itrix MSCI World ETF",
        "1nvestGold ETF",
        "1nvestPalladium ETF",
        "1nvestPlatinum ETF",
        "1nvestRhodium ETF",
        "NewGold ETF",
        "Krugerrand  Custodial Certificate",
        "NewPalladium ETF",
        "NewPlat ETF",
        "CoreShares Wealth GOVI ETF",
        "CoreShares Yield Selected Bond ETF",
        "1nvest SA Bond ETF",
        "FNB Inflation ETF",
        "Satrix GOVI ETF",
        "Satrix ILBI ETF",
        "Satrix SA Bond ETF",
        "Satrix ILBI ETF",
        "Dollar Custodial Certificate  - 10 Year",
        "Dollar Custodial Certificate - 2 Year",
        "1nvest Global Government Bond Index Feeder ETF",
        "1nvest ICE US Treasury Short Bond Index ETF",
        "FNB World Government Bond ETF",
        "Satrix S&P Namibia Bond ETF",
        "Satrix Global Aggregate Bond ETF",
        "Satrix TRACI 3 Month  ETF",
        "Satrix Multi Asset Passive Portfolios Solutions Growth ETF",
        "Satrix Multi Asset Passive Portfolios Solutions Protect ETF",
        "CoreShares SA Property Income ETF",
        "1nvest SA Property ETF",
        "Satrix Property ETF",
        "1nvest Global REIT Index Feeder ETF",
        "Satrix Reitway Global Property ETF",
        "Coreshares  S&P Global Property ETF",
        "Reitway Global Property ESG Prescient ETF",
        "Reitway Global Property Diversified Prescient ETF",
        "Sygnia Itrix Global Property ETF",
    ]

    codes = [
        "ETFT40",
        "ETFSWX",
        "FNBT40",
        "STX40",
        "STXSWX",
        "SYGSW4",
        "SYGT40",
        "CSNT40",
        "CTOP20",
        "CTOP50",
        "DIVTRX",
        "FNBMID",
        "STXT50",
        "STXDEQ",
        "STXGEQ",
        "STXMEQ",
        "STXEQM",
        "STXVEQ",
        "STXLVL",
        "STXSHA",
        "SMART",
        "STXCAP",
        "STXDIV",
        "STXFIN",
        "STXID",
        "STXIND",
        "STXMMT",
        "STXQUA",
        "STXRAF",
        "STXRES",
        "CSP500",
        "ETF500",
        "ETF5IT",
        "ETFEMA",
        "ETFSRI",
        "ETFWLD",
        "FNBEQF",
        "GLOBAL",
        "GLODIV",
        "STX500",
        "STXCHN",
        "STXCTY",
        "STXEME",
        "STXEMG",
        "STXESG",
        "STXHLT",
        "STXIFR",
        "STXNDA",
        "STXNDQ",
        "STXWDM",
        "SYG4IR",
        "SYG500",
        "SYGCN",
        "SYGEMF",
        "SYGESG",
        "SYGEU",
        "SYGH",
        "SYGJP",
        "SYGSE",
        "SYGUK",
        "SYGUS",
        "SYGWD",
        "ETFGLD",
        "ETFPLD",
        "ETFPLT",
        "ETFRHO",
        "GLD",
        "KCCGLD",
        "NGPLD",
        "NGPLT",
        "CSGOVI",
        "CSYSB",
        "ETFBND",
        "FNBINF",
        "STXGVI",
        "STXIFL",
        "STXGOV",
        "STXILB",
        "DCCUSD",
        "DCCUS2",
        "ETFGGB",
        "ETFUSD",
        "FNBWGB",
        "STXNAM",
        "STXGBD",
        "STXTRA",
        "STXMAG",
        "STXMAP ",
        "CSPROP",
        "ETFSAP",
        "STXPRO",
        "ETFGRE",
        "STXGPR",
        "GLPROP",
        "RWESG",
        "RWDVF",
        "SYGP",
    ]

    for i in range(len(companyNames)):
        print(companyNames[i] + " - " + codes[i])


def GetStockHistory(Code):
    df = yf.download(Code+'.JO')
    df['Date'] = df.index
    return df


def GetStockHistoryAllMarkets(Code):
    df = yf.download(Code)
    df['Date'] = df.index
    return df


if __name__ == '__main__':
    ReturnSouthAfricanETFs()
    # GetStockHistoryAllMarkets('AAPL')
    # GetStockHistory('AAPL')
    # ReturnListStocks()
