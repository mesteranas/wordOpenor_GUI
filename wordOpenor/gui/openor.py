from . import bookMarks
from docx import Document
import winsound,guiTools
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class Openor(qt.QDialog):
    def __init__(self,p,path:str,spliter:str):
        super().__init__(p)
        self.spliter=spliter
        self.path=path
        self.resize(600,600)
        self.pages=[]
        doc = Document(path)
        fullText = "\n".join(paragraph.text for paragraph in doc.paragraphs)
        self.pages=self.paginateText(fullText)
        self.index=bookMarks.getPageNumber(path)
        layout=qt.QVBoxLayout(self)
        self.text=guiTools.QReadOnlyTextEdit()
        self.text.setText(self.pages[self.index])
        layout.addWidget(self.text)
        self.pageNumber=qt.QLineEdit()
        self.pageNumber.setReadOnly(True)
        self.pageNumber.setText(str(self.index+1))
        layout.addWidget(self.pageNumber)
        buttonsLayout=qt.QHBoxLayout()
        self.nextPage=qt.QPushButton(_("next page"))
        self.nextPage.setShortcut("alt+right")
        self.nextPage.clicked.connect(self.onNextPage)
        buttonsLayout.addWidget(self.nextPage)
        self.goToPage=qt.QPushButton(_("go to page"))
        self.goToPage.setShortcut("ctrl+g")
        self.goToPage.clicked.connect(self.goToGoPage)
        buttonsLayout.addWidget(self.goToPage)
        self.previousPage=qt.QPushButton(_("previouse page"))
        self.previousPage.setShortcut("alt+left")
        self.previousPage.clicked.connect(self.onPreviousePage)
        buttonsLayout.addWidget(self.previousPage)
        layout.addLayout(buttonsLayout)
    def onNextPage(self):
        if self.index+1==len(self.pages):
            self.index=0
        else:
            self.index+=1
        pageNumberText=str(self.index+1)
        self.pageNumber.setText(pageNumberText)
        guiTools.speak(pageNumberText)
        bookMarks.editPage(self.path,self.index)
        self.text.setText(self.pages[self.index])
        winsound.PlaySound("data/sounds/next_page.wav",1)
    def onPreviousePage(self):
        if self.index==0:
            self.index=len(self.pages)-1
        else:
            self.index-=1
        pageNumberText=str(self.index+1)
        self.pageNumber.setText(pageNumberText)
        guiTools.speak(pageNumberText)
        bookMarks.editPage(self.path,self.index)
        self.text.setText(self.pages[self.index])
        winsound.PlaySound("data/sounds/previous_page.wav",1)
    def paginateText(self,text):
        words = text.split("\n")
        pages = []
        page=""
        for i in words:
            page+=i + "\n"
            if i.startswith(self.spliter):
                pages.append(page)
                page=""
        return pages
    def goToGoPage(self):
        page,ok=qt.QInputDialog.getInt(self,_("page number"),_("type page number"),self.index+1,1,len(self.pages))
        if ok:
            self.index=page-1
            pageNumberText=str(self.index+1)
            self.pageNumber.setText(pageNumberText)
            guiTools.speak(pageNumberText)
            bookMarks.editPage(self.path,self.index)
            self.text.setText(self.pages[self.index])