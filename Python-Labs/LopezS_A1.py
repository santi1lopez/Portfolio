"""
Name: Santiago Lopez
Class: CSEC 1436

Purpose: Program that reads a log file, analyzes each login event, computes a risk socre,classifies the threat level, and generates a security report

English Language Steps
    Open the File with the Users information
    Read and analyze the login information from the file
    Analyze the Users login attempts, login time, downloaded data and if MFA is enabled or not
    Calcualte the Risk score using the point system
    Analyz to see if the threat risk is LOW MEDIUM or HIGH or CRITICAL
    Count and report if there is any Insider Threats
    Count and Report if there is any Brute Force Indicators
    Calculate the total users analyzed, average risk score, highest risk score, number of LOW threats, number of MEDIUM threats,Number of HIGH threats
    Calculate the Number of Critical threats, Potential Insider Threats, Brute Force Indicators
    Calculate the Security Compliance Rate  
    Write the Statistical reuslts in a tabluated form 

Test
    1. test001,0,12,50,True,60
    Risk Score- 5.00
    Expected Threat- LOW

    2. test002,7,14,200,False,120
    Risk Score- 226.27
    Expected Threat - HIGH

    3. test003,3,23,80,True,45
    Risk Score- 60.00
    Expected Threat- LOW

    4.test004,12,2,900,False,180
    Risk Score- 486.75
    Expected Threat- HIGH

    5.test005,2,8,100,True,30
    Risk Score- 8.66
    Expected Threat- LOW

    6. test006,5,18,500,False,90
    Risk Score - 159.22
    Expected Threat - MEDIUM

    7.test007,10,19,450,True,75
    Risk Score - 199.00
    Expected Threat- MEDIUM

    8. test008,20,1,1200,False,300
    Risk Score- 618.65
    Expected Threat- CRITICAL

Psuedo Code
    Set all Counters and Totals to <== 0
    Open SecLog.txt for reading
    Skip the first line of the file

        Read User information
        Set Column to 1
        Read the character in each of the lines
            If the letter is a comma
                Skip the column or move to the next
            Else
                correct where the letter goes
            Convert MFA to True or False
        Risk <== 0
        Users <== Users +1

        If FailedAttempts <= 2
            Risk <== Risk + 5
        Else If FailedAttempts <=5
            Risk <== Risk + 15
        Else If FailedAttempts <= 10
            Risk <== Risk + 30
        Else 
            Risk <== Risk + 50
        
        If LoginHour >= 8 and LoginHour <= 18
            Risk <== Risk + 5
        Else
            Risk <== Risk + 20
        
        If DownloadMB <= 100
            Risk <== Risk + 5
        Else If DownloadMB <= 500
            Risk <== Risk + 20
        Else 
            Risk <== Risk + 40
        
        If MFA == True
            BaseRisk <== BaseRisk - 10
            MFAUsers <== MFAUsers + 1
        Else    
            Risk <== Risk + 25
        
        RiskScore <== Risk * sqrt (1+ FailedAttempts)

        RiskScore <== Round RiskScore to 2 decimal places

        If RiskSocre < 100
            ThreatLevel<== LOW
            LOWCount <== LOWCount + 1
        Else If RiskScore < 200
            ThreatLevel <== MEDIUM
            MEDCount <== MEDCount + 1
        Else If RiskScore < 500
            ThreatLevel <== HIGH
            HIGHCount <== HIGHCount + 1
        Else
            ThreatLevel <== Critical
            CriticalCount <== CriticalCount + 1
        
        If DownloadMB > 400 and (LoginHour < 8 or LoginHour > 18)
            InsiderThreats <== InsiderThreats + 1
        
        If FailedAttempts >= 8
            BruteForce <== BruteForce + 1

        TotalRisk <== TotalRisk + RiskScore

        If RiskScore > HighestRisk
            HighestRisk <== RiskScore
        
        Write Username, RiskScore, and Threat Level to output file
    
    If Users> 0
    AvgRisk <== TotalRisk/Users
    ComplianceRate <== MFAUsers/ Users * 100
    Else
    AvgRisk <== 0
    ComplianceRate <== 0

    Print Users,AvgRisk, and HighestRisk
    Print LOWCount, MEDCount, HIGHCount, and CRITICALCount
    Print InsiderThreats and BruteForce
    Print ComplianceRate

"""
import math

Users = 0
TotalRiskScore = 0
HighestRiskScore = 0

