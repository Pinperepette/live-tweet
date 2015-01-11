#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'livetweet.ui'
#
# Created: Sun Mar  2 02:48:35 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!
from twitter import *
from PyQt4 import QtCore, QtGui
import os,sys,signal
import tempfile

cartella = tempfile.mkdtemp()



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(524, 693)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(524, 600))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.webView = QtWebKit.QWebView(self.centralwidget)
        self.webView.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy)
        self.webView.setMinimumSize(QtCore.QSize(0, 0))
        self.webView.setBaseSize(QtCore.QSize(490, 0))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("http://team.bugs3.com/livetweet/LT.html")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.gridLayout.addWidget(self.webView, 0, 0, 1, 1)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lcdNumber = QtGui.QLCDNumber(self.frame)
        self.lcdNumber.setFrameShadow(QtGui.QFrame.Sunken)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(3)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.dial = QtGui.QDial(self.frame)
        self.dial.setWrapping(False)
        self.dial.setNotchTarget(13.7)
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName(_fromUtf8("dial"))
        self.horizontalLayout.addWidget(self.dial)
        self.pushButton = QtGui.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("color:rgb(128, 128, 128)"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 524, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuLive_Tweet = QtGui.QMenu(self.menubar)
        self.menuLive_Tweet.setObjectName(_fromUtf8("menuLive_Tweet"))
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout_LiveTweet = QtGui.QAction(MainWindow)
        self.actionAbout_LiveTweet.setObjectName(_fromUtf8("actionAbout_LiveTweet"))
        self.menuLive_Tweet.addAction(self.actionAbout_LiveTweet)
        self.menubar.addAction(self.menuLive_Tweet.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.dial, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdNumber.display)
        QtCore.QObject.connect(self.actionAbout_LiveTweet, QtCore.SIGNAL(_fromUtf8("triggered()")), self.about)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        signal.signal(signal.SIGINT, signal.SIG_DFL)
        self.pushButton.clicked.connect(self.crea)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Live Tweet", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#808080;\">Search:</span></p></body></html>", None))
        self.pushButton.setText(_translate("MainWindow", "Start", None))
        
        self.actionAbout_LiveTweet.setText(_translate("MainWindow", "About Live Tweet", None))
        

    def crea(self):
        indice = 0
        APP_KEY ='your APP_KEY'
        APP_SECRET = 'your APP_SECRET'
        OAUTH_TOKEN = 'your AUTH_TOKEN'
        OAUTH_SECRET ='your AUTH_SECRET'
        outfile = open(cartella+'/index.html', "w", encoding = "UTF-8")
        tw = self.lineEdit.text()
        n = int(self.lcdNumber.value())
        print (tw, n)  
        outfile.write ("""\
        <!DOCTYPE html>
        <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <title>Test Figata</title>
        <link href="http://team.bugs3.com/livetweet/style.css" rel="stylesheet" type="text/css" />
        </head>
        <body>
        <div id="twitter">
        """)
        
        
        t = Twitter(
            auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
                       APP_KEY, APP_SECRET)
           )
        
        search_results = t.search.tweets(q=tw, result_type='recent', count=n)
        
        for tweet in search_results['statuses']:
            indice = indice + 1
            a = 'copia'
            b = "()"
            print ('<div id="',indice,'"','''onClick="''','{}{}{}'.format(a,indice,b),'''"class="twitter"''','>', file = outfile)
            print ('''\
            <script type="text/javascript">
            function''', '{}{}{}'.format(a,indice,b),'''
            { 
            document.getElementById("diretta").innerHTML= document.getElementById("''',indice,'''").innerHTML
            }   
            </script>''', file = outfile)
            print ('<img src="', tweet['user']['profile_image_url'], '"/>', file = outfile)
            print ('<h1>', tweet['user']['name'], '</h1>', file = outfile)
            print ('<h2>@',tweet['user']['screen_name'], '</h2>', file = outfile)
            print ('<p>', tweet['text'], '</p>', file = outfile)
            print ("</div>", file = outfile)
    
        outfile.write ('</div>')
        outfile.write ("""<div id="header">""")    
        outfile.write ("""<div id="diretta"></div>""")
        outfile.write ('</div>') 
        outfile.write ("""</body>
        </html>
        """)
        #print ('Finito.')
        #print (tw, n)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8(cartella+"/index.html")))

    def about(self):
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("http://team.bugs3.com/livetweet/about/about.html")))

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

