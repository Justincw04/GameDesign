#Justin Cortez Wartell

#String Practice

strVar="My name is M"
print(strVar)
print(len(strVar))
print(strVar[len(strVar)-1])
indexNum= strVar.find("name")
print(indexNum)
print(strVar[indexNum: indexNum+4])
print(strVar[indexNum: ])
print(strVar[:indexNum+1])
print(strVar.replace('name', 'initial'))
strVar=strVar.upper()
print(strVar)


strText="Here are the instructions to install Drivers 1. After the download is completed go to where you saved the folder. (By default everything you download from the Internet is saved to the Downloads folder) 2. Right click on the folder and choose ''Extract All'' and then choose ''Extract'' again. 3. Once all the contents have been extracted you may delete/disregard the folder with the zip icon. 4. Next, open and Run the SETUP file. (In most cases it is a setup .exe file OR one listed below: * setup application *Asussetup *pnpinstal64 *pnputil *Igxpin 5. Please choose to 'repair' or 'update' the existing installation (driver) IF any one of those options do appear during the set up."
print(strText)
print(strText.find("Drivers"))
print(len(strText))
print(strText.replace('Extract', 'EXTRACT'))
print(strText.replace('setup' 'Setup', 'SETUP'))