LOWCount = 0
MEDCount = 0
HIGHCount = 0
CritCount = 0

InsiderThreats = 0
BruteIndicators = 0
MFAUsers = 0

number= 0
with open("SecLog.txt","r") as InFile: 
    with open ("LopezS_A01Output.txt","w") as OutFile:
        OutFile.write("Username\tRisk Score\tThreat Level\n")
        for Aline in InFile:
            Aline = Aline.strip()
            number= number + 1
            if number > 1:
                print("Processing User")
                Username= ""
                FailedAttempts= ""
                LoginHour = ""
                DataDownloadedMB= ""
                MFAUser= ""
                MFAEnab= ""
                SessionDuration= ""
                column= 1

                for letter in Aline:   
                    if letter == ",":
                        column = column + 1
                    elif column == 1 :
                        Username = Username + letter
                    elif column == 2:
                        FailedAttempts= FailedAttempts + letter
                    elif column == 3:
                        LoginHour = LoginHour + letter
                    elif column == 4:
                        DataDownloadedMB = DataDownloadedMB + letter
                    elif column == 5:
                        MFAEnab = MFAEnab + letter
                    elif column == 6:
                        SessionDuration = SessionDuration + letter

                FailedAttempts = int(FailedAttempts)
                LoginHour = int(LoginHour)
                DataDownloadedMB= float(DataDownloadedMB)
                MFAEnab= MFAEnab == "True"
                SessionDuration = int(SessionDuration)
                Risk= 0
                if FailedAttempts <= 2:
                        Risk = Risk + 5
                elif FailedAttempts <= 5:
                        Risk = Risk+ 15
                elif FailedAttempts <= 10:
                        Risk= Risk + 30
                else:
                        Risk= Risk + 50

                if LoginHour >= 8 and LoginHour <= 18:
                        Risk= Risk + 5
                else:
                        Risk = Risk + 20

                if DataDownloadedMB <= 100:
                        Risk= Risk + 5
                elif DataDownloadedMB <= 500:
                        Risk= Risk + 20
                else:
                        Risk = Risk + 40

                if MFAEnab == True:
                        Risk = Risk - 10
                        MFAUsers= MFAUsers+ 1
                else:
                        Risk = Risk + 25
                RiskScore = Risk * math.sqrt(1+ FailedAttempts)
                RiskScore = round(RiskScore,2)

                if RiskScore < 100:
                        ThreatLevel = "LOW"
                        LOWCount= LOWCount + 1
                elif RiskScore < 200:
                        ThreatLevel = "MEDIUM"
                        MEDCount = MEDCount + 1
                elif RiskScore < 500:
                        ThreatLevel = "HIGH" 
                        HIGHCount = HIGHCount + 1
                else:
                        ThreatLevel = "CRITICAL" 
                        CritCount= CritCount + 1
                    
                if DataDownloadedMB > 400 and (LoginHour<8 or LoginHour> 18):
                        InsiderThreats= InsiderThreats + 1
                if FailedAttempts >= 8:
                        BruteIndicators= BruteIndicators + 1

                Users= Users + 1
                TotalRiskScore = TotalRiskScore + RiskScore
                if RiskScore > HighestRiskScore:
                        HighestRiskScore = RiskScore

                OutFile.write(Username +"\t"+str(RiskScore)+"\t"+ThreatLevel+ "\n")
           
        AvgRisk= TotalRiskScore/ Users
        MComplianceRate= (MFAUsers/ Users)* 100
        OutFile.write("\nSUMMARY STATISTICS\n")
        OutFile.write("Total Users: " + str(Users) + "\n")
        OutFile.write("Average Risk Score: "+ str(round(AvgRisk,2))+ "\n")
        OutFile.write("Highest Risk Score: "+ str(HighestRiskScore)+ "\n")
        OutFile.write("LOW Users: "+ str(LOWCount)+ "\n")
        OutFile.write("MEDIUM Users: "+ str(MEDCount)+ "\n")
        OutFile.write("HIGH Users: "+ str (HIGHCount)+ "\n")
        OutFile.write("CRITICAL Users: "+ str(CritCount)+ "\n")
        OutFile.write("Potential Insider Threats: "+ str(InsiderThreats)+"\n")
        OutFile.write("Brute Force Indicators "+ str(BruteIndicators)+ "\n")
        OutFile.write("MFA Compliance Rate: "+ str(round(MComplianceRate,2))+ "%\n")

                
            
           


